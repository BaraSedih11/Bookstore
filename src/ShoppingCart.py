from src.InventoryManager import InventoryManager
from src.Book import Book


class ShoppingCart:
    """
    Represents a shopping cart for holding books.
    """

    def __init__(self, inventory):
        """
        Initializes the shopping cart.

        Args:
            inventory (InventoryManager): The inventory from which books are sourced.
        """
        if not isinstance(inventory, InventoryManager):
            raise TypeError("Inventory must be an instance of InventoryManager")
        self._books = []
        self._total_price = 0
        self._inventory = inventory

    def add_book(self, book):
        """
        Adds a book to the shopping cart.

        If the book is already in the cart, its quantity is updated. Otherwise, the book is added.

        Args:
            book (Book): The book to add to the cart.
        """
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        for item in self._books:
            if item.title == book.title:
                item.quantity += book.quantity
                break
        else:
            self._books.append(book)
        self.update_total_price()

    def remove_book(self, book_title, quantity):
        """
        Removes a specific quantity of a book from the shopping cart.

        Args:
            book_title (str): The title of the book to remove from the cart.
            quantity (int): The quantity of the book to remove.
        """
        if not isinstance(book_title, str):
            raise TypeError("Book title must be a string")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if self.search_book(book_title) is None:
            raise ValueError("Book title must be in the shopping cart")

        for item in self._books:
            if item.title == book_title:
                if item.quantity <= quantity:
                    self._books.remove(item)
                else:
                    item.quantity -= quantity
                break

        self.update_total_price()

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        for item in self._books:
            print("Title:", item.title)
            print("Price:", item.price)
            print("Quantity:", item.quantity)
            print("Total Price:", item.get_total_price())
            print()

    @property
    def total_price(self):
        """
        Total price of all books in the shopping cart.
        """
        return self._total_price

    def update_total_price(self):
        self._total_price = 0
        for book in self._books:
            self._total_price += book.quantity * book.price

    def empty_cart(self):
        """
        Empties the shopping cart.
        """
        self._books = []
        self.update_total_price()

    def update_quantity(self, book, new_quantity):
        """
        Updates the quantity of a book in the shopping cart.

        Args:
            book (Book): The book whose quantity is to be updated.
            new_quantity (int): The new quantity of the book.
        """
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("New quantity must be a non-negative integer")
        for item in self._books:
            if item.title == book.title:
                item.quantity = new_quantity
                break

        self.update_total_price()

    @property
    def books(self):
        """
        List of books in the shopping cart.
        """
        return self._books

    @property
    def inventory(self):
        """
        Inventory associated with the shopping cart.
        """
        return self._inventory

    @books.setter
    def books(self, new_books):
        """
        Setter for the list of books in the shopping cart.

        Args:
            new_books (list): The new list of books.
        """
        if not isinstance(new_books, list):
            raise TypeError("Books must be provided as a list")
        if not all(isinstance(book, Book) for book in new_books):
            raise TypeError("Invalid type for items in 'books'. Expected Book objects.")

        self._books = []

        for book in new_books:
            self.add_book(book)

        self.update_total_price()

    def search_book(self, book_title):
        """
        Search for a book by title.

        Args:
            book_title (str): The title of the book to search for.

        Returns:
            Book or None: The book object if found, None otherwise.
        """
        if not isinstance(book_title, str):
            raise TypeError("book_title must be a string")
        for book in self._books:
            if book.title == book_title:
                return book
        return None
