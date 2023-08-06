# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['savit', 'savit.config']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['savit = savit.main:app']}

setup_kwargs = {
    'name': 'savit',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'ivansantiagojr',
    'author_email': 'ivansantiago.junior@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
