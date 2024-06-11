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
    request = ("Please enter a topping: ")
    if request in toppings:
        print(request, "Are available")
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
    else:
        print("Processing...")
        time.sleep(1)
        print("This Scrament is not available")
        
        