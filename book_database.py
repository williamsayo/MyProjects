import sqlite3

conn = sqlite3.Connection('bookstore.sqlite3')
cur = conn.cursor()

cur.execute('create table books(id integer primary key,title varchar(50) not null,author varchar(50),year date,isbn varchar(30))')

conn.close