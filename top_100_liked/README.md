# top_100_liked

2.add-two-numbers

python链表的使用方法



3.longest-substring-without-repeating-characters

每次遇到一个重复的字符都要把其对应的上一个字符之前的所有字符删去



4.median-of-two-sorted-arrays

类似于归并排序



*11.container-with-most-water

从左右两个端点往中间靠，每次靠近的是矮柱的一侧



*15.3sum

先排序，然后左右两个指针往中间靠



*17.letter-combination-of-a-phone-number

回溯法，使用递归函数



*19.remove-Nth-node-from-end-of-list

用两个间距为N的指针去遍历链表



*22.generate-parentheses

回溯法，同时确保括号是合法的



*23.merge-k-sorted-lists

使用python3的queue模块的PriorityQueue，时间复杂度为$O(N\log k)$

这里要注意PriorityQueue的插入参数



或者取出所有元素，排序后生成新的链表$O(N\log N)$



或者使用归并排序$O(N\log k)$



*31.next-permutation

https://blog.csdn.net/Dby_freedom/article/details/85226270

下一个排列数

python交换数据

nums[pre_index], nums[after_index] = nums[after_index], nums[pre_index]



33.search-in-rotated-sorted-array

python  while A and B   是依次判断A和B的



34.find-first-and-last-position-of-element-in-sorted-array

二分查找



39.combination-sum

递归



41.first-missing-positive

使用两个集合分别记录每个数的+1数和1，以及非法数据，每次插入都验证是否合法



*42.trapping-rain-water

动规，分别从左到右和从右到左记录每个位置的最高左柱和最高右柱

water += min(max_left[i], max_right[i]) - height[i]



46.permutations

回溯，类似39/22/17

深浅复制的问题：ans.append(combination)

*1.ans.append(combination[:]) 

2.ans.append(copy.deepcopy(combination))

3.backtrack([])



48.rotate-image

正方形顺时针翻转in-place，注意索引位置



49.group-anagrams

把每个字符串都转成有序序列



55.jump-game

动规，记录当前点可达的最远距离，如果最远距离大于当前位置，则右移

（内部函数修改外部函数变量，nonlocal声明）



56.merge-intervals

先排序这些区间，这样每次都只需要和最后一个merged区间进行比较就行了



*72.edit-distance

$dp[i][j]$ 表示word1[:i]和word2[:j]的编辑距离

状态转移方程：

$dp[i][j] = dp[i-1][j-1]\ if\ word1[i-1] == word2[j-1]\ else\ 1+min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])$

初始化条件：

$dp[0][j] = j$ and $dp[i][0] = i$



时间复杂度：$O(mn)$

空间复杂度：$O(mn)$



75.sort-colors

遍历一遍数组，用两个指针分别表示01的交界及12的交界，每次遇到0或1则移动交界处的值，遇到2则pass



*78.subsets

方法一：

每新增一个元素，则把该元素加入结果集中的每一个子集

方法二：

回溯：以子集元素个数为终止条件进行n次backtrack



79.word-search

dfs



94.binary-tree-inorder-traversal

中根遍历，递归/栈



98.validate-binary-search-tree

检测是否为搜索二叉树，递归/栈



101.symmetric-tree

检测是否为镜像树，递归/栈，用两个root，分别比较root1.left和root2.right  和 root1.right和root2.left



102.binary-tree-level-order-traversal

层次遍历，用Level来记录每个节点的层次，queue



104.maximum-depth-of-binary-tree

求深度



*105.construct-binary-tree-from-preorder-and-inorder-traversal

根据先根序和中根序建树，递归



*114.flatten-binary-tree-to-linked-list

递归把左子树插到根节点和右子树中间



124.binary-tree-maximal-path-sum

递归遍历节点，关键是每个节点返回的路径值是单路径，而每次需要比较的路径还包括了从左子树到右子树的长路径



128.longest-consecutive-sequence

使用set的hash表，每次只看每个连续区间的最小值（即if num - 1 not in num_set:）



*136.single-number

方法一：

hash表

方法二：

数学解法

方法三

异或，相同返回0，0^a=a



*84.largest-rectangle-in-histogram

用栈来保存比当前bar出现过的更低的bar，直到碰到比栈尾元素更低的bar再计算面积



138.copy-list-with-random-pointer

遍历链表



141.linked-list-cycle

方法一：

hash表记录遍历过的节点，若出现重复则cycle

方法二：

用一个step=2和一个step=1的指针去遍历，如果cycle的情况下fast会追上slow而不是出现空指针



142.linked-list-cycle-2

返回循环链表的起点



*146.lru-cache

collections.OrderedDict() 按照插入顺序排列的字典



148.sort-list

先把数据遍历读出来，然后排序，构造新链表



160.intersection-of-two-linked-lists

方法一：

遍历A，把节点存入hash表，遍历B时判断节点是否存在于表中

方法二：

分别遍历A和B，记录两个链表的长度，从而根据长度差来调整下一次遍历的两个指针的间距