class Library:
    def __init__(self):
        self.available_book = {}

    def add_book(self, book_name, book_rating):
        if book_name not in self.available_book.keys():
            book = {}
            book[book_name] = book_rating
            self.available_book[book_name] = book
        else:
            print(f'{book_name} book already in the Library with Book ratings {self.available_book.get(book_name)}')
        
    def change_book_rating(self, book_name, new_rating):
        if book_name not in self.available_book.keys():
            print(f'\n{book_name} Book does not exist in the Library')
        else:
            book = self.available_book.get(book_name)
            book[book_name] = new_rating
            print(f'\n{book_name} Book rating updated to {new_rating}')

    def get_all_books(self):
        print(f'\n{self.available_book}')

    def delete_book(self, book_name):
        if book_name not in self.available_book.keys():
            print(f'\n{book_name} Book does not exist in the Library')
        else:
            self.available_book.pop(book_name)
            print(f'\n{book_name} Book has been deleted from the Library.')
        
    def get_book_by_name(self, book_name):
        if book_name not in self.available_book.keys():
            print(f'\n{book_name} Book does not exist in the Library.')
        else:
            book = self.available_book.get(book_name)
            print('\nHere is the', book)
            
    def get_book_by_ratings(self, book_ratings):
        books = self.available_book.values()
        book_same_rating = {}
        for book in books:
            if book_ratings in book.values():
                book_same_rating.update(book)
        print('\nNo Book has the rating of %s' %(book_ratings) if book_same_rating == {} else print(book_same_rating))

    
library = Library()

library.add_book(book_name='Atomic Habits', book_rating=7)

library.add_book(book_name='Atomic Habits', book_rating=7)

library.add_book(book_name='Think and Grow Rich', book_rating=7.58)

library.add_book(book_name='100 Days of Coding', book_rating=8.5)

library.add_book(book_name='Automate the Boring Stuff', book_rating=9.5)

library.get_all_books()

library.add_book(book_name='Python', book_rating=9.5)

library.change_book_rating(book_name='waless', new_rating=8)

library.change_book_rating(book_name='Atomic Habits', new_rating=8)

library.get_all_books()

library.delete_book(book_name='wale')

library.delete_book(book_name='Python')

library.get_book_by_name(book_name='waless')

library.get_book_by_name(book_name='Atomic Habits')

library.get_all_books()