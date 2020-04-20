# -*- coding: utf8 -*-

import os,re
import csv
import shutil
import pandas as pd
import numpy as np


def alarm_pase(alarm_inputdir,alarm_ouputfile=None):
    if not os.path.isdir(alarm_inputdir):
           print("请输入正确的alarm_log文件路径")
           return None

    elif alarm_ouputfile is None or not isinstance(alarm_ouputfile,str):

          return None

    else:
        with open(alarm_ouputfile,'w',newline='') as f:
             csvwt=csv.writer(f)
             csvwt.writerow(["ERBS","DATE_Time","Specific Problem","MO","Cause"])
             for file in ( os.path.abspath(os.path.join(alarm_inputdir,i)) for i in os.listdir(alarm_inputdir) if i.endswith(".log") or i.endswith(".txt")):
                 with open(file,'r') as alarmf:
                       line=alarmf.readline()
                       while line:
                             if line.strip().find("> alt") >= 0:
                                 ERBS=line.strip().split(">")[0]
                             if line.strip().startswith("Date") and line.strip().find("Specific Problem")>=1:
                                 line=alarmf.readline()
                                 line = alarmf.readline()
                                 while not line.strip().startswith(">>> Total"):
                                           temp=re.findall(r'(\w{1,}=\w{1,})',line.strip())
                                           line=line.replace(temp[0],"    %s"%temp[0]).strip()
                                           temp=re.findall(r'\(\w+',line.strip())
                                           line=line.replace(temp[0],"    %s"%temp[0]).strip()
                                           alarm_list=re.split('\s{1}[mMWwCc]\s{1}|\s{3,}|\s{3,}\(',line.strip())
                                           alarm_list.insert(0,ERBS)
                                           csvwt.writerow(alarm_list)
                                           line = alarmf.readline()

                             line=alarmf.readline()



def alarm_combine(alarmfile="",goncan="",alarm_config="",alarmfile_index=[],goncan_index=None,alarm_configindex=None,outputfile="",columns=[]):
    try:

        alarmfile_f=open(alarmfile)
        alarmfile_df=pd.read_csv(alarmfile_f)
        goncan_f=open(goncan)
        goncan_df=pd.read_csv(goncan_f)
        alarm_configf=open(alarm_config)
        alarm_configdf=pd.read_csv(alarm_configf)
        df=pd.merge(alarmfile_df,goncan_df,how='inner',left_on=alarmfile_index[0],right_on=goncan_index)
        df1=pd.merge(df,alarm_configdf,how='inner',left_on=alarmfile_index[1],right_on=alarm_configindex)
        df1=df1[columns]
        df1.to_excel(outputfile,index=False,sheet_name='ALARM')

    except Exception as e:
           print("Error:",e)

    finally:

        alarmfile_f.close()









if __name__=="__main__":
   alarm_combine(alarmfile="F:/345.csv",goncan="F:/goncan.csv",alarm_config="F:/ALARM_Config.csv",alarmfile_index=["ERBS","Specific Problem"],goncan_index="ENODEB",alarm_configindex="alarm_name",outputfile="F:/20200328.xlsx",columns=["ERBS","city","lon","lati","DATE_Time","network","Specific Problem","explain","network","Railway","lac","MO"])