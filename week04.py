class DrinkOrderSystem:
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_RATE = 0.1

    def __init__(self):
        self.drinks = ["Ice Americano", "Latte", "Watermelon juice"]
        self.prices = [2000, 3000, 4900]
        self.amounts = [0] * len(self.drinks)
        self.total_price = 0

    def apply_discount(self, price: int) -> int:
        """
        총 주문 금액이 일정 값 이상인 경우 할인 적용
        """
        if price >= self.DISCOUNT_THRESHOLD:
            discount = price * self.DISCOUNT_RATE
            return price - discount
        return price

    def order_process(self, idx: int):
        """
        음료 주문 처리: 금액 누적 및 수량 증가
        """
        print(f"You ordered {self.drinks[idx]}! Price: {self.prices[idx]} won. Thank you!")
        self.total_price += self.prices[idx]
        self.amounts[idx] += 1

    def show_summary(self):
        """
        주문 요약 출력
        """
        print("\nProduct\t\tPrice\tAmount\tSubtotal")
        for i in range(len(self.drinks)):
            if self.amounts[i] > 0:
                subtotal = self.prices[i] * self.amounts[i]
                print(f"{self.drinks[i]:<15}{self.prices[i]} x {self.amounts[i]}\t= {subtotal}")

        discounted_price = self.apply_discount(self.total_price)
        discount_amount = self.total_price - discounted_price

        print(f"\nTotal price: {self.total_price} won")
        if discount_amount > 0:
            print(f"Discount amount: {int(discount_amount)} won")
            print(f"Final price after discount: {int(discounted_price)} won")
        else:
            print("The discount has not been applied.")
            print(f"Final price: {self.total_price} won")

    def run(self):
        """
        전체 주문 시스템 실행 루프
        """
        menu_list = " ".join(
            [f"{i + 1}) {self.drinks[i]} {self.prices[i]} won" for i in range(len(self.drinks))]
        )
        menu_list += f" {len(self.drinks) + 1}) Exit: "

        while True:
            try:
                menu = int(input(menu_list))
                if 1 <= menu <= len(self.drinks):
                    self.order_process(menu - 1)
                elif menu == len(self.drinks) + 1:
                    print("You finish order.")
                    break
                else:
                    print(f"{menu} menu is invalid. Please try again.")
            except ValueError as err:
                print(f"Invalid input. Please enter a number.\n{err}")

        self.show_summary()


# 실행
if __name__ == "__main__":
    system = DrinkOrderSystem()
    system.run()
