# dynamic_programming
*5.longest-palindromic-substring

解法一：

暴力



解法二：

dp\[i][j] 表示字符串s[i:j]是否为回文子串

状态转移方程：

dp\[i][j] = dp\[i+1][j-1] if s[i] == s[j] else 0

初始化条件：

dp\[i][i] = 1

dp\[i][i+1] = 1 if s[i] == s[i+1] else 0



时间复杂度：O(n^2)

空间复杂度：O(n^2)



解法三：

计算当前步骤时，即子串长度为k时，只依赖于k-1的结果，故可以只用两个一维数组来保存中间状态

时间复杂度：O(n^2)

空间复杂度：O(n)





53.maximun-subarray

暴力会超时

解法一：

dp[i] 表示以nums[i]为结尾的连续子序列的最大和

状态转移方程：

dp[i] = max(nums[i], nums[i] + dp[i-1])





70.climbing-stairs

从后往前的递归会超时：return climbStairs(n - 1) + climbStairs(n - 2)

解法一：

状态转移方程：

dp[i] = dp[i -1] + dp[i - 2]





62.unique-paths

解法一：

状态转移方程：

dp\[i][j] = dp\[i][j - 1] + dp\[i - 1][j]

初始化条件：

dp\[i][0], dp\[0][j]= 1, 1





63.unique-paths2

解法一：

状态转移方程：

dp\[i][j] = 0 if dp\[i][j] is obstacle else dp\[i][j - 1] + dp\[i - 1][j]

初始化条件：

dp\[i][0], dp\[0][j]= 1, 1 遇到障碍后面的位置全等于0

如果起点为obstacle则直接返回0





64.minimum-path-sum

解法一：

状态转移方程：

dp\[i][j] += min(dp\[i - 1][j], dp\[i][j - 1])





*32.longest-valid-parentheses

解法一：

状态转移方程：

dp[i] = 0, s[i] == '('

​				else:

​				dp[i - 2] + 2, s[i - 1] == '('

​										else:

​										dp[i - 2] + 2 +dp[i - 2 - dp[i - 1]], s[i - 1 - dp[i - 1]] == '('

其中，dp[i - 2 - dp[i - 1]]表示当前有效字符串的前一位，是否也是一个有效字符串，直接相加

初始化dp = [0] * len(s)，计算过程中要注意判断索引是否越界





*91.decode-ways

解法一：

状态转移方程：

dp[i] = dp[i - 2], s[i] == '0' and s[i - 1] == '1' or '2' and s[i - 2] == '1' or '2'

​			dp[i - 1], s[i] == '0' and s[i - 1] == '1' or '2' and s[i - 2] != '1' or '2'

​			return 0, s[i] == '0' and s[i - 1] != '1' or '2'

​			dp[i - 1] + dp[i - 2], s[i] != '0' and s[i - 1: i + 1] make sense

​			dp[i - 1], s[i] != '0' and s[i - 1: i + 1] dosen't make sense

初始化条件：首位数字不得为0，其他情况下dp[0] = 1

有点类似斐波那契数列，然后考虑那些没有意义的组合





*96.unique-binary-search-tress

解法一：

状态转移方程：

dp[i] = for j = 0 to i - 1:

​				dp[i] += dp[j] * dp[i - j - 1]

卡特兰数：	

https://blog.csdn.net/u010582082/article/details/69569237





120.triangle

解法一：

从上往下

状态转移方程：

dp\[i][j] += min(dp\[i - 1][j], dp\[i - 1][j - 1])

解法二：

自底向上

状态转移方程：

dp\[i][j] += min(dp\[i + 1][j], dp\[i + 1][j + 1])





121.best-time-to-buy-and-sell-stock

解法一：

记录当前的最大值和最小值，每次遇到更小的值时，同时更新最大值和最小值；遇到更大的值时，更新最大值和maxProfit





*152.maximum-product-subarray

解法一：

pre_min:：当前连续数组的最小值

pre_max：当前连续数组的最大值

状态转移方程：

pre_min = min(pre_min * nums[i], pre_max * nums[i], nums[i])

pre_max = max(pre_min * nums[i], pre_max * nums[i], nums[i])

最终结果为pre_max出现过的最大值





198.house-robber

解法一：

类似于爬楼梯

状态转移方程：

dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])





213.house-robber2

解法一：

多了一个环形的限制条件，则取nums[1:]和nums[:-1]结果的最大值

状态转移方程：

dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])





221.maximal-square

解法一：

状态转移方程：

dp\[i][j] = 1 + min(dp\[i - 1][j - 1], dp\[i][j - 1], dp\[i - 1][j])

area = max(max, pow(dp\[j][j], 2))





264.ugly-number2

解法一：

分别用三个指针记录2,3,5的倍数，每次取指针对应数乘以该倍数的最小值

状态转移方程：

dp[i] = min(2 * dp[pointer_2], 3 * dp[pointer_3], 5 * dp[pointer_5])

且满足2 * dp[pointer_2] > dp[i - 1] and 3 * dp[pointer_3] > dp[i - 1] and 5 * dp[pointer_5] > dp[i - 1]





*279.perfect-squares

解法一：

DP

https://blog.csdn.net/qq_35481167/article/details/82817699

解法二;

math	

https://leetcode.com/problems/perfect-squares/discuss/428031/32ms-python-space-less-than-100





*300.longest-increasing-subsequence

解法一：

nums[i] <= nums[i - 1]，从当前位置往头搜索第一个小于nums[i]的数，索引为j，则 dp[i] = dp[j] + 1，如果没找到则dp[i] = 1

nums[i] > nums[i - 1]，则初始状态为now = dp[i - 1] + 1，从当前位置往头搜索所有nums[i] > nums[j]，now = max(now, dp[j] + 1)，从而dp[i] = now

而res = max(res, dp[i])

时间复杂度：O(n * n)

空间复杂度：O(n)



解法二：

简化解法一的代码



解法三：

维护一个递增数组，每次遇到小于最大值的数就通过二分查找插入，如果是末尾位置则直接插入，其他情况则覆盖地插入数组。最终这个数组不一定是那个递增序列，但数组的长度是要求的答案





303.range-sum-query-immutable

解法一：

就是聚合

dp[i] += dp[i - 1]





304.range-sum-query2D-immutable

解法一：

二维的聚合

dp\[i][j] = matrix\[i - 1][j - 1] + dp\[i - 1][j] + dp\[i][j - 1] - dp\[i - 1][j - 1]

计算结果时注意重复减的地方加回来





338.counting-bits

解法一：

找规律dp=[0, |1|, |1, 2|, |1, 2, 2, 3|, |1, 2, 2, 3, 2, 3, 3, 4|,...]

每次延长的部分都是前面部分对应位置+1