class InventoryManager:

    def __init__(self):
        self.inventory = []

    def add_book(self, book):
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
            if book.get_title() == book_title:
                book.set_quantity(book.get_quantity() + quantity)
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
