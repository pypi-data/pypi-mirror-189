#!/usr/bin/env python

from distutils.core import setup

packages = \
['src']

install_requires = \
['requests',
 'urllib3',
 'nonebot-adapter-onebot',
 'nonebot2>=2.0.0-rc.2,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-stupidjdsd',
    'version': '0.0.8',
    'description': 'nonebot-plugin-stupidjdsd',
    'author': 'ShunYu',
    'author_email': '1265257855@qq.com',
    'url': 'https://github.com/liu1272/nonebot-plugin-stupidjdsd',
    'packages': packages,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)