# #!__author__ = "yf"
# """
# pycharm
# """
# from selenium import webdriver
# import unittest
# import time
#
# class TestLogin(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         pass
#
#     def tearDown(self) -> None:
#         self.driver.quit()
#         pass
#
#     def testLogin(self):
#         self.driver.get("https://www.ablesky.com/login.do?fromurl=https://www.ablesky.com/recommend")
#         time.sleep(2)
#
#     def testLogin2(self):
#         self.driver.get("https://www.ablesky.com/login.do?fromurl=https://www.ablesky.com/recommend")
#         time.sleep(2)
#
#
#
# # if __name__ == "__main__":
# unittest.main()
#
import  ddt
import unittest


datas =[{"courseName": "课程名称",
         "hostTeacherId": "5778083",
         "lessonName": "课时标题",
         "startHour": "19",
         "startMin": "19",
         "endHour": "22",
         "endMin": "22",
         "courseNum": "100"},
        {"courseName": "课程名称2",
         "hostTeacherId": "5778083",
         "lessonName": "课时标题2",
         "startHour": "19",
         "startMin": "19",
         "endHour": "22",
         "endMin": "22",
         "courseNum": "100"}]

datas1 =({"courseName": "课程名称",
         "hostTeacherId": "5778083",
         "lessonName": "课时标题",
         "startHour": "19",
         "startMin": "19",
         "endHour": "22",
         "endMin": "22",
         "courseNum": "100"},
        {"courseName": "课程名称2",
         "hostTeacherId": "5778083",
         "lessonName": "课时标题2",
         "startHour": "19",
         "startMin": "19",
         "endHour": "22",
         "endMin": "22",
         "courseNum": "100"})

data1=(1,2,3,4,5,6)

@ddt.ddt
class TEST(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")

    def tearDownClass(cls) -> None:
        print("teardown")

    @ddt.data(data1)
    def testData1(self, data):
        print(data)

unittest.main()