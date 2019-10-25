#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 系统名称
desired_caps['platformVersion'] = '5.1'  # 系统的版本号
desired_caps['deviceName'] = 'QKKRNZNN99999999'  # 设备名称
desired_caps['appPackage'] = 'com.immuxin.muxin'  # APP包名
desired_caps['appActivity'] = '.ui.activity.GuideActivity'  # APP入口的activity

phone = 13011111111
pwd = 111111
message = 111