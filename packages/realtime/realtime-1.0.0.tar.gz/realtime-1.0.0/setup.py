# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['realtime']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.1,<3.0.0',
 'typing-extensions>=4.2.0,<5.0.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'realtime',
    'version': '1.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'Joel',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
