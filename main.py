import mysql.connector as ms

def connect():
    global db, cur
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    try:
        db = ms.connect(host="localhost", user=username, passwd=password)
        cur = db.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS library")
        cur.execute("USE library")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS book (book_id INT PRIMARY KEY, book_name VARCHAR(50),book_price FLOAT,genre VARCHAR(20),qty INT CHECK (qty>=0))"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS customers (order_id INT PRIMARY KEY, customer_name VARCHAR(50),book_id INT, book_name VARCHAR(50),book_price FLOAT,qty INT ChECK (qty>0),total FLOAT)"
        )

    except:
        print("Connection Failed. Username/Password Error\nTry again!")
        return False
    return True


def addbook():
    book_id = int(input("Enter Book ID: "))
    cur.execute(f"SELECT * FROM book WHERE book_id = {book_id}")
    ch = cur.fetchall()
    if ch:
        print("Book already exists in the Library!")
        k = input("Update Details? (y\\n) ")
        while k not in ("y", "n"):
            k = input("Update Details? (y\\n) ")
        if k == "n":
            return None
        qty = int(input("Enter Quantity: "))
        book_name = input("Enter Book Name: ")
        book_price = float(input("Enter Book Price: ₹"))
        genre = input("Enter Genre: ")
        cur.execute(
            f"UPDATE book SET qty = {qty},book_name = '{book_name}',book_price = {book_price},genre = '{genre}' WHERE book_id = {book_id}"
        )
        db.commit()
        print("Details Updated!")
        return None
    book_name = input("Enter Book Name: ")
    book_price = float(input("Enter Book Price: ₹"))
    genre = input("Enter Genre: ")
    qty = int(input("Enter Quantity: "))
    cur.execute(
        f"INSERT INTO book VALUES ({book_id},'{book_name}',{book_price},'{genre}',{qty})"
    )
    db.commit()


def removebook():
    book_id = int(input("Enter Book ID: "))
    cur.execute(f"SELECT * FROM book WHERE book_id = {book_id}")
    txt = cur.fetchall()
    if not txt:
        print("Book does not exists in Library!")
        return None
    for i in txt:
        print(f"Book Removed: {i}")
    cur.execute(f"DELETE FROM book WHERE book_id = {book_id}")
    db.commit()


def showbooks():
    cur.execute("SELECT * FROM book")
    print(
        f"{'-Book ID-':10} || {'-------Book Name-------':25} || {'-Book Price-':8} || {'-------Genre-------':20} || {'-Quantity-':>5}"
    )
    txt = cur.fetchall()
    for i in txt:
        print(f"{i[0]:10} || {i[1]:25} || {i[2]:12} || {i[3]:20} || {i[4]:>5}")


def sellbook():
    order_id = int(input("Enter Order ID: "))
    cur.execute(f"SELECT * FROM customers WHERE order_id = {order_id}")
    k = cur.fetchall()
    if k:
        print("Order ID already exists!")
        opt = input("Update Details? (y/n)")
        while opt not in ("y", "n"):
            opt = input("Update Details? (y/n)")
        if opt == "n":
            return None
        updating(order_id)
        return None
    book_id = int(input("Enter Book ID: "))
    cur.execute(f"SELECT * FROM book WHERE book_id = {book_id}")
    ch = cur.fetchall()
    if not ch:
        print("Book is not available in library!")
        return None
    qty = int(input("Enter Quantity: "))
    if qty > ch[0][4]:
        print(f"Sorry only {ch[0][4]} books are available.")
        return None
    c_name = input("Enter Customer Name: ")
    cur.execute(
        f'INSERT INTO customers VALUES ({order_id},"{c_name}",{ch[0][0]},"{ch[0][1]}",{ch[0][2]},{qty},{ch[0][2]*qty})'
    )
    cur.execute(f"UPDATE book SET qty = qty-{qty} WHERE book_id = {book_id}")
    db.commit()


def updating(order_id):
    book_id = int(input("Enter Book ID: "))
    cur.execute(f"SELECT * FROM book WHERE book_id = {book_id}")
    ch = cur.fetchall()
    if not ch:
        print("Book is not available in library!")
        return None
    qty = int(input("Enter Quantity: "))
    if qty > ch[0][4]:
        print(f"Sorry only {ch[0][4]} books are available.")
        return None
    c_name = input("Enter Customer Name: ")
    cur.execute(
        f'UPDATE customers SET customer_name = "{c_name}",book_name = "{ch[0][1]}",book_price = {ch[0][2]},qty = {qty},total = {ch[0][2]*qty} WHERE order_id = {order_id}'
    )
    db.commit()


def customers():
    cur.execute("SELECT * FROM customers")
    print(
        f"{'-Order ID-':10} || {'---Customer Name---':20} || {'-Book ID-':10} || {'------Book Name------':25} || {'-Book Price-':5} || {'Quantity':5} || {'Total':>5}"
    )
    txt = cur.fetchall()
    for i in txt:
        print(
            f"{i[0]:10} || {i[1]:20} || {i[2]:10} || {i[3]:25} || {i[4]:12} || {i[5]:8} || {i[6]:>5}"
        )


try:
    if __name__ == "__main__" and connect():
        while True:
            print("-" * 20)
            print(
                "1. Add Book\n"
                "2. Remove Book\n"
                "3. Check Book's Details\n"
                "4. Check Customers Details\n"
                "5. Sell Book\n"
                "6. Exit"
            )
            print("-" * 20)
            ch = int(input("Enter Your Choice (1-6): "))
            if ch == 1:
                addbook()
            elif ch == 2:
                removebook()
            elif ch == 3:
                showbooks()
            elif ch == 4:
                customers()
            elif ch == 5:
                sellbook()
            elif ch == 6:
                break
            else:
                print("Wrong Choice")
    print("Thankyou!")
except:
    print("Some Error Occurred. Try again!")
