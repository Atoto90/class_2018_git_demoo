reccomendation = 'Here is what we have'

breakfast = ['Bacon', 'Eggs', 'Toast', 'Hashbrowns']
lunch = ['Burger', 'Grilled Cheese', 'Soup']
sides = ['Fries', 'Salad', 'Mashed Potatoes', 'Corn']
dinner = ['Spaghetti', 'Ribs', 'Steak', 'Pizza']
chefs_choice = ['Steak', 'Mashed Potatoes']

# breakfast_bacon = 6
# breakfast_eggs = 4
# breakfast_toast = 5
# breakfast_hashbrowns = 3

# lunch_burger = 8
# lunch_grilled_cheese = 7
# lunch_soup = 6

# sides_fries = 3
# sides_salad = 5
# sides_mashed_potatoes = 4
# sides_corn = 3

# dinner_spaghetti = 12
# dinner_ribs = 18
# dinner_steak = 16
# dinner_pizza = 14

# chefs_choice_steak = 20

def menus():
  print(breakfast)
  print(lunch)
  print(sides)
  print(dinner)
  print(chefs_choice)

greeting = input('Welcome to Bottega Diner, anything to drink?:')

if greeting == 'yes please':
  print('Ok, our choices are water and soda.')

elif greeting == 'no thank you':
  print('Ready to order?')
  
drink = input()

if drink == 'soda please':
  print('Ok, coming right up.')

elif drink == 'water please':
  print('Ok, coming right up.')
  
order_greeting ='what would you like to have today?'
print(order_greeting)

choice = input("I would like to see the")
print(choice)

if choice == 'breakfast menu':
  print(breakfast)

elif choice == 'lunch menu':
  print(lunch)
  
elif choice == 'sides menu':
  print(sides)
  
elif choice == 'dinner menu':
  print(dinner)
  
elif chefs_choice == 'chefs_choice':
  print(chefs_choice)
  
else:
  print('Ok here is our menu')
  menus()

userchoice = input()

# cost = input(cost_item())

if userchoice == "bacon":
  cost_item1 = 6
  print(cost)
elif userchoice == "eggs":
  cost_item1 = 4
  print(cost)
elif userchoice == "toast":
  cost_item1 = 5
  print(cost)
elif userchoice == "hashbrowns":
  cost_item1 = 3
  print(cost)
elif userchoice == "burger":
  cost_item2 = 8
  print(cost)
elif userchoice == "grilled cheese":
  cost_item2 = 7
  print(cost)
elif userchoice == "soup":
  cost_item2 = 6
  print(cost)
elif userchoice == "fries":
  cost_item3 = 3
  print(cost)
elif userchoice == "salad":
  cost_item3 = 5
  print(cost)
elif userchoice == "mashed potatoes":
  cost_item3 = 4
  print(cost)
elif userchoice == "corn":
  cost_item3 = 3
  print(cost)
elif userchoice == "spaghetti":
  cost_item4 = 12
  print(cost)
elif userchoice == "ribs":
  cost_item4 = 18
  print(cost)
elif userchoice == "steak":
  cost_item4 = 16
  print(cost)
elif userchoice == "pizza":
  cost_item4 = 14
  print(cost)
elif userchoice == "chefs choice":
  cost_item5 = 20
  print(cost)

waitress_reply = 'Great choice, coming right up!'
print(waitress_reply)

# item_1 = float(cost_item1)
# item_2 = float(cost_item2)
# item_2 = float(cost_item3)
# item_2 = float(cost_item4)
# item_2 = float(cost_item5)


item_1 = float(input('price of item 1 = '))
print(item_1)
item_2 = float(input('price of item 2 = '))
print(item_2)
item_3 = float(input('price of item 3 = '))
print(item_3)
item_4 = float(input('price of item 4 = '))
print(item_4)
item_5 = float(input('price of item 5 = '))
print(item_5)

subTotal = (item_1 + item_2 + item_3 + item_4) or item_5
tip = subTotal * 0.15
total = subTotal + tip
print(total)

final_say = f'Your total is {total}, thanks for stopping by!'
print(final_say)
