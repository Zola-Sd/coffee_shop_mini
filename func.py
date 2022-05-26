import csv
import sys
import pymysql
import os
from setuptools import Command
import pandas as pd
from dotenv import load_dotenv


def connect_order_statusdb():# function that connect order status to the database 
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM order_status"
    cursor.execute(command)
    
    connection.commit()
    cursor.fetchall()
    cursor.close()
    connection.close()

order_status_list = connect_order_statusdb()

def view_order_status(): # function that view order status table from the data base
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM order_status"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    tup = list(result)
    for i in tup:
       print(i)

    cursor.close()
    connection.close()

def add_new_order_statusdb(): # function that add new order status
    status_input= input('PLEASE TYPE ORDER STATUS: ')
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f"INSERT INTO order_status(order_stat) VALUES (\'{status_input}\')"

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()

def delete_order_statusdb(): # function that delete from the order status table
    view_order_status()
    id = int(input('PLEASE ENTER THE NUMBER OF THE STATUS YOU WANT TO DELETE:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f'DELETE FROM order_status WHERE id = {id}' 

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()

####################################################################################################################

def connect_productdb(): # function that connect product to the database
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM products"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    #for i in result:
       # print(i,'\n')
    cursor.close()
    connection.close()
    
product_list = connect_productdb()

def view_products(): # function that view products table from the data base
    
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM products"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    tup = list(result)
    for value in tup:
       print(value)

    cursor.close()
    connection.close()

def add_new_productdb(): #function that add new products
    product= input('PLEASE TYPE PRODUCT NAME: ')
    price =float(input('WHAT IS THE PRICE OF THE PRODUCT?:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f"INSERT INTO products (products_name,price) VALUES (\'{product}\',{price})"

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()

def update_existing_productdb(): # function that update existing product
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    command = "SELECT * FROM products"
    cursor.execute(command)
    connection.commit()
    cursor.fetchall()
    view_products()
    items_id = int(input("PLEASE ENTER THE NUMBER OF THE SELECTED PRODUCT FROM THE LIST ABOVE:"))
    options = ["products_name","price"]
    for index,value in enumerate(options):
        print(index,value)
    chosen = int(input("PLEASE INPUT THE NUMBER OF WHAT YOU WOULD LIKE TO CHANGE FROM THE LIST ABOVE( ENTER 0 FOR PRODUCT NAME - ENTER 1 FOR PRICE): "))
    if chosen == 0:
       products_name= input("PLEASE TYPE THE NAME OF THE PRODUCT YOU WANT TO CHANGE: ").capitalize()
       updated_products_name = input("WHAT IS THE NAME OF THE NEW PRODUCT?: ").capitalize()
       change ="UPDATE products SET products_name = \'{updated_products_name}\' WHERE products_name =\'{products_name}\';"
       val = (updated_products_name,products_name)
       cursor.execute(change,val)
       connection.commit()
       print(cursor.rowcount, "record updated.")
    elif chosen == 1:
        price = float(input("WHAT IS THE PRICE OF THE NEW PRODUCT?: "))
        change =f"UPDATE products SET price = {price} WHERE items_id = {items_id}"
        cursor.execute(change)
        connection.commit()
        print(cursor.rowcount, "record updated.")
    cursor.close()
    connection.close()

def delete_productdb(): # function that delete products
    view_products()
    items_id = int(input('PLEASE ENTER THE NUMBER OF THE PRODUCT YOU WANT TO DELETE:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f'DELETE FROM products WHERE items_id = {items_id}' 

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()
    
def export_products_to_csv(): # function that export products table from the database to a csv file
    # Establish a database connection
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    sql_query = "SELECT * FROM products;" # here, the 'conn' is the variable that contains your database connection information from step 2
    df = pd.read_sql(sql_query,connection)
    df.to_csv (r'C:\Users\User\Documents\coffee_shop_mini\week 4\products_list.csv', index = False) # place 'r' before the path name
    print("File has been exported as csv file to selected location!")
    cursor.close()
    connection.close()

####################################################################################################################
def connect_courierdb(): # function that connect couriers to the database
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM couriers"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    cursor.close()
    connection.close()

courier_list = connect_courierdb()

def view_courier(): # function that view products table from the data base
    
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM couriers"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    tup = list(result)
    for value in tup:
       print(value)
    cursor.close()
    connection.close()

def add_new_courierdb(): #function that add new courier
    courier_name= input('PLEASE TYPE COURIER NAME: ')
    courier_phone_no =int(input('WHAT IS THE COURIER PHONE NUMBER ?:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f"INSERT INTO couriers (courier_name,courier_phone_no) VALUES (\'{courier_name}\',{courier_phone_no})"

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()

def update_existing_courierdb(): # function that update existing courier
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    command = "SELECT * FROM couriers"
    cursor.execute(command)
    connection.commit()
    cursor.fetchall()
    view_courier()
    courier_id = int(input("PLEASE ENTER THE NUMBER OF THE SELECTED COURIER FROM THE LIST ABOVE:"))
    options = ["courier_name","courier_phone_no"]
    for index,value in enumerate(options):
        print(index,value)
    chosen = int(input("PLEASE INPUT THE NUMBER OF WHAT YOU WOULD LIKE TO CHANGE FROM THE LIST ABOVE( ENTER 0 FOR COURIER NAME - ENTER 1 FOR COURIER PHONE NUMBER): "))
    if chosen == 0:
       courier_name= input("PLEASE TYPE THE NAME OF THE COURIER YOU WANT TO CHANGE: ").capitalize()
       updated_courier_name = input("WHAT IS THE NAME OF THE NEW COURIER?: ").capitalize()
       change ="UPDATE couriers SET courier_name = %s WHERE courier_name = %s"
       val = (updated_courier_name,courier_name)
       cursor.execute(change,val)
       connection.commit()
       print(cursor.rowcount, "record updated.")
    elif chosen == 1:
        updated_courier_phone_no = int(input("WHAT IS THE PHONE NUMBER FOR THE COURIER ?: "))
        change =f"UPDATE couriers SET courier_phone_no = {updated_courier_phone_no} WHERE courier_id = {courier_id}"
        cursor.execute(change)
        connection.commit()
        print(cursor.rowcount, "record updated.")
    cursor.close()
    connection.close()

def delete_courierdb(): # function that delete courier
    view_courier()

    courier_id = int(input('WHICH COURIER YOU WANT TO DELETE?:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f'DELETE FROM couriers WHERE courier_id = {courier_id}' 

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()
    
def export_couriers_to_csv(): # function that export couriers table from database to a csv file
    # Establish a database connection
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    sql_query = "SELECT * FROM couriers;" # here, the 'conn' is the variable that contains your database connection information from step 2
    df = pd.read_sql(sql_query,connection)
    df.to_csv (r'C:\Users\User\Documents\coffee_shop_mini\week 4\couriers_list.csv', index = False) # place 'r' before the path name
    print("File has been exported as csv file to selected location!")
    cursor.close()
    connection.close()

####################################################################################################################

def connect_orderdb(): # function that conect orders to database
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM orders"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    cursor.close()
    connection.close()
    
orders_list = connect_orderdb()

def view_orders(): # function that view orders table
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = "SELECT * FROM orders"
    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    tup = list(result)
    for value in tup:
       print(value)
    cursor.close()
    connection.close()

def add_new_orderdb(): # function that add new order
    customer_name = input('PLEASE TYPE CUSTOMER NAME: ')
    customer_address = input('PLEASE TYPE THE CUSTOMER ADDRESS:')
    customer_phone_no =(input('WHAT IS THE CUSTOMER PHONE NUMBER ?:'))
    view_courier()
    courier_id = int(input('WHICH COURIER YOU WANT TO SELECT?:'))
    order_status = "Prepared" 
    view_products()
    items_id = input("WHICH ITEMS YOU NEED TO ADD TO THIS ORDER?\n")
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f"INSERT INTO orders (customer_name,customer_address,customer_phone_no,courier_id,order_status,items_id) VALUES (\'{customer_name}\',\'{customer_address}\',{customer_phone_no},{courier_id},\'{order_status}\',\'{items_id}\')"

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()

def update_existing_orderdb(): # function that update existing order
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    command = "SELECT * FROM orders"
    cursor.execute(command)
    connection.commit()
    cursor.fetchall()
    view_orders()
    order_id = int(input("PLEASE ENTER THE NUMBER OF THE SELECTED ORDER FROM THE LIST ABOVE:")) # select the order id
    customer_name= input("PLEASE TYPE THE NAME OF THE CUSTOMER : ").capitalize()
    customer_address= input("PLEASE TYPE THE CUSTOMER ADDRESS: ").capitalize()
    customer_phone_no = input("PLEASE TYPE THE CUSTOMER PHONE NUMBER: ").capitalize()
    view_courier()
    cour_qur = "SELECT * FROM couriers;" # view the couriers table from the database
    cursor.execute(cour_qur)
    connection.commit()
    courier_list= cursor.fetchall()
    courier_id =int(input("PLEASE SELECT FROM THE LIST ABOVE WHICH COURIER YOU WANT TO ASSIGN ?"))
    view_products()
    prod_qur= "SELECT * FROM products;"
    cursor.execute(prod_qur)
    connection.commit()
    product_list= cursor.fetchall()
    items_id = input("PLEASE SELECT THE ITEMS FROM THE LIST ABOVE")
    view_order_status()
    updated_status_id = input("PLEASE SELECT THE ORDER STATUS FROM THE LIST ABOVE")
    if updated_status_id == 1:
        updated_status_id = "Confirmed"
    elif updated_status_id == 2:
        updated_status_id = "preparing"
    elif updated_status_id == 3:
        updated_status_id = "Out for Delivery"
    elif updated_status_id == 4:
        updated_status_id = "Deliverd"   

    command = f"UPDATE orders SET customer_name =\'{customer_name}\' , customer_address = \'{customer_address}\', customer_phone_no =\'{customer_phone_no}\', courier_id =\'{courier_id}\', order_status ={updated_status_id}, items_id = \'{items_id}\' WHERE order_id = {order_id};"
    cursor.execute(command)
    connection.commit()
    cursor.close()
    connection.close()

def delete_ordersdb(): # function that delete orders
    view_orders()
    order_id = int(input('WHICH ORDER YOU WANT TO DELETE?:'))
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    command = f'DELETE FROM orders WHERE order_id = {order_id}' 

    cursor.execute(command)
    
    connection.commit()
    result= cursor.fetchall()
    for i in result:
        print(i,'\n')
    cursor.close()
    connection.close()
    
def export_orders_to_csv(): # function that export orders table from database to a csv file 
    # Establish a database connection
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    # Add code here to insert a new record
    sql_query = "SELECT * FROM orders;" # here, the 'conn' is the variable that contains your database connection information from step 2
    df = pd.read_sql(sql_query,connection)
    df.to_csv (r'C:\Users\User\Documents\coffee_shop_mini\week 4\orders_list.csv', index = False) # place 'r' before the path name
    print("File has been exported as csv file to selected location!")
    cursor.close()
    connection.close()





