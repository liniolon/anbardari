# -*- coding: utf-8 -*-
#!/usr/bin/python

# Import Libraries
import sqlite3
from datetime import datetime

#global conn

class Admin():

    def CreateDatabaseClerk():
        sqlite3.connect('anbar.db')
        print("Database is Created Successfully")

    def CreateTableClerk():
        conn = sqlite3.connect('anbar.db')
        conn.execute('''create table clerk(

                                        id int primary_key not null,
                                        fullname text not null,
                                        password text not null,
                                        is_admin boolean not null
                    );''')
        print("Table is create")

    def InsertClerk(ID, fullname, password, is_admin):
        conn = sqlite3.connect('anbar.db')
        conn.execute("insert into clerk(id,fullname,password, is_admin)values({},'{}', '{}',{});".format(ID, fullname, password, is_admin))
        conn.commit()
        print("{} is add Successfully".format(fullname))
        conn.close()

    def DeleteClerk(ID):
        conn = sqlite3.connect('anbar.db')
        conn.execute("delete from clerk where id={};".format(ID))
        conn.commit()
        print("{} is removed Successfully".format(ID))
        conn.close()

    def UpdateClerk(ID, fullname,password, is_admin):
        conn = sqlite3.connect('anbar.db')
        conn.execute("update clerk set fullname='{}',password='{}', is_admin={} where id={};".format(fullname,password, is_admin, ID))
        conn.commit()
        print("{} is updated Successfully".format(ID))
        conn.close()

    def Search(ID):
        conn = sqlite3.connect('anbar.db')
        db = conn.execute("select * from clerk where id={};".format(ID))
        for i in db:
            print(i)

    def ShowAll():
        conn = sqlite3.connect('anbar.db')
        db = conn.execute("select * from clerk;")
        for i in db:
            print(i)

class Product:
    #def conn():
    #    global conn
    #    conn = sqlite3.connect('anbar.db')
    def CreateDatabaseProduct():
        conn = sqlite3.connect('anbar.db')
        print('Database is created')
    def CreateTableProduct():
        conn = sqlite3.connect('anbar.db', timeout=10)
        print("Connect is already in use")
        conn.execute("create table product(p_id int primary_key not null, p_name text not null,p_serial int not null, p_comment text not null);")
        print("Table is created")

    def InsertProduct(ID, name, serial, comment):
        conn = sqlite3.connect('anbar.db')
        #conn()
        conn.execute("insert into product(p_id, p_name, p_serial, p_comment)values({},'{}', {}, '{}');".format(ID, name, serial, comment))
        conn.commit()
        print("Product added Successfully")
        conn.close()

    def DeleteProduct(ID):
        #conn()
        conn.sqlite3.connect('anbar.db')
        conn.execute('delete from product weher id={};'.format(ID))
        conn.commit()
        print("Product is delete")
        conn.close()

    def UpdateProduct(ID, name, serial, comment):
    #    conn()
        conn.sqlite3.connect('anbar.db')
        conn.eexcute("update product set p_name='{}', p_serial={}, p_comment='{}' where p_id={};".format(name, serial, comment, ID))
        conn.commit()
        print("Product is updated")
        conn.close()

    def SearchProduct(ID):
        conn.sqlite3.connect('anbar.db')
        #conn()
        search = conn.execute('select * from product where p_id={};'.format(ID))
        for i in search:
            print(i)
        conn.commit()
        conn.close()

    def ShowAll():
        conn.sqlite3.connect('anbar.db')
        #conn()
        search = conn.execute('select * from product;')
        for i in search:
            print(i)
        conn.commit()
        conn.close()
