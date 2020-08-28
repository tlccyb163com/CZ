'''

二分顺序查找

'''



def binarySearch(alist, item):
    if alist==[]:
       return -1
       
    start=0
    end=len(alist)-1
    while start<=end:
          mid=(start+end)//2
          
          if item<alist[mid]:
             end=mid-1
             
          elif item>alist[mid]:
             start=mid+1
             
          else:
              return mid
              
    return -1
               
             
test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(test, 8))
print(binarySearch(test, 5))              
    
    
    
