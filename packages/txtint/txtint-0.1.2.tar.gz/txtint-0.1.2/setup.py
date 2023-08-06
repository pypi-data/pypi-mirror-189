# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['txt']
install_requires = \
['argcomplete>=2.0.0,<3.0.0', 'rich>=13.2.0,<14.0.0']

setup_kwargs = {
    'name': 'txtint',
    'version': '0.1.2',
    'description': 'tools for metamodern text interfaces',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ragt.ag/code/projects/txtint',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
