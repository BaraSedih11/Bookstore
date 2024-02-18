import uuid
import datetime


def generate_order_id():
    return uuid.uuid4()


def print_order_details(order):
    print("Order ID:", order["order_id"])
    print("Order Date:", order["order_date"])
    print("Book Purchased:")
    for item in order["books"]:
        print("Title:", item.get_title())
        print("Price:", item.get_price())
        print("Quantity:", item.get_quantity())
        print("Total Price for books:", item.get_total_price())
        print()
    print("Total Price for whole order:", order["total_price"])


class OrderProcessor:

    def __init__(self, shopping_cart, inventory):
        self.orders = []
        self.shopping_cart = shopping_cart
        self.inventory = inventory

    def place_order(self):
        order_id = generate_order_id()
        order_date = datetime.datetime.now()
        order = {
            "order_id": order_id,
            "order_date": order_date,
            "books": self.shopping_cart.get_books(),
            "total_price": self.shopping_cart.get_total_price()
        }
        self.orders.append(order)
        self.process_order(order)

    def process_order(self, order):
        for book in order['books']:
            self.inventory.remove_book(book.get_title())
            self.shopping_cart.remove_book(book.get_title())

    def view_orders(self):
        for order in self.orders:
            print_order_details(order)

    def generate_report(self):
        total_orders = len(self.orders)
        total_sales = sum(order["total_price"] for order in self.orders)
        print("Total Orders:", total_orders)
        print("Total Sales:", total_sales)
