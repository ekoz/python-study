#!/usr/bin/env python
# encoding: utf-8

"""
微信或QQ里保存的文件名称是时间戳，将时间戳重命名为日期开头的文件名
1. 微信保存的图片名称以 mmexport 开头
2. 手机拍照以 IMG_ 开头，IMG_20211017_175100.jpg
3. 视频文件名以 VID_ 开头，VID_20211001_102301.mp4
4. PC微信保存图片以 微信图片_ 开头
5. 单反相机拍摄的照片以 _DSC 开头
6. 其他类型建议按照文件创建时间或修改时间的最小值来重命名
6.1. 20211114_142952.jpg

@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: file_rename.py
@use file_rename.py "your_dir_path" or file_rename.py "your_dir_path" 1
@time: 2019/4/9 12:10
"""
import os
import time
import click
import re


def walk(dir_path, subdir, ctime_mode):
    """
    遍历 dir_path 的路径下的所有文件，将文件中是日期时间戳的文件名称改成 yyyy-MM-dd_HH.mm.ss 这种格式
    :param dir_path:
    :param subdir:
    :param ctime_mode:
    :return:
    """
    i = 0
    path = dir_path
    is_fmt_by_ctime = ctime_mode == 1
    if os.path.exists(path):
        fs = os.listdir(path)
        for f in fs:
            if os.path.isdir(path + "\\" + f):
                if subdir == 1:
                    # 包含子目录，进入下级目录处理
                    walk(path + "\\" + f, subdir, ctime_mode)
                continue
            # 文件名不包含 -，包含 - 一般都是已经处理好了的图片
            if f.find("-") == -1 or match(f) or is_fmt_by_ctime:
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
                    # 文件名称是已 2019 或 2020 年月日开头
                    if match(f):
                        # 处理 20211114_142952.jpg 的文件
                        new_name = fmt_ymd(f)
                        rename(path, f, new_name)
                    elif match2(f):
                        # 处理 20211114142952.jpg 的文件
                        new_name = fmt_ymd2(f)
                        rename(path, f, new_name)
                    continue
                elif f.find("IMG_") == 0 or f.find("VID_") == 0:
                    # 手机拍照以 IMG_ 开头
                    # 视频文件名以 VID_ 开头
                    new_name = f[4:]
                    new_name = fmt_ymd(new_name)
                    rename(path, f, new_name)
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
            + concat(base_name[8:])
        )
    else:
        new_base_name = base_name
    return new_base_name + extension


def concat(tmp_str):
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


def get_extension(f_name):
    """
    根据文件名获取后缀
    :param f_name: 2021--1-1-_30.-2.0-.59.-1.9-.17.2_.co.m..te.nc.en.t..mm.jpg or 16546275112.jpg
    :return:
    """
    if f_name.find(".") != -1:
        return f_name.rsplit(".", 1)[1]
    else:
        return f_name


def match(f_name):
    """
    判断当前文件名格式是否是 20211114_142952.jpg 或 20211114-142952.jpg
    :param f_name:
    :return:
    """
    return re.match("^[0-9]{8}(_|-)[0-9]{6}.\S", f_name)


def fmt_ymd(f_name):
    """
    如果当前文件名是 20211114_142952.jpg，那么整理成 2021-11-14_14.29.52.jpg
    :param f_name:
    :return:
    """
    if match(f_name):
        # .jpg
        extension = f_name[f_name.rfind(".") :]
        # 20210604145
        base_name = f_name[0 : f_name.rfind(".")]
        base_name = base_name.strip()
        new_base_name = (
            base_name[0:4]
            + "-"
            + base_name[4:6]
            + "-"
            + base_name[6:8]
            + "_"
            + concat(base_name[9:])
        )
        return new_base_name + extension
    else:
        return f_name


def match2(f_name):
    """
    判断当前文件名格式是否是 20200119124914.jpg
    :param f_name:
    :return:
    """
    return re.match("^([0-9]{10}|[0-9]{12}|[0-9]{14})\.\S", f_name)


def fmt_ymd2(f_name):
    """
    如果当前文件名是 20200119124914.jpg，那么整理成 2021-11-14_14.29.52.jpg
    :param f_name:
    :return:
    """
    if match2(f_name):
        # .jpg
        extension = f_name[f_name.rfind(".") :]
        # 20200119124914
        base_name = f_name[0 : f_name.rfind(".")]
        base_name = base_name.strip()
        new_base_name = (
            base_name[0:4]
            + "-"
            + base_name[4:6]
            + "-"
            + base_name[6:8]
            + "_"
            + concat(base_name[8:])
        )
        return new_base_name + extension
    else:
        return f_name


def rename(path, old_name, new_name):
    """
    相同路径下的文件重命名
    :param path:
    :param old_name:
    :param new_name:
    :return:
    """
    old_path = path + "\\" + old_name
    new_path = path + "\\" + new_name
    os.rename(old_path, new_path)


@click.command()
@click.option(
    "--dir_path",
    prompt="请输入待整理的磁盘路径，如：D:/Pictures/秋宝宝",
    help="输入待整理的磁盘路径，如：D:/Pictures/秋宝宝",
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "--subdir",
    required=False,
    default="0",
    prompt="是否包含子目录，1-是，否-0，默认为否",
    help="是否包含子目录，1-是，否-0，默认为否",
    type=click.Choice(["1", "0", ""]),
)
@click.option(
    "--ctime_mode",
    required=False,
    default="0",
    prompt="是否强制按文件时间戳转换，1-是，否-0，默认为否",
    help="是否强制按文件时间戳转换，1-是，否-0，默认为否",
    type=click.Choice(["1", "0", ""]),
)
def click_walk(dir_path, subdir, ctime_mode):
    click.echo(f"\n当前待扫描的磁盘路径是 {dir_path} ")

    if int(subdir) == 0:
        click.echo("本次扫描不包含子目录")
    else:
        click.echo("本次扫描包含子目录")

    if int(ctime_mode) == 0:
        click.echo("本次扫描不强制按文件时间戳转换")
    else:
        click.echo("本次扫描按文件时间戳转换")

    if os.path.exists(dir_path):
        walk(dir_path, int(subdir), int(ctime_mode))
        click.echo("扫描结束\n")
    else:
        click.echo(f"{dir_path} 路径不存在，请重新输入")


if __name__ == "__main__":
    click_walk()
