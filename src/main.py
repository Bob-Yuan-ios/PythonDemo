# This is a sample Python script.
import asyncio
from typing import Callable, Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#


# from utils.Coroutine import averager
#
# # 协程触发
# coro_avg = averager()
# # 协程预激活
# next(coro_avg)
# # 调用者给协程提供数据
# coro_avg.send(5)
# coro_avg.send(6)
# coro_avg.send(13)
# try:
#     coro_avg.send(None)
# except StopIteration as exc:
#     result = exc.value  # 执行完成会抛出异常，返回值包含在属性value里
#
# print('Record count is {},average is {}.'.format(result.count, result.average))


# from grammar.list import *
# # read_list()
# update_list()


# from grammar.tuple import *
# update_tuple()


# from grammar.dict import *
# update_dictionary()


# from grammar.control import *
# start_while()


from grammar.function import *

# a = '123'
# print('before function a is:', a)
# param_conversion(a)
# print('after function a is:', a)
#
# b = ['1', '2']
# print('before function b is:', b)
# param_conversion(b)
# print('after function b is:', b)


# default_value('123456')
# square = nth_power(2)
# cube = nth_power(3)
# print(square(2))
# print(cube(2))


# print(add(2, 3))
print(start_special())


