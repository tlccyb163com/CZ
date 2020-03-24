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
                   sftp.put(os.path.abspath(os.path.join(filesdir,file)),os.path.abspath(os.path.join(UploadDir,file)))

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
                    sftp.get(os.path.join(filesdir,file),os.path.abspath(os.path.join(DownloadDir,file)))

        except Exception as e:
               print(e)

        finally:
               tran.close()