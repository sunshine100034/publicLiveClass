#!__author__ = "yf"
"""
pycharm
"""
import sys

class MyException(Exception):
    def __str__(self):
        super(MyException, self).__new__()
        return "my exception occour"


def test():
    try:
        print("start of test")
        if len(sys.argv) == 1:
            raise MyException
        print("end of test")
    except MyException as e:
        print(e)

class Test():
    message = "this is static member"
    def __init__(self, color = "red"):
        print("constrator called")
        self.color = color
        # 私有变量和属性以__开头
        self.__name="fy"

    def __del__(self):
        print("decorator called")

    def showColor(self):
        print("this is showColor",self.color)

    def showMessage(self):
        print("this is showMessage",self.message)

    @staticmethod
    def printMessage():
        print("this is static method",Test.message)

    @classmethod
    def show(cls, name):
        return cls(name)

if __name__ == "__main__":
    test()
    aa = Test()
    aa.color = "green"
    aa.message = "this is a message"
    aa.showColor()
    aa.showMessage()
    print(aa.message)
    bb = Test()
    bb.showColor()
    bb.showMessage()
    print(bb.message)
    Test.printMessage()
    aa2 = Test.show("black")
    print(aa2.color)