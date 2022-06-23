from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.log import Log
from selenium.common.exceptions import NoSuchElementException
import allure
import time

_log = Log()

head = (By.CLASS_NAME, "monicker fl clearfix")
personal_center = (By.CLASS_NAME, "perCen")
tag_name = (By.CSS_SELECTOR, "div.rinei>div:first-child h2:first-child")
user_name = (By.CSS_SELECTOR, "div.top>span.name")
title_name = (By.CSS_SELECTOR, "div.monicker.fl.clearfix>span.nameSty")
user_info = (By.CSS_SELECTOR, "div.xinxi>span")
my_info = (By.XPATH, "//li[text()='我的信息']")
perfect_information = (By.CSS_SELECTOR, "div.message a")
my_delivery = (By.XPATH, "//p[text()='我的投递']")
my_collect = (By.XPATH, "//p[text()='我的收藏']")
my_apply = (By.XPATH, "//p[text()='我的报名']")
unfold_job_status = (By.CSS_SELECTOR, ".el-select")
r_job_status = (By.CSS_SELECTOR, "li.el-select-dropdown__item.selected.hover")
starting_salary = (By.CSS_SELECTOR, "请输入起始薪资")
end_salary = (By.CSS_SELECTOR, "请输入结束薪资")
job_my_attendance = (By.XPATH, "//p[text()='我的考勤']")
job_resume_preview = (By.XPATH, "//p[text()='简历预览']")
job_friends_share = (By.XPATH, "//p[text()='分享好友']")
job_sign_in = (By.XPATH, "//p[text()='签到']")
resume_refresh = (By.CSS_SELECTOR, "div.rinei>div:first-child h2:first-child span+a+span span")
r_resume_refresh = (By.CSS_SELECTOR, "div.rinei>div:first-child h2:first-child span+a+span span")
resume_preview = (By.CSS_SELECTOR, "div.rinei>div:first-child h2:first-child span+a span span")
r_edit_card = (By.CSS_SELECTOR, "div.myMessage2 div")
r_work_experience = (By.CSS_SELECTOR, "div.myMessage3 div")
r_skill_certificate = (By.CSS_SELECTOR, "div.myMessage4 div")
edit_card = (By.XPATH, "//div[@class='myMessage2']//span[@class='riCompile']/span")
expected_position = (By.XPATH, "//div[@class='myMessage2']//div[@class='btn']/span")
work_address = (By.XPATH, "//div[@class='myMessage2']//div[@class='bottomText']/p[1]")
self_introduction = (By.XPATH, "//div[@class='myMessage2']//div[@class='bottomText']/p[2]")
affirm_amend_card = (By.XPATH, "//div[@class='compileMyMessage']//span[@class='riCompile']/span[2]")
cancel_amend_card = (By.XPATH, "//div[@class='compileMyMessage']//span[@class='riCompile']/span[1]")
click_bir = (By.XPATH, "//div[@class='xinxi']/div[@class='top'][1]//input")
click_ed = (By.XPATH, "//div[@class='xinxi']/div[@class='top'][2]//input")
previous_year = (By.CSS_SELECTOR, "[aria-label='前一年']")
next_year = (By.CSS_SELECTOR, "[aria-label='后一年']")
last_month = (By.CSS_SELECTOR, "[aria-label='上个月']")
next_month = (By.CSS_SELECTOR, "[aria-label='下个月']")
current_year = (By.XPATH, "//span[@role='button'][1]")
current_month = (By.XPATH, "//span[@role='button'][2]")
click_education = (By.CSS_SELECTOR, "div.xinxi div.el-select input.el-input__inner")
click_working_years = (By.CSS_SELECTOR, "div.wantjob div.el-select input.el-input__inner")
want_job = (By.CSS_SELECTOR, ".wantjob .btn")
there_num = (By.XPATH, "//ul[@class='threeList']/li")
affirm_job = (By.CSS_SELECTOR, ".bottomBtn .Btn")
quit_job = (By.CSS_SELECTOR, ".addrescanle")
selected_job = (By.XPATH, "//div[@class='addressbox']//span[@class='xuanzhongCity']")
send_introduction = (By.CSS_SELECTOR, ".introduction textarea")
redact_work_experience = (By.CSS_SELECTOR, ".myMessage3 .riCompile")
affirm_work_experience = (By.XPATH, "//div[@class='compileMyMessage3']//span[@class='riCompile']/span[2]")
cancel_work_experience = (By.XPATH, "//div[@class='compileMyMessage3']//span[@class='riCompile']/span[1]")
s_firm_name = (By.CSS_SELECTOR, ".el-form-item label[for=company]+div input")
c_working_hours = (By.CSS_SELECTOR, ".el-col.el-col-24 span")
job_current_year = (By.XPATH, "//div[@class='el-picker-panel__body']/div[1]/*/div")
n_job_current_year = (By.XPATH, "//div[@class='el-picker-panel__body']/div[2]/*/div")
job_previous_year = (By.CSS_SELECTOR, ".el-icon-d-arrow-left")
job_next_year = (By.CSS_SELECTOR, ".el-icon-d-arrow-right")
job_last_month = (By.CSS_SELECTOR, ".el-icon-arrow-left")
job_next_month = (By.CSS_SELECTOR, ".el-icon-arrow-right")
r_job_content = (By.CSS_SELECTOR, ".el-form-item .el-textarea textarea")
new_job_content = (By.CSS_SELECTOR, "button.el-button--small")
skill_certificate = (By.CSS_SELECTOR, ".myMessage4 .riCompile")
affirm_skill_certificate = (By.XPATH, "//div[@class='compilemyMessage4']//span[@class='riCompile']/span[2]")
cancel_skill_certificate = (By.XPATH, "//div[@class='compilemyMessage4']//span[@class='riCompile']/span[1]")
send_skill_name = (By.XPATH, "//label[text()='技能名称']/following-sibling::div/div[@class='el-col el-col-10']//input")
c_skill_end_time = (By.CSS_SELECTOR, ".el-form-item.TimeBox input")
skill_present_year = (By.XPATH, "//span[@class='el-date-picker__header-label']")
skill_previous_year = (By.CSS_SELECTOR, "button[aria-label=前一年]")
skill_next_year = (By.CSS_SELECTOR, "button[aria-label=后一年]")
upload = (By.NAME, "file")
c_new_skill = (By.CSS_SELECTOR, ".el-button--small")
c_posted_position = (By.CSS_SELECTOR, "p.number")
c_interested_me = (By.CSS_SELECTOR, "p.number1")
r_interested = (By.CSS_SELECTOR, ".myMessage1 h2")
c_resume_state = (By.CSS_SELECTOR, ".shang .el-select input")
s_firm_post_name = (By.CSS_SELECTOR, ".myMessage1 .el-input-group--append input")
c_firm_post_inquire = (By.CSS_SELECTOR, ".inputBox .el-input-group--append span")
r_application_details = (By.CSS_SELECTOR, ".el-table__row")
c_next_page = (By.CSS_SELECTOR, "button.btn-next")
c_previous_page = (By.CSS_SELECTOR, "btn-prev")
s_collect_input = (By.CSS_SELECTOR, "div.rinei input")
c_collect_find = (By.CSS_SELECTOR, "div.rinei input+div")
r_collect_list = (By.CSS_SELECTOR, "table.el-table__body tr div")
d_collect = (By.CSS_SELECTOR, "table.el-table__body span")
r_balance = (By.CSS_SELECTOR, ".rightbtn span")
r_recharge = (By.CSS_SELECTOR, ".rightbtn .btn")
c_record = (By.CSS_SELECTOR, ".resume span")
record_details = (By.CSS_SELECTOR, ".right")
new_record_details = (By.XPATH, "//div[@class='.right'][1]")
verification_code = (By.CSS_SELECTOR, "span.textcolor")
s_phone = (By.CSS_SELECTOR, "p.inputBox1 input.el-input__inner")
s_verification_code = (By.CSS_SELECTOR, "p.inputBox input[placeholder='请输入验证码']")
s_pwd = (By.CSS_SELECTOR, "p.inputBox input[placeholder='请输入新密码']")
s_new_pwd = (By.CSS_SELECTOR, "p.inputBox input[placeholder='请再次输入密码']")
c_pwd_amend = (By.CSS_SELECTOR, "div.btn")
c_affirm_btn = (By.CSS_SELECTOR, "div.bottomBtn span+span")
rtext_code = (By.XPATH, "//div[@class='el-input-group__append']/span")


