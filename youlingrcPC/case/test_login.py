import pytest
import allure
import time
from common.log import Log

_log = Log()

data = [
    ('15797629873', '', '密码不能为空！'),
    ('', '123456', '请输入正确的手机号码！'),
]
data2 = [
    ('15797629873', '111111', '输入的账号或密码错误~'),
    ('13611111122', '123456', '输入的账号或密码错误~')
]


@allure.epic("用户登录/注册测试")
@allure.feature("用户登录")
@pytest.mark.usefixtures("quit_rc_login")
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # reruns表示失败后执行几次，reruns_delay表示失败后等待几秒后，在重新执行
class Test_Login:

    @allure.story("用户名/密码框测试")
    @allure.title("测试用户名或密码不输入时的系统提示")
    @pytest.mark.parametrize('data', data)
    def test_login_01(self, get_driver, data):
        """测试用户名或密码不输入时的系统提示"""
        print("测试数据%s" % (data,))
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("定位并输入手机号码"):
            get_driver[1].input_user(data[0])
        with allure.step("定位并输入密码"):
            get_driver[1].input_password(data[1])
        with allure.step("点击登录按钮"):
            get_driver[1].click_login_l()
        with allure.step("获取登录后的系统提示"):
            text = get_driver[1].alert_text()
        with allure.step("断言系统是否弹出正确的异常提示"):
            _log.info("断言系统的提示-- %s == %s" % (text,data[2]))
            assert text == data[2]

    @allure.story("用户名/密码框测试")
    @allure.title("测试用户名或密码输入错误时的系统提示")
    @pytest.mark.parametrize('data2', data2)
    def test_login_02(self, get_driver, data2):
        """测试用户名或密码输入错误时的系统提示"""
        print("测试数据%s" % (data2,))
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("定位并输入手机号码"):
            get_driver[1].input_user(data2[0])
        with allure.step("定位并输入密码"):
            get_driver[1].input_password(data2[1])
        with allure.step("点击登录按钮"):
            get_driver[1].click_login_l()
        with allure.step("获取登录后的系统提示"):
            text = get_driver[1].alert_text()
            assert text == data2[2]
            _log.info("断言系统的提示-- %s == %s" % (text, data2[2]))

    @allure.story("验证码获取测试")
    @allure.title("不输入手机号，进行验证码获取")
    def test_login_03(self, get_driver):
        """进入登录页，将登录方式切换为验证码登录，不输入手机号，进行验证码获取"""
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("切换到验证码登录"):
            get_driver[1].code_login()
        with allure.step("点击获取验证码"):
            get_driver[1].click_code()
        with allure.step("获取系统提示"):
            text = get_driver[1].alert_text()
            _log.info("断言系统的提示-- %s == 请输入手机号码" % text)
            assert text == "请输入手机号码"

    @allure.story("验证码获取测试")
    @allure.title("输入错误的手机号，再进行验证码获取")
    def test_login_04(self, get_driver):
        """进入登录页，将登录方式切换为验证码登录，输入错误的手机号，进行验证码获取"""
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("切换到验证码登录"):
            get_driver[1].code_login()
        with allure.step("定位并输入手机号码"):
            get_driver[1].input_user(user="18998819566")
        with allure.step("点击获取验证码"):
            get_driver[1].click_code()
        with allure.step("获取系统提示"):
            text = get_driver[1].alert_text()
            _log.info("断言系统的提示-- %s == 帐号未注册，发送失败" % text)
            assert text == "帐号未注册，发送失败"

    @allure.story("验证码获取测试")
    @allure.title("输入正确的手机号、错误的验证码，再进行验证码登录")
    def test_login_05(self, get_driver):
        """进入登录页，将登录方式切换为验证码登录，输入正确的手机号、错误的验证码，进行验证码获取"""
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("切换到验证码登录"):
            get_driver[1].code_login()
        with allure.step("定位并输入手机号码"):
            get_driver[1].input_user(user="18998819566")
        with allure.step("定位并输入错误验证码"):
            get_driver[1].input_code(code="123456")
        with allure.step("点击登录按钮"):
            get_driver[1].click_login_l2()
        with allure.step("获取系统提示"):
            text = get_driver[1].alert_text()
            _log.info("断言系统的提示-- %s == 验证码错误" % text)
            assert text == "验证码错误"

    @allure.story("验证码获取测试")
    @allure.title("输入错误的手机号、正确的验证码，再进行验证码获取")
    def test_login_06(self, get_driver):
        """进入登录页，将登录方式切换为验证码登录，输入错误的手机号、正确的验证码，再进行验证码获取"""
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("切换到验证码登录"):
            get_driver[1].code_login()
        with allure.step("定位并输入手机号码"):
            get_driver[1].input_user(user="15321547841")
        with allure.step("定位并输入错误验证码"):
            get_driver[1].input_code(code="666666")
        with allure.step("点击登录按钮"):
            get_driver[1].click_login_l2()
        with allure.step("获取系统提示"):
            text = get_driver[1].alert_text()
            _log.info("断言系统的提示-- %s == 验证码错误" % text)
            assert text == "验证码错误"

    @allure.story("验证码获取测试")
    @allure.title("不输入手机号、填写验证码，再进行验证码获取")
    def test_login_07(self, get_driver):
        """进入登录页，将登录方式切换为验证码登录，不输入手机号、正确的验证码，再进行验证码获取"""
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("切换到验证码登录"):
            get_driver[1].code_login()
        with allure.step("定位并输入错误验证码"):
            get_driver[1].input_code(code="666666")
        with allure.step("点击登录按钮"):
            get_driver[1].click_login_l2()
        with allure.step("获取系统提示"):
            text = get_driver[1].alert_text()
            _log.info("断言系统的提示-- %s == 请输入正确的手机号码" % text)
            assert text == "请输入正确的手机号码！"

    @allure.story("忘记密码功能测试")
    @allure.title("点击忘记密码，查看页面跳转")
    def test_login_08(self, get_driver):
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("点击忘记密码按钮"):
            get_driver[1].click_forget_password()
        with allure.step("定位忘记密码页的标签，进行断言"):
            r = get_driver[1].rtext_forget_password()
            assert r == "找回密码"

    @allure.story("忘记密码功能测试")
    @allure.title("从忘记密码页返回登录页")
    def test_login_09(self, get_driver):
        with allure.step("点击跳转登录页"):
            get_driver[1].click_login()
        with allure.step("点击忘记密码按钮"):
            get_driver[1].click_forget_password()
        with allure.step("点击返回登录页"):
            get_driver[1].click_return_login()
        with allure.step("断言页面是否为登录页"):
            r = get_driver[1].rtext_login_title()
            assert r == "密码登录"





















