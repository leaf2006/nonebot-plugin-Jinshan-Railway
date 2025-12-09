# Copyright © Leaf developer 2023-2025
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore

information_helper = on_command("help" , aliases={"帮助"} , priority=6 , block=True)

@information_helper.handle()
async def helper():
    information_Helper_message = Message([
        "这是基于Nonebot2的很实用的金山铁路机器人，可以查询金山铁路列车车次详细信息、车站当日列车时刻表，将车站大屏公交化显示",
    ])

    await information_helper.finish(information_Helper_message)