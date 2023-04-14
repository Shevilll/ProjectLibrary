# ProjectLibrary
Library Management System

A Python based library management system, made for school project


Connection:
    username
    password


Tables:
    1. Books
    2. Customers


Menu:
    1. Add book
    2. Remove book
    3. Check Book's Details
    4. customers
    5. selling purchasing
    6. sql conncections


Book: 
    book_id : int,primary key
    book_name : varchar(50)
    book_price : float
    genre : varchar
    qty : int check qty>=0


Customers:
    order_id : int,primary key
    customer_name : varchar(50)
    book_id : int
    book_name : implemented from book
    book_price : implemented from book
    qty : int check qty >=0
    total : float

