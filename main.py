import uuid
import datetime


class Book:
    def __init__(self, title, author, price, quantity, category=None):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category}"

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_price(self, new_price):
        self.price = new_price

    def get_total_price(self):
        return self.price * self.quantity


class InventoryManager:

    def __init__(self):
        self.inventory = []

    def add_book(self, title, author, price, quantity, category):
        book = {
            "title": title,
            "author": author,
            "price": price,
            "quantity": quantity,
            "category": category
        }
        self.inventory.append(book)

    def assign_category(self, book_title, category):
        for book in self.inventory:
            if book["title"] == book_title:
                book["category"] = category
                break

    def view_inventory(self):
        for book in self.inventory:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Price:", book["price"])
            print("Quantity:", book["quantity"])
            print("Category:", book["category"])
            print()

    def add_stock(self, book_title, quantity):
        for book in self.inventory:
            if book["title"] == book_title:
                book["quantity"] += quantity
                break

    def remove_book(self, book_title):
        self.inventory = [book for book in self.inventory if book["title"] != book_title]

    def search_book(self, book_title):
        for book in self.inventory:
            if book["title"] == book_title:
                return book
        return None

    def get_books_by_category(self, category):
        category_books = []
        for book in self.inventory:
            if book["category"] == category:
                category_books.append(book)

        return category_books

    def update_book_details(self, book_title, new_details):
        for book in self.inventory:
            if book["title"] == book_title:
                for key, value in new_details.items():
                    if key in book:
                        book[key] = value

    def generate_report(self):
        total_books = len(self.inventory)
        categories = set(book["category"] for book in self.inventory)

        print("Inventory Report:")
        print("Total Number of Books:", total_books)
        print("Categories:", categories)


class ShoppingCart:

    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_items(self, book):
        for item in self.items:
            if item == book:
                item.quantity += book.get_quantity()
                break
            else:
                self.items.append(book)
            self.total_price += book.get_total_price()

    def remove_item(self, book):
        for item in self.items:
            if item == book:
                self.total_price -= item.get_total_price()
                self.items.remove(item)
                break

    def view_cart(self):
        for item in self.items:
            print("Title:", item['book'].title)
            print("Price:", item['book'].price)
            print("Quantity:", item['quantity'])
            print("Total Price:", item['book'].price * item['quantity'])
            print()

    def calculate_total(self):
        return self.total_price

    def empty_cart(self):
        self.items = []
        self.total_price = 0

    def update_quantity(self, book, new_quantity):
        for item in self.items:
            if item['bool'] == book:
                self.total_price -= item['book'].price * item['quantity']
                item['quantity'] = new_quantity
                self.total_price += item['book'].price * new_quantity
                break


class OrderProcessor:

    def __init__(self):
        self.orders = []

    def place_order(self, shopping_cart):
        order_id = self.generate_order_id()
        order_date = datetime.datetime.now()
        order = {
            "order_id": order_id,
            "order_date": order_date,
            "items": shopping_cart.items,
            "total_price": shopping_cart.total_price
        }
        self.orders.append(order)
        self.process_order(order)

    def generate_order_id(self):
        return uuid.uuid4()

    def process_order(self, order):
        for item in order['items']:
            item['book'].quantity -= item['quantity']

    def view_orders(self):
        for order in self.orders:
            self.print_order_details(order)

    def print_order_details(self, order):
        print("Order ID:", order["order_id"])
        print("Order Date:", order["order_date"])
        print("Items Purchased:")
        for item in order["items"]:
            print("Title:", item['book'].title)
            print("Price:", item['book'].price)
            print("Quantity:", item['quantity'])
            print("Total Price:", item['book'].price * item['quantity'])
            print()
        print("Total Price:", order["total_price"])

    def generate_report(self):
        total_orders = len(self.orders)
        total_sales = sum(order["total_price"] for order in self.orders)
        print("Total Orders:", total_orders)
        print("Total Sales:", total_sales)


if __name__ == '__main__':
    pass
