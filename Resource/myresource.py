#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
from Resource import element
from Resource import config


driver=webdriver.Remote('http://0.0.0.0:4444/wd/hub',config.desired_caps)

def wait():
    driver.implicitly_wait(15)

def pwdlogin():
    wait()
    driver.find_element_by_id(element.account_pwd_login).click()
    wait()
    driver.find_element_by_id(element.et_UserName).send_keys("13011111111")
    wait()
    driver.find_element_by_id(element.et_Password).send_keys("111111")
    wait()
    driver.find_element_by_id(element.loginBtn).click()
    wait()
    if driver.find_elements_by_id(element.muxin):
        print('登录成功')
    else:
        print("登录失败")

def send_message():
    wait()
    if driver.find_elements_by_id(element.ll_contacts):
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.etInput).send_keys(config.message)
        wait()
        driver.find_element_by_id(element.ivSendMsg).click()
        wait()
        if driver.find_elements_by_id(element.right_is_read):
            print('消息发送成功')
        else:
            print('消息发送失败')
    else:
        pwdlogin()
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.etInput).send_keys(config.message)
        wait()
        driver.find_element_by_id(element.ivSendMsg).click()
        wait()
        if driver.find_elements_by_id(element.right_is_read):
            print('消息发送成功')
        else:
            print('消息发送失败')

def send_photo():
    wait()
    if driver.find_elements_by_id(element.ivPhoto):
        driver.find_element_by_id(element.ivPhoto).click()
        wait()
        driver.find_element_by_xpath(element.photo).click()
        wait()
        driver.find_element_by_id(element.tv_done).click()
        wait()
        if driver.find_elements_by_id(element.rightMessage_image):
            print("照片发送成功")
        else:
            print("照片发送失败")
    else:
        pwdlogin(config.phone,config.pwd)
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        driver.find_element_by_id(element.ivPhoto).click()
        wait()
        driver.find_element_by_xpath(element.photo).click()
        wait()
        driver.find_element_by_id(element.tv_done).click()
        wait()
        if driver.find_elements_by_id(element.rightMessage_image):
            print("照片发送成功")
        else:
            print("照片发送失败")

def lock_start():
    wait()
    if driver.find_elements_by_id(element.chat_head_lock):
        driver.find_element_by_id(element.chat_head_back).click()
        wait()
        driver.find_element_by_id(element.iv_back).click()
        wait()
        driver.find_element_by_xpath(element.contacts2).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.chat_head_lock).click()
        wait()
        driver.find_element_by_id(element.chat_head_back).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        if driver.find_elements_by_id(element.linear_pass):
            print("上锁成功")
        else:
            print("上锁失败")
    else:
        pwdlogin(config.phone, config.pwd)
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts2).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.chat_head_lock).click()
        wait()
        driver.find_element_by_id(element.chat_head_back).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        if driver.find_element_by_id(element.linear_pass):
            print("上锁成功")
        else:
            print("上锁失败")
    driver.tap([(100,100)])
    wait()
    driver.find_element_by_id(element.iv_back).click()


def secretly():
    wait()
    if driver.find_elements_by_id(element.ll_contacts):
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.chat_head_secretly).click()
        wait()
        driver.find_element_by_id(element.etInput).send_keys(config.message)
        wait()
        driver.find_element_by_id(element.ivSendMsg).click()
        wait()
        if driver.find_element_by_id(element.chat_secretly_image):
            print("密聊开启成功")
        else:
            print("密聊开启失败")
        wait()
        driver.find_element_by_id(element.chat_head_secretly).click()
    else:
        pwdlogin(config.phone, config.pwd)
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.chat_head_secretly).click()
        wait()
        driver.find_element_by_id(element.etInput).send_keys(config.message)
        wait()
        driver.find_element_by_id(element.ivSendMsg).click()
        wait()
        if driver.find_element_by_id(element.chat_secretly_image):
            print("密聊开启成功")
        else:
            print("密聊开启失败")
        wait()
        driver.find_element_by_id(element.chat_head_secretly).click()

def user_information():
    wait()
    if driver.find_elements_by_id(element.chat_head_cir):
        driver.find_element_by_id(element.chat_head_cir).click()
        wait()
        driver.find_element_by_xpath(element.user_information).click()
        wait()
        if driver.find_element_by_id(element.friendmsg_userinfo_layout):
            print("用户信息查询成功")
        else:
            print("用户信息查询失败")
        wait()
        driver.find_element_by_id(element.iv_back).click()
        wait()
        driver.find_element_by_xpath(element.back).click()

    else:
        pwdlogin(config.phone,config.pwd)
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.chat_head_cir).click()
        wait()
        driver.find_element_by_xpath(element.user_information).click()
        wait()
        if driver.find_element_by_id(element.friendmsg_userinfo_layout):
            print("用户信息查询成功")
        else:
            print("用户信息查询失败")
        wait()
        driver.find_element_by_id(element.iv_back).click()
        wait()
        driver.find_element_by_xpath(element.back).click()

def location_send():
    wait()
    if driver.find_elements_by_id(element.ivMoreMenuItem):
        driver.find_element_by_id(element.ivMoreMenuItem).click()
        wait()
        driver.find_element_by_xpath(element.location).click()
        wait()
        driver.find_element_by_xpath(element.location_information).click()
        wait()
        driver.find_element_by_xpath(element.location_send).click()
        wait()
        if driver.find_element_by_id(element.message_map):
            print("位置发送成功")
        else:
            print("位置发送失败")
    else:
        pwdlogin(config.phone, config.pwd)
        wait()
        driver.find_element_by_id(element.ll_contacts).click()
        wait()
        driver.find_element_by_xpath(element.contacts).click()
        wait()
        driver.find_element_by_id(element.layoutSendMsg).click()
        wait()
        driver.find_element_by_id(element.ivMoreMenuItem).click()
        wait()
        driver.find_element_by_xpath(element.location).click()
        wait()
        driver.find_element_by_xpath(element.location_information).click()
        wait()
        driver.find_element_by_xpath(element.location_send).click()
        wait()
        if driver.find_element_by_id(element.message_map):
            print("位置发送成功")
        else:
            print("位置发送失败")

def home_search():
    wait()
    if driver.find_elements_by_id(element.chat_head_back):
        driver.find_element_by_id(element.chat_head_back).click()
        wait()
        driver.find_element_by_id(element.iv_back).click()
        wait()
        driver.find_element_by_id(element.muxin).click()
        wait()
        driver.find_element_by_id(element.custom_edit_query).click()
        wait()
        driver.find_element_by_id(element.custom_edit_query).send_keys("大")
        wait()
        driver.find_element_by_id(element.search_activity_search_right_text).click()
        wait()
        if "大风车" in driver.page_source:
            print("首页搜索成功")
        else:
            print("首页搜索失败")
    else:
        pwdlogin(config.phone, config.pwd)
        wait()
        driver.find_element_by_id(element.custom_edit_query).click()
        wait()
        driver.find_element_by_id(element.custom_edit_query).send_keys("大")
        wait()
        driver.find_element_by_id(element.search_activity_search_right_text).click()
        wait()
        if "大风车" in driver.page_source:
            print("首页搜索成功")
        else:
            print("首页搜索失败")







