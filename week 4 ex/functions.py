import csv
import sys
import os


#####################################################################################
def creat_products_file():
    lists=[]
    with open('products_list.csv','r') as f:
        thereader = csv.DictReader(f)
        for p in thereader :
            lists.append (p)
        return lists
products_list = creat_products_file()


 ########################### VIEW PRODUCTS LIST ####################################

def view_products():
   for index,value in enumerate(products_list):
        print(index,value)

########################### CREAT NEW PRODUCTS  ####################################

productsheads= ['PRODUCT','PRICE']
def add_new_product():
    product = input('PLEASE TYPE PRODUCT NAME: ')
    price =float(input('WHAT IS THE PRODUCT PRICE?:'))
    product_dict = {'PRODUCT':product,'PRICE':price }
    products_list.append(product_dict)
    with open ('products_list.csv','w', newline='') as p:
        writer= csv.DictWriter(p,fieldnames = productsheads)
        writer.writeheader()
        for p in products_list:
            writer.writerow(p)

########################### CREAT NEW PRODUCTS  ####################################

def updat_existing_product():
    view_products()
    product_change = int(input('which pro u want to update:'))
    result = products_list[product_change]
    for key,value in result.items():
        print(f'{key},{value}')
        update_product=input('what is the new product:')
        if update_product !='':
            result[key]= update_product
    view_products()


########################### DELETE PRODUCT  ####################################

def delete_product():
    view_products()
    
    product_change = int(input('WHICH PRODUCT YOU WANT TO DELETE?:'))
    del products_list[product_change]
    
    view_products()

############################## CREAT CSV FILE FOR  COURIERS ########################################
def creat_couriers_file():
    lists=[]
    with open('couriers_list.csv','r') as f:
        thereader = csv.DictReader(f)
        for p in thereader :
            lists.append (p)
        return lists
courier_list = creat_couriers_file()

 ########################### VIEW COURIERS LIST ####################################

def view_couriers():
    for index,value in enumerate(courier_list):
        print(index,value)

########################### CREAT NEW COURIERS  ####################################

couriersheads= ['NAME','PHONE']
def add_new_courier():
    name = input('PLEASE TYPE COURIER NAME: ')
    phone =int(input('WHAT IS THE COURIER PHONE NUMBER ?:'))
    courier_dict = {'NAME':name,'PHONE': phone }
    courier_list.append(courier_dict)
    with open ('couriers_list.csv','w', newline='') as p:
        writer= csv.DictWriter(p,fieldnames = couriersheads)
        writer.writeheader()
        for p in courier_list:
            writer.writerow(p)


########################### CREAT NEW COURIER  ####################################

def updat_existing_courier():
    view_couriers()
    courier_change = int(input('WHICH COURIER YOU WANT TO UPDATE?:'))
    result = courier_list[courier_change]
    for key,value in result.items():
        print(f'{key},{value}')
        update_courier=input('eNTER THE COURIER INFO :')
        if update_courier !='':
            result[key]= update_courier
    view_couriers()


# ########################### DELETE COURIERS  ####################################

def delete_courier():
    view_couriers()
    
    courier_change = int(input('WHICH COURIER YOU WANT TO DELETE?:'))
    del courier_list[courier_change]
    
    view_couriers()

############################## CREAT CSV FILE FOR  ORDERS ########################################
def creat_orders_file():
    lists=[]
    with open('orders_file.csv','r') as f:
        thereader = csv.DictReader(f)
        for p in thereader :
            lists.append (p)
        return lists
orders_list = creat_orders_file()

 ########################### VIEW ORDERS LIST ####################################

def view_orders():
    for index,value in enumerate(orders_list):
        print(index,value)

########################### CREAT NEW ORDER  ####################################

ordersheads= ['CUSTOMER NAME','CUSTOMER ADDRESS','CUSTOMER PHONE NO','COURIER','ORDER STATUS']
def add_new_order():
    name = input('PLEASE TYPE CUSTOMER NAME: ')
    address = input('PLEASE TYPE THE CUSTOMER ADDRESS:')
    phone =int(input('WHAT IS THE CUSTOMER PHONE NUMBER ?:'))
    view_couriers()
    courier_option = int(input('WHICH COURIER YOU WANT TO SELECT?:'))
    result = courier_list[courier_option]
    for key,value in result.items():
        print(f'{key},{value}')
    courier = result
    status = 'preparing'
    order_dict = {'CUSTOMER NAME':name,'CUSTOMER ADDRESS': address,'CUSTOMER PHONE NO':phone,'COURIER':result,'ORDER STATUS':status }
    orders_list.append(order_dict)
    with open ('orders_file.csv','w', newline='') as o:
        writer= csv.DictWriter(o,fieldnames = ordersheads)
        writer.writeheader()
        for o in orders_list:
            writer.writerow(o)


########################### UPDATE ORDER  ####################################

def updat_existing_order():
    view_orders()
    orders_change = int(input('WHICH ORDER YOU WANT TO UPDATE?:'))
    result = orders_list[orders_change]
    for key,value in result.items():
        print(f'{key},{value}')
        update_orders =input('ENTER THE ORDERS INFO :')
        if update_orders !='':
            result[key]= update_orders
    view_orders()


# ########################### DELETE ORDERS  ####################################

def delete_orders():
    view_orders()
    
    orders_change = int(input('WHICH ORDER YOU WANT TO DELETE?:'))
    del orders_list[orders_change]
    
    view_orders()













#                         ##### Read the csv couriers file ######
# def open_couriers():
#     try:
#         with open('couriers_list.csv') as c:
#             data = csv.reader(c)
#             for r in (data):
#                 print(r)
#     except Exception as e:
#         print('An error occured: ' + str(e))
#     print('Exiting App')

#                 ######## Read the orders csv file  #########
# def open_orders():
#     try:
#         with open('orders_file.csv') as o:
#             data = csv.reader(o)
#             for r in (data):
#                 print (r)
#     except Exception as e:
#         print('An error occured: ' + str(e))
#     print('Exiting App')
          
# #             ######### ORDERS STATUS LIST ###########

# def order_status_list():
#      order_status = ["Preparing","On it's Way","Deliverd"]
#      for index,value in enumerate(order_status):
#         print(index,value)
     


############################ Save ########################
# def save_file (couriers_list, header, new_list):
#     with open (couriers_list, 'w', newline='') as outfile:
#         writer = csv.DictWriter(outfile,fieldnames=header)
#         writer.writeheader()
#         for dict in new_list:
#             writer.writerow(dict)














# import csv

# def products_reader():
#     with open ('products_list.csv', 'r' ) as products:
#         csv_reader = csv.reader(products)
#         for line in csv_reader:
#             print (line)
# products_reader()






#### need to def a func to update an existing product 







#### need to def a dele 

# def delete_product():
#     view_products()
#     with open ('products_list.csv', newline='') as file:
#         row = ["product","price"]
#         writer = csv.DictWriter(file,fieldnames=row)
#         d = input('Select a product to delete:')
#         for line in product_list:
#             line.remove(d)
#     view_products

# # for row in csvreader:
# #         rows.remove(row)
