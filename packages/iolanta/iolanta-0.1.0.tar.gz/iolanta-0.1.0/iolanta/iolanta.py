import functools
import logging
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Type

import owlrl
from owlrl import OWLRL_Extension
from rdflib import ConjunctiveGraph, Namespace, URIRef
from urlpath import URL

from iolanta import entry_points
from iolanta.conversions import path_to_url, url_to_path
from iolanta.loaders import Loader
from iolanta.loaders.base import SourceType
from iolanta.loaders.local_directory import merge_contexts
from iolanta.models import LDContext
from iolanta.namespaces import LOCAL
from iolanta.parsers.yaml import YAML
from iolanta.plugin import Plugin
from ldflex import LDFlex


@dataclass
class Iolanta:
    """Iolanta is a Semantic web browser."""

    loader: Loader[SourceType]
    graph: ConjunctiveGraph = field(
        default_factory=functools.partial(
            ConjunctiveGraph,
            identifier=LOCAL.term('_inference'),
        ),
    )
    namespaces: Dict[str, Namespace] = field(default_factory=dict)
    force_plugins: List[Type[Plugin]] = field(default_factory=list)

    logger: logging.Logger = field(
        default_factory=functools.partial(
            logging.getLogger,
            name='iolanta',
        ),
    )

    @property
    def plugin_classes(self) -> List[Type[Plugin]]:
        """Installed Iolanta plugins."""
        return self.force_plugins or entry_points.plugins('iolanta.plugins')

    @cached_property
    def plugins(self) -> List[Plugin]:
        return [
            plugin_class(iolanta=self)
            for plugin_class in self.plugin_classes
        ]

    @cached_property
    def ldflex(self) -> LDFlex:
        """LDFlex is a wrapper to make SPARQL querying RDF graphs bearable."""
        return LDFlex(self.graph)

    @cached_property
    def namespaces_to_bind(self) -> Dict[str, Namespace]:
        return {
            key: Namespace(value)
            for key, value in self.default_context['@context'].items()
            if (
                isinstance(value, str)
                and not value.startswith('@')
                and not key.startswith('@')
            )
        }

    def add(  # type: ignore
        self,
        source: Any,
        context: Optional[LDContext] = None,
        graph_iri: Optional[URIRef] = None,
    ) -> 'Iolanta':
        """Parse & load information from given URL into the graph."""
        quads = list(
            self.loader.as_quad_stream(
                source=source,
                iri=graph_iri,
                context=context or self.default_context,
                root_loader=self.loader,
            ),
        )

        self.graph.addN(quads)

        self.bind_namespaces(**self.namespaces_to_bind)

        self.infer()

        return self

    def infer(self) -> 'Iolanta':
        self.logger.info('Inference: OWL RL started...')
        owlrl.DeductiveClosure(OWLRL_Extension).expand(self.graph)
        self.logger.info('Inference: OWL RL complete.')

        return self

    def bind_namespaces(self, **mappings: Namespace) -> 'Iolanta':
        """Bind namespaces."""
        self.graph.bind(prefix='local', namespace=LOCAL)

        for prefix, namespace in mappings.items():
            self.graph.bind(prefix=prefix, namespace=namespace)

        return self

    @property
    def query(self):
        return self.ldflex.query

    @cached_property
    def context_paths(self) -> Iterable[Path]:
        directory = Path(__file__).parent / 'data'

        yield directory / 'context.yaml'

        for plugin in self.plugins:
            if path := plugin.context_path:
                yield path

    @cached_property
    def default_context(self) -> LDContext:
        """Construct default context from plugins."""
        context_documents = [
            YAML().as_jsonld_document(path.open('r'))
            for path in self.context_paths
        ]

        for context in context_documents:
            if isinstance(context, list):
                raise ValueError('Context cannot be a list: %s', context)

        return merge_contexts(*context_documents)   # type: ignore

    def add_files_from_plugins(self):
        for plugin in self.plugins:
            self.add(plugin.data_files)

    def __post_init__(self):
        self.add_files_from_plugins()

    def expand_qname(self, qname: str) -> URIRef:
        try:
            return self.graph.namespace_manager.expand_curie(qname)
        except ValueError:
            return URIRef(qname)
