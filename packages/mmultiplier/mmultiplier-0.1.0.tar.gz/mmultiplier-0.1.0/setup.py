# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mmultiplier']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mmultiplier',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Mohamad Nosratian',
    'author_email': 'mohn.info@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
