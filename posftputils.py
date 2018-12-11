# -*- coding: utf-8 -*-
import ftplib
import os

from Entity.GetBranch import GetBranch


def ftp_upload():
  host = '192.168.72.220'
  username = "sy"
  password = "buynow"
  sqllite_db = 'jsPos'
  activebranch = GetBranch()
  branches = activebranch.get_active_branch()
  # 数据库模板
  db_template = sqllite_db + '.db'
  if os.path.exists(db_template):
      print db_template + ' is found'

  for row in branches:
      local_sqllite_db = sqllite_db + row[0] + '.db'
      if os.path.exists(local_sqllite_db):
        try:

          f = ftplib.FTP()  # 实例化FTP对象
          f.connect(host)
          f.login(username, password)  # 登录
          # '''以二进制形式上传文件'''
          file_remote = '/posapp/'+row[0]+db_template
          file_local = local_sqllite_db
          print file_remote
          print file_local
          bufsize = 1024  # 设置缓冲器大小
          fp = open(file_local, 'rb')
          f.storbinary('STOR ' + file_remote, fp, bufsize)
          fp.close()
          f.quit()
        except BaseException as e:
            print ("ftp error", e)

ftp_upload()

