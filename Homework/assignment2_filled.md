# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by 夏天明 元培学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 10 | 22H2

Python编程环境：Spyder IDE 5.4.3 | Python 3.11.4 64-bit




## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/



思路：简单实现。在init中就将分数化为最简



##### 代码

```python
from math import gcd

class Frac:
    def __init__(self, a, b):
        d = gcd(a, b)
        self.a = a//d
        self.b = b//d
    
    def __add__(self, other):
        a, b, c, d = self.a, self.b, other.a, other.b
        return Frac(a*d+c*b, b*d)
    
    def __str__(self):
        return f"{self.a}/{self.b}"

a, b, c, d = map(int, input().split())
print(Frac(a, b) + Frac(c, d))
```



代码运行截图 

![image-20240227133132374](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227133132374.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：实际是贪心，挑性价比高的



##### 代码

```python
n, w = map(int, input().split())
s = sorted(([int(i) for i in input().split()] for j in range(n)), key=lambda x: x[0]/x[1])
ans = 0
try:
    while s[-1][1] < w:
        ans += s[-1][0]
        w -= s[-1][1]
        s.pop()
    ans += w / s[-1][1] * s[-1][0]
except IndexError:
    pass
print("%.1f" % ans)
```



代码运行截图 

![image-20240227133327251](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227133327251.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：用堆维护要用的技能



##### 代码

```python
from heapq import heappush, heapreplace
for w in range(int(input())):
    n, m, b = map(int, input().split())
    skill = {}
    time = set()
    for i in range(n):
        t, x = map(int, input().split())
        time.add(t)
        if t in skill:
            if len(skill[t]) < m:
                heappush(skill[t], x)
            elif skill[t][0] < x:
                heapreplace(skill[t], x)
        else:
            skill[t] = [x]
    for t in sorted(time):
        b -= sum(skill[t])
        if b <= 0:
            print(t)
            break
    if b > 0:
        print("alive")
```



代码运行截图 

![image-20240227133954582](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227133954582.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：欧拉筛



##### 代码

```python
import math
 
isprime = [True]*(10**6 + 1)
isprime[0] = isprime[1] = False
for k in range(10**6 + 1):
    if isprime[k]:
        j = k * 2
        while j < 10**6 + 1:
            isprime[j] = False
            j += k
 
n = int(input())
s = list(map(int, input().split()))
for i in s:
    print("YES" if math.sqrt(i).is_integer() and isprime[int(math.sqrt(i))] else "NO")
```



代码运行截图 

![image-20240227134135534](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227134135534.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：找不能整除的数就好了



##### 代码

```python
for w in range(int(input())):
    n, x = map(int, input().split())
    arr = [int(i)%x for i in input().split()]
    if sum(arr)%x: print(n)
    else:
        arr2 = [bool(i) for i in arr]
        arr3 = list(reversed(arr2))
        try:
            print(n - min(arr2.index(1), arr3.index(1)) - 1)
        except ValueError:
            print("-1")
```



代码运行截图 

![image-20240227134236469](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227134236469.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：素数问题，直接算



##### 代码

```python
from math import sqrt
primes = [1]*10**4
for i in range(2, 10**4):
    if primes[i]:
        for j in range(2, 10**4//i):
            primes[j*i] = 0
m, n = map(int, input().split())
for w in range(m):
    raw = [int(i) for i in input().split()]
    scores = sum(i for i in raw if sqrt(i).is_integer() and primes[int(sqrt(i))])
    print(f"{scores/len(raw):.2f}" if scores else 0)
```



代码运行截图 

![image-20240227135714254](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227135714254.png)



## 2. 学习总结和收获

顺便简单复习计概基础知识了。现在看有些之前写的代码，也挺巧妙的





