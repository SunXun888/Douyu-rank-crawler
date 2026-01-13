import requests
import json
import pandas as pd
import copy

# ===================== 请求链接拿到原始数据 =====================
rank_type = [
   #网游竞技,单机热游,手游休闲,娱乐天地,颜值,科技文化,语音互动,语音直播   
    "PCgame", "djry", "syxx", "yl", "yz", "kjwh", "yp", "voice"
]
url = "https://www.douyu.com/directory/rank_list/" + "根据需求自行替换rank_type里面的字符串"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
resp = requests.get(url=url,headers=headers)
data_json = resp.text
# print(resp.text)

# ===================== 处理多余的数据，留下关键的json列表 =====================
key_index = data_json.find("rankList")
ranklist_json1 = data_json[key_index:]
ranklist_json2 = ranklist_json1[:-1021]
# print(ranklist_json2)
ranklist_json = '{' + '"' + ranklist_json2 + '}'
# print(ranklist_json)
# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write(ranklist_json) 
rankList = json.loads(ranklist_json)
print(rankList)

# ===================== 对各种榜单进行分类 =====================
# 周榜
rank_user_weekList =rankList["rankList"]["userList"]["weekList"]  #用户活跃榜
rank_contribute_weekList =rankList["rankList"]["contributeList"]["weekList"]  #主播真友榜
rank_anchor_weekList =rankList["rankList"]["anchorList"]["weekList"]  #巨星主播榜
# 日榜
rank_user_dayList =rankList["rankList"]["userList"]["dayList"]  #用户活跃榜
rank_contribute_dayList =rankList["rankList"]["contributeList"]["dayList"]  #主播真友榜
rank_anchor_dayList =rankList["rankList"]["anchorList"]["dayList"]  #巨星主播榜
#  月榜
rank_user_monthList =rankList["rankList"]["userList"]["monthList"]  #用户活跃榜
rank_contribute_monthList =rankList["rankList"]["contributeList"]["monthList"]  #主播真友榜
rank_anchor_monthList =rankList["rankList"]["anchorList"]["monthList"]  #巨星主播榜
# 主播粉丝榜
rank_fans_intimacyList =rankList["rankList"]["fansList"]["intimacyList"]  #周亲密度榜
rank_fans_newAddList =rankList["rankList"]["fansList"]["newAddList"]  #周新增数榜
# print(rank_fans_newAddList)

# ===================== 处理用户活跃榜单个用户数据 =====================
def process_userList_single_user(user_dict):
    flattened_user = copy.deepcopy(user_dict)
    # 处理growthInfo嵌套字段
    if 'growthInfo' in flattened_user:
        growth_info = flattened_user.pop('growthInfo')
        for sub_key, sub_value in growth_info.items():
            flattened_user[f'growthInfo_{sub_key}'] = sub_value
    # 补充缺失字段（保证所有用户字段一致，Excel列不混乱）
    default_fields = {
        'uid': '', 'gx': 0, 'number': '', 'level': 0,
        'nickname': '未知用户', 'noble_lvl': '0', 'statu': '0',
        'avatar': '', 'id': '', 'title': '', 'ttl': 0
    }
    for field, default_val in default_fields.items():
        if field not in flattened_user:
            flattened_user[field] = default_val

    return flattened_user
# ===================== 处理主播真友榜单个用户数据 =====================
def process_contributeList_single_user(user_dict):
    flattened_user = copy.deepcopy(user_dict)
    # 处理anchorLevelInfo嵌套字段
    if 'anchorLevelInfo' in flattened_user:
        anchorLevel_Info = flattened_user.pop('anchorLevelInfo')
        for sub_key, sub_value in anchorLevel_Info.items():
            flattened_user[f'anchorLevelInfo_{sub_key}'] = sub_value
    # 处理growthInfo嵌套字段
    if 'growthInfo' in flattened_user:
        growth_info = flattened_user.pop('growthInfo')
        for sub_key, sub_value in growth_info.items():
            flattened_user[f'growthInfo_{sub_key}'] = sub_value
    # 补充缺失字段（保证所有用户字段一致，Excel列不混乱）
    default_fields = {
        'room_id': '', 'uavatar': '', 'level': 0, 'is_stealth': 0, 
        'vipId': 0, 'noble_lvl': '', 'statu': '', 'avatar': '',
        'anickname': '', 'title': '', 'ttl': 0, 'catagory': '',
        'uid': '', 'gx': 0, 'owner_uid': '', 'id': 0, 'unickname': ''
    }
    for field, default_val in default_fields.items():
        if field not in flattened_user:
            flattened_user[field] = default_val

    return flattened_user
