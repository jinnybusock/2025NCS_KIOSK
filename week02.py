# 1) Ice Americano : 2000 2) Latte : 3000
drinks= ["Ice Americano", "Latte"]
prices= [2000, 3000]

while True:
    menu = input(f"1) {drinks[0]} {prices[0]} 2) {drinks[1]} {prices[1]}  3) Exit : ")

    if menu== "1":
        print(f"You ordered {drinks[0]}! Price : {prices[0]} won. Thank you")

    elif menu== "2":
        print(f"You ordered {drinks[1]}! Price : {prices[1]} won. Thank you")

    elif menu == "3":
        print("You finish order")
        break
    else:
        print(f"{menu} menu is not existed. Please try again.")