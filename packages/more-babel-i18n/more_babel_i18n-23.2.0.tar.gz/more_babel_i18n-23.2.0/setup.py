# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['more', 'more.babel_i18n']

package_data = \
{'': ['*']}

install_requires = \
['Babel>=2.11.0,<3.0.0', 'Jinja2>=3.1.2,<4.0.0', 'morepath>=0.19,<0.20']

setup_kwargs = {
    'name': 'more-babel-i18n',
    'version': '23.2.0',
    'description': 'i18n/l10n support for Morepath applications and Jinja2 templates',
    'long_description': "more.babel_i18n\n===============\n\nWARNING: This is an early version that works for me. Please don't rely on it ;)\n\nInternationalization and localization (i18n / l10n) support for Morepath applications based on [Babel](https://github.com/python-babel/babel).\nMost code is taken from the flask-babel(super) project.\n",
    'author': 'Tobias dpausp',
    'author_email': 'dpausp@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/edemocracy/more.babel_i18n',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
