"""
크롬의 인터넷 히스토리 삭제하기
Author : Hior Lee
2021.6.16
"""

import pywinmacro as pw
import time
import random

# 크롬 아이콘 위치
location0 = (65,424)
# 크롬 설정 위치
location1 = (1896,49)
# 인터넷 사용기록 삭제 위치
location2 = (69,250)
# 기간 콤보 위치
location3 = (847,434)
# 전체기간 위치
location4 = (835,526)
# 삭제 위치
location5 = (1121,763)

def del_cr_hstr():

    pw.double_click(location0)
    time.sleep(0.5)

    pw.key_on("window")
    time.sleep(0.5)
    pw.key_press_once("up_arrow")
    time.sleep(0.5)
    pw.key_off("window")
    time.sleep(0.5)

    pw.click(location1)
    time.sleep(1)
    for i in range(4):
        pw.key_press_once("down_arrow")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(1)
    pw.key_press_once("enter")
    time.sleep(1)

    pw.click(location2)
    time.sleep(1)

    pw.click(location3)
    time.sleep(1)

    pw.click(location4)
    time.sleep(1)

    pw.click(location5)
    time.sleep(1)

del_cr_hstr()

