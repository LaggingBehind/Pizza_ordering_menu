import time

def hello_message():
    print("Welcome to Cheesus Crust Pizza!")
    print("How may we serve thee?")
    pizza_topping()
    
def pizza_topping():
    toppings = ["Mushrooms",
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