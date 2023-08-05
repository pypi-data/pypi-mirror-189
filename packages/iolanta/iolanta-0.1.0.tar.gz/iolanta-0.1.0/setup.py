# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iolanta',
 'iolanta.cli',
 'iolanta.cli.formatters',
 'iolanta.facet',
 'iolanta.graph_providers',
 'iolanta.loaders',
 'iolanta.parsers',
 'iolanta_record',
 'iolanta_record.facets',
 'ldflex']

package_data = \
{'': ['*'],
 'iolanta': ['data/*'],
 'iolanta.facet': ['sparql/*'],
 'iolanta_record': ['data/*']}

install_requires = \
['PyLD>=2.0.3,<3.0.0',
 'classes>=0.4.0,<0.5.0',
 'deepmerge>=0.1.1,<0.2.0',
 'documented>=0.1.1,<0.2.0',
 'dominate>=2.6.0,<3.0.0',
 'funcy>=1.17,<2.0',
 'lambdas>=0.1.0,<0.2.0',
 'more-itertools>=9.0.0,<10.0.0',
 'owlrl>=6.0.2,<7.0.0',
 'python-frontmatter>=0.5.0,<0.6.0',
 'rdflib>=6.2.0,<7.0.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=13.3.1,<14.0.0',
 'typer>=0.7.0,<0.8.0',
 'urlpath>=1.1.7,<2.0.0']

entry_points = \
{'console_scripts': ['iolanta = iolanta.cli:app'],
 'iolanta.plugins': ['record = iolanta_record:IolantaRecord']}

setup_kwargs = {
    'name': 'iolanta',
    'version': '0.1.0',
    'description': 'Semantic Web browser',
    'long_description': '# iolanta\n\nStub repo for the iolanta browser.\n\n',
    'author': 'Anatoly Scherbakov',
    'author_email': 'altaisoft@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
