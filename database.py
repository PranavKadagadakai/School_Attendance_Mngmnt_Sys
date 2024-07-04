import mysql.connector as a
con= a.connect(host='localhost',password='Jeeshan@87867',user='root')

#create cursor
c=con.cursor()
c.execute('create database if not exist AMS')
c.execute('use AMS')

#Table Creation
