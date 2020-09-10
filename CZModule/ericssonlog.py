# -*- coding: utf8 -*-

import re
import os

'''
ericsson ALARMlog Parse Module,this Module return is dict
'''
def ALARMlog_parse(filelog:str):

    if filelog is None or not isinstance(filelog,str):
    
        return
    
    with open(filelog,'r') as f:
          line=f.readline()
          ERBS=""
          while line:
                if "> alt" in line:
                   ERBS=line.strip().split(">")[0]
                   
                if "Date" in line and "Specific Problem" in line:
                   line=f.readline()
                   line=f.readline()
                   while not line.strip().startswith(">>> Total"):
                             
                             Alarm=re.match(r'(?P<Date_Time>[\d]{4}-[\d]{2}-[\d]{2}\s[\d]{2}:[\d]{2}:[\d]{2})\s(?P<S>[a-zA-Z])\s(?P<Specific_Problem>[\w\s]{1,})\s{1,}(?P<MO>[^\s]{1,}=[^\s]{1,})\s{1,}\((?P<Cause>.*)\)',line)
                             if Alarm is not None:
                                Alarm_dic={k:v.strip() for k,v in Alarm.groupdict().items()}
                                Alarm_dic["ERBS"]=ERBS
                                yield Alarm_dic
                             line=f.readline()                            
                line=f.readline()

'''
ericsson LTEKGETlog Parse Module,this Module return is dict
''' 
def LTEKGET_parse(filelog,MOList=["EUtranCellFDD"]):

    if filelog is None or not isinstance(filelog,str):
        return 
         
    if filelog is None or not isinstance(MOList,list):
        return 
    try:
        MOList=[i.lower() for i in MOList]
        
    except Exception as e:
           print (e)
    
    with open(filelog,'r') as f:
        ERBS=""
        line=f.readline()
        while line:       
            if "kget all" in line.strip().lower():
                ERBS=line.partition(">")[0]
                
            if line.startswith("MO") and line.strip().rpartition(",")[-1].partition("=")[0].lower() in MOList:
               dic={}
               dic["ERBS"]=ERBS
               dic["MoType"]=re.split(r'[,=]+',line.strip())[-2]
               dic["MO"]=line.strip().partition(" ")[-1]
               
               for _ in range(2):
                  line=f.readline()
               
               while not line.startswith("========"):
                         
                        linematch=re.match(r'\w+\[(\d+)\].*',line.strip())
                        linestruct=re.match(r'Struct\s+[\w]+\s+has\s+(\d+)\s+members:',line.strip())
                         
                        if linematch is not None:
                           linematchname=re.split(r'\[',line.strip())[0]
                           if int(linematch.group(1))==0:
                              dic[linematchname]=""
                              line=f.readline()
                              
                           elif int(linematch.group(1))>=1:
                                if len(re.split(r'\s{2,}',line.strip()))>1:
                                   dic[linematchname]=re.split(r'\s{2,}',line.strip())[1]
                                   line=f.readline()
                                   
                                else:
                                    lines=""
                                    line=f.readline()
                                    while ">>>" in line:
                                          lines=lines+line+"\n"
                                          line=f.readline()
                                    dic[linematchname]=lines
                                    
                        elif linestruct is not None:
                            structname=re.split(r'\s+',line.strip())[1]
                            if int(linestruct.group(1))==0:
                                dic[structname]=""
                                line=f.readline()
                            else:
                                line=f.readline()
                                while ">>>" in line:
                                      dic["%s_%s"%(structname,re.split(r'[.=]+',line.strip())[1])]=re.split(r'[.=]+',line.strip())[2] if len(re.split(r'[.=]+',line.strip()))==3 else ""     
                                      line=f.readline()        
                             
                        else:
                             
                             dic[re.split(r'\s{2,}',line.strip())[0]]=re.split(r'\s{2,}',line.strip())[1] if len(re.split(r'\s{2,}',line.strip()))==2 else ""
                             line=f.readline()
                             
               yield dic        
            line=f.readline()    
         
             
             
#LTEKGET_parse(filelog="F:/CZEGFL340350.log")         


for i in LTEKGET_parse(filelog="F:/CZEGFL340350.log"):
      print (i) 
                         
#for i in os.listdir("F:/ALARM_input"):
#      for j in ALARMlog_parse("/".join(os.path.join("F:/ALARM_input",i).split("\\"))):
#          print ("/".join(os.path.join("F:/ALARM_input",i).split("\\")))
#          print (j)             