class PersonalCenter(Base):

    @allure.step("鼠标悬停到个人头像上")
    def hover_head(self):
        _log.info("鼠标悬停到个人头像上-- %s" % head[1])
        self.hover_element(head)

    @allure.step("获取导航栏用户姓名")
    def rtext_title_name(self):
        _log.info("获取导航栏用户姓名-- %s" % title_name[1])
        r = self.rtext(title_name)
        return r

    @allure.step("切换到个人中心")
    def switch_personal_center(self):
        _log.info("切换到个人中心-- %s" % personal_center[1])
        self.clk(personal_center)

    @allure.step("切换模块")
    def click_module(self, module):
        m = (By.XPATH, "//li[text()='%s']" % module)
        _log.info("切换模块-- %s" % m[1])
        self.clk(m)

    @allure.step("获取页面标签")
    def tag_name(self):
        _log.info("获取页面标签-- %s" % tag_name[1])
        t = self.rtext(tag_name)
        return t

    @allure.step("获取当前用户的用户姓名")
    def rtext_user_name(self):
        _log.info("获取当前用户的用户姓名-- %s" % user_name[1])
        t = self.rtext(user_name)
        return t

    @allure.step("获取用户信息")
    def rtext_user_info(self):
        _log.info("获取用户信息-- %s" % user_info[1])
        r = self.rtexts(user_info)
        return r

    @allure.step("返回我的信息页")
    def return_my_info(self):
        _log.info("返回我的信息页-- %s" % perfect_information[1])
        self.clk(my_info)

    @allure.step("点击完善求职信息")
    def perfect_information(self):
        _log.info("点击完善求职信息-- %s" % perfect_information[1])
        self.clk(perfect_information)

    @allure.step("点击我的投递")
    def my_delivery(self):
        _log.info("点击我的投递-- %s" % my_delivery[1])
        self.clk(my_delivery)

    @allure.step("点击我的收藏")
    def my_collect(self):
        _log.info("点击我的收藏-- %s" % my_collect[1])
        self.clk(my_collect)

    @allure.step("点击我的报名")
    def my_apply(self):
        _log.info("点击我的报名-- %s" % my_apply[1])
        self.clk(my_apply)

    @allure.step("展开求职状态列表")
    def unfold_job_status(self):
        _log.info("展开求职状态列表-- %s" % unfold_job_status[1])
        self.clk(unfold_job_status)

    @allure.step("选择求职状态")
    def select_job_status(self, text):
        # text:  离职-随时到岗  在职-在找工作   在职-不考虑
        job_status = (By.XPATH, "//div[@class='el-select-dropdown el-popper']//span[text()='%s']" % text)
        _log.info("选择求职状态-- %s" % job_status[1])
        self.clk(job_status)

    @allure.step("获取简历页用户的求职状态")
    def retxt_job_status(self):
        _log.info("获取简历页用户的求职状态-- %s" % r_job_status[1])
        r = self.rtext(r_job_status)
        return r

    @allure.step("输入起始薪资")
    def starting_salary(self, text):
        if str.isdigit(text):
            _log.info("输入起始薪资-- %s" % starting_salary[1])
            self.sendkeys(starting_salary, text)
        else:
            _log.error("手机号类型错误，请输入数字")
            print("起始薪资输入格式错误，请输入数字")

    @allure.step("输入结束薪资")
    def end_salary(self, text):
        if str.isdigit(text):
            _log.info("输入起始薪资-- %s" % end_salary[1])
            self.sendkeys(end_salary, text)
        else:
            _log.error("手机号类型错误，请输入数字")
            print("起始薪资输入格式错误，请输入数字")

    @allure.step("点击求职管理中的我的考勤")
    def job_management_my_attendance(self):
        _log.info("点击求职管理中的我的考勤-- %s" % job_my_attendance[1])
        self.clk(job_my_attendance)

    @allure.step("点击求职管理中的简历预览")
    def job_management_resume_preview(self):
        _log.info("点击求职管理中的简历预览-- %s" % job_resume_preview[1])
        self.clk(job_resume_preview)

    @allure.step("点击求职管理中的分享好友")
    def job_management_friends_share(self):
        _log.info("点击求职管理中的分享好友-- %s" % job_friends_share[1])
        self.clk(job_friends_share)

    @allure.step("点击求职管理中的签到")
    def job_management_sign_in(self):
        _log.info("点击求职管理中的签到-- %s" % job_sign_in[1])
        self.clk(job_sign_in)

    @allure.step("点击简历刷新")
    def click_resume_refresh(self):
        _log.info("点击简历刷新-- %s" % resume_refresh[1])
        self.clk(resume_refresh)

    @allure.step("获取简历刷新按钮的当前文本")
    def rtext_resume_refresh(self):
        _log.info("获取简历刷新按钮的当前文本-- %s" % r_resume_refresh[1])
        r = self.rtext(r_resume_refresh)
        return r

    @allure.step("点击简历预览")
    def click_resume_preview(self):
        _log.info("点击简历刷新-- %s" % resume_preview[1])
        self.clk(resume_preview)

    @allure.step("获取我的名片中全部文本")
    def rtext_edit_card(self):
        _log.info("获取我的名片中全部文本-- %s" % r_edit_card[1])
        r = self.rtext(r_edit_card)
        return r

    @allure.step("获取工作经验中全部文本")
    def rtext_work_experience (self):
        _log.info("获取工作经验中全部文本-- %s" % r_work_experience[1])
        r = self.rtext(r_work_experience)
        return r

    @allure.step("获取技能证书中全部文本")
    def rtext_skill_certificate(self):
        _log.info("获取技能证书中全部文本-- %s" % r_skill_certificate[1])
        r = self.rtext(r_skill_certificate)
        return r

    @allure.step("点击我的名片中的编辑按钮")
    def click_edit_card(self):
        _log.info("点击我的名片中的编辑按钮-- %s" % edit_card[1])
        self.clk(edit_card)

    @allure.step("获取用户期望职位")
    def rtexts_expected_position(self):
        _log.info("获取用户期望职位-- %s" % expected_position[1])
        r = self.rtexts(expected_position)
        return r

    @allure.step("获取用户信息")
    def rtext_user_xinxi(self, num):
        #   num  1:性别   2:年龄    3:学历    4:工作经验
        xinxi = (By.XPATH, "//div[@class='myMessage2']//div[@class='xinxi']/span[%s]" % num)
        _log.info("获取用户信息-- %s" % xinxi[1])
        r = self.rtext(xinxi)
        return r

    @allure.step("获取用户工作地址")
    def rtext_work_address(self):
        _log.info("获取用户工作地址-- %s" % work_address[1])
        r = self.rtext(work_address)
        return r

    @allure.step("获取用户自我介绍")
    def rtext_self_introduction(self):
        _log.info("获取用户自我介绍-- %s" % self_introduction[1])
        r = self.rtext(self_introduction)
        return r

    @allure.step("确认修改编辑后的我的名片")
    def click_affirm_amend_card(self):
        _log.info("确认修改编辑后的我的名片-- %s" % affirm_amend_card[1])
        self.clk(affirm_amend_card)

    @allure.step("取消修改编辑后的我的名片")
    def click_cancel_amend_card(self):
        _log.info("取消修改编辑后的我的名片-- %s" % cancel_amend_card[1])
        self.clk(cancel_amend_card)

    @allure.step("编辑名片中，点击生日控件")
    def click_birthday(self):
        _log.info("编辑名片中，点击生日控件-- %s" % click_bir[1])
        self.clk(click_bir)

    @allure.step("编辑名片中，点击学历控件")
    def click_education(self):
        _log.info("编辑名片中，点击学历控件-- %s" % click_ed[1])
        self.clk(click_ed)

    @allure.step("切换出生日期")
    def cut_birthday(self, year, month, day):
        cy = self.rtext(current_year)
        cy = int(cy[:-2])
        cm = self.rtext(current_month)
        cm = int(cm[:-2])
        if year-cy < 0:
            for i in range(abs(year-cy)):
                self.clk(previous_year)
        elif year-cy > 0:
            for i in range(year-cy):
                self.clk(next_year)
        if month-cm < 0:
            for i in range(abs(month-cm)):
                self.clk(last_month)
        elif month-cm > 0:
            for i in range(year-cy):
                self.clk(next_month)
        click_day = (By.CSS_SELECTOR, ".available * span:nth-child(1)")
        _log.info("切换出生日期-- %s" %click_day[1])
        self.findElements(click_day)[day-1].click()
        # self.clk(click_day)

    @allure.step("选择学历")
    def select_education(self, num):
        #   1:"小学以下", 2:"小学", 3:"初中", 4:"高中", 5:"中专", 6:"大专", 7:"本科", 8:"硕士", 9:"博士"
        education = {1:"小学以下", 2:"小学", 3:"初中", 4:"高中", 5:"中专", 6:"大专", 7:"本科", 8:"硕士", 9:"博士"}
        _log.info("点击学历选择框-- %s" % click_education[1])
        self.clk(click_education)
        e = (By.XPATH, "//span[text()='%s']" % education[num])
        time.sleep(0.5)
        ee = (By.CSS_SELECTOR, "div[x-placement=top-start]")
        while not self.isElementPresent(e):
            self.keyboard_down(ee)
        _log.info("选择学历-- %s" % e[1])
        self.clk(e)

    @allure.step("选择工龄")
    def select_working_years(self, num):
        #   working_years: 应届生，1-3年，3-5年，5-10年，10年以上
        working = {1: "应届生", 2: "1-3年", 3: "3-5年", 4: "5-10年", 5: "10年以上"}
        _log.info("点击工龄选择框-- %s" % click_working_years[1])
        self.clk(click_working_years)
        e = (By.XPATH, "//span[text()='%s']" % working[num])
        _log.info("选择工龄-- %s" % e[1])
        time.sleep(0.5)
        self.clk(e)

    @allure.step("点击想要的工作按钮")
    def click_want_job(self):
        _log.info("点击想要的工作按钮-- %s" % want_job[1])
        self.clk(want_job)

    @allure.step("选择想要的一级工作")
    def select_want_job_one(self, job_one):
        j_one = (By.XPATH, "//div[@class='el-scrollbar__view']//span[text()='%s']" % job_one)
        _log.info("选择想要的一级工作-- %s" % j_one[1])
        self.clk(j_one)

    @allure.step("选择想要的二级工作")
    def select_want_job_two(self,job_two):
        j_two = (By.XPATH, "//div[@class='el-scrollbar__view']//span[text()='%s']" % job_two)
        _log.info("选择想要的二级工作-- %s" % j_two[1])
        self.clk(j_two)

    @allure.step("选择想要的三级工作")
    def select_want_job_there(self,num):
        _log.info("选择想要的三级工作-- %s" % there_num[1])
        self.findElements(there_num)[num].click()

    @allure.step("获取三级工作岗位数量")
    def number_job_there(self):
        _log.info("获取三级工作岗位数量-- %s" % there_num[1])
        return len(self.findElements(there_num))

    @allure.step("确认想要的工作")
    def select_want_job_affirm(self):
        _log.info("选择想要的工作-- %s" % affirm_job[1])
        self.clk(affirm_job)

    @allure.step("关闭向要的工作弹窗")
    def quit_want_job(self):
        _log.info("选择想要的工作-- %s" % quit_job[1])
        self.clk(quit_job)

    @allure.step("获取已选择的想要的工作")
    def rtext_selected_job(self):
        _log.info("获取已选择的想要的工作-- %s" % selected_job[1])
        r = self.rtexts(selected_job)
        return r

    @allure.step("取消选中的想要的工作")
    def cancel_want_job(self, job):
        cancel_job = (By.XPATH, "//div[@class='addressbox']//span[text()='%s']/img" % job)
        _log.info("取消选中的想要的工作-- %s" % cancel_job[1])
        self.clk(cancel_job)

    @allure.step("填写自我介绍")
    def send_self_introduction(self, text):
        _log.info("取消选中的想要的工作-- %s" % send_introduction[1])
        self.sendkeys(send_introduction, text)

    @allure.step("编辑工作经历")
    def click_redact_work_experience(self):
        _log.info("取消选中的想要的工作-- %s" % redact_work_experience[1])
        self.clk(redact_work_experience)

    @allure.step("确认修改编辑工作经历")
    def click_affirm_work_experience(self):
        _log.info("确认修改编辑工作经历-- %s" % affirm_work_experience[1])
        self.clk(affirm_amend_card)

    @allure.step("取消修改编辑工作经历")
    def click_cancel_work_experience(self):
        _log.info("取消修改编辑工作经历-- %s" % cancel_work_experience[1])
        self.clk(cancel_amend_card)

    @allure.step("选择职位")
    def select_position(self, position_one, position_two, position_there):
        click_position_one = (By.XPATH, "//div[@id='cascader-menu-2621-0']//li/span[text()='%s']" % position_one)
        _log.info("选择一级职位-- %s" % click_position_one[1])
        self.clk(click_position_one)
        click_position_two = (By.XPATH, "//div[@id='cascader-menu-6307-1']//li/span[text()='%s']" % position_two)
        _log.info("选择二级职位-- %s" % click_position_two[1])
        self.clk(click_position_two)
        click_position_there= (By.XPATH, "//div[@id='cascader-menu-9560-2']//li/span[text()='%s']" % position_there)
        _log.info("选择三级职位-- %s" % click_position_there[1])
        self.clk(click_position_there)

    @allure.step("填写公司名称")
    def sendkeys_firm_name(self, text):
        _log.info("填写公司名称-- %s" % s_firm_name[1])
        self.sendkeys(s_firm_name, text)

    @allure.step("选择工作时间段")
    def click_working_hours(self, start_year, start_month, start_day, end_year, end_month, end_day):
        _log.info("点击弹出工作时间段弹窗-- %s" % c_working_hours[1])
        self.clk(c_working_hours)

        #   获取当前年月
        cy = self.rtext(job_current_year)
        cy = cy.findall("\d+", cy)
        sy = str(cy[0])
        sm = str(cy[1])
        #   选择开始时间
        if start_year - sy < 0:
            for i in range(abs(start_year - sy)):
                self.clk(job_previous_year)
        elif start_year - sy > 0:
            for i in range(start_year - sy):
                self.clk(job_next_year)
        if start_month - sm < 0:
            for i in range(abs(start_month - sm)):
                self.clk(job_last_month)
        elif start_month - sm > 0:
            for i in range(start_month - sm):
                self.clk(job_next_month)
        click_start_day = (By.CSS_SELECTOR, ".is-left .available * span:nth-child(%s)" % start_day)
        _log.info("选择开始时间-- %s" % click_start_day[1])
        self.clk(click_start_day)

        #   获取下个月的年月
        n_cy = self.rtext(job_current_year)
        n_cy = n_cy.findall("\d+", n_cy)
        ny = str(n_cy[0])
        nm = str(n_cy[1])
        #   选择结束时间
        if end_year - ny < 0:
            for i in range(abs(end_year - ny)):
                self.clk(job_previous_year)
        elif end_year - ny > 0:
            for i in range(end_year - ny):
                self.clk(job_next_year)
        if end_month - nm < 0:
            for i in range(abs(end_month - nm)):
                self.clk(job_last_month)
        elif end_month - nm > 0:
            for i in range(end_month - nm):
                self.clk(job_next_month)
        click_end_day = (By.CSS_SELECTOR, ".is-right .available * span:nth-child(%s)" % end_day)
        _log.info("选择结束时间-- %s" % click_end_day[1])
        self.clk(click_end_day)

    @allure.step("填写工作内容")
    def rtext_job_content(self, text):
        self.sendkeys(r_job_content, text)

    @allure.step("点击新增工作经验")
    def click_new_job_content(self):
        self.clk(new_job_content)

    @allure.step("删除工作经验")
    def click_del_job_content(self):
        del_job_content = (By.CSS_SELECTOR, "#pane-four div.el-row:nth-child(1) button.el-button--danger span")     # nth-child(1):第几个删除按钮
        self.clk(del_job_content)

    @allure.step("编辑技能证书")
    def click_skill_certificate(self):
        _log.info("取消选中的想要的工作-- %s" % skill_certificate[1])
        self.clk(skill_certificate)

    @allure.step("确认修改编辑技能证书")
    def click_affirm_skill_certificate(self):
        _log.info("确认修改编辑技能证书-- %s" % affirm_skill_certificate[1])
        self.clk(affirm_skill_certificate)

    @allure.step("取消修改编辑技能证书")
    def click_cancel_skill_certificate(self):
        _log.info("取消修改编辑技能证书-- %s" % cancel_skill_certificate[1])
        self.clk(cancel_skill_certificate)

    @allure.step("填写技能名称")
    def send_skill_name(self, text):
        _log.info("填写技能名称-- %s" % send_skill_name[1])
        self.sendkeys(send_skill_name, text)

    @allure.step("选择技能证书有效期截止时间")
    def click_skill_end_time(self, year, month):
        """
        :param year: 年，只填写数字
        :param month: 月，只填写数字
        :return:
        """
        _log.info("选择技能证书有效期截止时间-- %s" % c_skill_end_time[1])
        self.clk(c_skill_end_time)
        present_year = self.rtext(skill_present_year)
        present_year.findall("\d+", present_year)
        if year - present_year < 0:
            for i in range(abs(year - present_year)):
                self.clk(skill_previous_year)
        elif year - present_year > 0:
            for i in range(year - present_year):
                self.clk(skill_next_year)
        skill_m = (By.CSS_SELECTOR, "//table[@class='el-month-table']//a[%s]" % month)
        self.clk(skill_m)

    @allure.step("点击上传图片按钮")
    def upload_pictures(self, os):
        _log.info("点击上传图片按钮-- %s" % upload[1])
        self.sendkeys(upload, os)

    @allure.step("新增技能证书")
    def new_skill(self):
        _log.info("点击上传图片按钮-- %s" % c_new_skill[1])
        self.clk(c_new_skill)

    @allure.step("切换到已投递的职位")
    def click_posted_position(self):
        _log.info("切换到已投递的职位-- %s" % c_posted_position[1])
        self.clk(c_posted_position)

    @allure.step("切换到对我感兴趣")
    def click_interested_me(self):
        _log.info("切换到对我感兴趣-- %s" % c_interested_me[1])
        self.clk(c_interested_me)

    @allure.step("获取我投递的页列表标签")
    def rtext_interested_title(self):
        _log.info("获取我投递的页列表标签-- %s" % r_interested[1])
        return self.rtext(r_interested)

    @allure.step("点击简历状态")
    def click_resume_state(self):
        _log.info("点击简历状态-- %s" % c_resume_state[1])
        self.clk(c_resume_state)
        _log.info("选择简历类型-- %s" % c_resume_state[1])

    @allure.step("选择简历状态")
    def select_resume_state(self, state):
        s_resume_state = (By.XPATH, "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='%s']" % state)
        _log.info("选择简历状态-- %s" % s_resume_state[1])
        self.clk(s_resume_state)

    @allure.step("输入企业、职位名称")
    def send_firm_post_name(self, name):
        _log.info("输入企业、职位名称-- %s" % s_firm_post_name[1])
        self.sendkeys(s_firm_post_name, name)

    @allure.step("点击搜索按钮")
    def click_firm_post_name_inquire(self):
        _log.info("点击查询按钮-- %s" % c_firm_post_inquire[1])
        self.clk(c_firm_post_inquire)

    @allure.step("获取当前页简历投递详情信息")
    def r_application_details(self):
        _log.info("获取当前页简历投递详情信息-- %s" % r_application_details[1])
        r = self.r

        texts(r_application_details)
        print(r)
        return r

    @allure.step("切换简历投递列表")
    def cut_application_details_list(self, num):
        """
        :param num:页数
        :return:
        """
        c_application_details = (By.XPATH, "//ul[@class='el-pager']/li[text()='%s']" % num)
        _log.info("切换简历投递列表-- %s" % c_application_details[1])
        self.rtexts(c_application_details)

    @allure.step("点击下一页按钮")
    def click_next_page(self):
        _log.info("点击下一页按钮-- %s" % c_next_page[1])
        self.rtexts(c_next_page)

    @allure.step("点击上一页按钮")
    def click_previous_page(self):
        _log.info("点击上一页按钮-- %s" % c_previous_page[1])
        self.rtexts(c_previous_page)

    @allure.step("收藏页输入框输入")
    def send_collect_input(self, text):
        _log.info("收藏页输入框输入-- %s" % s_collect_input[1])
        self.sendkeys(s_collect_input, text)

    @allure.step("点击收藏页输入框查询按钮")
    def click_collect_find(self):
        _log.info("点击收藏页输入框查询按钮-- %s" % c_collect_find[1])
        self.clk(c_collect_find)

    @allure.step("获取收藏页列表数据")
    def rtext_collect_list(self):
        _log.info("获取当前页简历投递详情信息-- %s" % r_collect_list[1])
        self.rtexts(r_collect_list)

    @allure.step("删除收藏的岗位")
    def del_collect(self):
        _log.info("删除收藏的岗位-- %s" % d_collect[1])
        self.clk(d_collect)

    @allure.step("获取优豆余额")
    def rtext_bean_balance(self):
        _log.info("获取优豆余额-- %s" % r_balance[1])
        self.rtext(r_balance)

    @allure.step("点击去充值按钮")
    def click_recharge(self):
        _log.info("点击去充值按钮-- %s" % r_recharge[1])
        self.clk(r_recharge)

    @allure.step("点击跳转到优豆记录、我的任务页")
    def click_bean_record(self):
        _log.info("点击跳转到优豆记录、我的任务页-- %s" % c_record[1])
        self.clk(c_record)

    @allure.step("点击我的任务去完成")
    def click_to_complete(self, num):
        #   num:1 签到、2 简历投递、3 创建名片、4 完善简历、5 完成验证、6 分享链接、7 分享并成功注册
        c_complete = (By.XPATH, "//div[@class='myMessage2']//div[@class='centent'][%s]//div[@class='btn']" % num)
        _log.info("点击我的任务去完成-- %s" % c_complete[1])
        self.clk(c_complete)

    @allure.step("获取优豆记录：类型、数量")
    def rtext_bean_record_details(self):
        _log.info("获取优豆记录：类型、数量-- %s" % record_details[1])
        self.rtexts(record_details)

    @allure.step("获取最新的优豆记录")
    def rtext_bean_record_details(self):
        _log.info("获取最新的优豆记录-- %s" % new_record_details[1])
        self.rtexts(new_record_details)

    @allure.step("修改密码，点击候选验证码")
    def click_verification_code(self):
        _log.info("修改密码，点击候选验证码-- %s" % verification_code[1])
        self.clk(verification_code)

    @allure.step("输入要修改密码的手机号")
    def sendkey_phone(self, phone):
        _log.info("输入要修改密码的手机号-- %s" % s_phone[1])
        self.sendkeys(s_phone, phone)

    @allure.step("输入验证码")
    def sendkey_verification_code(self, code):
        _log.info("输入要修改密码的手机号-- %s" % s_verification_code[1])
        self.sendkeys(s_verification_code, code)

    @allure.step("输入新密码")
    def sendkey_pwd(self, pwd):
        _log.info("输入要修改密码的手机号-- %s" % s_pwd[1])
        self.sendkeys(s_pwd, pwd)

    @allure.step("确认新密码")
    def sendkey_new_pwd(self, new_pwd):
        _log.info("输入要修改密码的手机号-- %s" % s_new_pwd[1])
        self.sendkeys(s_new_pwd, new_pwd)

    @allure.step("提交密码修改")
    def click_pwd_amend(self):
        _log.info("提交密码修改-- %s" % c_pwd_amend[1])
        self.clk(c_pwd_amend)

    @allure.step("点击确认按钮")
    def click_affirm_btn(self):
        _log.info("点击确认按钮-- %s" % c_affirm_btn[1])
        self.clk(c_affirm_btn)

    @allure.step("获取系统提示")
    def code_text(self):
        _log.info("获取系统提示-- %s" % rtext_code[1])
        return self.rtext(rtext_code)
















