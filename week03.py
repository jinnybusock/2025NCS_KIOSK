drinks= ["Ice Americano", "Latte"]
prices= [2000, 3000]
amounts= [0 for _ in range(len(drinks))]
total_price= 0
menu_lists= ""

#drinks= ["Ice Americano", "Latte", "Watermelon juice"]
#prices= [2000, 3000, 4900]
#amounts= [0, 0, 0]
#total_price= 0
#menu_lists= ""

def order_process(idx: int):
    global total_price
    print(f"You ordered {drinks[idx]}! Price : {prices[idx]} won. Thank you")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

for k in range(len(drinks)):
    menu_lists+= f"{k+1}) {drinks[k]} {prices[k]} won "

menu_lists+= f"{len(drinks)+ 1}) Exit: "

while True:
    menu= int(input(menu_lists))
    if len(drinks) >= menu>= 1:
        order_process(menu- 1)

    elif menu == len(drinks)+ 1:
        print("You finish order")
        break

    else:
        print(f"{menu} menu is not existed. Please try again.")

print("Product Price Amount Subtotal")

for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x {amounts[i]} {prices[i] * amounts[i]}")

print(f"Total price : {total_price}")