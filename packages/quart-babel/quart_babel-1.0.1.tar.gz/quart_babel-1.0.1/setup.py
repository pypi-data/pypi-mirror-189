# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quart_babel']

package_data = \
{'': ['*']}

install_requires = \
['Babel>=2.11.0,<3.0.0',
 'asgi-tools>=0.64.8,<0.65.0',
 'importlib-metadata>=6.0.0,<7.0.0',
 'ipapi>=1.0.4,<2.0.0',
 'quart>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'quart-babel',
    'version': '1.0.1',
    'description': 'Implements i18n and l10n support for Quart.',
    'long_description': '# Quart Babel\n\n![Quart Uploads Logo](logos/logo.png)\n\nImplements i18n and l10n support for Quart.  This is based on the Python\n[babel][] module as well as [pytz][] both of which are installed automatically\nfor you if you install this library.\n\nThe original code for this extension was taken from Flask-Babel and Flask-BabelPlus. \nFlask-Babel can be found [here][flask-babel] and Flask-BabelPlus can be found \n[here][flask-babelplus]\n\n# Installation \n\nInstall the extension with the following command:\n\n    $ pip3 install quart-babel\n\n# Usage\n\nTo use the extension simply import the class wrapper and pass the Quart app \nobject back to here. Do so like this:\n\n    from quart import Quart\n    from quart_babel import Babel \n\n    app = Quart(__name__)\n    babel = Babel(app)\n\n\n# Documentation\n\nThe for Quart-Babel and is available [here][docs].\n\n[babel]: https://github.com/python-babel/babel\n[pytz]: https://pypi.python.org/pypi/pytz/\n[flask-babel]: https://flask-babel.tkte.ch/\n[flask-babelplus]: https://github.com/sh4nks/flask-babelplus\n[docs]: https://quart-babel.readthedocs.io\n',
    'author': 'Chris Rood',
    'author_email': 'quart.addons@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
