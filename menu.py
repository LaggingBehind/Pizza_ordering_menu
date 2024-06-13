
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
  "Wine":"We dont5 serve wine, friend"
}

total_cost = 0  


def hello_message():
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
        total_cost += selected_pizza["price"]
        order_list.append(selected_pizza["name"])
        break
      else:print("Invalid selection. Please choose a menu item number")
  exept ValueError:
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
  
#   request = input("What would you like on your body of crust?: ")
#   if request in toppings:
#     price = toppings.get(request)  # Use get() to handle cheese case
#     if price:  # Check if price exists (cheese won't have a price)
#       print(request, "is available for", f"${price:.2f}")  # Format price with 2 decimals
#     else:
#       print(toppings[request])  # Print the included message for cheese
#     soft_drinks()
#   else:
#     print("Processing...")
#     time.sleep(1)
#     print(request, "Sorry not available")
#     quit()


#   drinks = {
#     "Coke": 1.25,
#     "Mountain Dew": 1.25,
#     "Sprite": 1.25,
#     "Wine": "We don't serve wine, friend",
#     "Water": 0.50}
#   request = input("Enter your sacrament: ")
#   if request in drinks:
#     price = drinks.get(request)
#     if price:
#       print(request, "is available for", f"${price:.2f}")
#     else:
#       print(drinks[request])  # Print the unavailability message for wine
#     thank_customer()
#   else:
#     print("Processing...")
#     time.sleep(1)
#     print(request, "This sacrament is not available")

# def thank_customer():
#   print("Have a blessed day")

# hello_message()
