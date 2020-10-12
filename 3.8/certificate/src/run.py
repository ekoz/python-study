#!/usr/bin/env python
# encoding: utf-8

"""
奖状生成器
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@time: 2020/10/10 12:02

@see Python在图片上添加文字 https://blog.csdn.net/sinat_29957455/article/details/88071078
@see 获取授权码，解决python发邮件报错：535, b'Login Fail. Please enter your authorization code to login https://blog.csdn.net/weixin_44915703/article/details/104417030
@see Python SMTP发送邮件 https://www.runoob.com/python/python-email.html
@see SMTP发送邮件 https://www.liaoxuefeng.com/wiki/1016959663602400/1017790702398272
@see 14.2. configparser — Configuration file parser https://docs.python.org/3.5/library/configparser.html
"""
import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image
import xlrd
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import configparser

cur_year = datetime.datetime.now().year
cur_month = datetime.datetime.now().month
cur_day = datetime.datetime.now().day

config = configparser.ConfigParser()
config.read("./config.conf", encoding="utf-8")

#####################################
# 初始化数据
####################################
# win10宋体字库路径
fontpath = config["base"]["font_path"]
# 围棋选手excel表格路径
xlsx_path = config["base"]["xlsx_path"]
# 围棋证书模板图片路径
template_img_path = config["base"]["template_img_path"]
# 证书生成路径，以 / 结尾
dest_path = config["base"]["dest_path"]
#####################################
# 第三方 SMTP 服务，请注意不要泄露密码
####################################
# 设置服务器
mail_host = config["email"]["mail_host"]
mail_port = config["email"]["mail_port"]
# 用户名
mail_user = config["email"]["mail_user"]
# 口令，非邮箱密码，通过开启 STMP 协议获取授权码
mail_pass = config["email"]["mail_pass"]
# 建立邮箱连接
smtpSender = smtplib.SMTP(mail_host, mail_port)
# 通过指定的账号登录
smtpSender.login(mail_user, mail_pass)


def cv_imread(filePath):
    # 支持读取中文路径名
    return cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)


def put_text(text, x, y, color, font_size=1, font_weight=2):
    # 参数说明：照片/添加的文字/左下角坐标/字体/字体大小/颜色/字体粗细
    # 不支持中文文本
    cv2.putText(
        bg_img,
        str(text),
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        font_size,
        color,
        font_weight,
        cv2.LINE_AA,
    )


def draw_text(draw, text, x, y, color, font_size=36):
    # 采用 pil 库输入中文
    p_font = ImageFont.truetype(fontpath, font_size)
    draw.text((x, y), str(text), font=p_font, fill=color)


def get_user_list():
    # 读取excel中的行，获取用户清单，样例如下
    # [[1.0, '宋江', 4.0, 49974670.0], [2.0, '卢俊义', 7.0, 37200035.0], [3.0, '吴用', 6.0, 48610391.0]]
    # 返回一个二维数组
    user_list = []
    wb = xlrd.open_workbook(xlsx_path)
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        user_list.append(sheet.row_values(i))
    return user_list


def create_certificate(name, grade):
    # 根据指定的用户名和段位数生成证书
    bg_img = cv_imread(template_img_path)
    img_pil = Image.fromarray(bg_img)
    draw = ImageDraw.Draw(img_pil)
    if len(name) == 2:
        draw_text(draw, name, 284, 270, (255, 0, 0), 36)
    else:
        draw_text(draw, name, 276, 274, (255, 0, 0), 30)

    draw_text(draw, int(grade), 440, 270, (0, 0, 0), 36)
    draw_text(draw, cur_year, 505, 430, (0, 0, 0), 24)
    draw_text(draw, cur_month, 580, 430, (0, 0, 0), 24)
    draw_text(draw, cur_day, 625, 430, (0, 0, 0), 24)
    cer_img = np.array(img_pil)
    # user_info[0] 是 excel 第一列的编号
    cer_img_path = dest_path + str(user_info[0]) + "_" + str(grade) + ".jpg"
    cv2.imwrite(cer_img_path, cer_img)
    return cer_img_path


def send_mail(img_path, email="eko.z@outlook.com"):
    # 将证书发送给指定的用户
    img_data = open(img_path, "rb").read()
    msg = MIMEMultipart()
    msg["Subject"] = "请查收您的围棋段位证书"
    msg["From"] = mail_user
    msg["To"] = format_email(email)

    text = MIMEText("围棋段位证书详见附件")
    msg.attach(text)
    # 将证书作为附件插入邮件体中
    image = MIMEImage(img_data, name=os.path.basename(img_path))
    msg.attach(image)

    try:
        smtpSender.sendmail(msg["From"], msg["To"], msg.as_string())
        print("[" + msg["To"] + "] 邮件发送成功")
    except smtplib.SMTPException:
        print("Error[" + msg["To"] + "]: 无法发送邮件")


def format_email(mail_addr):
    # 格式化用户的qq号成为邮箱
    # 由于 excel 中生成的qq号是一个浮点数，所以这里采用 try-except 的方式判断，建议修改 excel 中的qq号格式，根据实际情况修改
    try:
        mail_addr = float(mail_addr)
        return str(int(mail_addr)) + "@qq.com"
    except ValueError:
        return mail_addr


if __name__ == "__main__":
    # 方法执行
    for user_info in get_user_list():
        cer_img_path = create_certificate(user_info[1], user_info[2])
        send_mail(cer_img_path, user_info[3])
    smtpSender.quit()