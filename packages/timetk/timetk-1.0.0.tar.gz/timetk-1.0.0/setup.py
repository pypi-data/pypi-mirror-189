# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timetk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'timetk',
    'version': '1.0.0',
    'description': 'time toolkit',
    'long_description': '',
    'author': 'wayfaring-stranger',
    'author_email': 'zw6p226m@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
