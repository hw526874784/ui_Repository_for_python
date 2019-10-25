#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from Resource import element
sys.path.append('/Users/hewei/test1/ui/Resource')
from Resource import myresource
from Resource import config

myresource.pwdlogin(config.phone,config.pwd)

