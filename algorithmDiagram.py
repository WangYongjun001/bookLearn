# coding: utf-8
# 算法图解

def binary_search(order_list, item):
    """
    二分查找，查找位置
    大O表示法：O(math.log(n,2))或者O(math.log2(n))
    list: 数组需要有序
    :return: 元素在列表中的索引
    """
    _count = 0
    low = 0
    high = len(order_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = order_list[mid]
        _count += 1
        print("第 %s 次，索引：%s，值：%s" % (_count, mid, guess))
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# 一次走一个或两个台阶是：费波拉希数列 斐波那契数列(Fibonacci sequence),
# 旅行商问题 O(n!)

# 数组和链表：数组占用内存块，插入数据时分配内存不够会重新分配内存；链表则是上一个元素储存下一个元素的地址（单项链表），不需要储存内存相连
def find_smallest(arr):
    """找出列表最小值，返回索引"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    选择排序，每次append列表最小值
    大O表示法：O(n×n)
    """
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


# 递归和快速排序
# 分治法（divide and conquer， D&C）是一种解决问题的思路（递归）
# 欧几里得算法（辗转相除法）与更相减损法比较：都可求最大公约数

def sum_1(arr):
    """求列表各元素和"""
    if arr == []:
        return 0
    return arr[0] + sum_1(arr[1:])


def counts_2(arr):
    """求列表长度"""
    if arr == []:
        return 0
    return 1 + counts_2(arr[1:])


def euclidean_algorithm(num1, num2):
    """欧几里得算法 求最大公约数"""
    if num2 > num1:
        num1, num2 = num2, num1
    remainder = num1 % num2
    if remainder == 0:
        return num2
    else:
        return euclidean_algorithm(num2, remainder)


def euclidean_algorithm_1(num1, num2):
    """欧几里得算法 求最大公约数"""
    if num2 > num1:
        num1, num2 = num2, num1
    while (num1 % num2 != 0):
        num1, num2 = num2, num1 % num2
    return num2


def subtraction_loss_algorithm(num1, num2):
    """更相减损法 求最大公约数"""
    if num2 > num1:
        num1, num2 = num2, num1
    reminder = num1 - num2
    if reminder == num2:
        return num2
    else:
        return subtraction_loss_algorithm(num2, reminder)


def subtraction_loss_algorithm_1(num1, num2):
    """更相减损法 求最大公约数"""
    while (num1 != num2):
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1, num2


def stein_algotithm(num1, num2):
    """
    Stein算法 求最大公约数
    Stein算法很好的解决了辗转相除法中的这个缺陷，Stein算法只有整数的移位和加减法。下面就来说一下Stein算法的原理：
    若a和b都是偶数，则记录下公约数2，然后都除2（即右移1位）；
    若其中一个数是偶数，则偶数除2，因为此时2不可能是这两个数的公约数了
    若两个都是奇数，则a = |a-b|，b = min(a,b)，因为若d是a和b的公约数，那么d也是|a-b|和min(a,b)的公约数。
    Stein算法比辗转相除法更加快速，简易。它与每一次进行更相减损法得到的结果似乎存在着微妙的联系，通过下面的比较，可以发现两种算法之间的联系。 [2]
    更相减损法：操作	甲数	乙数	Stein算法：操作	甲数	乙数
                    98	    63		                98   	 63
                    98-63=35	63	35	98是偶数，除以2	49	63
                    63-35=28	35	28	都是奇数，63-49=14	49	14
                    35-28=7	28	7	14是偶数，除以2	49	7
                    28-7=21	7	21	49-7=42	42	7
                    21-7=14	7	14	42是偶数，除以2	21	7
                    14-7=7	7	7	21-7=14	14
                    7
                    7-7=0	7	0	14是偶数，除以2	7	7
                    7-7=0	7	0

    """
    pass


if __name__ == "__main__":
    # 二分查找
    ordered_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p"]
    binary_search(ordered_list, "p")
    # 选择排序
    disordered_list = ["f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "a", "b", "c", "d", "e", "p"]
    print(selection_sort(disordered_list))
    # 递归相加
    print(sum_1([1, 2, 3, 4]))
    print(counts_2([1, 2, 3, 4]))
    print(euclidean_algorithm(1350, 1440))
    print(euclidean_algorithm_1(1350, 1440))
    print(subtraction_loss_algorithm(1350, 1440))
    print(subtraction_loss_algorithm_1(1350, 1440))
