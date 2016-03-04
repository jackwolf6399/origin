list = []

food = ("Your shopping list is empty. Name a new item: ")
print(food)
food = input()
list.append(food)

nextFood = ("Your shopping list contains {}. Name a new item: ".format(list))
print(nextFood)

while len(list) != 0:
	nextFood = input()
	if nextFood == "done":
		print("Ok, your list is {}. Good luck!".format(list))
		break
	else:
		list.append(nextFood)
		done = "Type 'done' if list is finished or a new item."
		print("Your shopping list contains {}. {}".format(list, done))