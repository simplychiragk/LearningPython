"Program to calculate the area of a rectangle"
"date: 23-01-2026"
"time: 01:51 AM"

"program starts here"

print("Welcome to the Shopping Cart Program!")
print("This program allows you to add items to your shopping cart and view the total cost.")
item = input("Please enter the name of the item you want to add to your cart: ")
price = float(input("Please enter the price of the item: "))
quantity = int(input("Please enter the quantity of the item: "))
total_cost = price * quantity
print(f"You have added {quantity} of {item} to your cart.")
print(f"The total cost for this item is: ${total_cost}")
print("Thank you for using the Shopping Cart Program!")
