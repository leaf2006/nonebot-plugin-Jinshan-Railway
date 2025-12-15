import json
import datetime  
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .data_loader import railway_data as rd # 导入数据

station_screen = on_command("大屏" , aliases={"dp"} , priority=6)
@station_screen.handle()  # 车站大屏
async def handle_station_screen(args: Message = CommandArg()):
    station_name_input = args.extract_plain_text()
    if not station_name_input:
        return

    res_station_screen = rd.parsed_station_data.get(station_name_input)
    if not res_station_screen:
        await station_screen.finish(f"{station_name_input} 站点暂无数据")
        return

    station_screen_details = ""

    special_stations = {"上海南", "金山卫"}

# 傻逼AI我操你妈
    for item in res_station_screen:
        train_code = item['车次']
        arrive_time = item.get('到达时间', 'null')
        departure_time = item.get('发车时间', 'null')

        # 统一处理 None 值，将其转换为 'null' 字符串
        if arrive_time is None:
            arrive_time = 'null'
        if departure_time is None:
            departure_time = 'null'

        if station_name_input in special_stations:
            if departure_time != "null":
                station_screen_details += f"{train_code}：{departure_time}开\n"
        elif station_name_input == "莘庄":
            if arrive_time == "null":
                station_screen_details += f"{train_code}：{departure_time}开\n"
            else:
                station_screen_details += f"{train_code}：{arrive_time}到，{departure_time}开\n"
        else:
            station_screen_details += f"{train_code}：{arrive_time}到，{departure_time}开\n"

    result = Message([
        f"{station_name_input}站:\n",
        station_screen_details,
    ])

    await station_screen.finish(result)