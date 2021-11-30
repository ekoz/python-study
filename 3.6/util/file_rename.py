#!/usr/bin/env python
# encoding: utf-8

"""
微信或QQ里保存的文件名称是时间戳，将时间戳重命名为日期开头的文件名
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: file_rename.py
@use file_rename.py "your_dir_path" or file_rename.py "your_dir_path" 1
@time: 2019/4/9 12:10
"""
import sys
import os
import time


def walk(path_list):
    """
    遍历 path_list 的路径下的所有文件，将文件中是日期时间戳的文件名称改成yyyyMMddHHmmss这种格式
    :param path_list:
    :return:
    """
    i = 0
    if len(path_list) == 0:
        return
    path = path_list[0]
    is_fmt_by_ctime = False
    if len(path_list) == 2 and path_list[1] == "1":
        # 参数强制采用 ctime 重命名
        is_fmt_by_ctime = True
    if os.path.exists(path):
        # print(path)
        fs = os.listdir(path)
        for f in fs:
            # 文件名不包含 -
            if f.find("-") == -1 or is_fmt_by_ctime:
                if is_fmt_by_ctime:
                    dt = time.localtime(fmt_prefix_by_ctime(path, f))
                elif f.find("mmexport") == 0:
                    # 文件名以 mmexport 开头
                    # 微信保存的图片已 mmexport 开头
                    try:
                        dt = time.localtime(int(f[8:].split(".")[0]) / 1000)
                    except:
                        # 当前文件名不是时间戳，根据日期来重命名
                        dt = time.localtime(fmt_prefix_by_ctime(path, f))
                elif f.find("20") == 0:
                    # 文件名称是已 2019 或 2020 年月日开头，不作处理
                    continue
                elif f.find("IMG_") == 0 or f.find("VID_") == 0:
                    # 手机拍照以 IMG_ 开头
                    # 视频文件名以 VID_ 开头
                    new_name = f[4:]
                    old_path = path + "\\" + f
                    new_path = path + "\\" + new_name
                    os.rename(old_path, new_path)
                    continue
                elif f.find("微信图片_") == 0:
                    # 微信图片_转存以这四个字开头
                    fmt_prefix(path, f, "微信图片_")
                    # 202106041453135
                    # 2021-06-04_14.53.13.5
                    continue
                elif f.find("_DSC") == 0:
                    # 单反相机拍摄出来的照片以 _DSC 开头，忘记了是佳能还是尼康。。
                    # 实现方案：获取照片的创建日期和修改日期，取最小值，注意：修改日期不一定大于创建日期
                    dt = time.localtime(fmt_prefix_by_ctime(path, f))
                # elif len(f) > 17:
                #     # 文件名不是时间戳，时间戳是13位，加上 .mp4 或者 .jpg 是 4 位
                #     continue
                else:
                    # 时间戳文件名
                    try:
                        dt = time.localtime(int(f.split(".")[0]) / 1000)
                    except:
                        # 当前文件名不是时间戳，根据日期来重命名
                        dt = time.localtime(fmt_prefix_by_ctime(path, f))

                dt_str = time.strftime("%Y-%m-%d_%H.%M.%S", dt)
                new_name = dt_str + "." + get_extension(f)

                old_path = path + "\\" + f
                new_path = path + "\\" + new_name
                if os.path.exists(new_path):
                    i = i + 1
                    new_path = path + "\\" + dt_str + str(i) + "." + get_extension(f)
                os.rename(old_path, new_path)
            elif f.find("Screenshot_") == 0:
                # 手机截屏文件名前缀
                fmt_prefix(path, f, "Screenshot_")
                continue
    else:
        print(path + " is not directory.")


def fmt_prefix_by_ctime(path, file_name):
    """
    根据文件的创建时间和修改时间，来重命名文件
    :param path:
    :param file_name:
    :return:
    """
    file_path = path + "\\" + file_name
    # os.path.getctime(file_path) 1601208283.1814914
    # os.path.getmtime(file_path) 1601208283.1814914
    return int(min(os.path.getctime(file_path), os.path.getmtime(file_path)))


def fmt_prefix(path, file_name, prefix):
    """
    根据前缀格式化文件名，移除前缀，保留后面的文本
    :param path:
    :param file_name:
    :param prefix:
    :return:
    """
    new_name = file_name[len(prefix) :]
    new_name = fmt_filename(new_name)
    old_path = path + "\\" + file_name
    new_path = path + "\\" + new_name
    os.rename(old_path, new_path)


def fmt_filename(new_name):
    """
    重新包装文件名
    :param new_name:
    :return:
    """
    # .jpg
    extension = new_name[new_name.rfind(".") :]
    # 20210604145
    base_name = new_name[0 : new_name.rfind(".")]
    base_name = base_name.strip()
    if len(base_name) > 8:
        new_base_name = (
            base_name[0:4]
            + "-"
            + base_name[4:6]
            + "-"
            + base_name[6:8]
            + "_"
            + join_str_with_dot(base_name[8:])
        )
    else:
        new_base_name = base_name
    return new_base_name + extension


def join_str_with_dot(tmp_str):
    """
    用西文点 . 作为连接符连接字符串
    :param tmp_str:
    :return:
    """
    tmp_arr = []
    for n in range(len(tmp_str)):
        if n % 2 == 0:
            tmp_arr.append(tmp_str[n : n + 2])
    return ".".join(tmp_arr)


def get_extension(fname):
    """
    根据文件名获取后缀
    :param fname: 2021--1-1-_30.-2.0-.59.-1.9-.17.2_.co.m..te.nc.en.t..mm.jpg or 16546275112.jpg
    :return:
    """
    if fname.find(".") != -1:
        return fname.rsplit(".", 1)[1]
    else:
        return fname


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    walk(sys.argv[1:])
