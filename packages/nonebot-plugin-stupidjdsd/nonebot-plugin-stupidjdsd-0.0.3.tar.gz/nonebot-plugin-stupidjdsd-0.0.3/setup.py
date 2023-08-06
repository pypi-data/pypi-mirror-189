#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "nonebot-plugin-stupidjdsd",      #这里是pip项目发布的名称
    version = "0.0.3",  #版本号，数值大的会优先被pip
    keywords = ["pip", "nonebot-plugin-stupidjdsd"],			# 关键字
    description = "ShunYu's package.",	# 描述
    long_description = "ShunYu's package.",
    license = "MIT Licence",		# 许可证

    url = "https://github.com/liu1272/nonebot-plugin-stupidjdsd",     #项目相关文件地址，一般是github项目地址即可
    author = "ShunYu",			# 作者
    author_email = "1265257855@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests", "urllib3","nonebot-adapter-onebot","nonebot2"]          #这个项目依赖的第三方库
)
