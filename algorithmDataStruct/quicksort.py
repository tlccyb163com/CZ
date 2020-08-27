
'''
快速排序
'''

numlist=[2,2,4,5,3,8,1,11,13,9,2,2,1]


def quicksort(arr,start,end):
    if start>=end:
       return arr
       
    low=start
    high=end
    mid=arr[start]
    
    while low < high:
     
          while low < high and arr[high]>=mid:
                high=high-1      
          arr[low]=arr[high]
          
          while low<high and arr[low]<=mid:
                low=low+1
          arr[high]=arr[low]
          
    arr[low]=mid
    quicksort(arr,start,low)
    quicksort(arr,low+1,end)
    
if __name__=="__main__":
    print (numlist)
    quicksort(numlist,0,len(numlist)-1)
    print (numlist)
        
    
