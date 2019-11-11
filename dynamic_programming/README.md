# dynamic_programming
5.longest-palindromic-substring

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

dp\[i][j] = min(dp\[i - 1][j], dp\[i][j - 1]) + dp\[i][j]

