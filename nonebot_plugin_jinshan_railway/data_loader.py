import json
class railway_data:
    # 载入金山铁路车站数据、列车数据json文件
    with open('nonebot_plugin_jinshan_railway/data/train_data.json', "r" ,encoding="utf-8") as file_train_data:
        parsed_train_data = json.load(file_train_data)

    with open('nonebot_plugin_jinshan_railway/data/station_data.json', "r" ,encoding="utf-8") as file_station_data:
        parsed_station_data = json.load(file_station_data)