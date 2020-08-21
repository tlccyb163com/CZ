# -*- coding: utf8 -*-

import os
import paramiko


class sftp(object):

    def __init__(self,**kwargs):
        self.ip=kwargs.get("ip")
        self.port=kwargs.get("port")
        self.user=kwargs.get("user")
        self.passwd=kwargs.get("passwd")

        if self.ip is None or self.port is None or self.user is None or self.passwd is None:

           print ("IP address, port, user name and password are required to initialize SFTP,for example ip='*.*.*.*',prot='',user='',passwd=''")

    def FileUpload(self,filesdir="",UploadDir=""):
        try:
            tran=paramiko.Transport((self.ip,self.port))
            tran.connect(username=self.user,password=self.passwd)
            sftp=paramiko.SFTPClient.from_transport(tran)
            for file in os.listdir(filesdir):
                if os.path.isfile(os.path.abspath(os.path.join(filesdir,file))):
                   src="/".join(os.path.join(filesdir,file).split("\\"))
                   dest="/".join(os.path.join(UploadDir,file).split("\\"))
                   sftp.put(src,dest)

        except Exception as e:
               print(e)
        finally:
             tran.close()
             
    def singlefileupload(self,file="",UploadDir=""):
        
        try:
            print ("start---")
            tran=paramiko.Transport((self.ip,self.port))
            tran.connect(username=self.user,password=self.passwd)
            sftp=paramiko.SFTPClient.from_transport(tran)
            filename="/".join(file.split("\\")).split("/")[-1]
            src=file
            dest="/".join(os.path.join(UploadDir,filename).split("\\"))
            sftp.put(src,dest)
            print("end----")
            
        except Exception as e:
               print (e,"------------------")
               
        finally:
              tran.close()
            
            
            
    def singlefiledownload(self,file,DownloadDir=""):
        try:
            if not os.path.exists(DownloadDir):
                   print ("DownloadDir is not Exists")
            else:
                 tran=paramiko.Transport((self.ip,self.port))
                 tran.connect(username=self.user,password=self.passwd)
                 sftp=paramiko.SFTPClient.from_transport(tran)
                 src=file
                 dest="/".join(os.path.join(DownloadDir,file).split("\\"))
                 sftp.get(src,dest)
                 
        except Exception as e:
                
                print(e)
                
        finally:
                
                tran.close()
                 
                 
                
        


    def FileDownload(self,filesdir="",DownloadDir=""):
        try:
            if not os.path.exists(DownloadDir):
                print ("DownloadDir is not Exists")
            else:
                tran=paramiko.Transport((self.ip,self.port))
                tran.connect(username=self.user,password=self.passwd)
                sftp=paramiko.SFTPClient.from_transport(tran)
                for file in sftp.listdir(filesdir):
                    src="/".join(os.path.join(filesdir,file).split("\\"))
                    dest="/".join(os.path.join(DownloadDir,file).split("\\"))
                    sftp.get(src,dest)

        except Exception as e:
               print(e)

        finally:
               tran.close()