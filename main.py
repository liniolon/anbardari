# -*- coding: utf-8 -*-
#!/usr/bin/env python 

# Imports needs library :D 
import sqlite3 
import os 

from datetime import datetime 
from admin import Admin

def AdminDatabase():
    db = Admin()
    db.CreateTableClerk()

def AdminInsertClerk():
    ID = int(input("Enter ID for CLERK: "))
    name = str(input("Enter NAME of CLERK: "))
    is_admin = int(input("Is ADMIN? (0=No, 1=Yes): "))

    insert = Admin.InsertClerk(ID,name,is_admin)

def AdminDeleteClerk():
    ID = int(input("Enter ID for CLERK: "))
    delete = Admin.DeleteClerk(ID)

def AdminUpdateClerk():
    ID = int(input("Enter ID for update: "))
    name = str(input("Enter NEW FULLNAME for CLERK: "))
    is_admin = int(input("Is Admin? (0=No, 1=Yes):  "))

    update = Admin.UpdateClerk(ID,name,is_admin)

def AdminSearchClerk():
    ID = int(input("Enter an ID for Search: "))

    search = Admin.Search(ID)

def AdminShowAllClerk():
    show = Admin.ShowAll()


def main():
    
    while operate != 7:
        operate = int(input("""
#### Storage Software ####
List Of Operations: 
    1. Create Database and Tables 
    2. Insert A NEW CLERK 
    3. Delete A CLERK 
    4. Update A CLERK
    5. Search CLERK from database 
    6. Show ALL 
    7. Exit 
Enter number>>>"""))
        if operate == 1:
            AdminDatabase()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 2: 
            AdminInsertClerk()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 3: 
            AdminDeleteClerk()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 4: 
            AdminUpdateClerk()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 5:
            AdminSearchClerk()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 6: 
            AdminShowAllClerk()
            operate = int(input("Do you wan't to Quite? (press=7) "))
        elif operate == 7:
            print("Bye")
            os.system('sleep 2')
            break



if __name__ == '__main__':
    main()


