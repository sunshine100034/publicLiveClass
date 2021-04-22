#!__author__ = "yf"
"""
pycharm
"""
import logging
import time
import os




def LOG( *args, **kwargs):

    # 创建log文件
    if "filename" in kwargs:
        filename = kwargs["filename"]
        logging.basicConfig(filename=filename, format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
        logging.info("start")
    # 输出log日志
    for arg in args:
        logging.info(arg)


def saveScreenShot(driver):
    nowtime = time.strftime("%Y%m%d%H%M%S")
    file = nowtime + ".jpg"
    # file_path = os.path.realpath(__file__)
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, file)
    file = os.path.normpath(file)
    driver.get_screenshot_as_file(file)

