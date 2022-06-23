from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from common.log import Log
import allure
import time

_log = Log()

click_login = (By.CLASS_NAME, "loginSty")
loc_user = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
loc_user2 = (By.XPATH, "//div[@id='pane-second']//input[@placeholder='输入手机号']")
loc_pwd = (By.CSS_SELECTOR, "[placeholder='请输入密码']")
click_login_l = (By.XPATH, "//span[text()='登录']")
forget_password = (By.CLASS_NAME, "wjpassword")
r_forget_password = (By.CSS_SELECTOR, "div h2")
c_return_login = (By.CSS_SELECTOR, "p i")
r_login_title = (By.CSS_SELECTOR, ".password")
remember_password = (By.CLASS_NAME, "el-checkbox__inner")
pwd_login = (By.CSS_SELECTOR, ".password")
code_login = (By.CSS_SELECTOR, "span.verification")
rtext_code = (By.XPATH, "//div[@class='el-input-group__append']/span")
click_code = (By.CLASS_NAME, "el-input-group__append")
loc_code = (By.CSS_SELECTOR, "[placeholder='请输入验证码']")
alert_text = (By.XPATH, "//div[@role='alert']")
hover_name = (By.CSS_SELECTOR, "span.nameSty.fl")
r_user_identity = (By.CSS_SELECTOR, "div.cutClass")
pwd_text = (By.XPATH, "//div[text()='密码登录']")
code_text = (By.XPATH, "//div[text()='验证码登录']")
loc_ele = (By.CSS_SELECTOR, "div.comheader")
head = (By.CSS_SELECTOR, ".monicker.fl.clearfix")
qy_rc_quit = (By.CSS_SELECTOR, "div.exit")
hover_ele = (By.XPATH, "//div[@class='monicker fl clearfix']")


class LoginFun(Base):
    #   登录界面元素

    @allure.step("点击跳转登录页面")
    def click_login(self):
        #   点击跳转登录页面
        _log.info("点击 %s 元素跳转到登录页" % click_login[1])
        self.clk(click_login)

    @allure.step("定位手机号输入框,并输入手机号")
    def input_user(self, user=""):
        #   定位手机号输入框
        if str.isdigit(user):
            _log.info("定位 %s 元素进行手机号输入" % loc_user[1])
            self.sendkeys(loc_user, user)
        else:
            _log.error("手机号类型错误，请输入数字")
            print("手机号格式错误")

    @allure.step("定位密码输入框，并输入密码")
    def input_password(self, pwd=""):
        #   定位密码输入框
        _log.info("定位 %s 元素进行密码输入" % loc_pwd[1])
        self.sendkeys(loc_pwd, pwd)

    @allure.step("点击登录按钮")
    def click_login_l(self):
        #   点击登录按钮
        _log.info("点击 %s 元素进行登录操作" % click_login_l[1])
        self.clk(click_login_l)

    @allure.step("点击忘记密码")
    def click_forget_password(self):
        _log.info("点击 %s 元素，跳转到忘记密码页" % forget_password[1])
        self.clk(forget_password)

    @allure.step("获取忘记密码页页面标签")
    def rtext_forget_password(self):
        _log.info("获取忘记密码页页面标签-- %s" % r_forget_password[1])
        r = self.rtext(r_forget_password)
        return r

    @allure.step("点击忘记密码页的登录按钮，返回登录页")
    def click_return_login(self):
        _log.info("点击 %s 元素，跳转到忘记密码页" % c_return_login[1])
        self.clk(c_return_login)

    @allure.step("获取登录页标签")
    def rtext_login_title(self):
        _log.info("获取忘记密码页页面标签-- %s" % r_login_title[1])
        r = self.rtext(r_login_title)
        return r

    @allure.step("记住密码按钮是否勾选")
    def selected_remember_password(self):
        x = self.is_selected_ele(remember_password)
        _log.info("元素 %s 已被选中 -- %s" % (remember_password[1], x))
        return x

    @allure.step("点击记住密码")
    def click_remember_password(self):
        #   点击获取验证码
        _log.info("点击 %s 元素，获取验证码" % remember_password[1])
        self.clk(remember_password)

    @allure.step("切换密码登录")
    def pwd_login(self):
        #   切换密码登录
        _log.info("点击 %s 元素切换到密码登录" % pwd_login[1])
        self.clk(pwd_login)

    @allure.step("切换验证码登录")
    def code_login(self):
        #   切换验证码登录
        _log.info("点击 %s 元素切换到验证码登录" % code_login[1])
        self.clk(code_login)

    @allure.step("获取验证码按钮提示文字")
    def code_text(self):
        _log.info("获取 %s 元素的提示文字" % rtext_code[1])
        return self.rtext(rtext_code)

    @allure.step("点击获取验证码")
    def click_code(self):
        #   点击获取验证码
        _log.info("点击 %s 元素，获取验证码" % click_code[1])
        self.clk(click_code)

    @allure.step("定位验证码输入框")
    def input_code(self, code):
        if str.isdigit(code):
            _log.info("获取 %s 元素的文本" % loc_code[1])
            self.sendkeys(loc_code, code)
        else:
            _log.error("验证码类型错误，请输入数字")
            print("验证码类型错误")

    @allure.step("点击验证码登录按钮")
    def click_login_l2(self):
        #   点击登录按钮
        _log.info("点击 %s 元素，进行登录" % click_login_l[1])
        self.clk(click_login_l)

    @allure.step("查看登录页是否存在系统提示")
    def alert_present(self):
        _log.info("获取页面元素 %s " % alert_text[1])
        return self.isElementPresent(alert_text)

    @allure.step("查看登录页系统提示内容")
    def alert_text(self):
        #   页面提示，包括登录提示、获取验证码提示、登录失败提示
        _log.info("获取 %s 元素的文本" % alert_text[1])
        return self.rtext(alert_text)

    @allure.step("登录优领人才")
    def login_rc(self, user, password):
        #   登录优领人才
        self.click_login()
        self.input_user(user)
        self.input_password(password)
        self.click_login_l()

    @allure.step("查看是否是企业用户")
    def exist_ele(self):
        #   查看是否是企业用户
        self.hover_element(hover_name)
        text = self.rtexts(r_user_identity)
        if text == '切换为招聘者':
            _log.info("当前版本为个人版")
            pass
        else:
            _log.error("请切换为个人版")

    @allure.step("鼠标悬停到个人头像上")
    def hover_head(self):
        _log.info("鼠标悬停到个人头像上-- %s" % head[1])
        self.hover_element(head)

    @allure.step("退出优领人才")
    def quit_rc_qy(self):
        #   退出企业版优领人才
        self.clk(qy_rc_quit)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.maximize_window()
    driver.refresh()
    LoginFun(driver).click_login()
    LoginFun(driver).input_user()
    LoginFun(driver).input_password()
    LoginFun(driver).click_login_l()
    print(LoginFun(driver).alert_text())
