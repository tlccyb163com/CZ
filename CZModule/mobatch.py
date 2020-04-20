# -*- coding: utf8 -*-

import os,re,csv
import time


class mobatch(object):

    def __init__(self,filename=None):
        if filename is None:
            return
        self.filename=filename
    '''
       inv_parselicense返回值是表头、内容的列表
       header is [ERBS,FeatureName,FeatureKey ,FAJ ,LicenseState ,FeatureState,ServiceState,ValidFrom,ValidUntil,Description]
    '''
    @property
    def logname(self):
        return self.filename

    @logname.setter
    def logname(self,value):
        self.filename=value

    def inv_parse(self):
        header=[]
        content_list=[]
        fingerprint=[]
        with open(self.filename,'r',encoding='utf-8',errors='ignore') as f:
             line=f.readline()
             while line:
                   if "> inv" in line:
                       ERBS=line.strip().split(">")[0]
                       header.append("ERBS")

                   if line.startswith("FingerPrint:"):
                      fingerprint.append(ERBS)
                      finger_split=re.split(r'[\s]{1,}',line.strip())

                      if len(finger_split)>=2:
                         fingerprint.append(finger_split[1])
                      else:
                          finger_split.append("NULL")


                   if "LicenseState" in line and "FeatureState" in line and "ServiceState" in line:
                       header=header+line.strip().split()
                       line=f.readline()
                       line=f.readline()
                       while not line.startswith("========") and not line.startswith("------"):
                           temp_replace = re.findall(r'(1 \(ENABLED\)|1 \(ACTIVATED\)|1 \(OPERABLE\)|0 \(INOPERABLE\)|0 \(DISABLED\)|0 \(DEACTIVATED\)|[\d]{4}-[\d]{1,2}-[\d]{1,2}|No Limit|CXC[\d/]{5,})',line)
                           for i in temp_replace:
                               line=line.replace(i,"     %s     "%i)
                           line_list=re.split(r'[\s]{5,}',line.strip())

                           if line_list[0].startswith("CXC40"):
                                  line_list.insert(0,"FeatureName_NULL")

                           if len(line_list)==8:
                                  line_list.insert(-1,"NULL")

                           if len(line_list)==7:
                               line_list.insert(-1, "NULL")
                               line_list.insert(-2, "NULL")

                           line_list.insert(0,ERBS)
                           content_list.append(line_list)
                           line=f.readline()
                       break

                   line=f.readline()
        return header,content_list,fingerprint






if __name__=='__main__':

    invpath=os.path.join(os.path.dirname(__file__),"invinput")
    output=os.path.join(os.path.dirname(__file__),"invoutput")
    fingerprint_file = "/".join(os.path.join(output, "fingerprint_%s.csv" % time.strftime('%Y%m%d%H%M', time.localtime())).split("\\"))
    license_file="/".join(os.path.join(output, "license_%s.csv" % time.strftime('%Y%m%d%H%M', time.localtime())).split("\\"))

    if not os.path.isdir(output):
        os.mkdir(output)
    temp=0
    for file in os.listdir(invpath):
        if file.find(".log")>=1:
             file="/".join(os.path.join(invpath,file).split("\\"))
             mo=mobatch(file)
             header,content_list,fingerprint=mo.inv_parse()


             with open(fingerprint_file,'a',newline='') as f:
                 csvwrite = csv.writer(f)
                 csvwrite.writerow(fingerprint)

             with open(license_file,'a',newline='') as f:
                   csvwrite=csv.writer(f)
                   if temp==0:
                       csvwrite.writerow(header)
                       temp=1
                   for i in content_list:
                        csvwrite.writerow(i)




