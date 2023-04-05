print("welcome to ahmed's delly, here is the menu")

# the menu
starters = ["Garlic Bread", "Salad", "Mozzarella Sticks", "Fruit", "Soup"]
mains = ["Pizza", "Burger", " pasta ", "Fish and Chips", "Roast Chicken"]
desserts = ["Cheesecake", "Chocolate Brownie", "Apple Pie", "Ice Cream", "Fruit Salad"]

# Initialise the order list
orders = []

# show the menu
print("Starters:")
for item in starters:
    print("- " + item)
print("Mains:")
for item in mains:
    print("- " + item)
print("Desserts:")
for item in desserts:
    print("- " + item)

# Take the customer's order three times
for i in range(3):
    print("Order", i+1)
    starter = input("What starter would you like? ")
    main = input("What main course would you like? ")
    dessert = input("What dessert would you like? ")
    orders.append([starter, main, dessert])

# Print the user's order back to them
print("Your order:")
for i in range(len(orders)):
    print("Order", i+1)
    print("Starter: " + orders[i][0])
    print("Main course: " + orders[i][1])
    print("Dessert: " + orders[i][2])
