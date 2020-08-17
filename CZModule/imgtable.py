#!C:\Users\tlccyb1\AppData\Local\Programs\Python\Python36-32\python
# -*- coding: utf8 -*-


from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont
import time,os



def ImgWriteTable1(**kwargs):
    '''
    header is a table header for example ["Name", "Age","Country","City"]
    data is  a list struct data for example [[1,2,3],[2,3,4]]
    '''
    if kwargs.get("header") is None or kwargs.get("data") is None:
       return 
    
    header=kwargs.get("header")
    data=kwargs.get("data")    
    fonturl='C:\\WINDOWS\\Fonts\\SIMYOU.TTF' if kwargs.get("fonturl") is None else kwargs.get("fonturl")
    fontsize=15 if kwargs.get("fontsize") is None else kwargs.get("fontsize")
    fontcolor='black' if kwargs.get("fontcolor") is None else kwargs.get("fontcolor")
    ImagFile=kwargs.get("ImagFile")
    imgspace=300 if kwargs.get("imgspace") is None else kwargs.get("imgspace")
    savedfile=os.path.abspath(os.path.join(os.getcwd(), "%s.PNG"%time.strftime("%y%m%d%H%M%S", time.localtime()))) if kwargs.get("savedfile") is None else kwargs.get("savedfile")
    
    if data is None or savedfile is None:
       return
       
    tab=PrettyTable()
    try:
       tab.field_names=header
       for row in data:
           tab.add_row(row)
       tab_info = str(tab)
       print (tab_info)
           
    except Exception as e:
           print ("error---",e)
           
    try:
        font = ImageFont.truetype(fonturl,fontsize,encoding='utf-8')
        if ImagFile is None:
           im=Image.new('RGB',(imgspace, imgspace),(0,0,0,0))
        else:
           im=Image.open(ImagFile)
        
        draw=ImageDraw.Draw(im, "RGB")
        img_size = draw.multiline_textsize(tab_info, font=font)
        im_new = im.resize((img_size[0]+imgspace*2, img_size[1]+imgspace*2))
        del im
        del draw
        draw = ImageDraw.Draw(im_new, 'RGB')
        
        draw.multiline_text((imgspace,imgspace), tab_info,font=font,fill=fontcolor)
        im_new.save(savedfile)
    except Exception as e:
           print ("error-----",e)

    return savedfile           
        
    
    
           
    







def ImgWriteTable():
    tab = PrettyTable()
    # 设置表头
    tab.field_names = ["Name", "Age","Country","City"]
    # 表格内容插入
    tab.add_row(['chal','23','中国','Shanghai'])
    tab.add_row(['charle','29','China','Xuzhou'])
    tab.add_row(['jack','32','United States','Washington'])
    tab_info = str(tab)
    space = 100
     
    # PIL模块中，确定写入到图片中的文本字体
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\SIMYOU.TTF', 15, encoding='utf-8')
    # Image模块创建一个图片对象
    im = Image.new('RGB',(50, 50),(0,0,0,0))
    # ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im, "RGB")
    # 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    # 图片初始化的大小为10-10，现在根据图片内容要重新设置图片的大小
    im_new = im.resize((img_size[0]+space*2, img_size[1]+space*2))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')
    # 批量写入到图片中，这里的multiline_text会自动识别换行符
    # python2
    #draw.multiline_text((space,space), unicode(tab_info, 'utf-8'), fill=(255,255,255), font=font)
    # python3
    draw.multiline_text((space,space), tab_info, fill=(255,255,255), font=font)
     
    im_new.save('F:/12345.PNG', "PNG")
    del draw


if __name__=="__main__":
    ImgWriteTable1(header=["Name", "Age","Country","City"],data=[['chal','23','中国','Shanghai'],['charle','29','China','Xuzhou']],ImagFile="F:/01.jpg")
