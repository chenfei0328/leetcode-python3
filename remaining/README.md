6 ZigZag Conversion

找索引之间的关系，则可以避免额外的内存空间

C++

```C++
class Solution {
public:
    string convert(string s, int numRows) {
        if(1 == numRows) {
            return s;
        }
        int len = s.length();
        if(len < 2 || len <= numRows) {
            return s;
        }
        
        string ans = "";
        int step = numRows + numRows - 2;
        for(int row = 0; row < numRows; ++row) {
            int index = row;
            if(row == 0 || row == numRows - 1) {
                while(index < len) {
                    ans += s[index];
                    index += step;
                }
            }
            else {
                int step1 = step - 2 * row;
                int step2 = step - step1;
                bool first = true;
                while(index < len) {
                    ans += s[index];
                    if(first) {
                        index += step1;
                        first = false;
                    }
                    else {
                        index += step2;
                        first = true;
                    }
                }
            }
        }
        return ans;
    }
};
```



8 String to Integer (atoi)

先判断字符串的合法位置在哪，并确定符号。接着从合法数字位开始计算直到遇见非数字为止，或超出 int 范围

C++

```c++
class Solution {
public:
    int myAtoi(string str) {
        long long ans = 0;
        int len = str.length();
        int i = 0;
        bool minus = false;
        while(i < len) {
            if(' ' == str[i]) {
                i++;
            }
            else if('-' == str[i]) {
                minus = true;
                i++;
                break;
            }
            else if('+' == str[i]) {
                i++;
                break;
            }
            else if(str[i] >= '0' && str[i] <= '9') {
                break;
            }
            else {
                return 0;
            }
        }
        
        if(i == len) {
            return 0;
        }
        
        while(i < len) {
            if(str[i] >= '0' && str[i] <= '9') {
                ans = 10 * ans + str[i] - '0';
                if(minus && ans > pow(2, 31)) {
                    return -pow(2, 31);
                }
                if(!minus && ans > pow(2, 31) - 1) {
                    return pow(2, 31) - 1;
                }
                i++;
            }
            else {
                break;
            }
        }
        return minus ? -ans : ans;
    }
};
```



9 Palindrome Number

判断一个整数是否为回文数据，直接转。或者通过`to_string(x)`转换为字符串来做。

```c++
string str = to_string(x);
// <algorithm>
reverse(str.begin(), str.end());
// 反向迭代器
string s(str.rbegin(), str.rend());
```



```c++
// 把整数逆置的话要考虑逆置后的数超过了int范围
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        if(x >= 0 && x <= 9) {
            return true;
        }
        
        long long reversed = 0;
        int temp = x;
        while(temp > 0) {
            reversed = 10 * reversed + temp % 10;
            temp /= 10;
        }
        return reversed == x ? true : false;
    }
};

// 只逆置一半的数据
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        if(x >= 0 && x <= 9) {
            return true;
        }
        
        int reversed = 0;
        while(x > reversed) {
            reversed = 10 * reversed + x % 10;
            x /= 10;
        }
        return x == reversed || x == reversed / 10;
    }
};
```



12 Integer to Roman

map 的初始化和其他基本用法

