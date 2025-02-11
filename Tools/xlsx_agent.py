# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2025/2/10 14:20
# 按规则读取 Excel 内容，并转成 json 数组格式

import pandas as pd
import json
import glob
import os

# 定义 json key
custom_keys = [
    "grade",
    "name",
    "gender",
    "id_card_no",
    "practice",
    "dorm",
    "phone",
    "phone_parents",
    "phone_contact",
    "remark",
]


excel_path = "2025年春季学期实习学生去向表（22级-信息部）.xlsx"


def load_data_by_folder(xls_folder_path):
    """
    根据指定的文件夹读取Excel内容并返回一个列表
    :param xls_folder_path:
    :return:
    """
    result = []
    xls_files = glob.glob(os.path.join(xls_folder_path, "*.xlsx"))
    for file_path in xls_files:
        try:
            # 自动选择合适的引擎
            result = result + load_data_by_xls(file_path)
        except Exception as e:
            print(f"读取文件 {os.path.basename(file_path)} 时出错：{e}")
    return result


def load_data_by_xls(xls_path):
    """
    根据指定的 Excel 路径，读取首个Sheet页内容，返回一个列表
    :param xls_path:
    :return:
    """
    result = []
    df = pd.read_excel(xls_path, header=3, dtype=str, keep_default_na=False)

    data_dict = []
    for index, row in df.iterrows():
        data_dict.append({custom_keys[i]: row[i] for i in range(len(custom_keys))})

    result = result + data_dict
    return result


def load_data_by_xls_multi(xls_path):
    """
    根据指定的 Excel 路径，读取全部 sheet 页面得内容，返回一个列表
    :param xls_path:
    :return:
    """
    result = []
    xls = pd.ExcelFile(xls_path)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(
            xls_path, sheet_name=sheet_name, header=3, dtype=str, keep_default_na=False
        )

        data_dict = []
        for index, row in df.iterrows():
            data_dict.append(
                {custom_keys[i]: str(row[i]) for i in range(len(custom_keys))}
            )

        result = result + data_dict

    return result


# json_data = json.dumps(load_data_by_xls(excel_path), ensure_ascii=False, indent=2)

json_data = json.dumps(
    load_data_by_folder("./20250210"),
    ensure_ascii=False,
    indent=2,
)

print(json_data)
