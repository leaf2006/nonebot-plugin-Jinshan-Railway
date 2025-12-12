# Copyright © Leaf developer 2023-2025
import json
# import datetime  
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .data_loader import railway_data as rd # 导入数据

train_number_info = on_command("车次" , aliases={"cc"} , priority=6 , block=True)

@train_number_info.handle() # 查询车次信息
async def handle_train_number_info(args:  Message = CommandArg()):
    if train_number_input := args.extract_plain_text():
        res_train_number = rd.parsed_train_data.get('routes', {}).get('trains', [])
        for train in res_train_number:
            if train.get('train_number') == train_number_input.upper():
                train_type = train.get('type')
                stops = train.get('stops', [])
                stops_result = ""
                if stops:
                    num = 1
                    for i, stop in enumerate(stops , start=1):
                        station = stop.get('station')
                        arrival = stop.get('arrival')
                        departure = stop.get('departure')
                        stops_result += str(station) + "：" + str(arrival) + "到，" + str(departure) + "开" + " \n"
                break
        
        train_number_info_result = Message([
            "🚝" , train_number_input , "次列车：\n",
            "类型：" , train_type , "\n \n",
            stops_result,"\n \n",
            "数据更新时间：",rd.parsed_station_data['schedule_effective_date']
        ]) # type:ignore
        
        await train_number_info.finish(train_number_info_result)
    else:
        await train_number_info.finish("未查询到该车次，请确认您输入的车次号为金山铁路列车！")
