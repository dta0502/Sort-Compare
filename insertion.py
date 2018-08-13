#辅助函数——交换两个数组
def exchange(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

#插入排序函数
def insertion(a):
    length = len(a)
    for i in range(1,length):
        j = i
        while (j>0 and a[j]<a[j-1]):
            exchange(a,j,j-1)
            j -= 1

if __name__ == '__main__': 
    import random
    a = []
    for i in range(20):
        a.append(i)
    random.shuffle(a) #打乱数组a的顺序
    print("未排序数组：")
    print(a)
    insertion(a) 
    print("插入排序后数组： ")
    print(a)
