#!C:\Users\tlccyb1\AppData\Local\Programs\Python\Python36-32\python
# -*- coding: utf8 -*-

import pymysql
import logging
import os


class mysqldb(object):

#构造方法初始化      
      def __init__(self,**kwargs):
          self.host=kwargs.get("host")
          self.database=kwargs.get("database")
          self.user=kwargs.get("user")
          self.password=kwargs.get("password")
          self.port=kwargs.get("port")
          self.__connection=None
          self.__cursor=None

#打开数据库连接和cursor          
      def open(self):
          self.__connection=pymysql.Connect(host=self.host,db=self.database,user=self.user,passwd=self.password,charset='utf8',use_unicode=True)
          self.__cursor=self.__connection.cursor()
          self.__cursor.rowcount
          
#mysql的插入、更新、删除操作          
      def mysqlExcute(self,sql):
          try:            
             self.__cursor.execute(sql)
             self.__connection.commit()
          except:
             self.__connection.rollback()
#mysql的查询操作
      def mysqlselect(self,sql):
          self.__cursor.execute(sql)
          result=self.__cursor.fetchall()
          
          return result,self.__cursor.rowcount
          
#mysql的数据关闭                   
      def close(self):
          self.__connection.close()
          self.__connection=None
          self.__cursor=None
          
              
          
          
if __name__ == '__main__':
     sql='insert into 51job (job_name,job_company_name,job_place,job_salary) values ("Mongodb","江苏常州联通","科二路","15000")'
     db=mysqldb('127.0.0.1','cz','root','123456',3306)
     try:
        db.open()    
        db.mysqlExcute(sql)        
     finally:   
        db.close()
        
           
