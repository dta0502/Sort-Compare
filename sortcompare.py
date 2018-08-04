class sortCompare():
    def __init__(self,sortname,length,numberOfArrays):
        self.sortname = sortname
        self.length = length
        self.numberOfArrays = numberOfArrays

    #辅助函数——交换两个数组
    def exchange(self,a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    #插入排序函数
    def insertion(self,a):
        length = len(a)
        for i in range(1,length):
            j = i
            while(j>0 and a[j]<a[j-1]):
                self.exchange(a,j,j-1)
                j -= 1
    
    #选择排序函数(无返回值)
    def selection(self,a):
        length = len(a)
        for i in range(length):
            minIndex = i
            for j in range(i+1,length):
                if a[j] < a[minIndex]:
                    minIndex = j
            self.exchange(a,i,minIndex)
    

    #检查排序结果是否正确
    def check_list(self,oriArray,Array):
        newArray = sorted(oriArray)
        if newArray == Array:
            return True
        else:
            return False

    #下面开始是计时函数
    def time(self,a):
        import time
        time_start = time.time()
        if self.sortname == 'Selection':
            self.selection(a)
        if self.sortname == 'Insertion':
            self.insertion(a)
        time_end = time.time()
        return (time_end - time_start)

    def timeRandomInput(self):
        import random
        totalTime = 0
        #测试数组数
        for i in range(self.numberOfArrays):
            #数组大小
            a = []
            for j in range(self.length):
                a.append(random.randint(1,10))
            totalTime += self.time(a)
        return totalTime

if __name__ == '__main__':
    sortname1 = 'Insertion' 
    sortname2 = 'Selection'
    length = 100
    numberOfArrays = 100
    f1 = sortCompare(sortname1,length,numberOfArrays)
    f2 = sortCompare(sortname2,length,numberOfArrays)
    print("InsertionSort's total time:")
    print(f1.timeRandomInput())
     
    print("SelectionSort's total time:")
    print(f2.timeRandomInput())


