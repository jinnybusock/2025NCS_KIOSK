# 1) Ice Americano : 2000 2) Latte : 3000
drinks= ["Ice Americano", "Latte"]
prices= [2000, 3000]
amounts= [0, 0]
total_price= 0
# order_list= ''

while True:
    menu = input(f"1) {drinks[0]} {prices[0]} 2) {drinks[1]} {prices[1]}  3) Exit : ")

    if menu== "1":
        print(f"You ordered {drinks[0]}! Price : {prices[0]} won. Thank you")
        total_price=total_price+ prices[0]
        # order_list+= drinks[0]+ '\n'
        amounts[0]= amounts[0]+ 1

    elif menu== "2":
        print(f"You ordered {drinks[1]}! Price : {prices[1]} won. Thank you")
        total_price =total_price+ prices[1]
        # order_list += drinks[1]+ '\n'
        amounts[1]= amounts[1]+ 1

    elif menu == "3":
        print("You finish order")
        break
    else:
        print(f"{menu} menu is not existed. Please try again.")

# print(order_list)
print(f"{drinks[0]} {prices[0]} x {amounts[0]} {prices[0]* amounts[0]}")
print(f"{drinks[1]} {prices[1]} x {amounts[1]} {prices[0]* amounts[1]}")
print(f"Total price : {total_price}")