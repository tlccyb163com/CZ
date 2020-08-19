
from PIL import Image, ImageDraw, ImageFont
import time,os
import prettytable as pt



class table(object):

      def __init__(self,**kwargs):
      
          self.style=pt.MSWORD_FRIENDLY if kwargs.get("style") is None else kwargs.get("style")
          self.border=1 if kwargs.get("border") is None else kwargs.get("border")
          self.horizontal_char="-" if kwargs.get("horizontal_char") is None else kwargs.get("horizontal_char")
          
      def tab_info_fromlist(self,**kwargs):
          try:
              if kwargs.get("header") is None or kwargs.get("data") is None:
                 return
                 
              '''
               header is a table header for example ["Name", "Age","Country","City"]
               data is  a list struct data for example [[1,2,3],[2,3,4]]
              '''
              header=kwargs.get("header")
              data=kwargs.get("data")
              tab=pt.PrettyTable()
              tab.set_style(self.style)
              tab.border=self.border
              tab.horizontal_char=self.horizontal_char
              tab.field_names=header
              for row in data:
                  tab.add_row(row)
              return str(tab)
           
          except Exception as e:
                 print ("errorerr------",e)
                 
      def tab_info_fromcsv(self,**kwargs):
          try:
             f=open(kwargs.get("csvfile"),"r")
             tab=pt.from_csv(f)
             tab.set_style(self.style)
             tab.border=self.border
             tab.horizontal_char=self.horizontal_char
             return str(tab)
             
          except Exception as e:
                 print("----",e)
                 
          finally:
                f.close()
             
             
             
          
class ImgWriteTable(object):

      def __init__(self,**kwargs):
      
         self.x_imgspace=800 if kwargs.get("x_imgspace") is None else kwargs.get("x_imgspace")
         self.y_imgspace=300 if kwargs.get("y_imgspace") is None else kwargs.get("y_imgspace")
         self.ImagFile=kwargs.get("ImagFile")
         self.im=Image.new('RGB',(self.x_imgspace, self.y_imgspace),(0,0,0,0)) if self.ImagFile is None else Image.open(self.ImagFile)
         
      def Drawmultiline(self,**kwargs):
          fonturl='C:\\WINDOWS\\Fonts\\SIMYOU.TTF' if kwargs.get("fonturl") is None else kwargs.get("fonturl")
          fontsize=15 if kwargs.get("fontsize") is None else kwargs.get("fontsize")
          fontcolor='white' if kwargs.get("fontcolor") is None else kwargs.get("fontcolor")
          x_space=50 if kwargs.get("x_space") is None else kwargs.get("x_space")
          y_space=50 if kwargs.get("y_space") is None else kwargs.get("y_space")
          tab_info=kwargs.get("tab_info")
          
          if tab_info is None:
              return
          
          try:
             
             font=ImageFont.truetype(fonturl,fontsize,encoding='utf-8')
             draw=ImageDraw.Draw(self.im, "RGB")
             draw.multiline_text((x_space,y_space), tab_info,font=font,fill=fontcolor)
             
          except Exception as e:
                 print ("error---",e)
                 
      def savefile(self,**kwargs):
          savedfile=os.path.abspath(os.path.join(os.getcwd(), "%s.PNG"%time.strftime("%y%m%d%H%M%S", time.localtime()))) if kwargs.get("savedfile") is None else kwargs.get("savedfile")
          self.im.save(savedfile)
          return savedfile
          
  


if __name__=="__main__":
    table=table()
    tab_info=table.tab_info_fromlist(header=["ENODEB","Railway","city","lon","lati","network","lac"],data=[["SQEWo5987","京沪高速","宿迁","118.594","34.2994","3G","53732"],["SQEWo5987","京沪高速","宿迁","118.594","34.2994","3G","53732"]])
    a=ImgWriteTable(ImagFile="F:/cyb.jpg")
    a.Drawmultiline(tab_info=tab_info)
    a.savefile()
