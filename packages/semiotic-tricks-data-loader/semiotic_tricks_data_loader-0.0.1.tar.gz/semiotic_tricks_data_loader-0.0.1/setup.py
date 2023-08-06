# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['semiotic_tricks_data_loader', 'semiotic_tricks_data_loader.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.2,<9.0.0']

entry_points = \
{'console_scripts': ['stdl = semiotic_tricks_data_loader.commands:entry_point']}

setup_kwargs = {
    'name': 'semiotic-tricks-data-loader',
    'version': '0.0.1',
    'description': '',
    'long_description': '# semiotic_tricks_data_loader',
    'author': 'Denis Shchtskyi',
    'author_email': 'denis.shchutskyi@branderstudio.com',
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
