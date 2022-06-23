import pytest
import allure
import datetime
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("个人端——我的页面")
@allure.feature("我的信息页测试")
@pytest.mark.usefixtures("get_driver", "login_rc")
class Test_personal_center:

    @allure.story("我的信息页")
    @allure.title("断言用户名称与标签栏名称是否一致")
    def test_message_01(self, get_driver):
        personal = get_driver[6]
        with allure.step("获取导航栏用户姓名"):
            title_name = personal.rtext_title_name()
        with allure.step("获取当前用户姓名"):
            user_name = personal.rtext_user_name()
        with allure.step("断言姓名是否相同"):
            assert title_name == user_name

    @allure.story("我的信息页")
    @allure.title("点击完善信息链接，查看页面跳转")
    def test_message_02(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击完善信息链接"):
            personal.perfect_information()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言姓名是否相同"):
            pytest.assume("我的简历" in title)
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击我的投递，查看页面跳转")
    def test_message_03(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击我的投递"):
            personal.my_delivery()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            pytest.assume("我的投递" == title)
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击我的收藏，查看页面跳转")
    def test_message_04(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击我的收藏"):
            personal.my_collect()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            pytest.assume("我的收藏" == title)
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击我的报名，查看页面跳转")
    def test_message_05(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击我的报名"):
            personal.my_apply()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            pytest.assume("我的报名" == title)
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("切换求职状态，并去到我的简历页查看状态是否变更")
    def test_message_06(self, get_driver):
        personal = get_driver[6]
        with allure.step("展开并切换求职状态"):
            personal.unfold_job_status()
            personal.select_job_status(text="离职-随时到岗")
            personal.unfold_job_status()
            personal.select_job_status(text="在职-在找工作")
        with allure.step("断言切换后的系统提示"):
            code = personal.code_text()
            pytest.assume(code == "切换成功")
            personal.return_my_info()
        # with allure.step("切换到我的简历页，获取在职信息"):
        #     personal.click_module("我的简历")
        #     r = personal.retxt_job_status()
        #     pytest.assume(r == "在职-在找工作")

    @allure.story("我的信息页")
    @allure.title("点击我的考勤，查看页面跳转")
    def test_message_07(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击我的考勤"):
            personal.job_management_my_attendance()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            assert "我的考勤" == title
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击简历预览，查看页面跳转")
    def test_message_08(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击简历预览"):
            personal.job_management_resume_preview()
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            assert "我的简历" == title
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击分享好友，查看页面跳转")
    def test_message_09(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击分享好友"):
            personal.job_management_friends_share()
            personal.return_my_info()

    @allure.story("我的信息页")
    @allure.title("点击签到，查看页面跳转")
    def test_message_10(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击签到"):
            personal.job_management_sign_in()
        with allure.step("断言标签是否相同"):
            code = personal.code_text()
            pytest.assume(code == "签到成功")
            personal.return_my_info()

    @allure.story("我的简历页")
    @allure.title("点击我的简历页，查看页面跳转")
    def test_resume_01(self, get_driver):
        personal = get_driver[6]
        with allure.step("点击我的简历"):
            personal.click_module(module="我的简历")
        with allure.step("获取跳转后页面标签"):
            title = personal.tag_name()
        with allure.step("断言标签是否相同"):
            pytest.assume("我的简历" == title)
            personal.return_my_info()

    @allure.story("我的简历页")
    @allure.title("点击简历刷新按钮，查看系统提示")
    def test_resume_02(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的简历页"):
            personal.click_module(module="我的简历")
        with allure.step("获取简历刷新按钮的当前文本"):
            text = personal.rtext_resume_refresh()
            if text == "简历刷新":
                with allure.step("点击简历刷新按钮"):
                    title = personal.click_resume_refresh()
                with allure.step("断言系统提示"):
                    pytest.assume("简历刷新成功" == title)
                    personal.return_my_info()
            elif text == "简历已刷新":
                with allure.step("点击简历刷新按钮"):
                    title = personal.click_resume_refresh()
                with allure.step("断言系统提示"):
                    pytest.assume("简历已刷新" == title)
                    personal.return_my_info()
            else:
                _log.error("简历刷新按钮未获取")

    @allure.story("我的简历页")
    @allure.title("点击预览简历，查看预览详情")
    def test_resume_03(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的简历页"):
            personal.click_module(module="我的简历")
        with allure.step("获取我的简历页，我的名片中全部文本"):
            edit_card = personal.rtext_edit_card()
        with allure.step("获取我的简历页，工作经验中全部文本"):
            work_experience = personal.rtext_work_experience()
            print(work_experience)
        with allure.step("获取我的简历页，技能证书中全部文本"):
            skill_certificate = personal.rtext_skill_certificate()
            print(skill_certificate)
        with allure.step("点击预览简历按钮"):
            personal.click_resume_preview()
        with allure.step("切换至新打开的窗口"):
            personal.cut_win()
        with allure.step("获取预览简历页，我的名片中全部文本"):
            p_edit_card = personal.rtext_edit_card()
        with allure.step("获取预览简历页，工作经验中全部文本"):
            p_work_experience = personal.rtext_work_experience()
        with allure.step("获取我的简历页，技能证书中全部文本"):
            p_skill_certificate = personal.rtext_skill_certificate()
        with allure.step("断言预览简历页内容是否正确"):
            if not pytest.assume(p_edit_card.replace(" ", "") == edit_card.replace(" ", "")):
                _log.error(edit_card)
                _log.error(p_edit_card)
            if "暂时没有工作经历，点击有上角编辑添加~" == work_experience:
                pytest.assume(p_work_experience == "暂时未添加工作经历!!!")
            else:
                if not pytest.assume(p_work_experience.replace(" ", "") == work_experience.replace(" ", "")):
                    _log.error(work_experience)
                    _log.error(p_work_experience)
            if "暂时没有技能证书，点击有上角编辑添加~" == skill_certificate:
                pytest.assume(p_skill_certificate == "暂时未添加技能证书!!!")
            else:
                if not pytest.assume(p_skill_certificate.replace(" ", "") == skill_certificate.replace(" ", "")):
                    _log.error(skill_certificate)
                    _log.error(p_skill_certificate)
        with allure.step("切换回原窗口"):
            get_driver[0].close()
            personal.cutBack_win()

    @allure.story("我的简历页")
    @allure.title("修改用户的年龄、学历、工作年限并保存，查看信息修改后展示是否正确")
    def test_resume_04(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的简历页"):
            personal.click_module(module="我的简历")
        with allure.step("点击我的名片中的编辑按钮"):
            personal.click_edit_card()
        with allure.step("选择出生年龄"):
            personal.click_birthday()
            y = random.randint(1950, 2010)
            m = random.randint(1, 12)
            d = random.randint(1, 28)
            personal.cut_birthday(year=int(y), month=int(m), day=int(d))
        with allure.step("选择学历"):
            e = random.randint(1,9)
            personal.select_education(num=e)
        with allure.step("选择工龄"):
            w = random.randint(1, 5)
            personal.select_working_years(num=w)
        with allure.step("确认名片编辑"):
            personal.click_affirm_amend_card()
        with allure.step("获取用户当前年龄"):
            u_y = personal.rtext_user_xinxi(2)
        with allure.step("获取用户学历"):
            u_e = personal.rtext_user_xinxi(3)
        with allure.step("获取用户工龄"):
            u_w = personal.rtext_user_xinxi(4)
        with allure.step("判断年龄是否正确"):
            new_y = datetime.datetime.today().year
            x = new_y - y
            pytest.assume('%s岁' %x == u_y)
        with allure.step("判断学历是否选择一致"):
            education = {1: "小学以下", 2: "小学", 3: "初中", 4: "高中", 5: "中专", 6: "大专", 7: "本科", 8: "硕士", 9: "博士"}
            pytest.assume(education[e] == u_e)
        with allure.step("判断工龄是否选择一致"):
            working = {1: "应届生", 2: "1-3年", 3: "3-5年", 4: "5-10年", 5: "10年以上"}
            pytest.assume(working[w] == u_w)

    @allure.story("我的简历页")
    @allure.title("选择想要的工作并保存，查看信息修改后展示是否正确")
    def test_resume_05(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的简历页"):
            personal.click_module(module="我的简历")
        with allure.step("点击我的名片中的编辑按钮"):
            personal.click_edit_card()
        with allure.step("点击想要的工作按钮"):
            personal.click_want_job()
        with allure.step("选择想要的工作"):
            personal.select_want_job_one(job_one="服务行业")
            personal.select_want_job_two(job_two="司机")
            num = personal.number_job_there()
            n = random.sample(range(1,num), 5)
            for i in range(5):
                personal.select_want_job_there(num=n[i-1])
        with allure.step("获取已选择的想要的工作"):
            text = personal.rtext_selected_job()
        with allure.step("确认想要工作的选择"):
            personal.select_want_job_affirm()
        with allure.step("保存名片"):
            personal.click_affirm_amend_card()
        with allure.step("获取用户期望的职位"):
            time.sleep(2)     # 等待页面中 期望的职位 数据刷新
            text2 = personal.rtexts_expected_position()
        with allure.step("断言选择的想要的职位是否和确认后页面展示的期望职位一致"):
            print(text[0], text2[0])
            pytest.assume(text[0] == text2[0])

    @allure.story("我的投递页")
    @allure.title("切换到我的投递页，查看页面跳转")
    def test_delivery_01(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的投递页"):
            personal.click_module(module="我的投递")
        with allure.step("获取页面标签"):
            t = personal.tag_name()
        with allure.step("断言页面标签是否为我的投递"):
            pytest.assume(t == "我的投递")

    @allure.story("我的投递页")
    @allure.title("点击对我感兴趣的，查看列表变换")
    def test_delivery_02(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的投递页"):
            personal.click_module(module="我的投递")
        with allure.step("点击对我感兴趣的"):
            personal.click_interested_me()
        with allure.step("获取列表标签，并断言"):
            title = personal.rtext_interested_title()
            pytest.assume(title == "感兴趣的简历")

    @allure.story("我的投递页")
    @allure.title("点击已投递的简历，查看列表变换")
    def test_delivery_03(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的投递页"):
            personal.click_module(module="我的投递")
        with allure.step("点击对我感兴趣的"):
            personal.click_interested_me()
        with allure.step("点击已投递的简历，查看列表变换"):
            personal.click_posted_position()
        with allure.step("获取列表标签，并断言"):
            title = personal.rtext_interested_title()
            pytest.assume(title == "已投递的简历")

    @allure.story("我的投递页")
    @allure.title("输入筛选条件，对简历进行筛选")
    def test_deliver_04(self, get_driver):
        personal = get_driver[6]
        with allure.step("切换到我的投递页"):
            personal.click_module(module="我的投递")
        with allure.step("输入要筛选的条件"):
            personal.send_firm_post_name("上海")
        with allure.step("点击搜索按钮"):
            personal.click_firm_post_name_inquire()
        with allure.step("获取搜索后的企业名称，并进行断言"):
            r = personal.r_application_details()
            print(r)


















