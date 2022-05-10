
# from file_manager import *
# import file_manager 
# import os
import json
from tkinter.font import BOLD




                          #####READ PRODUCTS AND COURIERS FILES#####
try:
    with open("products_file.txt","r")as file:
        product_list=file.read().split()
        print(f'PROUDUCT LIST\n(){product_list}'+'\n')
except Exception as e:
    print('An error occured: ' + str(e))
try:
    with open("couriers_file.txt", "r") as file:
        courier_list=file.read().split()
        print(f'COURIER LIST\n{courier_list}'+'\n')
except Exception as e:
    print('An error occured: ' + str(e))

def save_product():
    try:
        with open("products_file.txt", "w+") as file:
            for product in product_list:
                file.writelines(product+'\n')

    except Exception as e:
            print('An error occured: ' + str(e))

def save_courier():
    try:
        with open("couriers_file.txt", "w+") as file:
            for courier in courier_list:
                file.writelines(courier+'\n')
    except Exception as e:
        print('An error occured: ' + str(e))
    print('Exiting App')


    


                            #### MAIN MENU ####
print ("Please select an option\nA / PRODUCTS MENU \nB / COURIERS MENU\nC / ORDERS MENU\nD / SAVE PRODUCTS MENU\nE / SAVE COURIERS MENU")
input_cho=input('')
while True:
    
    if input_cho == 'A':
        print ('Please Choose an option:')
        print("0/Exit\n1/Select a product\n2/Add new product\n3/Replace product\n4/Delete product")
        
                        #### PRODUCTS INPUT OPTION #### 
        input_option=input('')
        if input_option == '0':
            print("Exit")
            break
#### product selection
        elif input_option == '1':
            print (' Please Select a Product')
            print(product_list)
            #print(type(product_file))
            input_opti=input('')
            if input_opti == '1':
                print (product_list[1])
                print('\n')
            elif input_opti == '2':
                print (product_list[2])
                print('\n')
            elif input_opti == '3':
                print (product_list[3])
                print('\n')
            elif input_opti == '4':
                print (product_list[4])
                print('\n')
#### adding new item to the products list        
        elif input_option == '2':
            print ("Add new product")
            print(product_list)
        #print(type(products))
            new_product = product_list.append(input(''))
            print (product_list)
            print ('Do you want to continue adding?')
            input_user = input('')
            while input_user == 'Y':
                print('Add new product')
                print(product_list)
                #print(type(products))
                new_product = product_list.append(input(''))
                print (product_list)
                print ('Do you want to continue adding?')
                input_user = input('')
            if input_user == 'N':
                save_product()
                print('Exit')
                

