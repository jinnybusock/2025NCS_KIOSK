#drinks= ["Ice Americano", "Latte"]
#prices= [2000, 3000]
# amounts= [0, 0]
#amounts= [0]* len(drinks)
#total_price= 0

drinks= ["Ice Americano", "Latte", "Watermelon juice"]
prices= [2000, 3000, 4900]
amounts= [0] * len(drinks)
total_price= 0
#menu_lists= ""

DISCOUNT_THRESHOLD= 10000
DISCOUNT_RATE= 0.1

def apply_discount(price: int):
    """
    총 주문 금액이 일정 값 이상인 경우 할인 적용하여 최종 가격 리턴하는 함수
    A function that returns the price by reflecting the discount rate when the total exceeds certain amount.
    :param price: Price before discount
    :return: Price after discount
    """
    if price>= DISCOUNT_THRESHOLD:
        discount= price* DISCOUNT_RATE

        return price- discount

    return price

def order_process(idx: int):
    """
    음료 주문 디스플레이 및 누적금액 계산과 수량 처리 함수
    :param idx: list's index num
    """
    #global 공부하기
    global total_price
    print(f"You ordered {drinks[idx]}! Price : {prices[idx]} won. Thank you")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

menu_lists= " ".join([f"{k+1}) {drinks[k]} {prices[k]} won " for k in range(len(drinks))])
menu_lists+= f"{len(drinks)+ 1}) Exit: "

# help(abs)
# help(len)
# help(order_process)

while True:
    try:
        menu = int(input(menu_lists))
        if len(drinks) >= menu >= 1:
            order_process(menu - 1)

        elif menu == len(drinks) + 1:
            print("You finish order")
            break

        else:
            print(f"{menu} menu is invalid. Please try again.")
    except ValueError as err:
        print(f"Cannot find menu number. Please put valuable number\n{err}")

print("Product Price Amount Subtotal")

for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x {amounts[i]} {prices[i] * amounts[i]}")

discounted_price= apply_discount(total_price)
discount_amount= total_price- discounted_price

print(f"Total price: {total_price}won")

if discount_amount> 0:
    print(f"Discount amount : {discount_amount}won")
    print(f"Total price : {discounted_price}won")

else:
    print(f"The discount has not been applied")
    print(f"Total price : {total_price}won")
