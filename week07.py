from typing import List  # type hint
import kiosk

if __name__ == "__main__":
    # menu_drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice", "Ice tea"]
    # menu_prices = [2000, 3000, 4900, 3300]
    menu_drinks = ["Ice Americano", "Cafe Latte"]
    menu_prices = [2000, 3000]
    menu_drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice", "Ice tea"]
    menu_prices = [2000, 3000, 4900, 3300]
    # menu_drinks = ["Ice Americano", "Cafe Latte"]
    # menu_prices = [2000, 3000]

    menu = kiosk.Menu(menu_drinks, menu_prices)
    order_processor = kiosk.OrderProcessor(menu)  # has-a, aggregation