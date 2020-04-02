# -*- coding: utf8 -*-
import ftplib
import os



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


    def close(self):
        self.ftp.close()


