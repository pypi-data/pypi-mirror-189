# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spyderml', 'spyderml.lib']

package_data = \
{'': ['*'], 'spyderml': ['bin/*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'colorama>=0.4.6,<0.5.0',
 'requests>=2.28.2,<3.0.0',
 'urllib3>=1.26.14,<2.0.0',
 'webtech>=1.3.2,<2.0.0']

entry_points = \
{'console_scripts': ['spyderml = main:main']}

setup_kwargs = {
    'name': 'spyder-ml',
    'version': '1.2.2',
    'description': 'A tool made to facilitate the analysis of html code.',
    'long_description': '<h1 align="center">Spyder-HTML</h1>\n\n<p align="center">\n<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>\n<img src="http://img.shields.io/static/v1?label=VERSION&message=1.2.2&color=blue&style=for-the-badge"/>\n<img src="https://img.shields.io/github/license/accessmaker/Spyder-ml?style=for-the-badge"/>\n</p>\n\n\nA tool made to facilitate the analysis of html code.\n\n<h2>INSTALL(git clone):</h2>\n\ngit clone https://github.com/accessmaker/Spyder-ml\n\npython setup.py install\n\n\n<h2>INSTALL(PIP):</h2>\n\n\npip install spyder-ml\n\n\n<h2>USAGE:</h2>\n\nspyderml [-h] [-t TARGET | -f FILE | --update]\n         [--tags TAGS | --comments | --attribs ATTRIBS | --getjs | --techs]\n         [-o OUTPUT]\n\nA tool made to facilitate the analysis of html code.\n\noptions:<br>\n  -h, --help            show this help message and exit<br>\n  -t TARGET, --target TARGET<br>\n                        Parameter that defines the target URL<\n                        http://example.com/index.html <br>\n  -f FILE, --file FILE  Parameter that defines target URLs<br>\n  --update              Flag responsible for updating the database.<br>\n  --tags TAGS           Flag that defines which tags the program will bring<br>\n  --comments            Flag that brings the comments<br>\n  --attribs ATTRIBS     Flag that defines which attributes the application\n                        will look for.<br>\n  --getjs               Flag that brings all JS files from the page.<br>\n  --techs               Flag trying to discover the technologies of the page.<br>\n  -o OUTPUT, --output OUTPUT\n                        Flag that defines in which file the command output\n                        will be saved.<br>\n\n\'Functionality\': It searches the html document for specific things',
    'author': 'Lucas dSilva',
    'author_email': 'accessmaker.mlbb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/accessmaker/Spyder-ml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
