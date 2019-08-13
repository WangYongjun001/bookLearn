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
    if not arr:
        return 0
    return arr[0] + sum_1(arr[1:])


def counts_2(arr):
    """求列表长度"""
    if not arr:
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
    """欧几里得算法 求最大公约数    消除多余运算"""
    if num2 > num1:
        num1, num2 = num2, num1
    remainder = num1 % num2
    while remainder:
        num1, num2 = num2, remainder
        remainder = num1 % num2
    return num2
    # while (num1 % num2 != 0):
    #     num1, num2 = num2, num1 % num2
    # return num2


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
    """更相减损法 求最大公约数   消除多余运算 """
    while True:
        if num1 > num2:
            num1 -= num2
        elif num1 < num2:
            num2 -= num1
        else:
            return num1, num2
    # while (num1 != num2):
    #     if num1 > num2:
    #         num1 -= num2
    #     else:
    #         num2 -= num1
    # return num1, num2


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
    """O(nlogn)"""
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

graph = {
    "start": {"a": 6, "b": 2, },
    "a": {"fin": 1},
    "b": {"a": 3, "b": 5},
    "fin": {}
}
# 1 第一步
start_node = "start"
costs = {}
parents = {}
for node in graph.keys():
    if node != start_node:
        costs[node] = graph[start_node].get(node) or float("inf")
        parents[node] = 0  # TODO
print(costs)
parents = {"a": "start", "b": "start", "fin": None}
processed = []


def dijkstra_algorithm():
    """狄克斯特拉算法实现"""
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")  # 正无穷大
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 第8章 贪婪算法

# 二项式定理：https://baike.baidu.com/item/%E4%BA%8C%E9%A1%B9%E5%BC%8F%E5%AE%9A%E7%90%86/7134359?fr=aladdin
# 广播电台覆盖问题


def greedy_algorithm():
    """
    解决广播电台广告投放问题的，这是一种近似算法 （approximation algorithm），O(n**2)，
    1 选出这样一个广播台， 即它覆盖了最多的未覆盖州
    2 重复第一步， 直到覆盖了所有的州
    """
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {"kone": {"id", "nv", "ut"},
                "ktwo": {"wa", "id", "mt"},
                "kthree": {"or", "nv", "ca"},
                "kfour": {"nv", "ut"},
                "kfive": {"ca", "az"}}

    final_stations = set()  # 空集合定义方法，不能用 {}
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station  # 交集
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
                print(best_station)
        final_stations.add(best_station)
        states_needed -= states_covered
    return final_stations  # 集合无序


# NP完全问题的简单定义是， 以难解著称的问题， 如旅行商问题和集合
# 覆盖问题。 很多非常聪明的人都认为， 根本不可能编写出可快速解决这
# 些问题的算法。

# 第九章 动态规划
# 一、分治法与动态规划主要共同点：
#
# 1）二者都要求原问题具有最优子结构性质，都是将原问题分而治之，分解成若干个规模较小(小到很容易解决的程序)的子问题。然后将子问题的解合并，形成原问题的解。
#
# 二、分治法与动态规划实现方法：
#
# ① 分治法通常利用递归求解。
#
# ② 动态规划通常利用迭代法自底向上求解，但也能用具有记忆功能的递归法自顶向下求解。
# 三、分治法与动态规划主要区别：
#
# ① 分治法将分解后的子问题看成相互独立的。
#
# ② 动态规划将分解后的子问题理解为相互间有联系，有重叠部分。

# 第十章 KNN

# 第十一章 其他
# 1 树
# 二叉查找树（binary search tree）数据结构
# B树是一种特殊的二叉树， 数据库 常用它来存储数据
# 红黑树、堆、伸展树

# 2 反向索引
# 一个散列表， 将单词映射到包含它的页面。 这种数据结构被称为反向索引 （inverted index） ， 常用于创建搜索发动机

# 3 傅里叶变换
# 处理信号

# 4 并行算法
# 注意并行性管理开销和负载均衡

# 5 MapReduce 分布式算法（属并行算法）
# MapReduce是一种流行的分布式算法， 你可通过流行的开源工具Apache Hadoop来使用它
# map映射和reduce归并。

# 6 布隆过滤器和HyperLogLog
# 比散列表更适合处理大量数据， 是一种概率型数据结构，可能存在误报

# 7 SHA算法
# 另一种散列函数 安全散列算法（secure hash algotithm,）算法
# 用于创建散列表的散列函数根据字符串生成数组索引，
# 而SHA根据字符串生成另一个字符串。是局部不敏感，更改其中一个字符，生成的字符串差别很大
# 比对文件、检查密码 当前， 最安全的密码散列函数是bcrypt，

# 8 局部敏感的散列算法
# Simhash Google使用Simhash来判断网页是否已搜集

# 9 Diffie-Hellman密钥交换及RSA
# 消息加密 双方无需知道加密算法
# 分为公钥和私钥

# 10 线性规划
# 使用Simplex算法

if __name__ == "__main__":
    # # 二分查找
    # ordered_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p"]
    # binary_search(ordered_list, "p")
    # # 选择排序
    # disordered_list = ["f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "a", "b", "c", "d", "e", "p"]
    # print(selection_sort(disordered_list))
    # # 递归相加
    # print(sum_1([1, 2, 3, 4]))
    # print(counts_2([1, 2, 3, 4]))
    # print(euclidean_algorithm(1350, 1440))
    # print(euclidean_algorithm_1(1350, 1440))
    # print(subtraction_loss_algorithm(1350, 1440))
    # print(subtraction_loss_algorithm_1(1350, 1440))
    # disordered_list = ["f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "a", "b", "c", "d", "e", "p"]
    # print(quick_sort(disordered_list))
    # print(breadth_first_search())
    print(greedy_algorithm())
    pass
