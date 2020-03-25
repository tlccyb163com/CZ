# -*- coding: utf8 -*-

import pandas as pd
import time
import pyodbc,xlrd,xlwt

class sqlquery:

# 初始化连接、查询语句、文件导出名
      def __init__(self,conn,sql,outputcsv_file):
          self.conn=conn
          self.sql=sql
          self.outputcsv_file=outputcsv_file

      def Tocsv(self):
          try:
              CCon=pyodbc.connect(self.conn)
              Data=pd.read_sql(self.sql,CCon)
              Data.to_csv(self.outputcsv_file,index=False)

          except Exception as e:
               print (e)

          finally:
               CCon.close