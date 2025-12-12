# Copyright © Leaf developer 2023-2025
#   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from .config import Config
from .help import handle_helper
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

                         
