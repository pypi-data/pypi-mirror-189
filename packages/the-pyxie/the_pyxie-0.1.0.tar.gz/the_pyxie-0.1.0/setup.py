# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['the_pyxie']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'the-pyxie',
    'version': '0.1.0',
    'description': 'Pyxie might help you with html',
    'long_description': '',
    'author': 'Daniel Konopka',
    'author_email': 'pyxie@konopka.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
