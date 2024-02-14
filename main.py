class Book:
    stock = []

    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.__quantity = quantity

    def add_bock(self, book):
        self.stock.append(book)



def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

