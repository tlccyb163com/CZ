
numlist=[2,4,5,1,3,8,10,3,7,4,12,21,23,9,15]

def Bubblesort(data):

    if len(data)<=1:
       return data
       
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
               data[j],data[j+1]=data[j+1],data[j]
    return data
    
    
if __name__=="__main__":
   a=Bubblesort(numlist)
   print (a)

   
    

