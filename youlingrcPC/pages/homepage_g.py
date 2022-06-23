from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.log import Log
from selenium.common.exceptions import NoSuchElementException
import allure
import time

_log = Log()

title_present = (By.CSS_SELECTOR, "a.textS")
click_home = (By.LINK_TEXT, "首页")
alert_text = (By.XPATH, "//div[@role='alert']")
slideshow = (By.CSS_SELECTOR, "div.el-carousel__container")
c_slideshow_left = (By.CSS_SELECTOR, ".el-carousel__arrow--left")
c_slideshow_right = (By.CSS_SELECTOR, ".el-carousel__arrow--right")
post_demand = (By.XPATH, "//*[@class='fixed']/*/p[text()='发布需求']")
post_demand_title = (By.XPATH, "//*[@class='youlingTitle']//div[@class='demandLi demandback']")
community_needs = (By.XPATH, "//div[@class='youlingTitle']//li[@class='demandLi']")
rpo_needs = (By.XPATH, "//div[@class='youlingTitle']//li[@class='demandLi']")
detail_send = (By.XPATH, "//div[@class='youlingTitle']//textarea[@class='el-textarea__inner']")
pop_phone = (By.XPATH, "//div[@class='youlingTitle']//input[@placeholder='请输入手机号，以便快速为你提供优质服务']")
click_code = (By.XPATH, "//div[@class='youlingTitle']//*[text()=' 获取验证码']")
send_code = (By.XPATH, "//div[@class='youlingTitle']//*[text()='请输入验证码']")
confirm_community = (By.XPATH, "//div[@class='youlingTitle']//p[text()='手机号']/../..//span[@class='detailAffirm']")
cancel_community = (By.XPATH, "//div[@class='youlingTitle']//p[text()='手机号']/../..//span[@class='detailCancel']")
click_position = (By.XPATH, "//div[@class='youlingTitle']//input[@readonly='readonly' and @placeholder='请选择']")
people_number = (By.XPATH, "//div[@class='youlingTitle']//p[text()='招聘人数']/..//input")
confirm_rpo = (By.XPATH, "//div[@class='youlingTitle']//div[@class='wantjob']/../..//span[text()='确认']")
cancel_rpo = (By.XPATH, "//div[@class='youlingTitle']//div[@class='wantjob']/../..//span[text()='取消']")
search_box = (By.XPATH, "//input[@placeholder='搜索职位、公司']")
search_type = (By.XPATH, "//div[@class='el-input-group__prepend']//input")
hover_search = (By.CSS_SELECTOR, ".el-select-dropdown__wrap.el-scrollbar__wrap")
r_search_type = (By.CSS_SELECTOR, "li.el-select-dropdown__item.selected.hover")
search_button = (By.XPATH, "//button[@class='el-button butselect el-button--default']")
more_job = (By.CLASS_NAME, "listSty clearfix reverlAll")


