
'''
Author: CJ Busca
Class: IT-140
Instructor: Lisa Fulton
Project: Grocery List Final
Date: 20284
'''

#Creation of empty data sctructures
grocery_item = {}

grocery_history = []

#Loop function for the while loop
stop = 'go'

while stop !='q':

  #This block asks the user to input name, quantity, and price of items
  item_name = input('Item name:\n')    
  quantity = input('Quantity purchased:\n')    
  cost = input('Price per item:\n')
 
  #This block utilizes the empty list above to store the data input from the user
  grocery_item['name'] = item_name
  grocery_item['number'] = int(quantity)
  grocery_item['price'] = float(cost)
  grocery_history.append(grocery_item.copy())
  #User has the option to continue inputting items or quit
  stop = input("Would you like to enter another item? \nType 'c' for continue or 'q' to quit:\n")

#The grand total has a set value that gets added for each price that is entered
grand_total = 0
#This block utilizes a for loop for the iterations of the entered objects
for index, item in enumerate(grocery_history):
  
  
  item_total = item['number'] * item['price']
  
  #This block details the total of al of the items in the iteration
  grand_total += (item_total)
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  
  
  item_total = 0
#Grand total of all items is displayed only when user inputs quit command
print('Grand total: $%.2f' % grand_total)
