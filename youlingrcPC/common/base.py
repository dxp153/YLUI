from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from common.log import Log
import time

_log = Log()


class Base:
    '''基于原生selenium的二次封装'''

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.poll_frequency = 0.5

    def findelement(self, loctor):
        if not isinstance(loctor, tuple):
            print('loctor参数类型输入错误，必须传元祖类型：loctor=("by,value")')
        else:
            ele = self.driver.find_element(loctor[0], loctor[1])
            return ele

    def findElement(self, loctor):
        #   定位单个元素
        #   loctor=("by,value")
        #   WebDriverWait(driver,timeout,poll_frequency).until(lambda x: x.find_element_by_id("someId"))
        #   *的作用就是把list或者元祖分开传入
        try:
            if not isinstance(loctor, tuple):
                print('loctor参数类型输入错误，必须传元祖类型：loctor=("by,value")')
            else:
                print('定位方式-》%s,value值-》%s' % (loctor[0], loctor[1]))
                ele = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    EC.presence_of_element_located(loctor))
                return ele
        except:
            _log.error("{0}页面未找到{1}元素".format(self, loctor))

    def findElements(self, loctor):
        #   定位组一组元素
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*loctor))
            return ele
        except:
            _log.error("{0}页面未找到{1}元素".format(self, loctor))

    def findElementEC(self, loctor):
        #   用EC里的方法定位元素
        ele = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.presence_of_element_located(loctor))
        return ele

    def sendkeys(self, loctor, text):
        #   定义send_keys方法，text是传入的内容
        try:
            ele = self.findElement(loctor)
            ele.send_keys(text)
        except AttributeError:
            _log.error("%s 页面未找到 %s 元素" % (self, loctor))

    def clear(self, loctor):
        #   清空输入框内容
        try:
            ele = self.findElement(loctor)
            ele.clear()
        except Exception as e:
            _log.error(e)

    def clk(self, loctor):
        #   定义click方法
        try:
            ele = self.findElement(loctor)
            ele.click()
        except Exception as e:
            _log.error(e)

    def rtext(self, loctor):
        #   获取元素文本值
        try:
            time.sleep(0.5)
            text = self.findElement(loctor).text
            return text
        except Exception as e:
            _log.error(e)

    def rtexts(self, loctor):
        #   获取复数元素的文本值
        try:
            text = []
            ele = self.findElements(loctor)
            num = len(self.findElements(loctor))
            for i in range(num):
                text.append(ele[i-1].text)
            return text, num
        except Exception as e:
            _log.error(e)

    def get_att(self, loctor, element):
        #   获取元素属性值     填写value可以获取到input输入框的内容
        try:
            ele = self.findElement(loctor).get_attribute(element)
            return ele
        except Exception as e:
            _log.error(e)

    def locxy_click(self, x, y, left_click=True):
        #   dr:浏览器
        #   x:页面x坐标
        #   y:页面y坐标
        #   left_click:True为鼠标左键点击，否则为右键
        if left_click:
            ActionChains(self.driver).move_by_offset(x, y).click().perform()
        else:
            ActionChains(self.driver).move_by_offset(x, y).context_click().perform()
        #   将鼠标恢复到移动前的位置
        ActionChains(self.driver).move_by_offset(-x, -y).perform()

    def hover_element(self, loctor):
        #   鼠标悬停
        try:
            ele = self.findElement(loctor)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            _log.error(e)

    def tap_element(self, loctor):
        #   模拟手指触摸屏幕元素  无法调用
        ele = self.findElement(loctor)
        tas = TouchActions(driver)
        tas.tap(ele).perform()

    def is_displayed_ele(self, loctor):
        #   判断元素是否隐藏
        try:
            ele = self.findElement(loctor).is_displayed()
            print(ele)
            return ele
        except Exception as e:
            _log.error(e)

    def is_selected_ele(self, loctor):
        # 判断元素是否选中   选中返回True，没有选中返回false
        try:
            ele = self.findElement(loctor).is_selected()
            print(ele)
            return ele
        except Exception as e:
            _log.error(e)

    def is_enabled_ele(self, loctor):
        #   判断元素是否可用
        try:
            ele = self.findElement(loctor).is_enabled()
            return ele
        except Exception as e:
            _log.error(e)

    def is_staleness_of(self, loctor):
        #   不会用
        ele = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.staleness_of(loctor))
        return ele

    def is_text_in_element(self, loctor, _text):
        #   对元素的text文本进行判断，返回bool值
        ele = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
            EC.text_to_be_present_in_element(loctor, _text))
        return ele

    def isElementPresent(self, locta):
        #   查询界面上是否有ele元素存在
        try:
            self.findElement(locta)
        except Exception as e:
            _log.error(e)
            return False
        else:
            return True

    def get_back_color(self, loctor):
        #   获取元素的color属性，已元组（tuple）的方式输出
        ele = self.findElement(loctor)
        t = ele.value_of_css_property("background-color")
        #   从第5位开始取值
        rpga = t[4:]
        #   将字符串转换成列表
        r = list(eval(rpga))
        #   去除最后一位
        rpg = r[:-1]
        print(rpg)
        #   返回元祖类型
        return tuple(rpg)

    def get_color(self, loctor):
        #   获取元素的color属性，已元组（tuple）的方式输出
        ele = self.findElement(loctor)
        t = ele.value_of_css_property("color")
        #   从第5位开始取值
        rpga = t[4:]
        #   将字符串转换成列表
        r = list(eval(rpga))
        #   去除最后一位
        rpg = r[:-1]
        print(rpg)
        #   返回元祖类型
        return tuple(rpg)

    def RGB_to_Hex(self, RGB):
        #   :param RGBA: a tuple, exp: (59, 201, 255, 255)
        #   :return hex_str: a str, exp: #3BC9FFFF
        hex_str = '#'
        for i in RGB:
            num = int(i)  # 将RGBA的数值转换成数字类型
            hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
        # print(hex_str)
        return hex_str.lower()

    def get_back_rpg(self, loctor):
        #   获取界面上元素的颜色
        rpg = self.get_back_color(loctor)
        h = self.RGB_to_Hex(rpg)
        print(h)
        return h

    def get_rpg(self, loctor):
        #   获取界面上元素的颜色
        rpg = self.get_color(loctor)
        h = self.RGB_to_Hex(rpg)
        print(h)
        return h

    def get_list_number(self, loctor):
        #   获取ul中li的总数，并返回
        ul = self.findElement(loctor)
        lis = ul.find_elements_by_xpath("li")
        return len(lis)

    def new_win(self, url="http://www.baidu.com"):
        # 打开新窗口
        js = "window.open('%s');" % url
        self.driver.execute_script(js)

    def cut_win(self):
        # 切换到新打开的窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def cutBack_win(self):
        # 切回到最初打开的窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def js_scrollTop(self, t):
        #  js模拟鼠标滑轮下滑
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=%s" % t
        self.driver.execute_script(js)

    def js_scrollLeft(self, t):
        #  js模拟鼠标滑轮you滑
        js = "var q=document.documentElement.scrollLeft=%s" % t
        self.driver.execute_script(js)

    def js_scrollIntoView(self, loctor):
        #   js将页面滑动到指定元素位置
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, self.findElement(loctor))

    def keyboard_down(self, loctor):
        #   模拟键盘点击下键
        self.findElement(loctor).send_keys(Keys.DOWN)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.youlingrc.com/#/entirety/subject")
    driver.find_elements_by_xpath("$('//div[@class=youlingTitle']//div[@class='postDemand']:visible').find('//div[@class='el-textarea']')")