# replacing items in the product list        
        elif input_option == '3':
            print("Replace a product")
            print(product_list)
            for count,enum_pro in enumerate(product_list):
                print(count,enum_pro)
                print("Select a product to replace")
                new_item = input('')
                new_product = input ('')
                product_list[product_list.index(new_item)]= new_product
                print (product_list)
                print ('Do you want to continue replacing?')
                print ('Choose Y / For Yes\n N / For No')
                input_option = input('')
            while input_option == 'Y':
                for count,enum_pro in enumerate(product_list):
                    print(count,enum_pro)
                print("Select a product to replace")
                new_item = input('')
                new_product = input ('')
                product_list[product_list.index(new_item)]= new_product
                print (product_list)
            if input_option == 'N':
                save_product()
                print('Exit')

 # item deleting from the products list                
        elif input_option == '4':
            print('Delete an item')
            print(product_list)
            print ('Select an item to remove')
            input_option = input('')
            if input_option == '1':
                product_list.pop(0)
                print(product_list)
            elif input_option == '2':
                product_list.pop(1)
                print(product_list)
            elif input_option == '3':
                product_list.pop(2)
                print(product_list)
            print ('Do you want to continue deleting ??') 
            print ('Choose\n Y / For Yes\n N / For No')
            input_option = input('')
            while input_option == 'Y':
                print('Delete an item')
                print(product_list)
                print ('Select an item to remove')
                input_option = input('')
                if input_option == '1':
                    product_list.pop(0)
                    print(product_list) 
                elif input_option == '2':
                    product_list.pop(1)
                    print(product_list)
                elif input_option == '3':
                    product_list.pop(2)
                    print(product_list)
                    save_product()

                                 #### COURIERS INPUT MENU ####
    elif input_cho == 'B':
        print ('Please Choose an option:')
        print("0/Exit\n1/Select a courier\n2/Add new courier\n3/Replace a courier\n4/Delete a courier")
        input_option=input('')
        if input_option == '0':
            print("Exit")

    # couriers selection
        elif input_option == '1':
            print(courier_list)
            # print(type(courier_file))
            input_opti=input('')
            if input_opti == '1':
                print (courier_list[0])
            elif input_opti == '2':
                print (courier_list[1])
            elif input_opti == '3':
                print (courier_list[2])

    # adding new item to the couriers list        
        elif input_option == '2':
            print ("Add new courier")
            print(courier_list)
            print(type(courier_list))
            new_courier = courier_list.append(input(''))
            print (courier_list)
            print ('Do you want to continue adding?')
            input_user = input('')
            while input_user == 'Y':
                print('Add new courier')
                print(courier_list)
                print(type(courier_list))
                new_courier = courier_list.append(input(''))
                print (courier_list)
                print ('Do you want to continue adding?')
                input_user = input('')
            if input_user == 'N':
                save_courier()
                print('Exit')


    # replacing items in the couriers list        
        elif input_option == '3':
            print("Replace a courier")
            for count,enum_cou in enumerate(courier_list):
                print(count,enum_cou)
            print("Select a courier to replace")
            courier = input('')
            new_couriers = input ('')
            courier_list[courier_list.index(courier)]= new_couriers
            print (courier_list)
            print ('Do you want to continue replacing?')
            input_option = input('')
        while input_option == 'Y':
            for count,enum_cou in enumerate(courier-list):
                print(count,enum_cou)
            print("Select a courier to replace")
            new_courier = input('')
            new_couriers = input ('')
            courier_list[courier_list.index(new_courier)]= new_couriers
            print (courier_list)
        if input_option == 'N':
            save_courier()
            print('Exit')

    # # item deleting from the couriers list
        elif input_option == '4':
            print('Delete an item')
            print(courier_list)
            print ('Select a courier to remove')
            input_option = input('')
            if input_option == '1':
                courier_list.pop(0)
                print(courier_list) 
            elif input_option == '2':
                courier_list.pop(1)
                print(courier_list)
            elif input_option == '3':
                courier_list.pop(2)
                print(courier_list) 
                print ('Do you want to continue removing?')
                print ('Y','N')
                input_user = input('')
                while input_user == 'Y':
                    print ('Select a courier to remove')
                    input_option = input('')
                    if input_option == '1':
                        courier_list.pop(0)
                        print(courier_list) 
                    elif input_option == '2':
                        courier_list.pop(1)
                        print(courier_list)
                    elif input_option == '3':
                        courier_list.pop(2)
                        print(courier_list)
                if input_option == 'N':
                    save_courier()
                    print('Exit')
#elif print('back to main menu'):
    
    elif input_cho == 'C':
        orders = {
        {"customer 1": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": "Martin",
        "status": "preparing"},
        {"customer 2": "Aisha",
        "customer_address": "Unit 3, 12 fontley Street, LONDON, SN1 2FR",
        "customer_phone": "0700000000",
        "courier":"Bob",
        "status": "preparing"}}
        print (orders)

    elif input_cho == 'D':
        save_product()
    elif input_cho == 'E':
        save_courier()
        break
    else:
        print ("Please select an option\nA / PRODUCTS MENU \nB / COURIERS MENU\nC / SAVE PRODUCTS MENU\nD / SAVE COURIERS MENU")
        input_cho=input('')