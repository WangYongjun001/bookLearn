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


def stein_algorithm(num1, num2):
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


# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # 基线条件
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)  # 递归条件


# 散列表，python的字典就是散列表

"""
        广度优先搜索，图算法，队列(queue)和栈(stack)（堆栈）
栈：   是一直只能访问其一端实现数据存储和检索的线性数据结构，规则是一种后进先出的形式。
队列： 队列是一种具有先进先出特征的线性数据结构，元素的增加只能在一端进行，元素的减少只能在另一端进行，
       元素增加的一端叫做队尾，而元素减少的一端叫做队首，Python中的from collections import deque可以实现，popleft().
堆：   是程序在运行是，而不是在编译时，申请一定大小的内存空间，即是动态分配内存，
       对其访问和一般访问没有区别（堆本质是在运行时请求操作系统动态分配给自己的内存）
"""


def person_is_seller(person):
    if person[-1] == "3":
        return True


def breadth_first_search(first_name="you", graph=None):
    """广度优先搜索，使用队列"""
    if not graph:
        graph = {
            'you': ['alice', 'bob', 'claire'],
            'bob': ['anuj', 'peggy'],
            'alice': ['peggy'],
            'claire': ['thom', 'jonny'],
            'anuj': [],
            'peggy': [],
            'thom': [],
            'jonny': []}
    from collections import deque
    search_queue = deque()
    search_queue += graph[first_name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print("没有芒果商人")
    return False


"""
        狄克斯特拉算法
1、从首节点开始，计算到各邻节点的权重，找到权重最低的节点（此时邻节点的父节点均为首届点）
2、选择权重最低的节点开始计算其到各邻节点的权重（首节点到该邻节点的总权重），添加其邻居父节点为该节点
3、依次选择权重第二低、第三低......的节点，计算各自到邻节点的权重。
   如果有邻节点相同，且计算到该邻节点的权重更低，则更新其权重为当前权重，父节点为当前节点。
4、重复以上2和3，直到首尾之间的都计算过邻节点的开销；（各节点只计算一次到邻节点的开销，且有顺序，因此权重不能为负）
5、最终计算出到尾节点最低的权重，并根据父节点逆向查找父节点，得到节点路径

        Dijkstra's Algorithm 基本思想：
若给定带权有向图G=(V,E)和源顶点v0，构筑一个源集合S，将v0加入其中。
① 对差集V\S中 个顶点vi，逐一计算从v0 至它的距离 D(v0 , vi ),若该两顶点之间没有边，则其距离为无穷大。
   求出其中距离最短的顶点w，将其加入到集合 S 中。
② 重新计算 v0 至差集 V\S 中各顶点的距离 D（v0, vi ）= Min(D(v0, vi ), D(v0, w ) + C(w, vi )).
   其中C（w, vi ）是顶点w 与 vi 之间边上的费用。
③ 重复 步骤①②。直至所有的顶点都加到集合S 中为止。

        在包含负权边的图中，要找出最短路径，可使用另一种算法——贝尔曼-福德算法（Bellman-Ford algorithm） 
"""


def dijkstra_algorithm():
    pass


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 贝尔曼-福德算法 （Bellman-Ford algorithm）

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
    disordered_list = ["f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "a", "b", "c", "d", "e", "p"]
    print(quick_sort(disordered_list))
    print(breadth_first_search())
