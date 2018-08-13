## 归并排序原理
归并排序体现的是一种**分治思想（Divide and conquer）**，下面是其排序的步骤：\
1）将数组一分为二（Divide array into two halves）\
2）对每部分进行递归式地排序（Recursively sort each half）\
3）合并两个部分（Merge two halves）
## 归并排序动图
![归并排序.gif](https://github.com/dta0502/Sort-Compare/blob/master/images/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F.gif)
## [归并排序代码](https://github.com/dta0502/Sort-Compare/blob/master/merge.py)
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
```python
未排序数组：
[4, 6, 2, 5, 16, 17, 7, 11, 19, 15, 0, 1, 18, 13, 9, 10, 14, 8, 12, 3]
归并排序后数组：
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

### 5. 归并排序与选择排序/插入排序的比较
这里我设置sortCompare函数中的数组大小为1000，数组个数为100个，下面是3种排序算法的运行时间：
```python
SelectionSort's total time:
5.374305248260498
InsertionSort's total time:
11.281434535980225
MergeSort's total time:
0.4907994270324707
```
归并排序的时间复杂度为`O(nlogn)`，选择排序和插入排序的时间复杂度均为`O(n^2)`，上面的运行时间也直观说明了这一点。
