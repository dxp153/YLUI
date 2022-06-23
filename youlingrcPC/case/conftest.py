import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_login import LoginFun
from pages.login_sgin import SginEle
from pages.homepage_g import HomePage
from pages.job_search import JobSearch
from pages.looking_talent import LookTalent
from pages.personal_center import PersonalCenter


@pytest.fixture(scope='module')
def get_driver():
    #   打开浏览器
    # option = webdriver.ChromeOptions()
    # option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)  # 静默启动
    driver = webdriver.Chrome()
    #   实例化 LoginFun
    login = LoginFun(driver)
    sgin = SginEle(driver)
    home = HomePage(driver)
    job = JobSearch(driver)
    talent = LookTalent(driver)
    personal = PersonalCenter(driver)
    yield driver, login, sgin, home, job, talent, personal
    #   退出浏览器
    driver.quit()


@allure.step("登录优领人才")
@pytest.fixture(scope="class")
def login_rc(get_driver):
    """登录优领人才"""
    driver = get_driver[0]
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.maximize_window()
    driver.refresh()
    login = get_driver[1]
    login.login_rc(user='15797629873', password="123456")
    yield
    q = get_driver[1]
    q.hover_head()
    q.quit_rc_qy()


@allure.step("打开优领人才pc端")
@pytest.fixture(scope="function")
def quit_rc(get_driver):
    #   打开优领人才网站
    driver = get_driver[0]
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.maximize_window()
    driver.refresh()
    yield
    q = get_driver[1]
    q.hover_head()
    q.quit_rc_qy()



@pytest.fixture(scope="function")
def quit_rc_login(get_driver):
    #   打开优领人才网站
    driver = get_driver[0]
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.maximize_window()
    driver.refresh()
