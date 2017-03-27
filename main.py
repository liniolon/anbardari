# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Imports needs library :D
import sqlite3
import os

from datetime import datetime
from admin import Admin, Product
from getpass import getpass


#def AdminDatabase():
#    db = Admin.CreateDatabaseClerk()
#    db = Admin.CreateTableClerk()

def AdminInsertClerk():
    ID = int(input("Enter ID for CLERK: "))
    name = str(input("Enter NAME of CLERK: "))
    password = getpass("Enter password: ")
    is_admin = int(input("Is ADMIN? (0=No, 1=Yes): "))

    insert = Admin.InsertClerk(ID,name, password,is_admin)

def AdminDeleteClerk():
    ID = int(input("Enter ID for CLERK: "))
    delete = Admin.DeleteClerk(ID)

def AdminUpdateClerk():
    ID = int(input("Enter ID for update: "))
    name = str(input("Enter NEW FULLNAME for CLERK: "))
    password = getpass("Enter password: ")
    is_admin = int(input("Is Admin? (0=No, 1=Yes):  "))

    update = Admin.UpdateClerk(ID,name, password,is_admin)

def AdminSearchClerk():
    ID = int(input("Enter an ID for Search: "))

    search = Admin.Search(ID)

def AdminShowAllClerk():
    show = Admin.ShowAll()

def ProductCreateTable():
    table = Product.CreateDatabaseProduct()
    table = Product.CreateTableProduct()

def ProductInsert():
    insert = Product()


    ID = int(input("Enter an ID for product: "))
    name = str(input("Enter a NAME for product: "))
    serial = int(input("Enter SERIAL code: "))
    comment = str(input("Enter COMMENT for product: "))
    insert.InsertProduct(ID, name, serial, comment)

def ProductDelete():
    delete = Product()
    ID = int(input("Enter an ID for delete: "))

    delete.DeleteProduct(ID)

def ProductUpdate():

    ID = int(input("Enter an ID for product: "))
    name = str(input("Enter a new NAME for product: "))
    serial = int(input("Enter new SERIAL code: "))
    comment = str(input("Enter new COMMENT for product: "))

    update = Product.UpdateProduct(name, serial, comment, ID)

def SearchProduct():
    ID = int(input("Enter an ID for SEARCH: "))

    search = Product.SearchProduct(ID)

def ShowProduct():
    show = Product.ShowAll()


def main():

#    os.system('if [ ! -f anbar.db ];then{}Do you want to create admin?{};fi'.format(AdminDatabase, AdminInsertClerk()))
    conn = sqlite3.connect('anbar.db')
    _user =  conn.execute('select fullname, password, is_admin from clerk')
    print("##### Login To 'Storage Software' #####\n")
    username = str(input("Enter Username: "))
    password = getpass("Enter password: ")
    for data in _user:
        if username == data[0] and password == data[1] and data[2] == 1:
            print("Login Successfully")
            while True:
                work = int(input("""
######## Admin Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
##################################
>>>"""))
                if work == 1:
                    os.system('clear')
                    userWork = int(input("""
######### Admin Panel Area | Users Managment ########
List Of Works:
    0. Create Database and Tables (Just use for once!)
    1. Insert User
    2. Delete User
    3. Update User
    4. Search User BY ID
    5. Show All Users
    6. Back
    7. Exit
#####################################################
>>>"""))
                    if userWork == 1:
                        AdminInsertClerk()
                        userWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 0:
                        AdminDatabase()
                        serWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 2:
                        AdminDeleteClerk()
                        userWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 3:
                        AdminUpdateClerk()
                        userWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 4:
                        AdminSearchClerk()
                        userWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 5:
                        AdminShowAllClerk()
                        userWork = int(input("Do yout want to do something? (Exit = 7) "))
                    elif userWork == 6:
                        work = int(input("""
######## Admin Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
##################################
    >>>"""))
                    elif userWork == 7:
                        print("Good Bye")
                        os.system('sleep 2')
                        break
                    else :
                        userWork = int(input("Out of range. Try again: "))
                elif work == 2:
                    Pwork = int(input("""
######## Admin Panel Area | Products ########
List of Works:
    0. Create Database and Tables (Just user once!)
    1. Insert Product
    2. Delete Product
    3. Update Product
    4. Search In product with ID
    5. Show All
    6. Back
    7. Exit
#############################################
>>>"""))
                    if Pwork == 1:
                        ProductInsert()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif Pwork == 2:
                        ProductDelete()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif Pwork == 3:
                        ProductUpdate()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif Pwork == 4:
                        SearchProduct()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif Pwork == 5:
                        ShowProduct()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif Pwork == 6:
                        work = int(input("""
######## Admin Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
##################################
>>>"""))
                    elif Pwork == 7:
                        print("Good Bye")
                        os.system('sleep 2')
                        break
                    elif Pwork == 0:
                        ProductCreateTable()
                        Pwork = int(input("Do you want to continue? (Exit = 7)"))
                    else :
                        Pwork = int(input("Out of range. Try Again: "))
                elif work == 3:
                    print("Good Bye")
                    os.system('sleep 2')
                    break

        elif username == data[0] and password == data[1] and data[2] == 0:
                print("Welcome :D")

                Uwork = int(input("""
######## User Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
#################################
>>>"""))
                if Uwork == 1:
                    UUwork = int(input("""
######## User Panel Admin | Users ########
List Of Works:
    1. Search User by ID
    2. Back
    3. Exit
##########################################
                    """))
                    if UUwork == 1:
                        AdminSearchClerk()
                        UUwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UUwork == 2:
                        Uwork = int(input("""
######## User Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
#################################
>>>"""))
                    elif UUwork == 3:
                        print("Good Bye")
                        os.system('sleep 2')
                        break
                elif Uwork ==2 :
                    UPwork = int(input("""
######## User Panel Area | Products ########
List of Works:
    1. Insert Product
    2. Delete Product
    3. Update Product
    4. Search In product with ID
    5. Show All
    6. Back
    7. Exit
#############################################
                    """))
                    if UPwork == 1:
                        ProductInsert()
                        UPwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UPwork == 2:
                        ProductDelete()
                        UPwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UPwork ==3:
                        ProductDelete()
                        UPwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UPwork == 4:
                        SearchProduct()
                        UPwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UPwork == 5:
                        ShowProduct()
                        UPwork = int(input("Do you want to continue? (Exit = 7)"))
                    elif UPwork == 6:
                        Uwork = int(input("""
######## User Panel Area ########
List Of Works:
    1. Users
    2. Products
    3. Exit
#################################
>>>"""))
                    elif UPwork == 7:
                        print("Good Bye")
                        os.system('sleep 2')
                        break
                    else:
                        UPwork = int(input("Out of range.Try again: "))
                elif Uwprk == 3:
                    print("Good Bye")
                    os.system('sleep 2')
                    break


if __name__ == '__main__':
    main()
