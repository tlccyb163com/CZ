
class people:
     def __init__(self,name):
         self.name=name

     @property
     def gname(self):
         return self.name

     @gname.setter
     def gname(self,value):
         self.name=value

p=people("cyb")
print(p.name)
p.name="ZLF"
print(p.name)


