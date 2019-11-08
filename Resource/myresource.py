#!/usr/bin/python
# -- coding: utf-8 --
from appium import webdriver
from Resource import element
from Resource import config
import unittest

class Test_case(unittest.TestCase):
    def startapp(self):
        webdriver.Remote('http://0.0.0.0:4444/wd/hub',config.desired_caps)

    driver = webdriver.Remote('http://0.0.0.0:4444/wd/hub',config.desired_caps)

    def wait(self):
        self.driver.implicitly_wait(15)

    def test_pwdlogin(self):
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
            print('登录成功————pass')
        else:
            print("登录成功————faild")


    def test_send_message(self):
        self.wait()
        if element.ll_contacts in self.driver.page_source:
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
            if self.driver.find_element_by_id(element.right_is_read):
                print('消息发送成功————pass')
            else:
                print('消息发送成功————faild')
        else:
            self.startapp()
            self.test_pwdlogin()
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
            if self.driver.find_element_by_id(element.right_is_read):
                print('消息发送成功————pass')
            else:
                print('消息发送成功————faild')


    def test_send_photo(self):
        self.wait()
        if element.ivPhoto in self.driver.page_source:
            self.driver.find_element_by_id(element.ivPhoto).click()
            self.wait()
            self.driver.find_element_by_xpath(element.photo).click()
            self.wait()
            self.driver.find_element_by_id(element.tv_done).click()
            self.wait()
            if self.driver.find_element_by_id(element.rightMessage_image):
                print("照片发送成功————pass")
            else:
                print("照片发送成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
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
            if self.driver.find_element_by_id(element.rightMessage_image):
                print("照片发送成功————pass")
            else:
                print("照片发送成功————faild")

    def test_lock_start(self):
        self.wait()
        if element.chat_head_lock in self.driver.page_source:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
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
                print("上锁成功————pass")
            else:
                print("上锁成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts2).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.chat_head_lock).click()
            self.driver.keyevent(4)
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            if self.driver.find_element_by_id(element.linear_pass):
                print("上锁成功————pass")
            else:
                print("上锁成功————faild")


    def test_lock_pwderro(self):
        self.wait()
        self.driver.find_element_by_id(element.linear_pass)
        self.driver.tap([(100,900)])
        self.driver.tap([(100,900)])
        self.driver.tap([(400,900)])
        self.driver.tap([(400,900)])
        self.wait()
        if self.driver.find_element_by_id(element.linear_pass):
            print("解锁失败,密码错误————pass")
        else:
            print("解锁失败,密码错误————faild")
        self.driver.keyevent(4)
        self.driver.keyevent(4)


    def test_secretly(self):
        self.wait()
        if element.ll_contacts in self.driver.page_source:
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
                print("密聊开启成功————pass")
            else:
                print("密聊开启成功————faild")
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()
        else:
            self.startapp()
            self.test_pwdlogin()
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
                print("密聊开启成功————pass")
            else:
                print("密聊开启成功————faild")
            self.wait()
            self.driver.find_element_by_id(element.chat_head_secretly).click()

    def test_user_information(self):
        self.wait()
        if element.chat_head_cir in self.driver.page_source:
            self.driver.find_element_by_id(element.chat_head_cir).click()
            self.wait()
            self.driver.find_element_by_xpath(element.user_information).click()
            self.wait()
            if self.driver.find_element_by_id(element.friendmsg_userinfo_layout):
                print("用户信息查询成功————pass")
            else:
                print("用户信息查询成功————faild")
            self.driver.keyevent(4)
            self.driver.keyevent(4)
        else:
            self.startapp()
            self.test_pwdlogin()
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
                print("用户信息查询成功————pass")
            else:
                print("用户信息查询成功————faild")
            self.wait()
            self.driver.keyevent(4)
            self.driver.keyevent(4)

    def test_location_send(self):
        self.wait()
        if element.ivMoreMenuItem in self.driver.page_source:
            self.driver.find_element_by_id(element.ivMoreMenuItem).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_information).click()
            self.wait()
            self.driver.find_element_by_xpath(element.location_send).click()
            self.wait()
            if self.driver.find_element_by_id(element.message_map):
                print("位置发送成功————pass")
            else:
                print("位置发送成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
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
                print("位置发送成功————pass")
            else:
                print("位置发送成功————faild")


    def test_red_bag_lack_money(self):
        self.wait()
        if element.message_map in self.driver.page_source:
            self.driver.find_element_by_xpath(element.red_bag).click()
            self.wait()
            self.driver.find_element_by_id(element.red_packets_money).click()
            self.wait()
            self.driver.find_element_by_id(element.red_packets_money).send_keys("100")
            self.wait()
            self.driver.find_element_by_id(element.red_packets_button).click()
            self.wait()
            if element.linear_pass in self.driver.page_source:
                print("红包发送失败,余额不足————faild")
            else:
                print("红包发送失败,余额不足————pass")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.ivMoreMenuItem).click()
            self.wait()
            self.driver.find_element_by_xpath(element.red_bag).click()
            self.wait()
            self.driver.find_element_by_id(element.red_packets_money).send_keys("100")
            self.wait()
            self.driver.find_element_by_id(element.red_packets_button).click()
            self.wait()
            if element.linear_pass in self.driver.page_source:
                print("红包发送失败,余额不足————faild")
            else:
                print("红包发送失败,余额不足————pass")


    def test_transfer_money_lack(self):
        self.wait()
        if element.red_packets_button in self.driver.page_source:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.wait()
            self.driver.find_element_by_xpath(element.transfer_money_xpath).click()
            self.wait()
            self.driver.find_element_by_id(element.transfer_money).send_keys("100")
            self.wait()
            self.driver.find_element_by_id(element.transfer_uniteButton).click()
            self.wait()
            if "余额不足" in self.driver.page_source.decode("utf-8", "ignore"):
                print("转账失败,余额不足————pass")
            else:
                print("转账失败,余额不足————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.layoutSendMsg).click()
            self.wait()
            self.driver.find_element_by_id(element.ivMoreMenuItem).click()
            self.wait()
            self.driver.find_element_by_xpath(element.transfer_money_xpath).click()
            self.wait()
            self.driver.find_element_by_id(element.transfer_money).send_keys("100")
            self.wait()
            self.driver.find_element_by_id(element.transfer_uniteButton).click()
            self.wait()
            if "余额不足" in self.driver.page_source:
                print("转账失败,余额不足————pass")
            else:
                print("转账,余额不足————faild")


    def test_home_search(self):
        self.wait()
        if  element.transfer_uniteButton in self.driver.page_source:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.wait()
            self.driver.find_element_by_id(element.muxin).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.wait()
            self.driver.find_element_by_id(element.search_activity_search_right_text).click()
            self.wait()
            if "tt123456" in self.driver.page_source:
                print("首页搜索成功————pass")
            else:
                print("首页搜索成功————faild")
            self.driver.keyevent(4)
            self.driver.keyevent(4)

        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.wait()
            self.driver.find_element_by_id(element.search_activity_search_right_text).click()
            self.wait()
            if "tt123456" in self.driver.page_source:
                print("首页搜索成功————pass")
            else:
                print("首页搜索成功————faild")
            self.driver.keyevent(4)
            self.driver.keyevent(4)



    def test_friends_search(self):
        self.wait()
        if  element.ll_contacts in self.driver.page_source:
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.driver.keyevent(66)
            self.wait()
            if "tt123456" in self.driver.page_source:
                print("好友搜索成功————pass")
            else:
                print("好友搜索成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("tt")
            self.driver.keyevent(66)
            self.wait()
            if "tt123456" in self.driver.page_source:
                print("好友搜索成功————pass")
            else:
                print("好友搜索成功————faild")


    def test_add_friends(self):
        self.wait()
        if  element.header_add_contasts in self.driver.page_source:
            self.driver.find_element_by_id(element.header_add_contasts).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("15675456460")
            self.wait()
            self.driver.find_element_by_xpath(element.find_friends).click()
            self.wait()
            if "1143527" in self.driver.page_source:
                print("添加好友成功————pass")
            else:
                print("添加好友成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.header_add_contasts).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("15675456460")
            self.wait()
            self.driver.find_element_by_xpath(element.find_friends).click()
            self.wait()
            if "1143527" in self.driver.page_source:
                print("添加好友成功————pass")
            else:
                print("添加好友成功————faild")


    def test_friends_nearby(self):
        self.wait()
        if  "1143527" in self.driver.page_source:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.wait()
            self.driver.find_element_by_xpath(element.friends_nearby).click()
            self.wait()
            if "100" in self.driver.page_source:
                print("添加附近的人成功————pass")
            else:
                print("添加附近的人成功————faild")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.header_add_contasts).click()
            self.wait()
            self.driver.find_element_by_xpath(element.friends_nearby).click()
            self.wait()
            if "100" in self.driver.page_source:
                print("添加附近的人成功————pass")
            else:
                print("添加附近的人成功————faild")


    def test_group_search(self):
        self.wait()
        if  "100" in self.driver.page_source:
            self.driver.keyevent(4)
            self.driver.keyevent(4)
            self.wait()
            self.driver.find_element_by_id(element.fragment_contacts_mygroup).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("123")
            self.driver.keyevent(66)
            self.wait()
            if "fgggg" in self.driver.page_source:
                print("群聊搜索成功————faild")
            else:
                print("群聊搜索成功————pass")
        else:
            self.startapp()
            self.test_pwdlogin()
            self.wait()
            self.driver.find_element_by_id(element.ll_contacts).click()
            self.wait()
            self.driver.find_element_by_id(element.fragment_contacts_mygroup).click()
            self.wait()
            self.driver.find_element_by_id(element.custom_edit_query).click()
            self.driver.find_element_by_id(element.custom_edit_query).send_keys("123")
            self.driver.keyevent(66)
            self.wait()
            if "fgggg" in self.driver.page_source:
                print("群聊搜索成功————faild")
            else:
                print("群聊搜索成功————pass")

    def test_loginfaied(self):
        self.startapp()
        self.driver.find_element_by_id(element.account_pwd_login).click()
        self.wait()
        self.driver.find_element_by_id(element.et_UserName).send_keys(config.phone)
        self.wait()
        self.driver.find_element_by_id(element.et_Password).send_keys(111112)
        self.wait()
        self.driver.find_element_by_id(element.loginBtn).click()
        self.wait()
        if self.driver.find_element_by_id(element.loginBtn):
            print('密码错误登录失败————pass')
        else:
            print("密码错误登录失败————faild")






def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_case("test_pwdlogin"))
    suiteTest.addTest(Test_case("test_send_message"))
    suiteTest.addTest(Test_case("test_send_photo"))
    suiteTest.addTest(Test_case("test_lock_start"))
    suiteTest.addTest(Test_case("test_lock_pwderro"))
    suiteTest.addTest(Test_case("test_secretly"))
    suiteTest.addTest(Test_case("test_user_information"))
    suiteTest.addTest(Test_case("test_location_send"))
    suiteTest.addTest(Test_case("test_red_bag_lack_money"))
    suiteTest.addTest(Test_case("test_transfer_money_lack"))
    suiteTest.addTest(Test_case("test_home_search"))
    suiteTest.addTest(Test_case("test_friends_search"))
    suiteTest.addTest(Test_case("test_add_friends"))
    suiteTest.addTest(Test_case("test_friends_nearby"))
    suiteTest.addTest(Test_case("test_group_search"))
    suiteTest.addTest(Test_case("test_loginfaied"))

    return suiteTest

if __name__ == '__main__':
    unittest.main(defaultTest='suite')


