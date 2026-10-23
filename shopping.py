item = input("Enter the item you want to buy:")
price = float(input("Enter the price:"))
quantity = int(input("Enter the qauntity you want:"))

total = price * quantity

print(f"you have pick {quantity} x {item}")
print(f"your total come to ${total}")