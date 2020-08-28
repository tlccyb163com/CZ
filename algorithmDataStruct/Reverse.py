'''

字符串反转

'''

def Reverse(s):
    
    if len(s)<=1:
       return s   
    else:
       L=list(s)
       left=0
       right=len(L)-1
       while left<right:
             L[left],L[right]=L[right],L[left]
             left += 1
             right -=1
             
       return "".join(L)
S="2ertwyq41"
print(Reverse(S))       