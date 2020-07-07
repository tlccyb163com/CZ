
# -*- coding: utf8 -*-
import configparser

def config_dict(filename=None):
    cfg_dict={}
    if filename is None or not isinstance(filename,str):
        return
    else:
        try:
            filename="/".join(filename.split("\\"))
            config=configparser.ConfigParser()
            config.read(filename,encoding='utf8')
            cfg_dict = {i: dict([j for j in config.items(i)]) for i in config.sections()}#-------->字典解析
            #cfg_dict=dict(map(lambda x:(x,dict([i for i in config.items(x)])),config.sections()))------>>>>高阶函数与匿名函数新式

        except Exception as e:
               print("error",e)
    return cfg_dict










