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



88.merge-sorted-array

从后往前遍历，$O(m+n)$

