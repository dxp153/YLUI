from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.log import Log
from selenium.common.exceptions import NoSuchElementException
import allure
import time

_log = Log()

click_sgin = (By.CSS_SELECTOR, "li.shu+li p")
switch_sgin_gr = (By.XPATH, "//span[text()='我要找工作']")
switch_sgin_qy = (By.XPATH, "//span[text()='我要招聘']")
loc_use_gr = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
loc_code_gr = (By.CSS_SELECTOR, "[placeholder='请输入验证码']")
click_code_gr = (By.CLASS_NAME, "el-input-group__append")
click_sgin_gr = (By.CLASS_NAME, "bttn")
loc_use_qy = (By.CSS_SELECTOR, "div#pane-second>*>*>*>*>input[placeholder='请输入手机号码']")
loc_pwd_qy = (By.CSS_SELECTOR, "div#pane-second>*>*>*>*>input[placeholder='请输入登录密码']")
alert_text = (By.XPATH, "//div[@role='alert']")
check_protocol = (By.CLASS_NAME, "el-checkbox__label")


class SginEle(Base):

    @allure.step("点击跳转注册页面")
    def click_sgin(self):
        _log.info("点击 %s 元素,跳转注册页面" % click_sgin[1])
        self.clk(click_sgin)

    @allure.step("切换个人用户注册")
    def switch_sgin_gr(self):
        _log.info("点击 %s 元素,切换个人用户注册" % switch_sgin_gr[1])
        self.clk(switch_sgin_gr)

    @allure.step("切换企业用户注册")
    def switch_sgin_qy(self):
        _log.info("点击 %s 元素,切换企业用户注册" % switch_sgin_qy[1])
        self.clk(switch_sgin_qy)

    @allure.step("输入注册的手机号")
    def input_user_gr(self, user):
        _log.info("向输入框 %s 中填写手机号" % loc_use_gr[1])
        self.sendkeys(loc_use_gr, user)

    @allure.step("输入验证码")
    def input_code_gr(self, code):
        _log.info("向输入框 %s 中填写验证码" % loc_code_gr[1])
        self.sendkeys(loc_code_gr, code)

    @allure.step("清空验证码输入框")
    def clear_code_gr(self):
        _log.info("清空 %s 元素输入框" % loc_code_gr[1])
        self.clear(loc_code_gr)

    @allure.step("点击获取验证码")
    def click_code_gr(self):
        _log.info("点击 %s 元素,获取验证码" % click_code_gr[1])
        self.clk(click_code_gr)

    @allure.step("点击注册按钮")
    def click_sgin_gr(self):
        _log.info("点击注册按钮-- %s" % click_code_gr[1])
        self.clk(click_sgin_gr)

    @allure.step("查看登录页是否存在系统提示")
    def alert_present(self):
        _log.info("获取页面元素 %s " % alert_text[1])
        return self.isElementPresent(alert_text)

    @allure.step("查看登录页系统提示内容")
    def alert_text(self):
        #   页面提示，包括登录提示、获取验证码提示、登录失败提示
        _log.info("获取 %s 元素的文本" % alert_text[1])
        return self.rtext(alert_text)

    @allure.step("优领协议是否勾选")
    def selected_remember_password(self):
        x = self.is_selected_ele(check_protocol)
        _log.info("元素 %s 已被选中 -- %s" % (check_protocol[1], x))
        return x

    @allure.step("点击勾选优领协议")
    def click_protocol(self):
        _log.info("点击 %s 元素,跳转协议页面" % check_protocol[1])
        self.clk(check_protocol)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.youlingrc.com")
    driver.maximize_window()
    driver.refresh()
    cs = SginEle(driver)
    cs.click_sgin()

    cs.click_protocol()
    t = cs.protocol_text()
    print(t)