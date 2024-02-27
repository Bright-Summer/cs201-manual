# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2023 fall, Complied by 夏天明 元培学院



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 10 | 22H2

Python编程环境：Spyder IDE 5.4.3 | Python 3.11.4 64-bit




## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：使用lru_cache进行剪枝，递归计算



##### 代码

```python
from functools import lru_cache

@lru_cache()
def T(n):
    if n < 2:
        return n
    elif n == 2:
        return 1
    else:
        return T(n-1) + T(n-2) + T(n-3)

print(T(int(input())))
```



代码运行截图 

![image-20240219164310135](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240219164310135.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：逐个检验s中的字符，是否有hello中的每个字符



##### 代码

```python
s = iter(input())
try:
    for l in "hello":
        while (True):
            if next(s) == l:
                break
    print("YES")
except StopIteration:
    print("NO")
```



代码运行截图 

![image-20240219171112325](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240219171112325.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：implementation



##### 代码

```python
s = input().lower()
ans = ""
for l in s:
    if l not in "aeiouy":
        ans += "." + l
print(ans)
```



代码运行截图 

![image-20240219172502947](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240219172502947.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：先用欧拉筛维护素数表，然后遍历



##### 代码

```python
n = int(input())
prime, cnt, st = [0]*n, 0, [False]*n   #st是素数打标记，primes是额外维护的素数列表
for i in range(2,n):
    if not st[i]:
        prime[cnt] = i
        cnt += 1
    for j in range(n):
        if prime[j]>=n/i: break
        st[prime[j]*i] = True
        if i%prime[j] == 0: break
for i in range(2,n):
    if st[i] == False and st[n-i] == False:
        print(i,n-i)
        break
```



代码运行截图 

![image-20240219180435660](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240219180435660.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：关注最大项即可



##### 代码

```python
def getItem(it):
    a = it.split("n^")
    r = int(a[1])
    if a[0] == "0":
        r = 0
    return r

s = [getItem(i) for i in input().split("+")]
print(f"n^{max(s)}")
```



代码运行截图 

![image-20240227142210142](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227142210142.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：桶，简单实现



##### 代码

```python
from collections import Counter

cnt = Counter(map(int, input().split()))
print(*sorted(i for i in cnt if cnt[i] == max(cnt.values())))
```



代码运行截图 

![image-20240227142617169](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240227142617169.png)



## 2. 学习总结和收获

复习计概知识，熟悉git的使用，与Github仓库同步管理
