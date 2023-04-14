# import mysql.connector as ms

# # establishing connection
# db = ms.connect(host = 'localhost',user = 'shevil',passwd = 'shevil',database = 'library')
# cur = db.cursor()
# cur.execute('create database if not exists library')
# cur.execute('use library')
# cur.execute('create table if not exists book (book_id int primary key, book_name varchar(50),book_price float,genre varchar(20),qty int check (qty>=0))')
# cur.execute('create table if not exists customers (order_id int primary key, customer_name varchar(50),book_id int, book_name varchar(50),book_price float,qty int check (qty>0),total float)')
