# -*- coding: utf-8 -*-
#!/usr/bin/env python


import pymongo             #导入pymongo模块         。PS：让py2.7安装pymongo的命令是 pip2 install  ,相应的让3安装就是pip3 install
import datetime            #导入时间模块


def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)  #设置主机地址和端口，建立数据库链接。
    db = client['example']                                      #或者使用字典的方式获取链接。
    #或者 db = client.example                                    #获取属性的方式
    return db  #返回获取到的数据库


def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']       #选择这个集合。多个document的合体，就是集合。
    print db.collection_names()     #打印集合名字
    return coll                     #返回集合


def insert_one_doc(db):
    # 插入一个document               #mongodb中每一条信息叫document
    coll = db['informations']       #选择这个集合
    information = {"name": "quyang", "age": "25"}     #字典，准备插入的字典。
    information_id = coll.insert(information)         #插入这一条字典，获取
    print information_id


def insert_multi_docs(db):
    # 批量插入documents,插入一个数组
    coll = db['informations']
    information = [{"name": "xiaoming", "age": "25"}, {"name": "xiaoqiang", "age": "24"}]  #数组中的对象为两个字典
    information_id = coll.insert(information)
    print information_id


def get_one_doc(db):
    # 有就返回一个，没有就返回None
    coll = db['informations']
    print coll.find_one()  # 返回第一条记录   #数据库查找
    print coll.find_one({"name": "quyang"})
    print coll.find_one({"name": "none"})


def get_one_by_id(db):
    # 通过objectid来查找一个doc
    coll = db['informations']
    obj = coll.find_one()      #返回第一条记录
    obj_id = obj["_id"]        #获取第一条记录的"_id"对象
    print "_id 为ObjectId类型，obj_id:" + str(obj_id)     #obj_id需要str处理

    print coll.find_one({"_id": obj_id})
    # 需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录###########################注意！！！！！！！⚠️
    print "_id 为str类型 "
    print coll.find_one({"_id": str(obj_id)})
    # 可以通过ObjectId方法把str转成ObjectId类型                               ###########################注意！！！！！！！⚠️
    from bson.objectid import ObjectId

    print "_id 转换成ObjectId类型"
    print coll.find_one({"_id": ObjectId(str(obj_id))})


def get_many_docs(db):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    coll = db['informations']
    #ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING
    for item in coll.find().sort("age", pymongo.DESCENDING):
        print item

    count = coll.count()
    print "集合中所有数据 %s个" % int(count)

    #条件查询
    count = coll.find({"name":"quyang"}).count()
    print "quyang: %s"%count

def clear_all_datas(db):
    #清空一个集合中的所有数据
    db["informations"].remove()

if __name__ == '__main__':
    db = get_db()          #建立链接
    my_collection = get_collection(db)  #获取集合
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}     #设置需要插入的内容，为一个字典。
    # 插入记录
    my_collection.insert(post)   #插入上面的字典
    insert_one_doc(db)     #插入25岁的quyang
    # 条件查询
    print my_collection.find_one({"x": "10"})    #查找部分
    # 查询表中所有的数据
    for iii in my_collection.find():             #全部查找
        print iii
    print my_collection.count()                  #获取集合文档条数
    my_collection.update({"author": "Mike"},
                         {"author": "quyang", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
                          "date": datetime.datetime.utcnow()})  #更新数据
    for jjj in my_collection.find():
        print jjj
    get_one_doc(db)        #获取第一条
    get_one_by_id(db)      #通过_id获取。id是自动增加的。
    get_many_docs(db)      #条件筛选。
    # clear_all_datas(db)  #可以清空所有内容，慎用！！！！！！！

    #《Torrent magnet存入数据库思路》

    #1.利用python字符串处理函数获取唯一✅标识，（先尝试是否可以手动增加_id进去）
    #2.每次保存数据之前，先搜索数据库，确保没有重复，然后再保存。
    #3.保存字段有：【文件名、文件大小、链接、时间、关键标识】
    #4.
    #5.