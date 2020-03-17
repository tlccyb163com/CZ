# -*- coding: utf8 -*-

import smtplib
import time,os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class sendmail:

       def __init__(self,mail_host,mail_user,passwd,receiver,subject,puretext,files):
             if not isinstance(receiver,list) or not isinstance(files,list):
                 print ("Please enter list type with receiver and files")
             else:
                 self.mail_host=mail_host
                 self.mail_user=mail_user
                 self.passwd=passwd
                 self.receiver=receiver
                 self.subject=subject
                 self.puretext=puretext
                 self.files=files


       def send(self):
           msg=MIMEMultipart()
           msg['From']=self.mail_user
           msg['To']=",".join(self.receiver)
           msg['Subject']=self.subject
           puretext=MIMEText(self.puretext)
           msg.attach(puretext)
           for file in self.files:
               jpgpart=MIMEApplication(open(file, 'rb').read())
               jpgpart.add_header('Content-Disposition', 'attachment', filename=file.split("/")[-1])

               msg.attach(jpgpart)

           try:
               smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
               smtpObj.login(self.mail_user, self.passwd)
               smtpObj.sendmail(self.mail_user, self.receiver, msg.as_string())
               print("mail has been send successfully........")
               smtpObj.quit()

           except Exception as e:
                  print (e)
