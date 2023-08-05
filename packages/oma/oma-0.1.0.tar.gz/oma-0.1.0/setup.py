# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oma']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['oma = oma.main:app']}

setup_kwargs = {
    'name': 'oma',
    'version': '0.1.0',
    'description': '',
    'long_description': '# OMA\n\nHandy tool to automate most of everyday mundane tasks',
    'author': 'Allan Dawson',
    'author_email': 'dawson7allan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
