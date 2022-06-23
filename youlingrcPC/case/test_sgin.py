import pytest
import allure
import time
from common.log import Log
from pages.login_sgin import SginEle

_log = Log()


@allure.epic("用户登录/注册测试")
@allure.feature("用户注册")
@pytest.mark.usefixtures("quit_rc_login")
@pytest.mark.flaky(reruns=3, reruns_delay=2)  # reruns表示失败后执行几次，reruns_delay表示失败后等待几秒后，在重新执行
class Test_sgin:

    @allure.story("个人注册测试")
    @allure.title("个人注册中，测试输入框中不插入数据时，点击注册是否有对应的提示")
    def test_sgin_01(self, get_driver):
        """个人注册中，测试输入框中不插入数据时，点击注册是否有对应的提示.断言输入框为空时的提示，和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            err = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 手机号码不能为空" % err)
            assert err == "手机号码不能为空"

    @allure.story("企业注册测试")
    @allure.title("企业注册中，测试输入框中不插入数据时，点击注册是否有对应的提示")
    def test_sgin_02(self, get_driver):
        """企业注册中，测试输入框中不插入数据时，点击注册是否有对应的提示.断言输入框为空时的提示，和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("点击切换到企业注册"):
            sgin.switch_sgin_qy()
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            err = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 手机号码不能为空" % err)
            assert err == "手机号码不能为空"

    @allure.story("验证码功能测试")
    @allure.title("未输入手机号时，点击获取验证码，查看系统提示")
    def test_sgin_03(self, get_driver):
        """未输入手机号时，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            text = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 请输入手机号码" % text)
            assert text == "请输入手机号码"

    @allure.story("验证码功能测试")
    @allure.title("输入已注册的手机号，点击获取验证码，查看系统提示")
    def test_sgin_04(self, get_driver):
        """输入已注册的手机号，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("输入注册手机号"):
            sgin.input_user_gr(user="15797629873")
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            text = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 帐号已注册，发送失败" % text)
            assert text == "帐号已注册，发送失败"

    @allure.story("验证码功能测试")
    @allure.title("输入格式错误的手机号，点击获取验证码，查看系统提示")
    def test_sgin_05(self, get_driver):
        """输入格式错误的手机号，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("输入注册手机号"):
            sgin.input_user_gr(user="157")
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t1 = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 验证码发送失败、请输入正确的手机号码" % t1)
            assert t1 == "验证码发送失败、请输入正确的手机号码"

    @allure.story("验证码功能测试")
    @allure.title("输入正确的手机号，输入错误的或格式错误的验证码，点击注册，查看系统提示")
    def test_sgin_06(self, get_driver):
        """输入正确的手机号和密码，输入错误的或格式错误的验证码，点击注册，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("输入注册手机号"):
            sgin.input_user_gr(user="15800009999")
        with allure.step("勾选平台注册协议"):
            sgin.click_protocol()
        with allure.step("输入验证码"):
            sgin.input_code_gr(code="000000")
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t1 = sgin.alert_text()
            assert t1 == "验证码不正确"
            _log.info("断言系统的提示-- %s == 验证码不正确" % t1)
        with allure.step("清空验证码输入框"):
            sgin.clear_code_gr()
        with allure.step("输入验证码"):
            sgin.input_code_gr(code="0000")
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t2 = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 验证码无效，请查验后再试" % t2)
            assert t2 == "验证码无效，请查验后再试"

    @allure.story("企业注册测试")
    @allure.title("企业注册中，未输入手机号时，点击获取验证码，查看系统提示")
    def test_sgin_07(self, get_driver):
        """未输入手机号时，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("切换企业账号注册"):
            sgin.switch_sgin_qy()
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            text = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 请输入手机号码" % text)
            assert text == "请输入手机号码"

    @allure.story("企业注册测试")
    @allure.title("企业注册中，输入已注册的手机号，点击获取验证码，查看系统提示")
    def test_sgin_08(self, get_driver):
        """输入已注册的手机号，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("切换企业账号注册"):
            sgin.switch_sgin_qy()
        with allure.step("输入注册的手机号"):
            sgin.input_user_gr(user="15797629873")
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            text = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 帐号已注册，发送失败" % text)
            assert text == "帐号已注册，发送失败"

    @allure.story("企业注册测试")
    @allure.title("企业注册中，输入格式错误的手机号，点击获取验证码，查看系统提示")
    def test_sgin_09(self, get_driver):
        """输入格式错误的手机号，点击获取验证码，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("切换企业账号注册"):
            sgin.switch_sgin_qy()
        with allure.step("输入注册的手机号"):
            sgin.input_user_gr(user="157")
        with allure.step("点击获取验证码"):
            sgin.click_code_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t1 = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 手机号格式不正确" % t1)
            assert t1 == "手机号格式不正确"

    @allure.story("企业注册测试")
    @allure.title("企业注册中，输入正确的手机号，输入错误的或格式错误的验证码，点击注册，查看系统提示")
    def test_sgin_10(self, get_driver):
        """输入正确的手机号和密码，输入错误的或格式错误的验证码，点击注册，查看系统提示.断言系统提示和字体颜色"""
        sgin = get_driver[2]
        with allure.step("点击跳转到注册页"):
            sgin.click_sgin()
        with allure.step("切换企业账号注册"):
            sgin.switch_sgin_qy()
        with allure.step("输入注册手机号"):
            sgin.input_user_gr(user="15800009999")
        with allure.step("勾选平台注册协议"):
            sgin.click_protocol()
        with allure.step("输入验证码"):
            sgin.input_code_gr(code="000000")
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t1 = sgin.alert_text()
            assert t1 == "验证码不正确"
            _log.info("断言系统的提示-- %s == 验证码不正确" % t1)
        with allure.step("清空验证码输入框"):
            sgin.clear_code_gr()
        with allure.step("输入验证码"):
            sgin.input_code_gr(code="0000")
        with allure.step("点击注册按钮"):
            sgin.click_sgin_gr()
        with allure.step("断言系统是否弹出正确的异常提示"):
            t2 = sgin.alert_text()
            _log.info("断言系统的提示-- %s == 验证码无效，请查验后再试" % t2)
            assert t2 == "验证码无效，请查验后再试"

    # @allure.story("查看优领注册协议")
    # def test_sgin_11(self, get_driver):
    #     """查看优领注册协议,断言proTitle"""
    #     sgin = get_driver[2]
    #     sgin.click_sgin()
    #     time.sleep(0.5)
    #     sgin.click_protocol()
    #     text = sgin.protocol_text()
    #     assert text == "注册协议"
