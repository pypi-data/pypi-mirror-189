import nonebot
import subprocess
from pathlib import Path
from .config import Config
from nonebot import get_driver
from nonebot import on_keyword
from nonebot.adapters.onebot.v12 import GroupMessageEvent,MessageEvent,Bot,Message,MessageSegment,Event



global_config = get_driver().config
config = Config.parse_obj(global_config)



# ———————————————————————————————————凌晨之后超时无回显的经典诵读FUCK功能—————————————————————————————————
jdsd = on_keyword({'FUCKJDSD','经典诵读刷分','fuckjdsd'})
@jdsd.handle()
async def sj():
    p = subprocess.Popen(r"Python C:\Users\12652\Desktop\QQbot\QQbot\src\plugins\经典诵读\jdsd_org.py", shell=True)
    zhungtaima = p.wait()
    if zhungtaima != 1:
        msg = 'FINISH! 获得21分'
    else:
        msg = 'ERROR! 请联系SUPERUSER'
    await jdsd.finish(Message(f'{msg}'))


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve())
)

