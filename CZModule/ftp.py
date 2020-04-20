# -*- coding: utf8 -*-
import ftplib
import os
from concurrent.futures import ThreadPoolExecutor,wait



class myftp(object):

    def __init__(self,host,user,passwd,port=21):

          self.host=host
          self.user=user
          self.passwd=passwd
          self.port=port
          self.ftp=ftplib.FTP()

    def login(self):
        self.ftp.connect(host=self.host, port=self.port)
        self.ftp.login(user=self.user,passwd=self.passwd)

    def UploadFile(self,LocalFile,RemoteFile):
        LocalFile = "/".join(LocalFile.split("\\"))
        RemoteFile = "/".join(RemoteFile.split("\\"))
        if not os.path.isfile(LocalFile):
            return
        try:
              buf_size=1024
              file_handler=open(LocalFile,'rb')
              self.ftp.storbinary('STOR %s' % RemoteFile, file_handler, buf_size)
        except Exception as e:
               print(e)


    def UploadFileDir(self,LocalDir,RemoteDir):
        LocalDir="/".join(LocalDir.split("\\"))
        RemoteDir="/".join(RemoteDir.split("\\"))
        if not os.path.isdir(LocalDir):
            return
        try:
            self.ftp.cwd(RemoteDir)
            buf_size = 1024
            for file in os.listdir(LocalDir):
                LocalFile="/".join(os.path.join(LocalDir,file).split("\\"))
                RemoteFile="/".join(os.path.join(RemoteDir,file).split("\\"))
                file_handler = open(LocalFile, 'rb')
                self.ftp.storbinary('STOR %s' % RemoteFile, file_handler, buf_size)
        except Exception as e:
               print(e)

    def DownLoadFile(self,LocalFile,RemoteFile):
        LocalFile="/".join(LocalFile.split("\\"))
        RemoteFile="/".join(RemoteFile.split("\\"))
        if os.path.exists(LocalFile):
            os.remove(LocalFile)
        with open(LocalFile, 'wb') as f:
            self.ftp.retrbinary('RETR ' + RemoteFile, f.write)

    def DownLoadFiletree(self,LocalDir,RemoteDir):

        LocalDir="/".join(LocalDir.split("\\"))
        RemoteDir="/".join(RemoteDir.split("\\"))
        if not os.path.exists(LocalDir):
            os.mkdir(LocalDir)
        self.ftp.cwd(RemoteDir)
        for file in self.ftp.nlst():
            Local=os.path.join(LocalDir,file)
            Local="/".join(Local.split("\\"))
            Remote=os.path.join(RemoteDir,file)
            Remote="/".join(Remote.split("\\"))
            if file.find(".")>=0:
                self.DownLoadFile(Local,Remote)
    @staticmethod
    def DownLoadFile2(LocalFile, RemoteFile, **kwargs):
        try:
            ftp = myftp(host=kwargs.get("host"), user=kwargs.get("user"), passwd=kwargs.get("passwd"))
            ftp.login()
            ftp.DownLoadFile(LocalFile=LocalFile, RemoteFile=RemoteFile)
        except Exception as e:
            print("error", e)
        finally:
            ftp.close()

    @staticmethod
    def multithread_DownLoadFiletree(**kwargs):
        LocalDir = "/".join(kwargs.get("LocalDir").split("\\"))
        RemoteDir = "/".join(kwargs.get("RemoteDir").split("\\"))
        ftp = ftplib.FTP()
        ftp.connect(host=kwargs.get("host"), port=21)
        ftp.login(user=kwargs.get("user"), passwd=kwargs.get("passwd"))
        ftp.cwd(RemoteDir)
        task_all = []
        t = ThreadPoolExecutor(max_workers=kwargs.get("workers"))
        for file in ftp.nlst():
            LocalFile = "/".join(os.path.join(LocalDir, file).split("\\"))
            RemoteFile = "/".join(os.path.join(RemoteDir, file).split("\\"))
            if file.find(".") >= 0:
                task = t.submit(myftp.DownLoadFile2, LocalFile, RemoteFile, host=kwargs.get("host"), user=kwargs.get("user"),
                                passwd=kwargs.get("passwd"), port=21)
                task_all.append(task)

        wait(task_all, return_when="ALL_COMPLETED")

    def close(self):
        self.ftp.close()





