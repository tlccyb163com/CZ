'''

求最长不重复字符串问题


'''

a="qweryhkeeeertyjlpqwfgttuiqeolabcdfhh"


def longsubstr(L):
    
    if len(L)<=1:
       return L 
     
    start=0
    end=0
    i=1
    temp={}
    temp[L[0]]=0
    lonstr=""
    while i<=len(L)-1:
            temp[L[i]]=i
            if L[i] in L[start:end+1]:
                start=temp[L[i]]+1
            end +=1    
            if len(L[start:end+1])>len(lonstr):
                 lonstr=L[start:end+1]
                 
            i +=1
               
    return lonstr

print(longsubstr(a))    
