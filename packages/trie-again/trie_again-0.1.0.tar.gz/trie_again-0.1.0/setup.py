# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trie_again']

package_data = \
{'': ['*']}

install_requires = \
['setuptools>=66.1.1,<67.0.0']

setup_kwargs = {
    'name': 'trie-again',
    'version': '0.1.0',
    'description': 'Trie data structure for prefix search and text completion',
    'long_description': '# Trie Again: Python Trie implementation optimized for T9 completion\n\n\n## Installation\n\n```bash\n\npip install trie-again\n\n```\n',
    'author': 'Egor Blagov',
    'author_email': 'e.m.blagov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
