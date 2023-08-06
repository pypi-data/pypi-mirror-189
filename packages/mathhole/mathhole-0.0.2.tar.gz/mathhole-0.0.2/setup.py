# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mathhole']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mathhole',
    'version': '0.0.2',
    'description': "An extremely bad, unintelligent math library for a moron to learn. Please don't use and if you do, it is at your own risk.",
    'long_description': "# Mathhole\n\n[![codecov](https://codecov.io/gh/aaronclong/mathhole/branch/master/graph/badge.svg?token=JJMIWOX7IS)](https://codecov.io/gh/aaronclong/mathhole)\n\nAn extremely bad, unintelligent math library for a moron to learn.\nPlease don't use and if you do, it is at your own risk.",
    'author': 'Aaron Long',
    'author_email': 'aaron.long.c@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aaronclong/mathhole',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
