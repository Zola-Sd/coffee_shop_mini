
# from file_manager import *
# import file_manager 
# import os
import json
from optparse import Option
from os import stat
from tkinter.font import BOLD
import pprint




                          #####READ PRODUCTS AND COURIERS FILES#####
try:
    with open("products_file.txt","r+")as file:
        product_list=file.read()
        print(f'PROUDUCT LIST\n{product_list}'+'\n')
except Exception as e:
    print('An error occured: ' + str(e))
    print (''' ==================================== ''')
try:
    with open("couriers_file.txt", "r+") as file:
        courier_list=file.readlines()
        print(f'COURIER LIST\n{courier_list}'+'\n')
except Exception as e:
    print('An error occured: ' + str(e))
    print (''' ==================================== ''')

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
orders = {
        1 : {"NAME" : "Emil",
    "ADDRESS" : "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "PHONE"  : "0789887334",
    "COURIER" : "Martin",
    "STATUS" : "preparing"},
         2 : {"NAME" : "Aisha",
    "ADDRESS" : "Flat 6, 12 Fontley Street, LONDON, SW1 2EF",
    "PHONE"  : "0700000000",
    "COURIER" : "Bob",
    "STATUS" : "ready"}
}

order_status=["PREPARING","ON IT's WAY","DELIVERD"]


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
            orde_input=int(input(''))
            if orde_input == '1':
                print (product_list[1])
                print('\n')
            elif orde_input == '2':
                print (product_list[2])
                print('\n')
            elif orde_input == '3':
                print (product_list[3])
                print('\n')
            elif orde_input == '4':
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
                new_item = str(input(''))
                new_product = input ('')
                product_list[product_list.index(new_item)]= new_product
                print (product_list)
                print ('Do you want to continue replacing?')
                print ('Choose Y / For Yes\n N / For No')
                input_option = str(input(''))
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

######### ORDERS INPUT MENU ######################

    
    elif input_cho == 'C':
        print ('Please Choose an option:')
        print("0/Exit\n1/View Orders\n2/Add new Order\n3/Replace an Order\n4/Delete an Order\n5/Assign a Courier")
        input_option=input('')
        if input_option == '0':
            print("Exit")
############ PRINT ORDERS ###################
        elif input_option == '1':
            def orders_list(): 
                for o_cust, o_info in orders.items():
                    print("\norder:", o_cust)
                    
                    for key in o_info:
                        print(key + ':', o_info[key])
            
            orders_list()
            print('EXIT')
        
########### ADD NEW ORDER ##################
        elif input_option == '2':
            new_order = { }

            size = int(input("How many orders you want to creat?: "))

            for i in range(size):
                dict_name = int(input("Enter the order number: "))
                new_order[dict_name] = {}
                Name = input("Enter name: ")
                address = input("Enter Address: ")
                phone = int(input("Enter phone number: "))
                print (courier_list)
                courier = int(input("select a courier: "))
                status = input("What is the status of the order?: ")
                new_order[dict_name]["Name"] = Name
                new_order[dict_name]["address"] = address
                new_order[dict_name]["phone"] = phone
                new_order[dict_name]["courier"] = courier
                new_order[dict_name]["status"] = status
                orders [3] = new_order  # why does the function break here ???
                print(orders)

####### UPDATE EXISTING ORDER STATUS ########
        elif input_option == '3':        
            print('ORDERS LIST')
            for i  in orders :
                print(i, orders[i])

            ### order status list with index
            print("select from the list: ")
            for index, value in enumerate(order_status):
                print(index, value)

            def update_order_status():
                print("CHOOSE AN ORDER TO UPDATE")
                user_enter = int(input(''))
                print("CHOOSE A STATUS")
                status_option = int(input(''))
                if user_enter == 1 and status_option == 0:
                    orders[1]['STATUS'] = order_status[0]
                    print(orders)
                elif user_enter == 1 and status_option == 1:
                    orders[1]['STATUS'] = order_status[1]
                    print(orders)
                elif user_enter == 1 and status_option == 2:
                    orders[1]['STATUS'] = order_status[2]
                    print(orders)
                elif user_enter == 2 and status_option == 0:
                    orders[2]['STATUS'] = order_status[0]
                    print(orders)
                elif user_enter == 2 and status_option == 1:
                    orders[2]['STATUS'] = order_status[1]
                    print(orders)
                elif user_enter == 2 and status_option == 2:
                    orders[2]['STATUS'] = order_status[2]
                    print(orders)
                
            update_order_status()
            print("EXIT")

########### UPDATE EXISTING ORDER ##############           
        
        elif input_option == '4':  

            def update_order():
                for o_cust, o_info in orders.items():
                    print("\norder:", o_cust)
                    for key in o_info:
                        print(key + ':', o_info[key])
                order_indx = int(input('please input the no of the order you want to update'))
                result = orders[order_indx]
                for key,value in result.items():
                    print(f'{key},{value}')
                    update_value = input('input the value you want to update:')
                    if update_value != "":
                        result[key] = update_value
                pprint.pprint(result)
            update_order()
            print('Exit')

########### DELETE AN ORDER ##############
        
        elif input_option == '5':
            
            def delete_order():
                for o_cust, o_info in orders.items():
                    print("\norder:", o_cust)
                    
                    for key in o_info:
                        print(key + ':', o_info[key])
                print("Select an order to delete")
                user_input= input('')
                if user_input == '1':
                    orders.pop(1)
                    print (orders)  
                elif user_input == '2':
                    orders.pop(2) 
                    print (orders)
            delete_order()
            print('EXIT')


# else:
#     print ("Please select an option\nA / PRODUCTS MENU \nB / COURIERS MENU\nC / SAVE PRODUCTS MENU\nD / SAVE COURIERS MENU")
#     input_cho=input('')
    
    elif input_cho == 'D':
        save_product()
        print('Exit')
    elif input_cho == 'E':
        save_courier()
    break

