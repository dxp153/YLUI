import pytest
import allure
import time
import random
from selenium.webdriver.common.by import By
from common.log import Log

_log = Log()


@allure.epic("首页测试")
@allure.feature("轮播图测试")
@pytest.mark.usefixtures("quit_rc_login")
class Test_home_slideshow:

    @allure.story("轮播图功能")
    @allure.title("测试首页轮播图的右切换")
    def test_slideshow_01(self, get_driver):
        """测试首页轮播图的显示和左右切换,并断言图片的style属性是否发生改变"""
        home = get_driver[3]
        with allure.step("鼠标悬浮于轮播图上"):
            home.hover_element_slideshow()
        with allure.step("鼠标点击右切"):
            home.click_slideshow_right()
        with allure.step("断言轮播图是否右切"):
            text = home.rtext_att_slideshow()
            assert text == "transform: translateX(-1920px) scale(1);"

    @allure.story("轮播图功能")
    @allure.title("测试首页轮播图的左切换")
    def test_slideshow_02(self, get_driver):
        """测试首页轮播图的显示和左右切换,并断言图片的style属性是否发生改变"""
        home = get_driver[3]
        with allure.step("鼠标悬浮于轮播图上"):
            home.hover_element_slideshow()
        with allure.step("鼠标点击左切"):
            home.click_slideshow_left()
        with allure.step("断言轮播图是否左切"):
            text = home.rtext_att_slideshow()
            assert text == "transform: translateX(1920px) scale(1);"

    @allure.story("轮播图功能")
    @allure.title("点击轮播图中的列表进行轮播图切换")
    def test_slideshow_03(self, get_driver):
        """测试首页轮播图的显示和左右切换,并断言图片的style属性是否发生改变"""
        home = get_driver[3]
        with allure.step("点击轮播图里选择按钮"):
            n = random.randint(1,3)
            home.click_slideshow(number=n)
        with allure.step("获取轮播图style参数断言"):
            text = home.rtext_att_slideshow(number=n)
            assert text == "transform: translateX(0px) scale(1);"



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@allure.epic("首页测试")
@allure.feature("搜索框测试")
@pytest.mark.usefixtures("quit_rc_login")
class Test_home_search:

    @allure.story("搜索模块跳转")
    @allure.title("将搜索框搜索条件选为找工作，查看搜索后的页面跳转")
    def test_search_01(self, get_driver):
        home = get_driver[3]
        with allure.step("点击搜索按钮"):
            home.click_search()
        with allure.step("获取跳转后的页面标签"):
            title = home.rtext_title_present()
        with allure.step("断言搜索类型与跳转后页面"):
            assert title == "找工作"

    @allure.story("搜索模块跳转")
    @allure.title("将搜索框搜索条件选为找人才，查看搜索后的页面跳转")
    def test_search_02(self, get_driver):
        home = get_driver[3]
        with allure.step("切换搜索类型为找人才"):
            home.click_search_type()
            home.hover_search_type()
            home.click_cut_search_type("找人才")
        with allure.step("点击搜索按钮"):
            home.click_search()
        with allure.step("获取跳转后的页面标签"):
            title = home.rtext_title_present()
        with allure.step("断言搜索类型与跳转后页面"):
            assert title == "找人才"

    @allure.story("搜索模块跳转")
    @allure.title("将搜索框搜索条件选为批量用工，查看搜索后的页面跳转")
    def test_search_03(self, get_driver):
        home = get_driver[3]
        with allure.step("切换搜索类型为批量用工"):
            home.click_search_type()
            home.hover_search_type()
            home.click_cut_search_type("批量用工")
        with allure.step("点击搜索按钮"):
            home.click_search()
        with allure.step("获取跳转后的页面标签"):
            title = home.rtext_title_present()
        with allure.step("断言搜索类型与跳转后页面"):
            assert title == "批量用工"

    @allure.story("搜索框搜索功能")
    @allure.title("搜索模块选择找工作，在输入搜索条件，点击搜索按钮，查看搜索结果")
    def test_search_04(self, get_driver):
        home = get_driver[3]
        job = get_driver[4]
        with allure.step("切换搜索类型为找工作"):
            home.click_search_type()
            home.hover_search_type()
            home.click_cut_search_type("找工作")
        with allure.step("搜索框中输入搜索条件-- 销售"):
            home.send_search(text="销售")
        with allure.step("点击搜索按钮"):
            home.click_search()
        with allure.step("获取搜索结果中的岗位名称和岗位类型"):
            text = []
            for i in range(10):
                X = (By.XPATH, "//div[@class='leftCentent']/ul[%s]" % (i+1))
                job.js_scrollIntoView(X)
                job_name = job.rtext_job_name(i + 1)
                firm_name = job.rtext_firm_name(i + 1)
                post_type = job.rtext_post_type(i + 1)
                text.append([job_name + firm_name + post_type])
        with allure.step("断言搜索结果中岗位名称、岗位类型、企业名称中是否是按搜索条件模糊查询的"):
            for x in range(len(text)):
                assert "销售" in text[x][0]

    @allure.story("搜索框搜索功能")
    @allure.title("搜索模块选择找人才，在输入搜索条件，点击搜索按钮，查看搜索结果")
    def test_search_05(self, get_driver):
        home = get_driver[3]
        talent = get_driver[5]
        with allure.step("切换搜索类型为找人才"):
            home.click_search_type()
            home.hover_search_type()
            home.click_cut_search_type("找人才")
        with allure.step("搜索框中输入搜索条件-- 装卸工"):
            home.send_search(text="装卸工")
        with allure.step("点击搜索按钮"):
            home.click_search()
        with allure.step("获取搜索结果中的岗位名称和岗位类型"):
            text = []
            for i in range(10):
                X = (By.XPATH, "//div[@class='leftCentent']/ul[%s]" % (i+1))
                talent.js_scrollIntoView(X)
                job_name = talent.rtext_intention_job(i + 1)
                text.append(job_name[0])
        with allure.step("断言"):
            for x in range(len(text)):
                assert "装卸工" in text[x]


@allure.epic("首页测试")
@allure.feature("首页岗位选择")
@pytest.mark.usefixtures("quit_rc_login")
class Test_home_post:

    @allure.story("选择对应的岗位")
    @allure.title("选择需要查询的岗位")
    def test_post_01(self, get_driver):
        home = get_driver[3]
        job = get_driver[4]
        with allure.step("选择需要查询的一级岗位"):
            home.hover_industry_one(industry="服务行业")
        with allure.step("选择三级岗位"):
            home.click_industry_there(" 促销导购 ")
        with allure.step("获取搜索结果中的岗位名称和岗位类型"):
            text = []
            for i in range(job.num_job_list()):
                X = (By.XPATH, "//div[@class='leftCentent']/ul[%s]" % (i + 1))
                job.js_scrollIntoView(X)
                job_name = job.rtext_job_name(i + 1)
                firm_name = job.rtext_firm_name(i + 1)
                post_type = job.rtext_post_type(i + 1)
                text.append([job_name + firm_name + post_type])
        with allure.step("断言搜索结果中岗位名称、岗位类型、企业名称中是否是按搜索条件模糊查询的"):
            for x in range(len(text)):
                assert "促销导购" in text[x][0]
