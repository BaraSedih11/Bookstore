class ShoppingCart:

    def __init__(self, inventory):
        self.books = []
        self.total_price = 0
        self.inventory = inventory

    def add_book(self, book):
        for item in self.books:
            if item.get_title == book.get_title():
                item.get_quantity += book.get_quantity()
                break
            else:
                self.books.append(book)
            self.total_price += book.get_total_price()

    def remove_book(self, book_title):
        for item in self.books:
            if item.get_title == book_title:
                self.total_price -= item.get_total_price()
                self.books.remove(item)
                break

    def view_cart(self):
        for item in self.books:
            print("Title:", item.get_title())
            print("Price:", item.get_price())
            print("Quantity:", item.get_quantity())
            print("Total Price:", item.get_total_price())
            print()

    def get_total_price(self):
        return self.total_price

    def empty_cart(self):
        self.books = []
        self.total_price = 0

    def update_quantity(self, book, new_quantity):
        for item in self.books:
            if item.get_title == book.get_title():
                self.total_price -= item.get_price() * item.get_quantity()
                item.set_quantity(new_quantity)
                self.total_price += item.get_price() * new_quantity
                break

    def get_books(self):
        return self.books
