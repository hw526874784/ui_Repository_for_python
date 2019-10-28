#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import os
# 用例路径
case_path = os.path.join(os.getcwd(), "Test_case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
from Resource import myresource


myresource.pwdlogin()
myresource.send_message()
myresource.send_photo()
myresource.lock_start()
myresource.secretly()
myresource.user_information()
myresource.location_send()
myresource.home_search()