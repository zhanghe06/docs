#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: micro_step_driver.py
@time: 2023-10-30 08:50
"""

import RPi.GPIO as GPIO
import time

# 规定GPIO引脚
IN1 = 18  # 接PUL- 步进脉冲信号
IN2 = 16  # 接PUL+ 步进脉冲信号
IN3 = 15  # 接DIR- 方向控制信号
IN4 = 13  # 接DIR+ 方向控制信号


def set_step(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)


def stop():
    set_step(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)


def forward(delay, steps):
    print("滑台右移")
    for i in range(0, steps):
        set_step(1, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(1, 0, 0, 1)
        time.sleep(delay)


def backward(delay, steps):
    print("滑台左移")
    for i in range(0, steps):
        set_step(1, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(1, 0, 1, 0)
        time.sleep(delay)


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)  # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def loop(angle):
    # 步进电机型号：42步进电机 两相四线步进电机 17HS3401-A
    # 直流电源：24V 1.2A
    # 丝杆：轴径8mm，导程4mm，行程260mm
    # 滑台：滑台可以组装多轴：十字滑台，龙门式，三轴
    # 电机初始运行方向由A+和A-控制；默认接线方式（黑B-、绿B+、蓝A-、红A+）逆时针输出（反转）滑台向左移动

    print("启动")
    # 步距角 1.8°
    angle_step = 1.8

    # 螺距 4mm
    screw_pitch = 4

    # 细分数 4
    # 细分数 1 200脉冲/步 每步1.8°
    # 细分数 4 800脉冲/步 每步1.8°/4=0.45°
    micro_step = 4

    # 间隔时间（>5us=0.000005s）

    # 脉冲数
    pulse_step = int(abs(angle)/(angle_step/micro_step))
    if angle > 0:
        forward(0.0001, pulse_step)  # 发射脉冲时间间隔0.0001（单位秒）
    else:
        backward(0.0001, pulse_step)  # 发射脉冲时间间隔0.0001（单位秒）
    # time.sleep(1)  # sleep 1s
    print("结束")
    stop()  # stop
    time.sleep(1)  # sleep 1s


def destroy():
    GPIO.cleanup()  # 释放数据


if __name__ == '__main__':  # Program start from here
    setup()
    while True:
        try:
            a = input("输入旋转角度:")
            if not a:
                continue
            loop(float(a))
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be executed.
            destroy()