```c++
class Solution {
public:
    string intToRoman(int num) {
        map<int, char> dict = {{1,'I'}, {5,'V'}, {10,'X'}, {50,'L'}, {100,'C'}, {500,'D'}, {1000,'M'}};
        
        string ans = "";
        int base = 1;
        while(num > 0) {
            int tmp1 = num % 10;
            int tmp2 = tmp1 * base;
            if(dict.find(tmp2) != dict.end()) {
                ans = dict[tmp2] + ans;
            }
            else if(tmp1 == 4) {
                if(base == 1) {
                    ans = "IV" + ans;
                }
                else if(base == 10) {
                    ans = "XL" + ans;
                }
                else {
                    ans = "CD" + ans;
                }
            }
            else if(tmp1 == 9) {
                if(base == 1) {
                    ans = "IX" + ans;
                }
                else if(base == 10) {
                    ans = "XC" + ans;
                }
                else {
                    ans = "CM" + ans;
                }
            }
            else {
                if(tmp1 > 5) {
                    string str(tmp1 - 5, dict[base]);
                    ans = str + ans;
                    ans = dict[5 * base] + ans;
                }
                else {
                    string str(tmp1, dict[base]);
                    ans = str + ans;
                }
            }         
            
            num /= 10;
            base *= 10;
        }
        return ans;
    }
};

// 其他解法
string intToRoman(int num) {
    string result = "";
    vector<pair<string, int>> mapping = {
        {"M", 1000},
        {"CM", 900},
        {"D", 500},
        {"CD", 400},
        {"C", 100},
        {"XC", 90},
        {"L", 50},
        {"XL", 40},
        {"X", 10},
        {"IX", 9},
        {"V", 5},
        {"IV", 4},
        {"I", 1}
    };
    for(auto& elem: mapping) {
        auto val = num/elem.second;
        if(val) {
            while(val) {
                result += elem.first;
                val--;
            }
            num = num % elem.second;
        }
    }
    return result;
}
```



16 3Sum Closest

双指针

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int global = INT_MAX, ans = 0;
        
        for(int i = 0; i < nums.size() - 2; ++i) {
            int l = i + 1, r = nums.size() - 1;

            while(l < r) {
                int tmp_sum = nums[i] + nums[l] + nums[r];
                if(abs(target - tmp_sum) < global) {
                    global = abs(target - tmp_sum);
                    ans = tmp_sum;
                }
                
                if(tmp_sum > target) {
                    r--;
                }
                else if(tmp_sum < target) {
                    l++;
                }
                else {
                    return target;
                }
            }
        }
        return ans;
    }
};
```



18 4Sum

多一层循环转换为 3Sum，或者牺牲空间来存所有两个数的 pair 来计算符合条件的两个 pair

```c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {  
        vector<vector<int>> ans;
        if(nums.size() < 4) {
            return ans;
        }
        set<vector<int>> ans_set;
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;
        for(int i = 0; i < nums.size() - 3; ++i) {
            if(i != 0 && nums[i] == nums[i - 1]) continue;
            for(int j = i + 1; j < nums.size() - 2; ++j) {
                if(j != i + 1 && nums[j] == nums[j - 1]) continue;
                
                int l = j + 1, r = nums.size() - 1;
                while(l < r) {
                    int tmp_sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if(tmp_sum == target) {
                        ans_set.insert({nums[i], nums[j], nums[l], nums[r]});
                        l++;
                        r--;
                    }
                    else if(tmp_sum > target) {
                        r--;
                    }
                    else {
                        l++;
                    }
                }
            }
        }
        for(auto vec: ans_set) {
            ans.push_back(vec);
        }
        return ans;
    }
};
```



24 Swap Nodes in Pairs

原地交换每两个结点

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* headPointer = new ListNode(0, head);
        ListNode* last = headPointer;
        ListNode* curr = last->next;
        while(curr != nullptr && curr->next != nullptr) {
            last->next = curr->next;
            curr->next = curr->next->next;
            last->next->next = curr;
            
            last = curr;
            curr = curr->next;
        }
        return headPointer->next;
    }
};
```



25 Reverse Nodes in k-Group

