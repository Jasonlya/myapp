# -*- coding: utf-8 -*-
"""
@Time ： 2024/2/6 21:47
@Auth ： liangya
@File ：demo.py
"""


# class C:
#     def __init__(self):
#         self.score = 85
#
#     @property  # @property 装饰器本身就相当于 getter 方法
#     def score_x(self):
#         if self.score < 60:
#             return "你妹的，不及格！"
#         else:
#             return self.score
#
#     @score_x.setter  # 给 score_x 属性装饰 setter 方法
#     def score_x(self, value):  # 附加方法与原始的特征属性相同的名称
#         if 0 <= value <= 100:
#             self.score = value
#         else:
#             print(f"输入的值 {value} 超出范围 0~100 ！")
#
#     @score_x.deleter  # 给 score_x 属性装饰 deleter 方法
#     def score_x(self):  # 附加方法与原始的特征属性相同的名称
#         del self.score
#
#
# c = C()
# print(c.score_x)
# c.score_x = 45
# print(c.score_x)


class MyClass():
    def __init__(self, name):
        self.name = name

    def get_info(self):  # 定义实例方法，有 self 参数
        print("实例方法")

    @classmethod
    def get_other(cls):  # 定义实例方法，有 cls 参数
        print("类方法" + MyClass.__name__)

    @staticmethod
    def get_my_class():  # 定义静态方法，无默认参数
        print("静态方法")


# 实例化
mc = MyClass("tom")

# 调用实例方法
mc.get_info()  # 实例方法

# 调用类方法，建议通过 类对象.类方法([实参]) 方法调用
MyClass.get_other()  # 类方法

# 调用静态方法，建议通过 类对象.类方法([实参]) 方法调用
MyClass.get_my_class()  # 静态方法
