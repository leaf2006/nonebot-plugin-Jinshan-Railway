import json
import datetime  
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .data_loader import railway_data as rd # 导入数据

station_screen = on_command("车站" , aliases={"cz"} , priority=6)

@station_screen.handle()  # 车站大屏
async def handle_station_screen(args: Message = CommandArg()):
    station_name_input = args.extract_plain_text()

    now_Time = datetime.datetime.now().strftime("%H:%M") # 将当前时间格式化为xx:xx

    if not station_name_input:
        return

    res_station_screen = rd.parsed_station_data.get(station_name_input)
    res_train_data = rd.parsed_train_data
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
        if int(train_code[-1]) % 2 == 0:
            direction = "上行（市区方向）"
        else:
            direction = "下行（金山卫方向）"


        # 统一处理 None 值，将其转换为 'null' 字符串
        if arrive_time is None:
            arrive_time = 'null'
        if departure_time is None:
            departure_time = 'null'
        if departure_time >= now_Time:
            if station_name_input in special_stations:
                if departure_time != "null":
                    station_screen_details += f"{train_code}，{direction}：{departure_time}开\n"
            elif station_name_input == "莘庄":
                if arrive_time == "null":
                    station_screen_details += f"{train_code}，{direction}：{departure_time}开\n"
                elif departure_time == "null":
                    pass
                else:
                    station_screen_details += f"{train_code}，{direction}：{arrive_time}到，{departure_time}开\n"
            else:
                station_screen_details += f"{train_code}，{direction}：{arrive_time}到，{departure_time}开\n"
        else:
            pass


    result = Message([
        f"🚉{station_name_input}站列车信息:\n",
        "------------------------------ \n",
        station_screen_details,
        "------------------------------ \n",
        "数据更新时间：",rd.parsed_train_data['schedule_effective_date'] # 车站数据里忘了搞数据更新时间了，反正两个我都是一块更新的，用车次数据里的凑合凑合用吧

    ])

    await station_screen.finish(result)