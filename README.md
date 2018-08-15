# Sort-Compare

1.五大排序算法（选择排序、插入排序、归并排序、快速排序、堆排序）的Python实现\
2.不同排序算法的运行时间比较-----sortcompare.py\
**3.算法分析-----[个人博客-排序算法的Python实现以及时间分析](https://blog.csdn.net/dta0502/article/details/81410840)**

## 排序算法的Python实现
### [选择排序分析](https://github.com/dta0502/Sort-Compare/blob/master/selection.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/selection.py)

### [插入排序分析](https://github.com/dta0502/Sort-Compare/blob/master/insertion.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/insertion.py)

### [归并排序分析](https://github.com/dta0502/Sort-Compare/blob/master/merge.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/merge.py)

### [快速排序分析](https://github.com/dta0502/Sort-Compare/blob/master/quick.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/quick.py)

### [堆排序分析](https://github.com/dta0502/Sort-Compare/blob/master/heap.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/heap.py)

## 各大排序算法运行时间对比
### 1. 数组大小为1000，数组个数为100
#### 1) random.random()
这个函数随机生成0-1之间的浮点数。
```python
SelectionSort's total time:
5.555765151977539
InsertionSort's total time:
11.97522497177124
MergeSort's total time:
0.540255069732666
QuickSort's total time:
0.31798601150512695
HeapSort's total time:
0.6184689998626709
```

#### 2) random.randint(1,10)
这个函数随机生成1-10之间的整数。
```python
SelectionSort's total time:
5.795068740844727
InsertionSort's total time:
10.428340673446655
MergeSort's total time:
0.5053162574768066
QuickSort's total time:
0.2666609287261963
HeapSort's total time:
0.5388846397399902
```

### 2. 数组大小为10，数组个数为100000
#### 1) random.random()
这个函数随机生成0-1之间的浮点数。
```python
SelectionSort's total time:
1.2794384956359863
InsertionSort's total time:
1.2449653148651123
MergeSort's total time:
2.4802358150482178
QuickSort's total time:
1.2663071155548096
HeapSort's total time:
2.2440004348754883
```

#### 2) random.randint(1,10)
这个函数随机生成1-10之间的整数。
```python
SelectionSort's total time:
1.246002197265625
InsertionSort's total time:
1.0966532230377197
MergeSort's total time:
2.417612075805664
QuickSort's total time:
1.1484196186065674
HeapSort's total time:
2.0112228393554688
```
