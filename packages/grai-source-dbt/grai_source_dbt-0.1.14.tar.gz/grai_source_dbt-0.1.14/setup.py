# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_dbt', 'grai_source_dbt.models']

package_data = \
{'': ['*'], 'grai_source_dbt': ['data/*']}

install_requires = \
['grai-client>=0.2.0,<0.3.0',
 'grai-schemas>=0.1.7,<0.2.0',
 'networkx>=2.8.3,<3.0.0',
 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'grai-source-dbt',
    'version': '0.1.14',
    'description': '',
    'long_description': 'None',
    'author': 'Ian Eaves',
    'author_email': 'ian@grai.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
