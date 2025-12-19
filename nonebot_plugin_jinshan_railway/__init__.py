# Copyright © Leaf developer 2023-2025

from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from .config import Config
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .train_number_info import handle_train_number_info
from .station_screen import handle_station_screen
# import nonebot_plugin_jinshan_railway.train_number_info
# import nonebot_plugin_jinshan_railway.help
# __plugin_meta__ = PluginMetadata(
#     name="nonebot_plugin_jinshan_railway",
#     description="",
#     usage="",
#     config=Config,
# )

# config = get_plugin_config(Config)

information_helper = on_command("help" , aliases={"帮助"} , priority=6 , block=True)

@information_helper.handle()
async def handle_helper():
    information_Helper_message = Message([
        "这是基于Nonebot2的很实用的金山铁路机器人，可以查询金山铁路列车车次详细信息、车站当日列车时刻表，将车站大屏公交化显示 \n",
        "使用方法：\n",
        "------------------------------ \n",
        "/小火车 [金山铁路列车车次] 或 /xhc [金山铁路列车车次] ： 通过车次查询该列车详细信息 \n",
        "/车站 [金山铁路车站名称] 或 /cz [金山铁路车站名称] ： 通过车站名称查看该车站大屏 \n",
        "------------------------------",
    ])

    await information_helper.finish(information_Helper_message)
                         
