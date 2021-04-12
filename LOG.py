#!__author__ = "yf"
"""
pycharm
"""
import logging




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

