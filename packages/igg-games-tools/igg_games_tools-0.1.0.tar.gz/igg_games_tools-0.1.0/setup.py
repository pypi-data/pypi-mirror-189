# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['igg_games_tools']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['igt = igg_games_tools.__main__:main']}

setup_kwargs = {
    'name': 'igg-games-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'jawide',
    'author_email': 'jawide@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
