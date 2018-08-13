## 选择排序原理
首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置（如果第一个元素就是最小元素那么它就和自己交换）。再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。这种方法叫做选择排序，因为它在不断地选择剩余元素之中的最小者。
## 选择排序动态图
![选择排序.gif](https://github.com/dta0502/Sort-Compare/blob/master/images/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F.gif)
## [选择排序的Python实现](https://github.com/dta0502/Sort-Compare/blob/master/selection.py)
