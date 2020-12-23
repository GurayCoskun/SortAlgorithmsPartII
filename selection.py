def selectionSort(arr,n): 
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, n): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
      
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    printArr(arr,n)

def printArr(arr,n):
    for i in range(n): 
       print ("% d" % arr[i]) 

if __name__ == '__main__':
    arr = [5, 6, 3, 4, 2] 
    n=len(arr)
    selectionSort(arr,n) 
    