#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
from Resource import element
from Resource import config
import unittest

class Test_case(unittest.TestCase):
    def startapp(self):
        webdriver.Remote('http://0.0.0.0:4444/wd/hub', config.desired_caps)

    driver = webdriver.Remote('http://0.0.0.0:4444/wd/hub',config.desired_caps)

    def wait(self):
        self.driver.implicitly_wait(15)

    def test1_pwdlogin(self):
        self.wait()
        self.driver.find_element_by_id(element.account_pwd_login).click()
        self.wait()
        self.driver.find_element_by_id(element.et_UserName).send_keys(config.phone)
        self.wait()
        self.driver.find_element_by_id(element.et_Password).send_keys(config.pwd)
        self.wait()
        self.driver.find_element_by_id(element.loginBtn).click()
        self.wait()
        if self.driver.find_elements_by_id(element.muxin):
            print('登录成功')
        else:
            print("登录失败")


    def test2_send_message(self):
        self.wait()
        if self.driver.find_elements_by_id(element.ll_contacts):
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.etInput).send_keys(config.message)
            self.wait()
            self.driver.find_element_by_id(element.ivSendMsg).click()
            self.wait()
            if self.driver.find_elements_by_id(element.right_is_read):
                print('消息发送成功')
            else:
                print('消息发送失败')
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.etInput).send_keys(config.message)
            self.wait()
            self.driver.find_element_by_id(element.ivSendMsg).click()
            self.wait()
            if self.driver.find_elements_by_id(element.right_is_read):
                print('消息发送成功')
            else:
                print('消息发送失败')


    def test3_send_photo(self):
        self.wait()
        if self.driver.find_elements_by_id(element.ivPhoto):
            self.driver.find_element_by_id(element.ivPhoto).click()
            self.wait()
            self.driver.find_element_by_xpath(element.photo).click()
            self.wait()
            self.driver.find_element_by_id(element.tv_done).click()
            self.wait()
            if self.driver.find_elements_by_id(element.rightMessage_image):
                print("照片发送成功")
            else:
                print("照片发送失败")
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.driver.find_element_by_id(element.ivPhoto).click()
            self.wait()
            self.driver.find_element_by_xpath(element.photo).click()
            self.wait()
            self.driver.find_element_by_id(element.tv_done).click()
            self.wait()
            if self.driver.find_elements_by_id(element.rightMessage_image):
                print("照片发送成功")
            else:
                print("照片发送失败")

    def test4_lock_start(self):
        self.wait()
        if self.driver.find_elements_by_id(element.chat_head_lock):
            self.driver.find_element_by_id(element.chat_head_back).click()
            self.wait()
            self.driver.find_element_by_id(element.iv_back).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts2).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_lock).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_back).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            if self.driver.find_elements_by_id(element.linear_pass):
                print("上锁成功")
            else:
                print("上锁失败")
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts2).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_lock).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_back).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            if self.driver.find_element_by_id(element.linear_pass):
                print("上锁成功")
            else:
                print("上锁失败")
        self.driver.tap([(100,100)])
        self.wait()
        self.driver.find_element_by_id(element.iv_back).click()


    def test5_secretly(self):
        self.wait()
        if self.driver.find_elements_by_id(element.ll_contacts):
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()
            self.wait()
            self.driver.find_element_by_id(element.etInput).send_keys(config.message)
            self.wait()
            self.driver.find_element_by_id(element.ivSendMsg).click()
            self.wait()
            if self.driver.find_element_by_id(element.chat_secretly_image):
                print("密聊开启成功")
            else:
                print("密聊开启失败")
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()
            self.wait()
            self.driver.find_element_by_id(element.etInput).send_keys(config.message)
            self.wait()
            self.driver.find_element_by_id(element.ivSendMsg).click()
            self.wait()
            if self.driver.find_element_by_id(element.chat_secretly_image):
                print("密聊开启成功")
            else:
                print("密聊开启失败")
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()

    def test6_user_information(self):
        self.wait()
        if self.driver.find_elements_by_id(element.chat_head_cir):
            self.driver.find_element_by_id(element.chat_head_cir).click()
            self.wait()
            self.driver.find_element_by_xpath(element.user_information).click()
            self.wait()
            if self.driver.find_element_by_id(element.friendmsg_userinfo_layout):
                print("用户信息查询成功")
            else:
                print("用户信息查询失败")
            self.wait()
            self.driver.find_element_by_id(element.iv_back).click()
            self.wait()
            self.driver.find_element_by_xpath(element.back).click()

        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_cir).click()
            self.wait()
            self.driver.find_element_by_xpath(element.user_information).click()
            self.wait()
            if self.driver.find_element_by_id(element.friendmsg_userinfo_layout):
                print("用户信息查询成功")
            else:
                print("用户信息查询失败")
            self.wait()
            self.driver.find_element_by_id(element.iv_back).click()
            self.wait()
            self.driver.find_element_by_xpath(element.back).click()

    def test7_location_send(self):
        self.wait()
        if self.driver.find_elements_by_id(element.ivMoreMenuItem):
            self.driver.find_element_by_id(element.ivMoreMenuItem).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_information).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_send).click()
            self.wait()
            if self.driver.find_element_by_id(element.message_map):
                print("位置发送成功")
            else:
                print("位置发送失败")
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.ivMoreMenuItem).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_information).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_send).click()
            self.wait()
            if self.driver.find_element_by_id(element.message_map):
                print("位置发送成功")
            else:
                print("位置发送失败")

    def test8_home_search(self):
        self.wait()
        if  self.driver.find_elements_by_id(element.chat_head_back):
            self.driver.find_element_by_id(element.chat_head_back).click()
            self.wait()
            self.driver.find_element_by_id(element.iv_back).click()
            self.wait()
            self.driver.find_element_by_id(element.muxin).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.wait()
            self.driver.find_element_by_id(element.search_activity_search_right_text).click()
            self.wait()
            if "大风车" in self.driver.page_source:
                print("首页搜索成功")
            else:
                print("首页搜索失败")
        else:
            self.startapp()
            self.test1_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.wait()
            self.driver.find_element_by_id(element.search_activity_search_right_text).click()
            self.wait()
            if "tt" in self.driver.page_source:
                print("首页搜索成功")
            else:
                print("首页搜索失败")


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_case("test1_pwdlogin"))
    suiteTest.addTest(Test_case("test2_send_message"))
    suiteTest.addTest(Test_case("test3_send_photo"))
    suiteTest.addTest(Test_case("test4_lock_start"))
    suiteTest.addTest(Test_case("test5_secretly"))
    suiteTest.addTest(Test_case("test6_user_information"))
    suiteTest.addTest(Test_case("test7_location_send"))
    suiteTest.addTest(Test_case("test8_home_search"))
    return suiteTest

if __name__ == '__main__':
    unittest.main(defaultTest='suite')



