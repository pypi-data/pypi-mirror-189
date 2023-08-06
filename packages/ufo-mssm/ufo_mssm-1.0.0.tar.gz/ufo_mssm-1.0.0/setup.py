# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ufo_mssm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ufo-mssm',
    'version': '1.0.0',
    'description': 'Minimal Supersymmetric Standard Model UFO',
    'long_description': '# UFO Minimal Supersymmetric Standard Model',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/ufo_mssm',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
