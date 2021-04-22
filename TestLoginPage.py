# #!__author__ = "yf"
# """
# pycharm
# """
from selenium import webdriver
import  ddt
import unittest
from selenium.common.exceptions import NoSuchElementException

from LOG import LOG
from LOG import saveScreenShot



class TestLogin1(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver
    # @classmethod
    # def setUpClass(cls) -> None:
    #     LOG(filename="test.log")
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--ignore-certificate-error")
    #     options.add_argument("--ignore-ssl-errors")
    #     caps = webdriver.DesiredCapabilities.CHROME.copy()
    #     caps['acceptInsecureCerts'] = True
    #     caps['acceptSslCerts'] = True
    #     cls.driver = webdriver.Chrome(options=options, desired_capabilities=caps)
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
    #     pass


    def Login(self, username, psw):
        print(username, psw)
        self.driver.get("https://www.ablesky.com/login.do?fromurl=https://www.ablesky.com/recommend")
        self.driver.maximize_window()
        # switch_ele = self.driver.find_element_by_class_name("login-switch-wrap")
        try:
            switch_ele = self.driver.find_element_by_class_name("login-switch")
            switch_ele.click()
            self.driver.find_element_by_id("J_loginUsername").send_keys(username)
            self.driver.find_element_by_id("J_loginPassword").send_keys(psw)
            self.driver.find_element_by_id("J_loginBtn").click()
        except NoSuchElementException as e:
            LOG("Error : not found {}".format(e))
            saveScreenShot(self.driver)
        except:
            LOG("Error : unknown exception")
            saveScreenShot(self.driver)

    # @ddt.file_data("login_data.json")
    # @ddt.unpack
    # def testALogin(self, **data):
    #     print(data)
    #     self.Login(data["username"], data["password"])
