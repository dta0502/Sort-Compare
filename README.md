# Sort-Compare

1.五大排序算法（选择排序、插入排序、归并排序、快速排序、堆排序）的Python实现\
2.不同排序算法的运行时间比较-----sortcompare.py\
**3.算法分析-----[个人博客-排序算法的Python实现以及时间分析](https://blog.csdn.net/dta0502/article/details/81410840)**

## 排序算法的Python实现
### [选择排序分析](https://github.com/dta0502/Sort-Compare/blob/master/selection.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/selection.py)

### [插入排序分析](https://github.com/dta0502/Sort-Compare/blob/master/insertion.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/insertion.py)

### [归并排序分析](https://github.com/dta0502/Sort-Compare/blob/master/merge.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/merge.py)

### [快速排序分析](https://github.com/dta0502/Sort-Compare/blob/master/quick.md)---[代码](https://github.com/dta0502/Sort-Compare/blob/master/quick.py)

## 各大排序算法运行时间对比
### 1. 数组大小为1000，数组个数为100
#### 1) random.random()
这个函数随机生成0-1之间的浮点数。
```python
SelectionSort's total time:
5.376079559326172
InsertionSort's total time:
10.705189943313599
MergeSort's total time:
0.4794747829437256
QuickSort's total time:
0.31154561042785645
```

#### 2) random.randint(1,10)
这个函数随机生成1-10之间的整数。
```python
SelectionSort's total time:
5.173416614532471
InsertionSort's total time:
10.060582637786865
MergeSort's total time:
0.5347213745117188
QuickSort's total time:
0.24558091163635254
```

### 2. 数组大小为10，数组个数为100000
#### 1) random.random()
这个函数随机生成0-1之间的浮点数。
```python
SelectionSort's total time:
1.20361328125
InsertionSort's total time:
1.200181007385254
MergeSort's total time:
2.400212049484253
QuickSort's total time:
1.111870288848877
```

#### 2) random.randint(1,10)
这个函数随机生成1-10之间的整数。
```python
SelectionSort's total time:
1.1860406398773193
InsertionSort's total time:
1.0625879764556885
MergeSort's total time:
2.4801878929138184
QuickSort's total time:
1.1623103618621826
```
