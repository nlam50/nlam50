#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

with open("courses.csv", "r") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        c.execute("INSERT INTO courses (code, mark, id) VALUES (?, ?, ?);", (row['code'], row['mark'], row['id']))
        #print(row['code'], row['mark'], row['id'])

#csv.DictReader() makes a dictionary out of a csv file


#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
