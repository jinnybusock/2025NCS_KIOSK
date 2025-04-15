from typing import List  # type hint
import kiosk

if __name__ == "__main__":
    menu_drinks = ["Ice Americano", "Cafe Latte"]
    menu_prices = [2000, 3000]

    menu = kiosk.Menu(menu_drinks, menu_prices)
    order_processor = kiosk.OrderProcessor() # has-a, aggregation
    order_processor.run(menu) # run 메서드에 Menu 객체를 전달