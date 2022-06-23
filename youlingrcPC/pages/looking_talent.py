from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.log import Log
from selenium.common.exceptions import NoSuchElementException
import allure
import time

_log = Log()


class LookTalent(Base):

    @allure.step("获取人才列表中期望的职位")
    def rtext_intention_job(self, num):
        r_intention_job = (By.XPATH, "//div[@class='leftCentent']/ul[%s]//div[@class='gonglei']/span" % num)
        _log.info("获取列表中的岗位名称-- %s" % r_intention_job[1])
        r = self.rtexts(r_intention_job)
        return r