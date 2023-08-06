# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fakepack']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['fake = fakepack.fakepack:fake']}

setup_kwargs = {
    'name': 'fakepack',
    'version': '0.0.2',
    'description': 'Fake packaging',
    'long_description': None,
    'author': 'zae-park',
    'author_email': 'tom941105@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
