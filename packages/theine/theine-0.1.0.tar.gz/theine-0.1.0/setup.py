# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['theine']

package_data = \
{'': ['*']}

install_requires = \
['cacheme-utils>=0.1.2,<0.2.0', 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'theine',
    'version': '0.1.0',
    'description': 'high performance in-memory cache',
    'long_description': '# theine\nhigh performance in-memory cache\n',
    'author': 'Yiling-J',
    'author_email': 'njjyl723@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
