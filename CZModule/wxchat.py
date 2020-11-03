# _*_ coding: utf-8 _*_


import itchat
'''

message_content:消息内容
files:发送的文件
toUserName:发送的用户
videos:发送视频文件
pictures:发送图片
'''

# 初始化登陆
#my=itchat.new_instance()
#my.auto_login(hotReload=True)


def send(mychat:itchat,**kwargs):
    if kwargs.get("message_content"):
       mychat.send(msg=kwargs.get("message_content"),toUserName=mychat.search_friends(kwargs.get("toUserName"))[0]["UserName"])
    
    if kwargs.get("files"):
       for file in kwargs.get("files"):
           mychat.send_file(fileDir=file,toUserName=mychat.search_friends(kwargs.get("toUserName"))[0]["UserName"])
           
    if kwargs.get("pictures"):
       for img in kwargs.get("pictures"):
           mychat.send_image(fileDir=img,toUserName=mychat.search_friends(kwargs.get("toUserName"))[0]["UserName"])
           
    if kwargs.get("videos"):
       for video in kwargs.get("videos"):
           mychat.send_video(fileDir=video,toUserName=mychat.search_friends(kwargs.get("toUserName"))[0]["UserName"])
    
    
    
    
