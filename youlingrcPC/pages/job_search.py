from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.log import Log
from selenium.common.exceptions import NoSuchElementException
import allure
import time

_log = Log()

list = (By.XPATH, "//div[@class='leftCentent']/ul")


class JobSearch(Base):

    @allure.step("获取列表当前页列表元素数量")
    def num_job_list(self):
        num = self.rtexts(list)[1]
        return num

    @allure.step("获取列表中的岗位名称")
    def rtext_job_name(self, num):
        r_job_name = (By.XPATH, "//div[@class='leftCentent']/ul[%s]//p[@class='textStyle']/span[1]" % num)
        _log.info("获取列表中的岗位名称-- %s" % r_job_name[1])
        r = self.rtext(r_job_name)
        return r

    @allure.step("获取列表中的企业名称")
    def rtext_firm_name(self, num):
        r_firm_name = (By.XPATH, "//div[@class='leftCentent']/ul[%s]//p[@class='textStyle']/span[2]" % num)
        _log.info("获取列表中的企业名称-- %s" % r_firm_name[1])
        r = self.rtext(r_firm_name)
        return r

    @allure.step("获取列表中的岗位类型")
    def rtext_post_type(self, num):
        r_post_type = (By.XPATH, "//div[@class='leftCentent']/ul[%s]//span[@class='Textright']" % num)
        _log.info("获取列表中的岗位类型-- %s" % r_post_type[1])
        r = self.rtext(r_post_type)
        return r

