import time
from tkinter import Menu
from urllib import request

#Menu and prices

menu_items = {
    "Large pizza": 12.99,
    "Medium pizza": 10.99,
    "Small pizza": 8.99}

toppings = {
    "Mushroom": 1.50,
    "Sausage": 2.00,
    "Pepperoni": 1.75,
    "Cheese": 1.00}

drinks = {
    "Coke": 1.50,
    "Mountian Dew": 1.50,
    "Sprite": 1.50,
    "Wine": 3.00,
    "Water": 1.00}

order_list = []

#Greet the customer

def hello_message():
    print("Welcome to Cheesus Crust Pizza!")
    print("How may we serve thee?")
    
#Begin order with size of pizza

    
    pizza_size()
def pizza_size():
    for size, price in menu_items.items():
        print(f"{size}: ${price:.2f}")
        
    size_selection = input("What size pizza would you like?: ")
    
    if size_selection not in menu_items.keys():
        print("Invalid entry")
        return 
     
        
# #Toppings selection
        
#         pizza_topping()
# def pizza_topping():
#     toppings = ["Mushroom",
#                 "Sausage",
#                 "pepperoni",
#                 "Cheese"]
#     request = input("What would you like on your body of crust?: ")
#     if request in toppings:
#         print(request, "Is available")
#         soft_drinks()
#     else:
#         print("Processing...")
#         time.sleep(1)
#         print(request,"Sorry not available")
#         quit()
        
# #Drink selection 

# def soft_drinks():
#     print("Select a sacrament")
#     drinks = ["Coke",
#               "Mountain Dew",
#               "Sprite",
#               "Wine",
#               "Water"]
#     request = input("Enter your sacrament: ")
#     if request in drinks:
#         print(request, "Is available")
#         thank_customer()
#     else:
#         print("Processing...")
#         time.sleep(1)
#         print("This Scrament is not available")
        
def thank_customer():
    print("Have a blessed day")
    
hello_message()