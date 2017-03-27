# -*- coding: utf-8 -*- 
#!/usr/bin/python 

# Import Libraries
import sqlite3 
from datetime import datetime 

#global conn

class Admin():
    #def __init__(self):
    #    global conn

    def CreateDatabaseClerk():
        sqlite3.connect('anbar.db')
        print("Database is Created Successfully")  
    
    def CreateTableClerk(): 
        conn = sqlite3.connect('anbar.db')
        conn.execute('''create table clerk(
                    
                                        id int primary_key not null, 
                                        fullname text not null,
                                        is_admin boolean not null 
                    );''')
        print("Table is create")
    
    def InsertClerk(ID, fullname, is_admin):
        conn = sqlite3.connect('anbar.db')
        conn.execute("insert into clerk(id,fullname,is_admin)values({},'{}',{});".format(ID, fullname, is_admin))
        conn.commit()
        print("{} is add Successfully".format(fullname))       
        conn.close()
    
    def DeleteClerk(ID):
        conn = sqlite3.connect('anbar.db')
        conn.execute("delete from clerk where id={};".format(ID))
        conn.commit()
        print("{} is removed Successfully".format(ID))
        conn.close()

    def UpdateClerk(ID, fullname, is_admin):
        conn = sqlite3.connect('anbar.db')
        conn.execute("update clerk set fullname='{}', is_admin={} where id={};".format(fullname, is_admin, ID))
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
    #def __ini__():
    #    global p_conn 
    #    p_conn.connect('anbar.db')
    #    print("Connected Successfully")
    def CreateTableProduct():
        conn = sqlite3.connect('anbar.db')
        print("Connect is already in use")
        conn.execute("create table product(p_id int primary_key not null, p_name text not null,p_serial int not null, p_comment text not null)")
        print("Table is created")
    
    def InsertProduct(ID, name, serial, comment):
        conn = sqlite3.connect('anbar.db')
        conn.execute("insert into product(p_id, p_name, p_serial, p_comment)values({},'{}', {}, '{}')".format(ID, name, serial, comment))
        conn.commit()
        print("Product added Successfully")
        conn.close()









