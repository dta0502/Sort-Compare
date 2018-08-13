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

def sort(a,aux,low,high):
    if high <= low:
        return
    mid = (low+high)//2 #保证mid是整数
    sort(a,aux,low,mid)
    sort(a,aux,mid+1,high)
    merge(a,aux,low,mid,high)

def mergeSort(a):
    low = 0
    high = len(a)-1 #注意：0~len(a)-1
    aux = [0] * len(a)
    sort(a,aux,low,high)
    return a

if __name__ == '__main__':
    import random
    a = []
    for i in range(20):
        a.append(i)
    random.shuffle(a) #打乱数组a的顺序
    print("未排序数组：")
    print(a)
    mergeSort(a)
    print("归并排序后数组：")
    print(a)

