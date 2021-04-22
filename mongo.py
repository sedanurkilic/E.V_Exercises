# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 02:39:15 2021

@author: X1
"""

from pymongo import MongoClient
host="localhost"
port=27017
db="examples"
connection=MongoClient(host,port)
try:
    db=connection[db]
except:
    print("disconnect to database")
collection=db['staff']
def menu():
    print("""
          Menu
          ----
          1-list
          2-add
          3-search
          4-delete
          5-update
          6-exit
          """)
def list():
    result=collection.find()
    for item in result:
        print(item["staff_number"],item["name"],item["surname"])
def add():
    staff_number=int(input("Please enter a number"))
    name=input("Please enter a name")
    surname=input("Please enter a surname")
    register=collection.insert_one({"staff_number":staff_number,"name":name,"surname":surname})
    list()
def search():
    no=int(input("Please enter a number"))
    result=collection.find({"staff_number":no})
    for item in result:
         print(item["staff_number"],item["name"],item["surname"])
def delete():
    no=int(input("Please enter a number"))
    result=collection.delete_one({"staff_number":no})
    list()
def update():
    no=int(input("Please enter a number"))
    result=collection.find({"staff_number":no})
    name=input("Please enter name")
    surname=input("Please enter surname")
    result=collection.update_one({"staff_number":no},{"$set":{"name":name,"surname":surname}})
    list()
while True:
    menu()
    choice=input("Please select operations")
    if choice=="1":
        list()
        continue
    if choice=="2":
        add()
        continue
    if choice=="3":
        search()
        continue
    if choice=="4":
        delete()
        continue
    if choice=="5":
        update()
        continue
    if choice=="6":
        break
    