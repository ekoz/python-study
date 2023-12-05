# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2021/8/19 21:01
import numpy as np
import cv2

cap = cv2.VideoCapture("D:/Images/Video/210513100308/210513100308.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        # waitKey 里的时间决定了视频的播放速度
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
