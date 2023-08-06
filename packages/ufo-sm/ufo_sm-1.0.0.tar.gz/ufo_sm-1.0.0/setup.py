# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ufo_sm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ufo-sm',
    'version': '1.0.0',
    'description': 'Standard Model UFO',
    'long_description': '# UFO Standard Model',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/feynml',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
