# 快速排序
---
## 快速排序原理
快速排序是一种分治的排序算法。它将一个数组分成两个子数组，将两部分独立地排序。\
快速排序和归并排序是互补的：\
归并排序：1）将数组分成两个子数组分别排序，并将有序的子数组归并以将整个数组排序；2）递归调用发生在处理整个数组之前；3）一个数组被等分为两半。\
快速排序：1）则是当两个子数组都有序时，整个数组也就自然有序了；2）递归调用发生在处理整个数组之后；3）切分（partition）的位置取决于数组的内容。

## 快速排序动图
[快速排序.gif](https://github.com/dta0502/Sort-Compare/blob/master/images/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F.gif)

## [快速排序代码](https://github.com/dta0502/Sort-Compare/blob/master/quick.py)
### 1. 切分---partition()
切分方法：先随意地取`a[lo]`作为切分元素（即那个将会被排定的元素），然后我们从数组的左端开始向右扫描直到找到一个大于等于它的元素，再从数组的右端开始向左扫描直到找到一个小于等于它的元素。这两个元素是没有排定的，因此我们交换它们的位置。如此继续，当两个指针相遇时，我们只需要将切分元素`a[lo]`和左子元素最右侧的元素`a[j]`交换然后返回j即可。
```python
def partition(a,low,high):
    i = low
    j = high + 1
    while True:
        #左边指针往右移动
        i += 1
        while a[i] < a[low]:
            if i == high:
                break
            i += 1
        #右边指针往左移动
        j -= 1
        while a[low] < a[j]:
            if j == low:
                break
            j -= 1
        #如果左右指针交叉，说明已经排序好了
        if i >= j:
            break
        #交换a[i]、a[j]
        exchange(a,i,j)
    exchange(a,low,j)
    return j
```

### 2. sort()函数
快速排序递归地将子数组`a[lo..hi]`排序，先用partition()方法将`a[j]`放到一个合适位置，然后再用递归调用将其他位置的元素排序。
```python
def sort(a,low,high):
    if low >= high:
        return
    j = partition(a,low,high)
    sort(a,low,j-1)
    sort(a,j+1,high)
```

### 3. quickSort()函数
为了保证快速排序函数quickSort()输入只有未排序的数组，这里调用前面的辅助函数sort()：
```python
def quickSort(a):
    length = len(a)
    sort(a,0,length-1)
```

### 4. 快速排序结果
`未排序数组：`\
`[4, 6, 2, 5, 16, 17, 7, 11, 19, 15, 0, 1, 18, 13, 9, 10, 14, 8, 12, 3]`\
`快速排序后数组：`\
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`

### 5. 快速排序与归并排序、选择排序、插入排序的比较
这里我设置sortCompare函数中的数组大小为1000，数组个数为100个，下面是4种排序算法的运行时间：\
```python
SelectionSort's total time:
5.730731010437012
InsertionSort's total time:
11.002668857574463
MergeSort's total time:
0.4718046188354492
QuickSort's total time:
0.30764150619506836
```
快速排序和归并排序的时间复杂度为O(nlogn)，选择排序和插入排序的时间复杂度均为O(n^2)，上面的运行时间也直观说明了这一点。

