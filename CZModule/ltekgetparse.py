# -*- coding: utf8 -*-
import os, time
import re
import copy

dict2 = {"EUtranCellFDD": {"MO": "", "alpha": "", "physicalLayerCellIdGroup": "", "physicalLayerSubCellId": "",
                           "cellRange": "", "changeNotification_changeNotificationSIB2": ""}}


def parse(file, dict1):
    dict={}

    for key1,val1 in dict1.items():
        temp={}
        for key in val1:
            temp[key]=""
        dict[key1]=temp

    f = open(file, 'r')
    line = f.readline()
    Kget_list = []
    while line:
        if line.startswith("MO"):
            MO =line.rsplit(",",1)[1].strip().split("=")[0]
            if MO in dict.keys():
                Cache={}
                Cache[MO] = dict.get(MO)
                Cache[MO]["MO"] = re.split(r'[\s]{3,}', line)[1].strip()
                line = f.readline()
                line = f.readline()

                while not line.startswith("========"):

                    if line.startswith("Struct") and "members" in line:
                        Structname = re.split(r'[\s]{1,}', line)[1]
                        line = f.readline()
                        while line.find(">>>") >= 0:
                            StructDetail = Structname + "_" + re.split(r'\.|=', line)[1]
                            StructDetail = Structname + "_" + re.split(r'\.|=', line)[1].strip()
                            if StructDetail in Cache[MO].keys():
                                if len(re.split(r'\.|=', line)) >= 3:
                                    Cache[MO][StructDetail] = re.split(r'\.|=', line)[2].strip()
                                else:
                                    Cache[MO][StructDetail] = ""
                            line = f.readline()
                    elif line.startswith("reservedBy["):
                        if "reservedBy" in Cache[MO].keys():
                            reservedBy_len=int(re.split('\[|\]',line.strip())[1])
                            if reservedBy_len>=1:
                               line=f.readline()
                               reservedBy_value=""
                               while line.find(">>>") >=0:
                                     reservedBy_value="%s \n %s"%(reservedBy_value,line)
                                     line=f.readline()

                               Cache[MO]["reservedBy"]=reservedBy_value
                    elif line.startswith("sectorCarrierRef["):
                        if "sectorCarrierRef" in Cache[MO].keys():
                            sectorCarrierRef_len=int(re.split('\[|\]',line.strip())[1])
                            if sectorCarrierRef_len>=1:
                                line=f.readline()
                                sectorCarrierRef_value=""
                                while line.find(">>>") >=0:
                                    sectorCarrierRef_value ="%s \n %s"%(sectorCarrierRef_value,line)
                                    line=f.readline()
                                Cache[MO]["sectorCarrierRef"] =sectorCarrierRef_value


                    else:
                        name = re.split(r'[\s]{3,}', line.strip())[0].strip()
                        if name in Cache[MO].keys():
                            if len(re.split(r'[\s]{3,}', line.strip())) >= 2:
                                Cache[MO][name] = re.split(r'[\s]{3,}', line)[1].strip()
                            else:
                                Cache[MO][name] = ""

                    line = f.readline()
                Kget_list.append(copy.deepcopy(Cache))


        line = f.readline()

    f.close()
    return Kget_list

#AA=parse("C:\\CZEZFL9504254.log",dict2)

#print(AA)




