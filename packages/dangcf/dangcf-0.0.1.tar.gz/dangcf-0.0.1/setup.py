# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dangcf', 'dangcf.cfbypass']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.2.0,<3.0.0',
 'numpy>=1.22.2,<2.0.0',
 'replit>=3.2.4,<4.0.0',
 'urllib3>=1.26.12,<2.0.0']

setup_kwargs = {
    'name': 'dangcf',
    'version': '0.0.1',
    'description': 'DangCF is a simple python-based request package for getting around the fundamentals of Cloudflare challenges. ',
    'long_description': None,
    'author': 'beliefs',
    'author_email': 'bio@fbi.ac',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<3.11',
}


setup(**setup_kwargs)
