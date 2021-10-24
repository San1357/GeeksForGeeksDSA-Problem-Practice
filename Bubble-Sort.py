
# bubble_sort Problem

# Question: Given an Integer N and a list arr. Sort the array using bubble sort algorithm.

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        
        
        
        for i in range(n):
            swapped = False
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    
                    swapped = True
            if not swapped:
                break
