# 1) Ice Americano : 2000 2) Latte : 3000
prices= [2000, 3000]

while True:
    menu = input(f"1) Ice Americano {prices[0]} 2) Latte {prices[1]}  3) Exit : ")

    if menu== "1":
        print(f"You ordered Ice Americano! Price : {prices[0]} won. Thank you")

    elif menu== "2":
        print(f"You ordered Latte! Price : {prices[1]} won. Thank you")

    else:
        print("You finish order")

    break