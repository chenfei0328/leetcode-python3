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