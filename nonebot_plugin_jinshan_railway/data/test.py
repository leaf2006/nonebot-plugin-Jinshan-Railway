# import json
# with open('nonebot-plugin-Jinshan-Railway/nonebot_plugin_jinshan_railway/data/station_data.json' , 'r' , encoding='utf-8') as station_data:
#     res_station_data = json.load(station_data)
# with open('nonebot-plugin-Jinshan-Railway/nonebot_plugin_jinshan_railway/data/train_data.json' , 'r' ,encoding='utf-8') as train_data:
#     data = json.load(train_data)

# inputer = "S1101"

# # 查询逻辑
# for train in data:
#     if train["train_number"] == inputer:
#         print(f"车次: {inputer}")
#         print(f"类型: {train['type']}")
#         print(f"停靠站: {train['stops']}")
#         break
# # 用inputer中的“S1201”查询这个json文件中关于这个车次的其他信息：如direction和departure，将这两个数据print出去。
# # bb = res_train_data['routes']['trains']
# # print(bb['S1101'])


import json

# # JSON数据
# data = [
#     {
#         "train_number": "S1001",
#         "type": "直达车",
#         "stops": [
#             { "station": "上海南", "arrival": None, "departure": "5:20" },
#             { "station": "金山卫", "arrival": "5:54", "departure": None }
#         ]
#     },
#     {
#         "train_number": "S1201",
#         "type": "站站停",
#         "stops": [
#             { "station": "上海南", "arrival": None, "departure": "5:50" },
#             { "station": "春申", "arrival": "6:00", "departure": "6:01" },
#             { "station": "新桥", "arrival": "6:09", "departure": "6:10" },
#             { "station": "车墩", "arrival": "6:17", "departure": "6:18" },
#             { "station": "叶榭", "arrival": "6:25", "departure": "6:26" },
#             { "station": "亭林", "arrival": "6:32", "departure": "6:33" },
#             { "station": "金山园区", "arrival": "6:39", "departure": "6:40" },
#             { "station": "金山卫", "arrival": "6:50", "departure": None }
#         ]
#     },
#     {
#         "train_number": "S1101",
#         "type": "大站车",
#         "stops": [
#             { "station": "上海南", "arrival": None, "departure": "6:18" },
#             { "station": "新桥", "arrival": "6:33", "departure": "6:34" },
#             { "station": "亭林", "arrival": "6:47", "departure": "6:48" },
#             { "station": "金山卫", "arrival": "7:01", "departure": None }
#         ]
#     }
# ]

# # 查询的车次
# inputer = "S1201"

# # 查询逻辑
# for train in data:
#     if train["train_number"] == inputer:
#         print(f"车次: {inputer}")
#         print(f"类型: {train['type']}")
#         print(f"停靠站: {train['stops']}")
#         break


with open('nonebot-plugin-Jinshan-Railway/nonebot_plugin_jinshan_railway/data/train_data.json', "r" , encoding="utf-8") as f:
    data = json.load(f)

# 避免覆盖内置函数名 `input`
query = "S1101"


# inputer = "S1201"

# # 查询逻辑
# for train in data:
#     if train[1]["train_number"] == inputer:
#         print(f"车次: {inputer}")
#         print(f"类型: {train['type']}")
#         print(f"停靠站: {train['stops']}")
#         break  
# 从 JSON 中取出 trains 列表并查找匹配的车次，打印类型和每个停靠站的详细信息
trains = data.get('routes', {}).get('trains', [])
for train in trains:
    if train.get('train_number') == query:
        print(f"车次: {query}")
        print(f"类型: {train.get('type')}")
        stops = train.get('stops', [])
        if stops:
            print("停靠站信息:")
            for i, stop in enumerate(stops, start=1):
                station = stop.get('station')
                arrival = stop.get('arrival')
                departure = stop.get('departure')
                print(f"  {i}. 站名: {station} | 到达: {arrival} | 发车: {departure}")
        else:
            print("停靠站: 无数据")
        break
else:
    print(f"未找到车次: {query}")