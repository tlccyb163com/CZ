# -*- coding:utf8 -*-


regdict={}

def reg(name):
    def warper(fn):
        regdict[name]=fn
        
    return warper
    
    
    
def default():
    print("this func is not registed")
    
    
def dispatch():
    while True:
          funcname=input("please input module name:")
          if funcname.lower()=="quit":
             break
          elif regdict.get(funcname) is None:
               default()
          else:
               regdict.get(funcname)()

@reg("f1")
def fool1():
    print ("this is fool1")
    
@reg("f2")
def fool2():
    print ("this is fool2")
    
    
    
if __name__=="__main__":
    dispatch()
    
    
