import time

#Menu and prices

menu_items = {
    "Large pizza": 12.99,
    "Medium pizza": 10.99,
    "Small pizza": 8.99}

toppings = {
    "Mushroom": 1.50,
    "Sausage": 2.00,
    "pepperoni": 1.75,
    "Cheese": 1.00}

drinks = {
    "Coke": 1.50,
    "Mountian Dew": 1.50,
    "Sprite": 1.50,
    "Wine": 3.00,
    "Water": 1.00}
order_list = []

def hello_message():
    print("Welcome to Cheesus Crust Pizza!")
    print("How may we serve thee?")
    
    pizza_size()
def pizza_size():
        size = ["Large",
                "Medium",
                "Small"]
        
    pizza_topping()
def pizza_topping():
    toppings = ["Mushroom",
                "Sausage",
                "pepperoni",
                "Cheese"]
    request = input("What would you like on your body of crust?: ")
    if request in toppings:
        print(request, "Is available")
        soft_drinks()
    else:
        print("Processing...")
        time.sleep(1)
        print(request,"Sorry not available")
        quit()

def soft_drinks():
    print("Select a sacrament")
    drinks = ["Coke",
              "Mountain Dew",
              "Sprite",
              "Wine",
              "Water"]
    request = input("Enter your sacrament: ")
    if request in drinks:
        print(request, "Is available")
        thank_customer()
    else:
        print("Processing...")
        time.sleep(1)
        print("This Scrament is not available")
        
def thank_customer():
    print("Have a blessed day")
    
hello_message()