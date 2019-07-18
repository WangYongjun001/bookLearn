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


if __name__ == "__main__":
    # 二分查找
    ordered_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p"]
    binary_search(ordered_list, "p")
    # 选择排序
    disordered_list = ["f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "a", "b", "c", "d", "e", "p"]
    print(selection_sort(disordered_list))
