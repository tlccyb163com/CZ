# -*- coding: utf8 -*-

import smtplib
import time,os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart



class mail(object):
      
      def __init__(self,**kwargs):
            '''
            mail of config setting
            '''
            self.mail_host=kwargs.get("mail_host")
            self.mail_user=kwargs.get("mail_user")
            self.passwd=kwargs.get("passwd")
            self.receiver=kwargs.get("receiver")
            self.subject=kwargs.get("subject")
            self.puretext=kwargs.get("puretext")
            self.html=kwargs.get("html")
            self.files=kwargs.get("files")
            
            assert isinstance(self.mail_host,str) and isinstance(self.mail_user,str) and isinstance(self.passwd,str) and isinstance(self.subject,str)
            
            assert isinstance(self.receiver,list)
            
            if self.puretext is not None:
               assert isinstance(self.puretext,str)
            if self.html is not None:
               assert isinstance(self.html,str)
            if self.files is not None:
               assert isinstance(self.files,list)
               
            
      def send(self):
           msg=MIMEMultipart()
           msg['From']=self.mail_user
           msg['To']=",".join(self.receiver)
           msg['Subject']=self.subject
           if self.puretext is not None:
              text= MIMEText(self.puretext)
              msg.attach(text)
              
           if self.html is not None:
              html=MIMEText(self.html)
              msg.attach(html)
           
           if self.files is not None:
              for file in self.files:
               jpgpart=MIMEApplication(open(file, 'rb').read())
               jpgpart.add_header('Content-Disposition', 'attachment', filename=file.split("/")[-1])
               msg.attach(jpgpart)
               
           try:
               smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
               smtpObj.login(self.mail_user, self.passwd)
               smtpObj.sendmail(self.mail_user, self.receiver, msg.as_string())
               smtpObj.quit()
               print("mail has been send successfully........")

           except Exception as e:
                  print ("mail send fail---",e)           
           
      
          