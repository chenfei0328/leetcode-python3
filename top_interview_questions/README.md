# top_interview_questions
7.reverse-integer

一般用整除/取余循环存入栈，然后再取出来，python则支持字符串和整数的方便转换以及字符串的逆序



13.roman-to-integer

当前字符比右边字符对应的值小时，则为负值



14.longest-common-prefix



26.remove-duplicates-from-sorted-array

用k来记录有序数值的个数，遇到新的数则直接赋值在k的位置



28.implement-strStr()

注意查询字符串本身为空字符串则返回0



36.valid-sudoku

用27个列表来存



54.spiral-matrix

一层一层往里读



66.plus-one

判断是否需要进位和首位insert(1,0)



73.set-matrix-zeroes

主要是空间上的限制，用 $O(n)$ 的set空间记录需要置0的列。在遍历完每一行后都判断是否需要将这行置0，同时更新set



*76.minimum-window-substring

用滑动窗口去做，每次碰到一个字符都计算当前窗口是否符合要求，如果符合则更新最小的窗口，同时更新窗口的起始位置

collections.Counter(t) 



88.merge-sorted-array

从后往前遍历，$O(m+n)$



103.binary-tree-zigzag-level-order-traversal

用两个stack轮流存每一行的结点



108.convert-sorted-array-to-binary-search-tree

递归创建二叉搜索树



*118.pascal's-triangle

可以动规，每一行的元素，第一个和最后一个都是1，其余位置都是上一行相邻两个位置之和



122.best-time-to-buy-and-sell-stock-2

递增则改变sell的位置，若减小则把之前的sell掉，减小的位置为下一次buy的位置



125.valid-palindrome

isalpha()  lower()  isdigit()



131.palindrome-partitioning

回溯递归



*134.gas-station

用一个remain来记录存量，lack来记录缺失的部分，当remain+lack》0则表示路径可通，同时起点为remain<0时的下一个位置



*150.evaluate-reverse-polish-notation

用栈来存数值，每次遇到符号则出栈两个数字进行计算，operation用lambda

//运算取整时保留整数的下界，int则是剪去小数部分，只保留前面的整数，即向零取整，round函数遵循四舍五入的法则



*162.find-peak-element

方法一：

遍历，$O(n)$

方法二：

二叉搜索的方法，每次寻找较小值的那一部分（确保了另一半是符合peak要求的） $O(\log_2 n)$



171.excel-sheet-column-number

ord(s)



172.factorial-trailing-zeroes

阶乘末尾0的个数和5的倍数有关



*179.largest-number

sorted函数中Key的函数的运用



*189.rotate-array

方法一：

reverse三次

方法二：

按step=k来把左部的元素移到右侧



*190.reverse-bits

b = bin(n)

b = b[2:]

b = int(b, base=2)



*191.number-of-1-bits

方法一：

遍历二进制字符串

方法二：

n &= (n-1)



202.happy-number

用一个字典存中间过程的数，如果重复出现了，则表示它不happy



*204.count-primes

统计素数个数，经典的做法，从小到大遍历，如果当前数是素数，则把该素数的倍数全设置为非素数，下次就不用遍历那些数了



*210.course-schedule-2

拓扑排序



*212.word-search-2

如果每个词都单独进行一遍dfs，会超时。要结合使用前缀树，将一些前缀相同的单词一起查找。



217.contains-duplicate

用hash表来存出现过的数



230.K-th-smallest-element-in-a-BST

二叉搜索树里寻找第k个小的树

方法一：

中序遍历取出第k个数 $O(n)$ 

方法二：

用栈，直接取到最左叶子，然后按序取到第k个结点 $O(\log n +k)$



237.delete-node-in-a-linked-list

node.val = node.next.val

node.next = node.next.next



242.valid-anagram

hash表，或collections.Counter()



*268.missing-number

方法一：

hash表来存所有的数，判断每个索引是否存在于数集中

方法二：

把所有的数和索引用异或连起来

方法三：

数学求和公式，差就是缺失的那个数



*315.count-of-smaller-number-after-self

增序排序，每次都找原数在排序后数组中的索引位置，即为该数的smaller number，然后删除该数（排序数组），该数对后续数的判断没有作用



*326.power-of-three

方法一：

不断除以3

方法二：

数学方法，用log来转换

方法三：

直接找到int范围内最大的3的倍数，然后除以任何数



328.odd-even-linked-list

用odd和even来表示奇列的末尾和偶列的末尾



*329.longest-increasing-path-in-a-matrix

dfs+memoization 每次记录都保存该点的path路径长



*334.increasing-triplet-subsequence

用两个指针来记录最小和第二小的数（按序的，而不是全局第二小），从而保证了前面有递增的两个小数



344.reverse-string

左右两端同时往中间移动



350.intersection-of-two-arrays-2

collections.Counter()



387.first-unique-character-in-a-string

用hash表来存各个字符的出现次数



*378.K-th-smallest-element-in-a-sorted-matrix

方法一：

heapq.nsmallest(k, heapq.merge(*matrix))[-1]

方法二：

用栈来存，入栈时记录该元素的行和列，每次出栈都入栈该元素的下一行元素



412.fizz-buzz



*454.4sum-2

点积

from itertools import product

AB = product(A, B)

sumAB = Counter(x + y for (x, y) in AB)

先点积，再counter，或者先counter，再点积