import re
import os

'''

update ~/moshell/sitefiles/ipdatabase

'''

def update_ip(**kwargs):

    if kwargs.get("source",None) is None:
       return
    
    if kwargs.get("dest",None) is None:
       return
       
    if not isinstance(kwargs.get("source"),str):
       return
    
    if not isinstance(kwargs.get("dest"),str):
       return
       
    source_dic={}
    with open(kwargs.get("source"),'r') as f:
         for line in f.readlines():
             ip=re.search(r'(\d+\.\d+\.\d+\.\d+)',line.strip())
             if ip:
                source_dic[ip.group(0)]=line.strip()
                
    with open(kwargs.get("dest"),'r') as f:
         for line in f.readlines():
              ip=re.search(r'(\d+\.\d+\.\d+\.\d+)',line.strip())
              if ip:
                   if ip not in source_dic.keys():
                      with open(kwargs.get("source"),'a+') as f_source:
                           f_source.write(line.strip()+"\n")
                      
                      
                      
if __name__=="__main__":
    update_ip(source="F:/ipdatabase_EricNpi",dest="F:/ipdatabase_public-1026")

    
