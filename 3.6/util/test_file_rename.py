#!/usr/bin/env python
# encoding: utf-8

import os

path = 'E:\\Ekoz\\Items\\2018-10-10 秋宝宝\\Images\\security'


def test1():
    if os.path.exists(path):
        # print(path)
        fs = os.listdir(path)
        for f in fs:
            if f.find('-'):
                file_name = f
                new_name = f
                if len(new_name) > 15:
                    # 202106041453135.jpg
                    # 2021-06-04_14.53.13.5.jpg
                    new_name = new_name[0:4] + '-' + new_name[4:6] \
                               + '-' + new_name[6:8] + '_' + new_name[8:10] \
                               + '.' + new_name[10:12] + '.' + new_name[12:14] \
                               + '.' + new_name[14:]
                print(new_name)
                old_path = path + "\\" + file_name
                new_path = path + "\\" + new_name
                os.rename(old_path, new_path)


def fmt_filename(new_name):
    # .jpg
    extension = new_name[new_name.rfind('.'):]
    # 20210604145
    base_name = new_name[0:new_name.rfind('.')]
    if len(base_name)>8:
        new_base_name = base_name[0:4] + '-' + base_name[4:6] \
                       + '-' + base_name[6:8] + '_' + join_str_with_dot(base_name[8:])
    return new_base_name + extension


def join_str_with_dot(tmp_str):
    tmp_arr = []
    for n in range(len(tmp_str)):
        if n % 2 == 0:
            tmp_arr.append(tmp_str[n:n + 2])
    return '.'.join(tmp_arr)


if __name__ == "__main__":
    # test1()
    print(fmt_filename('202106041453135.jpg'))
    print(fmt_filename('2021060414.jpg'))
    # print(join_str_with_dot('1256986354'))