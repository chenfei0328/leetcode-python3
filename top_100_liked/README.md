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



*139.word-break

dp = [0 for _ in range(l + 1)]

dp[0] = 1

对于每一个dp[i]，if 1，则去遍历后续的s[i:j]，如果存在于字典中，则dp[j]=1



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



*155.min-stack

每次push一个元素，如果最小值有更新（x <= self.minValue），则先push入原最小值，再push该元素

每次pop栈顶元素，如果该值等于最小值，则接着再pop一个元素（即push进来的最小值），然后更新最小值，即第二次pop的元素



169.majority-element

方法一：

hash表存储每个数的次数，当某个数的次数大于len(nums) / 2则停止

方法二：

使用collections.Counter

方法三：

排序数组，返回中间的值nums[len(nums)//2]



200.number-of-islands

经典的dfs



206.reverse-linked-list

in-place反转链表



207-course-schedule

dfs，判断是否有circle

from collections import defaultdict 

d = defaultdict(list)  默认字典的value为列表



208.implement-trie(prefix-tree)

每个字母都作为一个结点，把‘*’作为是否含有该单词的判断标准



*215.Kth-largest-element-in-an-array

方法一：

维护一个容量为k的堆

return heapq.nlargest(k, nums)[-1]

方法二：

先排序

return sorted(nums)[-k]



*234.palindrome-linked-list

方法一：

用栈来存链表元素，然后再读一遍链表并进行比较 time: $O(n)$ space: $O(n)$

方法二:

用一个slow和一个fast同时遍历链表，其中fast的遍历速度为slow的两倍，从而使slow能到达链表中点，并且slow的过程同时反转链表。最后同时从起点和中点开始遍历并比较

time: $O(n)$ space: $O(1)$



*236.lowest-common-ancestors-of-a-binary-tree

先把p和q的所有祖先记录下来，然后自底向上遍历q的祖先，第一次和p的祖先相同则是最小公共祖先



*238.product-of-array-except-self

从右往左记录记录每个位置的累积乘，然后从左往右计算累积乘，对应位置的两者之积为结果



239.sliding-window-maximum

当前窗口最大值为ans[i]，只有nums[i+1]>ans[i] 或 nums[i+1]<ans[i] && ans[i-w]==ans[i]才会更新ans[i+1]



*240.search-a-2D-matrix-2

从左下角或右上角开始搜索



283.move-zeros

循环一遍，即时记录非零的个数，即赋值的索引位置



*287.find-the-duplicate-number

方法一：

用set来存时间复杂为O(n)，空间复杂度为O(n)

方法二：

类似于链表中存在一个cycle，然后用追及方法来做。时间复杂为O(n)，空间复杂度为O(1)

141/142 linked list cycle



297.serialize-and-deserialize-binary-tree

序列化和反序列化二叉树



*337.house-robber-3

递归遍历左子树和右子树，递归函数第一项是计算了node.val的最大值，因此左右子树应返回的是不包含该结点的最大值；第二项是不计算node.val的最大值，即左右子树计算了该结点



*347.top-K-frequent-elements

先扫一遍所有元素的计数，根据计数建立一个size=k的大顶堆

count = collections.Counter(nums)

return heapq.nlargest(k, count.keys(), key=count.get)



394.decode-string

递归



*406.queue-reconstruction-by-height

关键是要先按照规则排序，然后按顺序把每个元素放在相应的位置



*416.partition-equal-subset-sum

方法一：

初始化：dp = [False] * (halfSum + 1)           dp[0] = True

对于每一个num in nums, dp[i+num] = True if dp[i] = True. 但需要注意的是i必须从大到小遍历

方法二：

回溯（个别案例Time Limit Exceeded）



437.path-sum-3

方法一：

以不同的起点，遍历子树  $O(n^2)$

方法二：

用stack来存累积和，每次新加入一个节点，更新stack里所有的值，将新生成的等于sum的个数加到总计数 $O(n)$



438.find-all-anagrams-in-a-string

使用hash表来存字符个数



448.find-all-numbers-disappeared-in-an-array

一次循环做记号，一次循环把标记的数删除；使用hash表能加快一定速度但使用了额外的空间



*494.target-sum

回溯会超时

dp\[i][j] 表示前i个数可组成j的个数，则有dp\[i][s+nums[i]] += dp\[i-1][s] 、dp\[i][s-nums[i]] += dp\[i-1][s]



*543.biameter-of-binary-tree

找最长路径



*560.subarray-sum-equals-K

方法一：

使用累计和，然后再计算每个区间的和（会超时）$O(n)$ 

方法二：

用map存累积和的个数，每次count += map[sum-k]，

---------sum-k-----(k)-----sum-----------sum-----------sum----------

---------sum-k----------------k-------------sum-----------sum----------

根据sum-k的个数来决定当前得到sum时，有几种区间可以选择



617.merge-two-binary-trees

递归地遍历两棵树的相同位置的结点



581.shortest-unsorted-continuus-subarray

方法一：

先sort然后找到左右元素不相等的位置 $O(n\log n)$

方法二

从左到右寻找需要移动的left，同时记录最小元素应该到哪个位置；从右往左也这样 $O(n)$



*621.task-scheduler

计算cooling interval的值，然后加上task的数量



*647.palindromic-substrings

回文字符串的个数，dp数组为上三角，参考第5题



*739.daily-temperatures

方法一：

从右往左遍历，当左<右则ans[左]=1，或者按右+ans[右]的顺序比较 $O(nw)$ 

方法二：

从右往左遍历，用栈来存储所有比当前元素更大的值，如果更小的则pop，因为后续元素也不需要这些值了 $O(n)$ 