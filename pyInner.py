# coding: utf-8
# python内置函数等
from functools import reduce

# 1
def map_fileter_reduce():
    """map, filter, reduce, 快速创建列表"""
    list_a = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x ** 2, list_a)))
    print([x ** 2 for x in list_a])
    print(list(map(lambda x: x >= 2, list_a)))
    print([x >= 2 for x in list_a])
    print(list(filter(lambda x: x >= 2, list_a)))
    print(reduce(lambda x, y: x + y, list_a))
    print(reduce(lambda x, y: x < y, list_a))


# 2 python参数详解
def test_args(a, b=1, c=2, *args, **kwargs):  # a,b,c是形参，1，2是实参
    """
    Python参数详解，参考下个python内置print函数
    :param a:       1. 必须参数
    :param b:       2. 默认参数  必须放到必须参数之后
    :param c:       2. 默认参数  必须放到必须参数之后
    👆 当存在默认参数和必须参数两种以上参数时，调用函数时一定要注意：👆
    :param args:    3. 可变参数  如果有默认参数，则默认参数的不再使用b=3这种方式传参，应写为
                    def test_1(a, *args, b=1, c=2, **kwargs)
                    👆 即使用时，位置参数不能在关键字参数之后 👆
    :param kwargs:  4. 关键字参数 形参名不能和位置参数形参命名一致
    :return:
                    👇
                    test_1(0, 2, 5, 1, 2, 3, d=4)
                    test_1(0, 2, 5, *[1, 2, 3], **{"d": 4})
                    test_1(0, 2, 5, 5, *[1, 2, 3], 6, *[7, 8, 9], e=5, **{"d": 4}, f=6, **{"g": 7})
    """
    print(a)
    print(b)
    print(c)
    print(args)  # 元祖
    print(kwargs)
    return 110


def builtins_print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
    """python内置的print源码部分
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass


# 3 装饰器
# 理解函数调用栈和递归
def dec_out(func):
    """
    装饰器无参的装饰器，print(test_decorator(0, 2, 5, 5, *[1, 2, 3], 6, *[7, 8, 9], e=5, **{"d": 4}, f=6, **{"g": 7}))
    :param func: 函数
    :return: 内部函数名
    """

    def dec_in(*args, **kwargs):
        """
        通过*args, **kwargs传参，可以使该装饰器能够 装饰 含不同类型参数的函数
        :param args:    函数的参数
        :param kwargs:  函数的参数
        :return: 被装饰函数的return值
        """
        print("装饰前处理....")
        print("dec_in-->", args, kwargs)
        ret = func(*args, **kwargs)
        print("装饰后处理，可以对装饰函数的返回值进行再处理")
        return ret

    return dec_in


def dec_args(h=1100):
    """
    装饰器传参0, 2, 5, 5, *[1, 2, 3], 6, *[7, 8, 9], e=5, **{"d": 4}, f=6, **{"g": 7}
    :param h:
    :return: 直接内部函数名
    """

    def dec_out(func):
        def dec_in(*args, **kwargs):
            print("装饰前处理....")
            print("dec_in-->", args, kwargs)
            ret = func(*args, **kwargs)
            print("装饰后处理，可以对装饰函数的返回值进行再处理")
            ret = ret + (h,)
            return ret

        return dec_in

    return dec_out


@dec_args(1200)  # 多个装饰器，外部装饰器（语法糖）先执行
def test_decorator(a, b=1, c=2, *args, **kwargs):
    print("执行部分")
    return a, b, c, args, kwargs


if __name__ == "__main__":
    pass
