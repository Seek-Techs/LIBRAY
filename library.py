class Library:
    def __init__(self):
        self.shelf = {}
        #self.book_name = book_name

    def add_book(self, book_name, rating=67):
        self.shelf[book_name] = rating
        #return self.shelf 

    def change_book_rating(self, book_name, rating=56):
        #self.shelf[book_name] = rating
        
        if book_name in self.shelf:
            self.shelf[book_name] = rating
            return self.shelf
        
        return 'Book not found'

    def get_all_books(self):
        return self.shelf

    def delete_book(self, book_name):
        self.shelf.pop(book_name)
        return self.shelf

    def get_book_by_name(self, book_name):
        if book_name in self.shelf:
            return book_name

        return 'It does not exist'

    
a = Library()
print(a.add_book('wale', 7))
print(a.add_book('waless', 7))
print(a.change_book_rating('walea', 8))
print(a.get_all_books())
#print(a.delete_book('wale'))
print(a.get_book_by_name('waless'))