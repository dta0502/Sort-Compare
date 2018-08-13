## 插入排序原理
通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当位置。在计算机的实现中，为了给要插入的元素腾出空间，我们需要将其余所有元素在插入之前都向右移动一位。这种算法叫做插入排序。
## 插入排序动图
![插入排序.gif](https://github.com/dta0502/Sort-Compare/blob/master/images/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.gif)
## [插入排序代码](https://github.com/dta0502/Sort-Compare/blob/master/insertion.py)
```python
#插入排序函数
def insertion(a):
    length = len(a)
    for i in range(1,length):
        j = i
        while (j>0 and a[j]<a[j-1]):
            exchange(a,j,j-1)
            j -= 1
```
