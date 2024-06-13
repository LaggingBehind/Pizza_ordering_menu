
order_list = []

pizza_menu = {
  1:{"name":"Large","price":9.99},
  2:{"name":"Medium","price":6.99},
  3:{"name":"Small","price":3.99},
}

toppings_menu = {
  "Mushrooms":1.50,
  "Sausage":2.00,
  "Pepperoni":1.75,
  "Cheese":1.00
}

drinks_menu = {
  "Coke":1.25,
  "Mountain Dew":1.25,
  "Sprite":1.25,
  "Water":0.50,
  "Wine":("We dont5 serve wine, friend")
}

total_cost = 0  


def greet_customer():
  print("Welcome to Cheesus Crust Pizza!")
  print("How may we serve thee?")
  
def choose_pizza_size():
  global total_cost
  print("Please select the size of your pizza:")
  for key, value in pizza_menu.items():
    print(f"{key}.{value['name']}-${value['price']:.2f}")
    
  while True:
    try:
      size_choice=int(input("Enter the number corresponding to your choice:"))
      if size_choice in pizza_menu:
        select_pizza = pizza_menu[size_choice]
        total_cost += size["price"]
        order_list.append(size()["name"])
        break
      else:print("Invalid selection. Please choose a menu item number")
    ValueError:
    print("Invalid, Please enter a number.")


def pizza_topping():
  global total_cost
  print("Please select your toppings(enter'done'when finnished):")
  for topping,price in toppings_menu.items():
    print(f"{topping}-${price:.2f}")
    
  while True:
    topping_choice=input("Enter a topping:")
    if topping_choice.lower()=='done':
      break
    elif topping_choice in toppings_menu:
      price=toppings_menu[topping_choice]
      total_cost+=price
      order_list.append(topping_choice)
    else:
      print(f"{topping_choice}is not available")
      
def soft_drink():
  global total_cost
  print("Select a sacrament")      
  for drink, price in drinks_menu.items():
    if isinstance(price,float):
      print(f"{drink}-${price:.2f}")
    else:
      print(f"{drink}-{price}")
      
  while True:
    drink_choice = input("Select a sacrament:")
    if drink_choice in drinks_menu:
      price = drinks_menu[drink_choice]
      if isinstance(price,float):
        total_cost +=price
        order_list.append(drink_choice)
      else:
        print(price)
      break
    else:
      print(f"{drink_choice} is not available")
      
def ask_another_order():
  while True: 
    another_order = input("Would you like another order? (y/n):")
    if another_order.lower() == 'y':
      process_order()     
    elif another_order.lower() == 'n':
      print(f"Your total is ${total_cost:.2f}")
      print("Have a blessed day!")
      break
    else:
      print("Invalid input. Please enter y or n")  
  
def process_order():
  choose_pizza_size()
  choose_toppings()
  choose_drink()
  ask_another_order()
  
  # Start order process
  greet_customer()
  process_order()
  