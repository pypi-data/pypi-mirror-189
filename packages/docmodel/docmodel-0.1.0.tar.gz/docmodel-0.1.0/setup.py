# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['docmodel']

package_data = \
{'': ['*']}

install_requires = \
['parsel>=1.6.0,<2.0.0', 'pre-commit>=3.0.4,<4.0.0']

setup_kwargs = {
    'name': 'docmodel',
    'version': '0.1.0',
    'description': '',
    'long_description': '# docmodel\n',
    'author': 'lhaze',
    'author_email': 'lhaze@lhaze.name',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
