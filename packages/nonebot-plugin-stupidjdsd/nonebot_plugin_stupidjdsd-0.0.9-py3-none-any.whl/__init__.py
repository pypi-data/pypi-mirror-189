'''
Author: 顺虞
Date: 2023-02-04
Help: https://github.com/liu1272/nonebot-plugin-stupidjdsd/
QQ: 1265257855
'''


import nonebot
import subprocess
from pathlib import Path
from .config import Config
from nonebot import get_driver
from nonebot import on_keyword
from nonebot.adapters.onebot.v12 import GroupMessageEvent,MessageEvent,Bot,Message,MessageSegment,Event



global_config = get_driver().config
config = Config.parse_obj(global_config)



jdsd = on_keyword({'经典诵读','jdsd'})
@jdsd.handle()
async def sj():
    #下面两个路径中选择一个，默认选择Script.py也就是没有匹配功能的脚本
    p = subprocess.Popen(r"Script.py", shell=True)
    # p = subprocess.Popen(r"Original_Script.py", shell=True)
    zhungtaima = p.wait()
    if zhungtaima != 1:
        msg = 'FINISH!'
    else:
        msg = 'ERROR!'
    await jdsd.finish(Message(f'{msg}'))


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve())
)
