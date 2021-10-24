
#GeeksForGeeks
#Question : Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.


#Code:

class Solution: 
    
    def selectionSort(self, arr,n):
        
        for i in range(0, n):
            min_index = i
            for j in range(i+1,n):
                if arr[j] < arr[min_index]: 
                    min_index = j
            
            (arr[i],arr[min_index]) = (arr[min_index], arr[i])
