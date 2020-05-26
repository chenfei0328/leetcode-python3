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

