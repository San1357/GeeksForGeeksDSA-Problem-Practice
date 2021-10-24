
#Question :


#Code:
class Solution:
    
    def insertionSort(self, alist, n):
        for i in range(1, n):
            key = alist[i]
            j = i -1
            
            while(j>=0 and key < alist[j]):
                alist[j+1] = alist[j]
                j = j-1
                
            alist[j+1] = key
