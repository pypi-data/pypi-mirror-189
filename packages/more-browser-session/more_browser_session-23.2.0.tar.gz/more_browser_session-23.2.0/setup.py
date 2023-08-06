# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['more', 'more.browser_session']

package_data = \
{'': ['*']}

install_requires = \
['Werkzeug>=2.2.2,<3.0.0', 'itsdangerous>=2.1.2,<3.0.0', 'morepath>=0.19,<0.20']

setup_kwargs = {
    'name': 'more-browser-session',
    'version': '23.2.0',
    'description': 'Session support for Morepath applications',
    'long_description': "more.browser_session\n====================\n\nWARNING: This is an early version that works for me. Please don't rely on it ;)\n\nImplements (HTTP, browser) session support for Morepath applications based on cookies signed by itsdangerous.\nMost code is taken from the Flask project.\n\nThe session data is signed, not encrypted! Don't store sensitive data in the session!\nSupport for encryption will be added soon.\n",
    'author': 'Tobias dpausp',
    'author_email': 'dpausp@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/edemocracy/more.browser_session',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
