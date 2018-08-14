#辅助函数——交换两个数
def exchange(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

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

if __name__ == '__main__':
    import random
    a = []
    for i in range(20):
        a.append(i)
    random.shuffle(a) #打乱数组a的顺序
    print("未排序数组：")
    print(a)
    heapSort(a)
    print("堆排序后数组：")
    print(a)
