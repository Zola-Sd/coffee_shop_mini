import csv
import sys 
from func import *
#from couriers_func import *
#from orders_func import *

######################### ORDER STATUS MENU ##############################

def order_status_menu():
    print("~~~~~ ORDERS STATUS MENU ~~~~~")
    print(" ##### WARNING THIS MENU IS FOR ADMIN USE ONLY ##### ")
    print("PLEASE NOTE THAT THIS LIST IS FOR ADMIN USE ONLY ")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    orders_status_options= ['0/ RETURN TO MAIN MENU','1/ VIEW ORDER STATUS LIST','2/ ADD NEW ORDER STATUS','3/ DELETE ORDER STATUS']
    for i in orders_status_options:
        print(i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_order_status()
        order_status_menu()
    elif user_option == 2:
        add_new_order_statusdb()
        view_order_status()
        order_status_menu()
    elif user_option == 3:
        delete_order_statusdb()
        view_order_status()
        order_status_menu()
    

# ######################## PRODUCTS MENU FUNCTIONS ########################


def product_menu():   
    print("~~~~~ PRODUCTS MENU ~~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    products_options= ['0/ RETURN TO MAIN MENU', '1/ VIEW PRODUCTS', '2/ ADD NEW PRODUCT', '3/ UPDATE EXISTING PRODUCT', '4/ DELETE PRODUCT']
    for i in products_options:
        print (i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_products()
        product_menu()
    elif user_option == 2:
        add_new_productdb()
        view_products()
        product_menu()
    elif user_option == 3:
        update_existing_productdb()
        view_products()
        product_menu()
    elif user_option == 4:
        delete_productdb()
        main_menu_list()
        

######################## COURIERS MENU  ########################
def courier_menu():    
    print("~~~~~ COURIERS MENU ~~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    products_options= ['0/ RETURN TO MAIN MENU', '1/ VIEW COURIERS', '2/ ADD NEW COURIER', '3/ UPDATE EXISTING COURIER', '4/ DELETE COURIER']
    for i in products_options:
        print (i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_courier()
        courier_menu()
    elif user_option == 2:
        add_new_courierdb()
        view_courier()
        courier_menu()
    elif user_option == 3:
        update_existing_courierdb()
        view_courier()
        courier_menu()
    elif user_option == 4 :
        delete_courierdb()
        main_menu_list()
         

######################### ORDERS MENU #########################################

def order_menu():    
    print("~~~~~ ORDERS MENU ~~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    orders_options= ['0/ RETURN TO MAIN MENU', '1/ VIEW ORDERS', '2/ ADD NEW ORDER', '3/ UPDATE EXISTING ORDER', '4/ DELETE ORDER']
    for i in orders_options:
        print (i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_orders()
        order_menu()
    elif user_option == 2:
        add_new_orderdb()
        view_orders()
        order_menu()
    elif user_option == 3:
        update_existing_orderdb()
        view_orders()
        order_menu()
    elif user_option == 4 :
        delete_ordersdb()
        main_menu_list()
         


######################################### MAIN MENU ###############################################################

def main_menu_list():
    print('----------------------------------------------------------------------------- ')
    print(" ~~~~    WELCOME TO AROMA CAFE    ~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    main_menu = ["0/ EXIT THE APP","1/ PRODUCTS MENU","2/ COURIERS MENU","3/ ORDERS MENU","4/ ORDER STATUS MENU","5/ SAVE TO CSV"]
    for i in main_menu:
        print(i)
    user_input= int(input("Enter an option:"))
    if user_input == 0:
        message=' ~~~~~ THANK YOU FOR USING THIS APP ~~~~~ '
        sys.exit(message)
    elif user_input == 1:
        product_menu()
    elif user_input == 2:
        courier_menu()
    elif user_input == 3:
        order_menu()
    elif user_input == 4:
        order_status_menu()
    elif user_input == 5:
        export_products_to_csv()
        export_couriers_to_csv()
        export_orders_to_csv()
    else:
        print ('NOT A VALID OPTION!!!!') 
        main_menu_list() 
main_menu_list()   

   

    

print()