class HomePage(Base):

    @allure.step("获取当前页标签")
    def rtext_title_present(self):
        _log.info("获取当前页标签-- %s" % title_present[1])
        r = self.rtext(title_present)
        return r

    @allure.step("切换到个人版首页")
    def click_home(self):
        _log.info("点击 %s 元素,跳转个人版首页" % click_home[1])
        self.clk(click_home)

    @allure.step("查看页面是否存在系统提示")
    def alert_present(self):
        _log.info("获取页面元素 %s " % alert_text[1])
        return self.isElementPresent(alert_text)

    @allure.step("查看页面上的系统提示内容")
    def alert_text(self):
        #   页面提示，包括登录提示、获取验证码提示、登录失败提示
        _log.info("获取 %s 元素的文本" % alert_text[1])
        return self.rtext(alert_text)

    @allure.step("鼠标悬停在轮播图上方")
    def hover_element_slideshow(self):
        _log.info("鼠标悬停在轮播图上方-- %s" % slideshow[1])
        self.hover_element(slideshow)

    @allure.step("获取第一张轮播图位置")
    def rtext_att_slideshow(self, number=1):
        one_slideshow = (By.XPATH, "//div[@class='el-carousel__container']/div[%s]" % number)
        _log.info("获取第一张轮播图位置-- %s" % one_slideshow[1])
        text = self.get_att(one_slideshow, "style")
        return text

    @allure.step("点击轮播图里的按钮进行轮播图选择")
    def click_slideshow(self, number=1):
        c_slideshow_li = (By.XPATH, "//ul[@class='el-carousel__indicators el-carousel__indicators--horizontal']/li[%s]" % number)
        _log.info("点击轮播图里的按钮进行轮播图选择-- %s" % c_slideshow_li[1])
        self.clk(c_slideshow_li)

    @allure.step("点击轮播图左切")
    def click_slideshow_left(self):
        _log.info("点击轮播图左切-- %s" % c_slideshow_left[1])
        self.clk(c_slideshow_left)

    @allure.step("点击轮播图右切")
    def click_slideshow_right(self):
        _log.info("点击轮播图右切-- %s" % c_slideshow_right[1])
        self.clk(c_slideshow_right)

    @allure.step("点击侧边栏发布需求")
    def click_post_demand(self):
        _log.info("点击侧边浮窗 %s 元素,进行需求发布" % post_demand[1])
        self.clk(post_demand)

    @allure.step("判断需求弹窗是否显示")
    def present_post_demand(self):
        _log.info("点击侧边浮窗 %s 元素,进行需求发布" % post_demand_title[1])
        self.isElementPresent(post_demand_title)

    @allure.step("切换到弹窗中发布社区服务需求")
    def click_community_needs(self):
        _log.info("点击 %s 元素切换到发布社区服务需求" % community_needs[1])
        self.clk(community_needs)

    @allure.step("切换到弹窗中的发布rpo需求")
    def click_rpo_needs(self):
        _log.info("点击 %s 元素切换到发布rpo需求" % rpo_needs[1])
        self.clk(rpo_needs)

    @allure.step("填写弹窗中详情需求")
    def send_detail_community(self, x, text):
        #   x: 0 社区详情需求  1  rpo 详情需求
        _log.info("填写详情需求-- %s" % rpo_needs[1])
        ele = self.findElements(detail_send)
        self.sendkeys(ele[x], text)

    @allure.step("填写弹窗中社区需求中的手机号")
    def send_phone_community(self, text):
        _log.info("填写弹窗中社区需求中的手机号-- %s" % rpo_needs[1])
        self.sendkeys(pop_phone, text)

    @allure.step("点击获取验证码按钮")
    def click_code_community(self):
        _log.info("填写弹窗中社区需求中获取验证码按钮-- %s" % rpo_needs[1])
        self.clk(click_code)

    @allure.step("填写弹窗中社区需求中的验证码")
    def send_code_community(self, text):
        _log.info("填写弹窗中社区需求中的验证码-- %s" % send_code[1])
        self.sendkeys(send_code, text)

    @allure.step("点击弹窗中社区需求中的确认按钮")
    def click_confirm_community(self):
        _log.info("点击弹窗中社区需求中的确认按钮-- %s" % confirm_community[1])
        self.clk(confirm_community)

    @allure.step("点击弹窗中社区需求中的取消按钮")
    def click_cancel_community(self):
        _log.info("点击弹窗中社区需求中的取消按钮-- %s" % cancel_community[1])
        self.clk(cancel_community)

    @allure.step("点击rpo需求弹窗中的职位类型")
    def click_position_rpo(self):
        _log.info("点击rpo需求弹窗中的职位类型-- %s" % click_position[1])
        self.clk(click_position)

    @allure.step("点击rpo职位类别的一级标签")
    def click_ul_one(self, lable):
        ul_one = (By.XPATH, "//div[@id='cascader-menu-960-0']//span[text()='%s']" % lable)
        _log.info("点击职位类别的一级标签-- %s" % ul_one[1])
        self.clk(ul_one)

    @allure.step("点击rpo职位类别的二级标签")
    def click_ul_two(self, lable):
        ul_two = (By.XPATH, "//div[@id='cascader-menu-7148-1']//span[text()='%s']" % lable)
        _log.info("点击职位类别的一级标签-- %s" % ul_two[1])
        self.clk(ul_two)

    @allure.step("点击rpo职位类别的三级标签")
    def click_ul_three(self, lable):
        ul_three = (By.XPATH, "//div[@id='cascader-menu-101-2']//span[text()='%s']" % lable)
        _log.info("点击职位类别的一级标签-- %s" % ul_three[1])
        self.clk(ul_three)

    @allure.step("填写rpo招聘人数")
    def send_people_number(self, number):
        _log.info("填写招聘人数-- %s" % people_number[1])
        self.sendkeys(people_number, number)

    @allure.step("点击弹窗中rpo中的确认按钮")
    def click_confirm_rpo(self):
        _log.info("点击弹窗中rpo中的确认按钮-- %s" % confirm_rpo[1])
        self.clk(confirm_rpo)

    @allure.step("点击弹窗中rpo中的取消按钮")
    def click_cancel_rpo(self):
        _log.info("点击弹窗中rpo中的取消按钮-- %s" % cancel_rpo[1])
        self.clk(cancel_rpo)

    @allure.step("首页搜索框中填写内容")
    def send_search(self, text):
        _log.info("首页搜索框中输入搜索内容-- %s" % search_box[1])
        self.sendkeys(search_box, text)

    @allure.step("获取搜索类型")
    def rtext_search_type(self):
        _log.info("获取搜索类型-- %s" % r_search_type[1])
        text = self.rtext(r_search_type)
        return text

    @allure.step("展开搜索类型")
    def click_search_type(self):
        _log.info("展开搜索类型-- %s" % search_type[1])
        self.clk(search_type)

    @allure.step("鼠标选停搜索类型")
    def hover_search_type(self):
        _log.info("鼠标选停在搜索类型-- %s" % hover_search[1])
        self.hover_element(hover_search)

    @allure.step("切换搜索类型")
    def click_cut_search_type(self, text):
        # text: 找工作、找人才、批量用工
        ty = (By.XPATH, "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='%s']" % text)
        _log.info("切换搜索类型-- %s" % ty[1])
        self.clk(ty)

    @allure.step("点击搜索按钮")
    def click_search(self):
        _log.info("点击搜索按钮-- %s" % search_button[1])
        self.clk(search_button)

    @allure.step("鼠标选停，显示更多的职位")
    def hover_more_job(self):
        _log.info("鼠标选停，显示更多的职位-- %s" % more_job[1])
        self.hover_element(more_job)

    @allure.step("鼠标悬停，停留在一级行业，对行业详情进行展开")
    def hover_industry_one(self, industry):
        #   industry: 行业名称
        ty = (By.XPATH, "//ul[@class='above']//div[text()='%s' and @class='fl']" % industry)
        _log.info("鼠标悬停，停留在%s，对行业详情进行展开-- %s" % (industry, ty[1]))
        if self.isElementPresent(ty):
            self.hover_element(ty)
        elif self.isElementPresent(ty):
            self.hover_more_job()
            self.hover_element(ty)
        else:
            _log.error("行业名称不存在")

    @allure.step("选择三级岗位")
    def click_industry_there(self, industry):
        #   industry_one: 行业名称  industry_there： 岗位名称
        ty = (By.XPATH, "//ul[@class='clearfix']/li[text()='%s'] " % industry)
        _log.info("选择三级岗位-- %s" % industry)
        self.clk(ty)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.maximize_window()
    driver.refresh()
    cs = HomePage(driver)
    cs.click_post_demand()
    cs.click_community_needs()
    # text = "shisuhdacnkcnxzjxl"
    # js = "document.getElementsByClassName('youlingTitle postDemand:visible el-textarea__inner').innerHTML='%s'" % text
    # t = driver.execute_script(js)
    # print(t)
    driver.execute_script("$('.youlingTitle .postDemand:visible').find('.el-textarea__inner')")
