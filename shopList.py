f = open("foodList.txt", 'r+')
shoppingList = f.read().splitlines()

item = None

while item != '':
	if len(shoppingList) == 0:
		print("Your list is empty.")
	else:
		print("Your shopping list contains:")
		itemNumber = 0
		for thing in shoppingList:
			itemNumber += 1
			print("{}. {}".format(itemNumber, thing))

	item = input("What item would you like to add? ")

	if item != '':
		shoppingList.append(item)
	
f.seek(0)
f.truncate()

for item in shoppingList:
	f.write(item + '\n')

print("This is your list! Good luck shopping!")

f.close()