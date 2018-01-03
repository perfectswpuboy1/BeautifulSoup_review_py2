# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 《Torrent magnet存入数据库思路》
'''
    # 1.利用python字符串处理函数获取唯一✅标识，（先尝试是否可以手动增加_id进去）
    # 2.每次保存数据之前，先搜索数据库，确保没有重复，然后再保存。
    # 3.保存字段有：【文件名、文件大小、链接、时间、关键标识】
    # 4.file_name0  filesize0   magnet0  datetime0  keywords0
    # 5.
'''
import pymongo             #导入pymongo模块         。PS：让py2.7安装pymongo的命令是 pip2 install  ,相应的让3安装就是pip3 install
import datetime            #导入时间模块

def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)  #设置主机地址和端口，建立数据库链接。
    db = client['torrentkitty']                                      #或者使用字典的方式获取链接。
    #或者 db = client.example                                    #获取属性的方式
    return db  #返回获取到的数据库

def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']       #选择这个集合。多个document的合体，就是集合。
    #print db.collection_names()     #打印集合名字
    return coll                     #返回集合

def insert_one_doc(db,file_name0,filesize0,magnet0,keywords0):
    # 插入一个document               #mongodb中每一条信息叫document
    coll = db['informations']       #选择这个集合
    #step1 获取magnet链接的keyid   21-61位为关键字串   [20:61]
    keywords0=magnet0[20:60]
    #step2 查找keywords0是否重复。
    if coll.find_one({"Vedio_KeyID": keywords0}) == None:
        pass
    else:
        information = {"Vedio_name": file_name0, "File_size": filesize0,"Magnet_Link": magnet0,"Save_Time": datetime.datetime.utcnow(),"Vedio_KeyID": keywords0}     #字典，准备插入的字典。
        information_id = coll.insert(information)         #插入这一条字典，获取
        print information_id
if __name__ == '__main__':
    print "Please use it by import!"