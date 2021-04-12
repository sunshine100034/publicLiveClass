# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from selenium import webdriver
import unittest
import time
import ddt
from LOG import LOG

from selenium.common.exceptions import NoSuchElementException
    

# 出错之后恢复机制 没有做？？？
@ddt.ddt
class TestLogin(unittest.TestCase):

    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     pass
    @classmethod
    def setUpClass(cls) -> None:
        LOG(filename="test.log")
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True
        caps['acceptSslCerts'] = True
        cls.driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        pass

    def saveScreenShot(self):
        nowtime = time.strftime("%Y%m%d%H%M%S")
        file = nowtime + ".jpg"
        # file_path = os.path.realpath(__file__)
        file_path = os.path.dirname(__file__)
        file = os.path.join(file_path, file)
        file = os.path.normpath(file)
        self.driver.get_screenshot_as_file(file)

    @ddt.file_data("login_data.json")
    @ddt.unpack
    def testALogin(self, **data):
        print(data)
        self.driver.get("https://www.ablesky.com/login.do?fromurl=https://www.ablesky.com/recommend")
        self.driver.maximize_window()
        # switch_ele = self.driver.find_element_by_class_name("login-switch-wrap")
        try:
            switch_ele = self.driver.find_element_by_class_name("login-switch")
            switch_ele.click()
            self.driver.find_element_by_id("J_loginUsername").send_keys(data["username"])
            self.driver.find_element_by_id("J_loginPassword").send_keys(data["password"])
            self.driver.find_element_by_id("J_loginBtn").click()
        except NoSuchElementException as e:
            LOG("Error : not found {}".format(e))
            self.saveScreenShot()
        except:
            LOG("Error : unknown exception")
            self.saveScreenShot()


    # 注意*datas前面的*号，*会把里面的数据解析成两个
    # @ddt.data(*datas)
    # def testPublishCourse(self, kwargs):

    @ddt.file_data("PublishCourse_data.json")
    @ddt.unpack
    def testBPublishCourse(self, **kwargs):
        print(kwargs)
        # self.Login()
        time.sleep(2)
        self.driver.get("https://www.ablesky.com/liveCourseRedirect.do?action=toPostLiveCourse&organizationId=2249")
        time.sleep(2)
        try:
            print(kwargs["courseName"])
            self.driver.find_element_by_id("J_inputBox").send_keys(kwargs["courseName"])

            # 老师
            # 保证下拉框显示出来，才能执行click操作
            self.driver.find_element_by_class_name("select-arrow").click()
            time.sleep(1)
            option_list = self.driver.find_element_by_class_name("select-selector-ul").find_elements_by_tag_name("li")
            for option in option_list:
                id = option.get_attribute("assistantid")
                if id == kwargs['hostTeacherId']:
                    option.click()
                    break
                pass

            # 助教
            self.driver.find_elements_by_class_name("select-arrow")[1].click()
            time.sleep(1)
            option_list = self.driver.find_elements_by_class_name("select-selector-ul")[1].find_elements_by_tag_name("li")
            for option in option_list:
                id = option.get_attribute("assistantid")
                if id == kwargs['assistantId']:
                    option.click()
                    break
                pass



            js = 'document.getElementById("J_startTime1").value="2020-12-15";'
            response = self.driver.execute_script(js)

            # 加课时
            lesson_list = kwargs["lesson"]
            lessonNum = len(lesson_list)
            for i in range(0,lessonNum):
                lesson = lesson_list[i]
                print(lesson["date"])
                self.driver.find_elements_by_class_name("title-input")[i].send_keys(lesson["lessonName"])
                print(lesson["date"])
                # 日历移除readonly属性
                js = 'document.getElementsByName("dateTime")[{}].removeAttribute("readonly");'.format(i)
                response = self.driver.execute_script(js)

                js = 'document.getElementsByName("dateTime")[{}].value="{}";'.format(i, lesson["date"])
                response = self.driver.execute_script(js)

                #还没研究出来为什么不可以，暂时先用js代替
                # self.driver.find_elements_by_class_name("init-date")[i].find_element_by_id("J_startTime1").clear()
                # self.driver.find_elements_by_class_name("init-date")[i].find_element_by_id("J_startTime1").send_keys(lesson["date"])
                self.driver.find_elements_by_class_name("start-hour")[i].send_keys(lesson["startHour"])
                self.driver.find_elements_by_class_name("start-min")[i].send_keys(lesson["startMin"])
                self.driver.find_elements_by_class_name("end-hour")[i].send_keys(lesson["endHour"])
                self.driver.find_elements_by_class_name("end-min")[i].send_keys(lesson["endMin"])
                if i< lessonNum - 1:
                    self.driver.find_element_by_class_name("graybtn25_text").click()

            # 教室真实容量
            self.driver.find_element_by_id("J_peopleBox").send_keys(kwargs["courseNum"])

            # 公开课模式
            eles = self.driver.find_elements_by_name("publicMode")
            if kwargs["publicmode"] == "true":
                eles[0].click()
            else:
                eles[1].click()
            self.driver.find_element_by_id("J_initNumber").send_keys(kwargs["iniNum"])


            self.driver.find_element_by_id("J_showDefaultPhoto").click()
            time.sleep(2)
            phote = self.driver.find_element_by_id("J_setDefalutPhoto")
            phote.find_element_by_xpath(".//a/img").click()

        #     服务分类，列表选择
            li_level1 = self.driver.find_elements_by_class_name("level2")
            li_level1[0].click()
            li_level2 = self.driver.find_elements_by_class_name("level3")
            li_level2[0].click()

            self.driver.find_element_by_class_name("greenbtn35_text").click()
            time.sleep(2)
        except NoSuchElementException as e:
            # print("not found")
            LOG("Error : element not found")
        except Exception as e:
            LOG("Error :{} ".format(e))
            self.saveScreenShot()
        except:
            LOG("Error : unknown exception")
            self.saveScreenShot()

        time.sleep(10)

    # def test_12306(self):
    #     self.driver.get("https://www.12306.cn/index/")
    #     time.sleep(2)
    #     js = 'document.getElementById("train_date").removeAttribute("readonly");'
    #     self.driver.execute_script(js)
    #     self.driver.find_element_by_id("train_date").send_keys("2020-12-14")
    #     time.sleep(10)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
