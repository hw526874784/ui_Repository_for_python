#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resource import element
import sys
sys.path.append('/Users/hewei/test1/ui/Resource')
from Resource import myresource
from Resource import config

myresource.location_send()