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



*150.evaluate-reverse-polish-notation

用栈来存数值，每次遇到符号则出栈两个数字进行计算，operation用lambda

//运算取整时保留整数的下界，int则是剪去小数部分，只保留前面的整数，即向零取整，round函数遵循四舍五入的法则