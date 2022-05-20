import csv
import sys 
from functions import *

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
        add_new_product()
        view_products()
        product_menu()
    elif user_option == 3:
        updat_existing_product()
        view_products()
        product_menu()
    elif user_option == 4:
        delete_product()
        main_menu_list()
        

######################## COURIERS MENU  ########################
def courier_menu():    
    print("~~~~~ COURIERS MENU ~~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    couriers_options= ['0/ RETURN TO MAIN MENU', '1/ VIEW COURIERS', '2/ ADD NEW COURIER', '3/ UPDATE EXISTING COURIER', '4/ DELETE COURIER']
    for i in couriers_options:
        print (i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_couriers()
        courier_menu()
    elif user_option == 2:
        add_new_courier()
        view_couriers()
        courier_menu()
    elif user_option == 3:
        updat_existing_courier()
        view_couriers()
        courier_menu()
    elif user_option == 4 :
        delete_courier()
        main_menu_list()
         

######################### ORDERS MENU #########################################

def orders_menu():    
    print("~~~~~ ORDERS MENU ~~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    orders_options = ['0/ RETURN TO MAIN MENU', '1/ VIEW ORDERS', '2/ ADD NEW ORDER', '3/ UPDATE EXISTING ORDER', '4/ DELETE ORDER']
    for i in orders_options:
        print (i)
    user_option = int(input('Enter an option:'))
    if user_option == 0:
        main_menu_list()
    elif user_option == 1:
        view_orders()
        orders_menu()
    elif user_option == 2:
        add_new_order()
        view_orders()
        orders_menu()
    elif user_option == 3:
        updat_existing_order()
        view_orders()
        orders_menu()
    elif user_option == 4 :
        delete_orders()
        main_menu_list()
         
############################### MAIN MENU ##########################################

def main_menu_list():
    print('----------------------------------------------------------------------------- ')
    print(" ~~~~    WELCOME TO AROMA CAFE    ~~~~")
    print('----------------------------------------------------------------------------- ')
    print("PLEASE SELECT AN OPTION")
    print("----------------------------------------")
    main_menu = ["0/ EXIT THE APP","1/ PRODUCTS MENU","2/ COURIERS MENU","3/ ORDERS MENU"]
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
        orders_menu()
    else:
        print ('NOT A VALID OPTION!!!!') 
        main_menu_list() 
main_menu_list()   

   

    