# ===================== 处理巨星主播榜单个用户数据 =====================
def process_anchorList_single_user(user_dict):
    flattened_user = copy.deepcopy(user_dict)
    # 处理anchorLevelInfo嵌套字段
    if 'anchorLevelInfo' in flattened_user:
        anchorLevel_Info = flattened_user.pop('anchorLevelInfo')
        for sub_key, sub_value in anchorLevel_Info.items():
            flattened_user[f'anchorLevelInfo_{sub_key}'] = sub_value
    # 补充缺失字段（保证所有用户字段一致，Excel列不混乱）
    default_fields = {
        'room_id': '', 'vipId': 0, 'statu': '', 'avatar': '', 
        'title': '', 'ttl': 0, 'sc': 0, 'catagory': '',
        'uid': '', 'nickname': '', 'is_live': False, 'id': 0
    }
    for field, default_val in default_fields.items():
        if field not in flattened_user:
            flattened_user[field] = default_val

    return flattened_user
# ===================== 处理主播粉丝榜周亲密度榜单个用户数据 =====================
def process_fansList_intimacyList_single_user(user_dict):
    flattened_user = copy.deepcopy(user_dict)
    # 补充缺失字段（保证所有用户字段一致，Excel列不混乱）
    default_fields = {
        'ci': '', 'vipId': 0, 'statu': '', 'avatar': '', 
        'anickname': '', 'title': '', 'rid': '', 'ttl': 0, 
        'week_num': 0, 'catagory': '', 'nrt': 0, 'isVertical': False, 
        'owner_uid': '0', 'is_live': True, 'totlo_fans_num': 0, 'idx': 0, 
        'fans_text': ''
    }
    for field, default_val in default_fields.items():
        if field not in flattened_user:
            flattened_user[field] = default_val

    return flattened_user
# ===================== 处理主播粉丝榜周新增数榜单个用户数据 =====================
def process_fansList_newAddList_single_user(user_dict):
    flattened_user = copy.deepcopy(user_dict)
    # 补充缺失字段（保证所有用户字段一致，Excel列不混乱）
    default_fields = {
        'week_num_ci': '', 'ci': '', 'vipId': 0, 'statu': '', 
        'avatar': '', 'anickname': '', 'title': '', 'rid': '', 
        'ttl': 0, 'week_num': 0, 'catagory': '', 'nrt': 0, 
        'isVertical': False, 'owner_uid': '', 'is_live': False, 
        'totlo_fans_num': 0, 'idx': 0, 'fans_text': ''
    }
    for field, default_val in default_fields.items():
        if field not in flattened_user:
            flattened_user[field] = default_val

    return flattened_user
# ===================== 封装通用的Excel导出函数（核心） =====================
def export_data_to_excel(data_list, process_func, excel_filename):
    # 批量处理数据
    processed_data = []
    for item in data_list:
        try:
            # 调用传入的处理函数，处理单个数据
            processed_item = process_func(item)
            processed_data.append(processed_item)
        except Exception as e:
            print(f"警告：处理单个数据时出错，跳过该数据 | 错误信息：{e}")
            continue
    
    # 导出Excel
    if processed_data:
        df = pd.DataFrame(processed_data)
        df.to_excel(excel_filename + ".xlsx", index=False, engine='openpyxl')
        print(f"成功导出 {len(processed_data)} 条数据到：{excel_filename + '.xlsx'}")
    else:
        print("无有效数据可导出！")


# 直接调用export_data_to_excel()函数即可
# data_list为原始数据，process_func为处理单个用户数据函数，excel_filename为导出的文件名


# ===================== 示例 =====================
# export_data_to_excel(rank_fans_intimacyList,process_fansList_newAddList_single_user,"主播粉丝榜周新增数榜")