24题的拓展，细分两个函数，一个是判断是否有 k 个结点需要逆置，一个专门用来逆置这 k 个结点

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool hasKGroup(ListNode* node, int k) {
        int i = 0;
        while(i < k && node->next != nullptr) {
            node = node->next;
            i++;
        }
        return i == k;
    }
    ListNode* reverseKNodes(ListNode* head, int k) {
        ListNode *curr = head->next->next;
        ListNode *pre = head->next;
        ListNode *nextNode = nullptr;
        int i = 1;
        while(i < k) {
            nextNode = curr->next;
            curr->next = head->next;
            head->next = curr;
            
            curr = nextNode;
            i++;
        }
        pre->next = curr;
        return pre;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k == 1) return head;
        ListNode *phead = new ListNode(0, head);
        ListNode *curr = phead;
        while(hasKGroup(curr, k)) {
            curr = reverseKNodes(curr, k);
        }
        return phead->next;
    }
};
```



27 Remove Element

实际上就是覆盖地把元素写到一个标记合法元素的分界位置

```c++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] != val) {
                if(len != i) {
                    nums[len] = nums[i];
                }
                len++;
            }
        }
        return len;
    }
};
```



35 Search Insert Position

二分查找，注意最后返回的是 l

```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        int mid = 0;
        while(l <= r) {
            mid = (l + r) / 2;
            if(nums[mid] == target) {
                return mid;
            }
            else if(nums[mid] > target) {
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```



40 Combination Sum Ⅱ

回溯

```c++
class Solution {
public:
    void findTarget(vector<vector<int>>& ans, vector<int>& combination, vector<int> candidates, int target, int k, int n) {
        if(target == 0) {
            ans.push_back(combination);
            return;
        }
        
        for(int i = k; i < n; ++i) {
            // 防止出现重复的组合
            if(i != k && candidates[i] == candidates[i - 1]) continue;
            
            if(candidates[i] <= target) {
                combination.push_back(candidates[i]);
                findTarget(ans, combination, candidates, target - candidates[i], i + 1, n);
                combination.pop_back();
            }
        }
        
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> combination;
        int n = candidates.size();
        
        if(n == 0) return ans;
        
        sort(candidates.begin(), candidates.end());
        findTarget(ans, combination, candidates, target, 0, n);
        
        return ans;
    }
};
```



43 Multiply Strings

两层循环逐一计算，用一个 m+n 长的数组来保存每一位的数字，并且在转换为字符串时注意首位无效的 0

```c++
class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0") return "0";
        if(num1 == "1") return num2;
        if(num2 == "1") return num1;
        
        int n = num1.length();
        int m = num2.length();
        vector<int> ans(n + m, 0);
        
        for(int i = n - 1; i >= 0; --i) {
            for(int j = m - 1; j >= 0; --j) {
                int sum = (num1[i] - '0') * (num2[j] - '0') + ans[i + j + 1];
                ans[i + j + 1] = sum % 10;
                ans[i + j] += sum / 10;
            }
        }
        
        string res;
        for(auto num: ans) {
            if(res.empty() && num == 0) continue;
            res += to_string(num);
        }
        return res;
    }
};
```



46 Permutations

回溯法，in-place

```c++
class Solution {
public:
    void backtrack(vector<vector<int>>& res, vector<int>& nums, int i, int n) {
        if(i == n) {
            res.push_back(nums);
            return;
        }
        for(int j = i; j < n; ++j) {
            swap(nums[j], nums[i]);
            backtrack(res, nums, i + 1, n);
            swap(nums[j], nums[i]);
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        if(n == 0) return res;
        backtrack(res, nums, 0, n);
        return res;
    }
};
```



47 Permutations Ⅱ

回溯，先判断元素是否唯一，唯一则执行回溯

```c++
class Solution {
public:
    vector<vector<int>> res;
    
    void backtrack(vector<int>& nums, int i, int n) {
        if(i == n) {
            res.push_back(nums);
            return;
        }
        unordered_set<int> seen;
        for(int j = i; j < n; ++j) {
            if(seen.find(nums[j]) == seen.end()) {
                swap(nums[j], nums[i]);
                backtrack(nums, i + 1, n);
                swap(nums[j], nums[i]);
                seen.insert(nums[j]);
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        int n = nums.size();     
        if(n == 0) return res;
        backtrack(nums, 0, n);
        return res;
    }
};
```

