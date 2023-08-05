# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tensortrans']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tensortrans',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Adi Gudimella',
    'author_email': 'adgudime@microsoft.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
