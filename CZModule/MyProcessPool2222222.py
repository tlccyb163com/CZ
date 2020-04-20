# -*- coding: utf8 -*-
import os,time
from concurrent.futures import ThreadPoolExecutor,wait
from CZModule.ftp import myftp
import ftplib



def pr(m,n):
    print (m,n)
    time.sleep(0.25)


def dwonload(file,remoteDir,Localdir):
    try:

       ftp=myftp(host="132.225.146.53",user="EricNpi",passwd="Jiangsu@666")
       ftp.login()
       Localfile=os.path.join(Localdir,file)
       file=os.path.join(remoteDir,file)
       ftp.DownLoadFile(LocalFile=Localfile,RemoteFile=file)

    except Exception as e:
        print(e)
    finally:
        ftp.close()

if __name__=="__main__":
     LocalDir="F:/"
     LocalDir1="F:/ZERO"
     ftp=ftplib.FTP()
     ftp.connect(host="132.225.146.53", port=21)
     ftp.login(user="EricNpi",passwd="Jiangsu@666")
     remoteDir="/home/EricNpi/ALARM_daily/ALARM_input"
     ftp.cwd(remoteDir)
     start=time.time()
     task_all=[]
     t=ThreadPoolExecutor(max_workers=5)
     for file in ftp.nlst():
         task=t.submit(dwonload,file,remoteDir,LocalDir)
         task_all.append(task)
     wait(task_all,return_when="ALL_COMPLETED")
     end=time.time()
     print("--------%s"%(end-start))

     start1 = time.time()

     for file in ftp.nlst():
         dwonload(file,remoteDir,LocalDir1)

     end1 = time.time()

     print("--------%s" % (end1 - start1))





