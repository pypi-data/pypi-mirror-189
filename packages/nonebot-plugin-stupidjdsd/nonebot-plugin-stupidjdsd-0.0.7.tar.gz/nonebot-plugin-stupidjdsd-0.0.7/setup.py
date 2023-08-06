#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='nonebot-plugin-stupidjdsd',
      version='0.0.7',
      description="nonebot-plugin-stupidjdsd",
      author='ShunYu',
      author_email='1265257855@qq.com',
      url='https://github.com/liu1272/nonebot-plugin-stupidjdsd',
      packages=find_packages(),
      install_requires=["requests", "urllib3","nonebot-adapter-onebot","nonebot2"],
     )
