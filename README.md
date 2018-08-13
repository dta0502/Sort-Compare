# Sort-Compare

1.五大排序算法（选择排序、插入排序、归并排序、快速排序、堆排序）的Python实现\
2.不同排序算法的运行时间比较-----sortcompare.py\
3.算法分析-----[个人博客](https://blog.csdn.net/dta0502/article/details/81410840)

## 选择排序
首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置（如果第一个元素就是最小元素那么它就和自己交换）。再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。这种方法叫做选择排序，因为它在不断地选择剩余元素之中的最小者。

### 1. 辅助函数——exchange()
```python
#辅助函数——交换两个数
def exchange(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
```

### 2. 选择排序主函数——selection()
```python
#选择排序函数(无返回值)
def selection(a):
    length = len(a)
    for i in range(length):
        minIndex = i
        for j in range(i+1,length):
            if a[j] < a[minIndex]:
                minIndex = j
        exchange(a,i,minIndex)
```

## 插入排序
通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当位置。在计算机的实现中，为了给要插入的元素腾出空间，我们需要将其余所有元素在插入之前都向右移动一位。这种算法叫做插入排序。
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

## 归并排序
归并排序体现的是一种**分治思想（Divide and conquer）**，下面是其排序的步骤：\
1）将数组一分为二（Divide array into two halves）\
2）对每部分进行递归式地排序（Recursively sort each half）\
3）合并两个部分（Merge two halves）

### 1. merge()函数：
具体步骤如下：\
1）给出原数组`a[]`，该数组的low到mid，mid+1到high的子数组是各自有序的。\
2）将数组复制到辅助数组（auxiliary array）中，两部分数组的首元素分别以i和j的下标，给原数组首元素以k的下标。\
3）比较i下标和j下标的元素，将较小值赋到k下标位置的元素内，然后对k和赋值的下标进行递增。\
4）重复上述过程，直到比较完全部元素。
```python
def merge(a,aux,low,mid,high):
    for k in range(low,high+1):
        aux[k] = a[k] #辅助数组
    i = low
    j = mid+1
    for k in range(low,high+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > high:
            a[k] = aux[i]
            i += 1
        elif aux[i]>aux[j]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1
```

### 2. sort()函数
要对子数组`a[lo..hi]`进行排序，先将它分为`a[lo..mid]`和`a[mid+1..hi]`两部分，分别通过递归调用将它们单独排序，最后将有序的子数组归并为最终的排序结果。
```python
def sort(a,aux,low,high):
    if high <= low:
        return
    mid = (low+high)//2 #保证mid是整数
    sort(a,aux,low,mid)
    sort(a,aux,mid+1,high)
    merge(a,aux,low,mid,high)
```

### 3. mergeSort()函数
为了保证归并排序函数mergeSort()输入只有未排序的数组，这里调用前面的辅助函数sort()：
```python
def mergeSort(a):
    low = 0
    high = len(a)-1 #注意：0~len(a)-1
    aux = [0] * len(a)
    sort(a,aux,low,high)
    return a
```

### 4. 归并排序结果
未排序数组：\
`[4, 6, 2, 5, 16, 17, 7, 11, 19, 15, 0, 1, 18, 13, 9, 10, 14, 8, 12, 3]`\
归并排序后数组：\
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`

### 5. 归并排序与选择排序/插入排序的比较
这里我设置sortCompare函数中的数组大小为1000，数组个数为100个，下面是3种排序算法的运行时间：\
`SelectionSort's total time:`\
`5.374305248260498`\
`InsertionSort's total time:`\
`11.281434535980225`\
`MergeSort's total time:`\
`0.4907994270324707`\
归并排序的时间复杂度为`O(nlogn)`，选择排序和插入排序的时间复杂度均为`O(n^2)`，上面的运行时间也直观说明了这一点。
