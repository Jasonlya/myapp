# -*- coding: utf-8 -*-
"""
@Time ： 2024/2/6 22:33
@Auth ： liangya
@File ：log.py
"""
import time
import os
import logging
from functools import wraps

import log


class YoungerLogDecorator:
    def __init__(self, logPath=None, logName=None):
        # wraps(cls)(self)
        self.logPath = logPath if logPath else './'
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
        self.logName = logName

    def __call__(self, cls):
        if not self.logName:
            self.logName = cls.__name__

        @wraps(cls)
        def inner(*args, **kwargs):
            if not hasattr(cls, 'log'):
                logger, filehandler = self.getLogger()
                setattr(cls, 'log', logger)
                setattr(cls, 'handler', filehandler)
                # ChildCls = self.retChildCls(cls)
            return self.retChildCls(cls)(*args, **kwargs)

        return inner

    def getLogger(self):
        file = os.path.realpath(os.path.join(self.logPath, f'{self.logName}.log'))
        logger = logging.getLogger(self.logName)
        # 设置日志等级
        logger.setLevel(logging.INFO)
        # 添加文件输出流
        filehandler = logging.FileHandler(file, mode='a', encoding='utf8')
        # 设置日志输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s')
        filehandler.setLevel(logging.INFO)
        filehandler.setFormatter(formatter)
        # 添加文件流到logger
        logger.addHandler(filehandler)
        return logger, filehandler

    def retChildCls(self, cls):
        """新建一个子类并返回，继承父类所有属性，同时给所有方法都添加装饰器"""

        class ChildCls(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def __getattribute__(self, item):
                attrs = super().__getattribute__(item)
                if str(type(attrs)) == "<class 'method'>":
                    def decorator(*args, **kwargs):
                        try:
                            res = attrs(*args, **kwargs)
                            # self.closeHandler()
                            return res
                        except Exception as e:
                            print(e)
                            self.log.exception(e)
                            # self.closeHandler()

                    return decorator
                else:
                    return attrs

            def closeHandler(self):
                self.handler.close()

        return ChildCls


@YoungerLogDecorator()
class Test:
    def __init__(self):
        self.log.info('使用__init__函数')

    def func1(self):
        self.log.info('使用func1函数')

    def func2(self):
        self.log.info('使用func2函数')

    def func(self):
        self.log.warning('hsdfsdf')
        self.log.info('this is info msg')

    def func3(self):
        self.log.info('使用func3函数')

    def func4(self):
        self.log.info('使用func4函数，关闭文件')

# t = Test()
# t.func()
# t.closeHandler()
# t1 = Test()
# t1.func2()
# t1.closeHandler()


def my_decorator(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"param: {param}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@my_decorator("hello")
def my_func():
    print("world")


my_func()

