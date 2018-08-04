class selectionSort():
    #辅助函数——交换两个数
    def exchange(self,a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    
    #选择排序函数(无返回值)
    def selection(self,a):
        length = len(a)
        for i in range(length):
            minIndex = i
            for j in range(i+1,length):
                if a[j] < a[minIndex]:
                    minIndex = j
            self.exchange(a,i,minIndex)

if __name__ == '__main__':
    import random
    a = []
    for i in range(20):
        a.append(i)
    random.shuffle(a) #打乱数组a的顺序
    print("未排序数组：")
    print(a)
    sel = selectionSort()
    sel.selection(a) 
    print("选择排序后数组： ")
    print(a)
