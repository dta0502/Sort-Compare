#下面开始是计时函数
def time(a,sortname):
    import time
    from selection import selection
    from insertion import insertion
    from merge import mergeSort
    from quick import quickSort
    from heap import heapSort
    time_start = time.time()
    if sortname == 'Selection':
        selection(a)
    if sortname == 'Insertion':
        insertion(a)
    if sortname == 'Merge':
        mergeSort(a)
    if sortname == 'Quick':
        quickSort(a)
    if sortname == 'Heap':
        heapSort(a)
    time_end = time.time()
    return (time_end - time_start)

def timeRandomInput(sortname,length,numberOfArrays):
    import random
    totalTime = 0
    #测试数组数
    for i in range(numberOfArrays):
        #数组大小
        a = []
        for j in range(length):
            #a.append(random.randint(1,10))#1-10的随机整数
            a.append(random.random())#0-1的随机浮点数
        totalTime += time(a,sortname)
    return totalTime

if __name__ == '__main__':
    sortname1 = 'Selection' 
    sortname2 = 'Insertion'
    sortname3 = 'Merge'
    sortname4 = 'Quick'
    sortname5 = 'Heap'
    length = 10
    numberOfArrays = 100000
    print("SelectionSort's total time:")
    print(timeRandomInput(sortname1,length,numberOfArrays))
     
    print("InsertionSort's total time:")
    print(timeRandomInput(sortname2,length,numberOfArrays))

    print("MergeSort's total time:")
    print(timeRandomInput(sortname3,length,numberOfArrays))

    print("QuickSort's total time:")
    print(timeRandomInput(sortname4,length,numberOfArrays))
    
    print("HeapSort's total time:")
    print(timeRandomInput(sortname5,length,numberOfArrays))
