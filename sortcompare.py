#下面开始是计时函数
def time(a,sortname):
    import time
    from selection import selection
    from insertion import insertion
    from merge import mergeSort
    time_start = time.time()
    if sortname == 'Selection':
        selection(a)
    if sortname == 'Insertion':
        insertion(a)
    if sortname == 'Merge':
        mergeSort(a)
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
            #a.append(random.randint(1,10))
            a.append(random.random())
        totalTime += time(a,sortname)
    return totalTime

if __name__ == '__main__':
    sortname1 = 'Selection' 
    sortname2 = 'Insertion'
    sortname3 = 'Merge'
    length = 1000
    numberOfArrays = 100
    print("SelectionSort's total time:")
    print(timeRandomInput(sortname1,length,numberOfArrays))
     
    print("InsertionSort's total time:")
    print(timeRandomInput(sortname2,length,numberOfArrays))

    print("MergeSort's total time:")
    print(timeRandomInput(sortname3,length,numberOfArrays))

