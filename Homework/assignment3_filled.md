# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by 夏天明 元培学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:

- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 10 | 22H2

Python编程环境：Spyder IDE 5.4.3 | Python 3.11.4 64-bit




## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：直接dp，dp[i]表示以第i颗导弹为最后一颗拦截的导弹时最多拦截的数量



##### 代码

```python
k = int(input())
h = [int(i) for i in input().split()]
dp = [1]*k
for i in range(k):
    for j in range(i):
        if h[i] <= h[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
```



代码运行截图 

![image-20240306222606973](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240306222606973.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：题面给了，只需要简单实现。注意使用f-string简化代码



##### 代码

```python
def move(n, a, b, c):
    if n == 0:
        return
    move(n-1, a, c, b)
    print(f"{n}:{a}->{c}")
    move(n-1, b, a, c)

n, a, b, c = input().split()
move(int(n), a, b, c)
```



代码运行截图 

![image-20240307132531557](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240307132531557.png)





**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：维护一个列表，用pop进行模拟实现



##### 代码

```python
while (s:=input()) != '0 0 0':
    n, p, m = map(int, s.split())
    p -= 1
    child = list(range(n))
    ans = []
    while child:
        p += m-1
        p %= len(child)
        ans.append(child.pop(p)+1)
    print(*ans, sep=',')
```



代码运行截图 

![](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240307132442074.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：贪心，直接从小到大排序即可



##### 代码

```python
n = int(input())
T = [(int(t), i) for i, t in enumerate(input().split())]
T.sort()
print(*[i+1 for t, i in T])
print(f"{sum(T[i][0]*(n-i-1) for i in range(n))/n:.2f}")
```



代码运行截图 

![image-20240307132739938](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240307132739938.png)



**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：直接套定义实现，注意不要原地修改排序距离和价格数组



##### 代码

```python
def med(arr):
    n = len(arr)
    return arr[n//2] if n&1 else (arr[n//2-1] + arr[n//2])/2

n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [sum(map(int,i.split(','))) for i in pairs]
cost = [int(i) for i in input().split()]
value = [d/c for d, c in zip(distances, cost)]
v_m = med(sorted(value))
c_m = med(sorted(cost))
print(len([0 for v, c in zip(value, cost) if v > v_m and c < c_m]))
```



代码运行截图 

![image-20240307132858866](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240307132858866.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：直接实现，用defaultdict来整理模型信息



##### 代码

```python
from collections import defaultdict

model = defaultdict(list)
for o in range(int(input())):
    name, num = input().split('-')
    model[name].append(num)
MB = {'M':1, 'B':1000}
for name, nums in sorted(model.items()):
    print(f"{name}: ", end='')
    print(*sorted(nums, key=lambda x: float(x[:-1])*MB[x[-1]]), sep=', ')
```



代码运行截图 

![image-20240307132950753](https://raw.githubusercontent.com/Bright-Summer/homework_picture_bed/main/img/image-20240307132950753.png)



## 2. 学习总结和收获

这次考试虽然有一些题之前做过了，但重写的过程也给了我一些新的启发，提交的代码相较于之前也更加简明

