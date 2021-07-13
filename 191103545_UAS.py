#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Program konversi suhu , dari Celcius , F

suhu_c = float(input('Masukan suhu dalam celcius  '))

suhu_f =(9./5)* suhu_c + 32

suhu_r = (4./5)* suhu_c

print("suhu celcius adalah :  %f" % (suhu_c))
print("suhu fahrenheit adalah : %2f " % (suhu_f))
print("suhu reamur adalah : %f " % (suhu_r))


# In[26]:


import mysql.connector

db = mysql.connector.connect(
     host ="localhost",
     user ="root",
     passwd = ""
)

if db.is_connected():
    print("Berhasil terbung ke database")


# In[27]:


import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")

print("Database berhasil dibuat!")


# In[37]:


import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="db_film"
)

cursor = db.cursor()
sql = """CREATE TABLE tbl_film (
  Kode_id INT AUTO_INCREMENT PRIMARY KEY,
  Judulfilm VARCHAR (255),
  Jenis_film VARCHAR (255)
)
"""
cursor.execute(sql)

print("Tabel film berhasil dibuat!")


# In[40]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tbl_film (Judulfilm, Jenis_film) VALUES (%s, %s)"
val = ("X-Men: Dark Phoenix", "Action")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[43]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tbl_film (Judulfilm, Jenis_film) VALUES (%s, %s)"
values = [
    ("Aladin","Fantasy"),
    ("Godzilla II : King of the Monsters","Fantasy"),
    ("John Wick: Chapter 3 - Parabellum","Action"),
    ("Stand by me 2","Animation")
]

for val in values:
    cursor.execute(sql,val)
    db.commit()
    
print("{} data ditambahkan".format(len(values)))


# In[51]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)
cursor= db.cursor()
sql = "SELECT * FROM tbl_film"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)


# In[53]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)
cursor= db.cursor()
sql= "SELECT * FROM tbl_film"
cursor.execute(sql)

result = cursor.fetchone()

print(result)


# In[63]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)
cursor= db.cursor()
sql = "UPDATE tbl_film SET Judulfilm=%s, Jenis_film=%s WHERE Kode_id=%s"
val = ("X-Men: Dark Phoenix", "Comedy Action",3)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))


# In[65]:


import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)
cursor= db.cursor()
sql = "Delete FROM tbl_film WHERE Kode_id=%s"
val = (4,)
cursor.execute(sql,val)

db.commit()

print("{} data di hapus".format(cursor.rowcount))


# In[67]:


import mysql.connector
import os

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="",
   database="db_film"
)
cursor= db.cursor()
keyword = input ("Kata kunci: ")
sql= "SELECT * FROM tbl_film WHERE Judulfilm LIKE %s OR Jenis_film LIKE %s"
val = ("%{}%".format(keyword),"%{}%".format(keyword))
cursor.execute(sql,val)
results = cursor.fetchall()

if cursor.rowcount < 0:
    print("Tidak ada data")
else:
    for data in results :
        print (data)


# In[ ]:




