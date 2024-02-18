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

