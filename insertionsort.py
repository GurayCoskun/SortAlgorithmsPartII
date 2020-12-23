def insertionSort(arr,n): 

    for i in range(1, n):  
        temp = arr[i] 
        j = i-1
        while (j >= 0 and temp < arr[j]) : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = temp
    printArr(arr,n)

def printArr(arr,n):
    for i in range(n): 
       print ("% d" % arr[i]) 

if __name__ == '__main__':
    arr = [5, 6, 3, 4, 2] 
    n=len(arr)
    insertionSort(arr,n) 
    