# 堆排序
## 堆的定义
在二叉堆的数组中，每个元素都要保证大于等于另两个特定位置的元素，也就是父节点一定要大于等于它的两个子节点，此时称为堆有序。

### （1）由下至上的堆有序化（上浮）
当插入一个元素时，我们一般先放到数组的末尾，然后让它一点点向上移动，直到移动到它的父节点（记住：k结点的父节点是）比他大，这种操作叫上浮swim()，完成这个操作后数组重新恢复有序性。

![swim](https://github.com/dta0502/Sort-Compare/blob/master/images/HeapSort/%E4%B8%8A%E6%B5%AE---swim.png)

### （2）由下至上的堆有序化（下沉）
一般删除最大键值的方式是将最大键值与数组的末尾进行交换，然后把最大键值的指向null，可是由于数组的末尾肯定不是最大的父节点，所以需要将它一点点向下移动，直到移动到它的子节点比它小为止，这种操作就叫下沉sink()，完成这个操作后数组重新恢复有序性。

![sink](https://github.com/dta0502/Sort-Compare/blob/master/images/HeapSort/%E4%B8%8B%E6%B2%89---sink.png)

```python
#下沉函数
def sink(a,k,N):
    while 2*k < N:
        #选出两个子结点中大的那个
        j = 2 * k
        if j<N and a[j]<a[j+1]: #j<N是为了保证j+1<=N
            j += 1
        #如果结点k不比两个子节点小，说明下沉结束
        if not a[k]<a[j]:
            break
        #下沉
        exchange(a,k,j)
        k = j
```

### （3）插入元素、删除最大元素操作
![insert and delete](https://github.com/dta0502/Sort-Compare/blob/master/images/HeapSort/%E6%8F%92%E5%85%A5%E5%85%83%E7%B4%A0%20%26%20%E5%88%A0%E9%99%A4%E6%9C%80%E5%A4%A7%E5%85%83%E7%B4%A0.png)

## 堆排序
堆排序可以分成两个阶段。在堆的构造阶段中，我们将原始数组重新组织安排进一个堆中；然后在下沉排序阶段，我们从堆中按递减顺序取出所有元素并得到排序结果。

### （1）堆的构造
**目的：N个给定的元素构造一个堆。**\
一个高效的方法：从右向左用sink()函数构造子堆。数组的每个位置都已经是一个子堆的根结点了，sink()对于这些子堆也适用。如果一个结点的两个子节点都已经是堆了，那么在该结点上调用sink()可以将它们变成一个堆。这个过程会递归得建立起堆的秩序。\
下图是一个堆构造的例子，首先调用sink(5,11)，然后调用sink(4,11)，一直到sink(1,11)：

![堆的构造](https://github.com/dta0502/Sort-Compare/blob/master/images/HeapSort/%E5%A0%86%E7%9A%84%E6%9E%84%E9%80%A0.png)

```python
    #第一步：堆的构造
    k = N // 2 #向下整除
    while k >= 0:
        sink(a,k,N-1)
        k -= 1
```

### （2）下沉排序
堆排序的主要工作都是在第二阶段完成的。这里我们将堆中的最大元素删除，然后放入堆缩小后数组中空出的位置。\
这个过程和选择排序有些类似，但所需的比较要少得多，因为堆提供了一种从未排序部分找出最大元素的有效方法。\
下图是一个下沉排序的例子：

![下沉排序](https://github.com/dta0502/Sort-Compare/blob/master/images/HeapSort/%E4%B8%8B%E6%B2%89%E6%8E%92%E5%BA%8F.png)

```python
    #第二步：下沉排序
    while N > 0:
        exchange(a,0,N-1)
        N -= 1
        sink(a,0,N-1)
```

### （3）堆排序主函数代码
```python
#堆排序主函数
def heapSort(a):
    N = len(a)
    #第一步：堆的构造
    k = N // 2 #向下整除
    while k >= 0:
        sink(a,k,N-1)
        k -= 1
    #第二步：下沉排序
    while N > 0:
        exchange(a,0,N-1)
        N -= 1
        sink(a,0,N-1)
```
