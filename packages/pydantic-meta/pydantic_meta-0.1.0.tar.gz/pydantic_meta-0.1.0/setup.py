# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_meta']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'pydantic-meta',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'VitailOG',
    'author_email': 'vzaharkiv28@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
