from custom_classes import Book, DVD, LibraryCollection, MediaItem

def run_simple_library():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    dvd1 = DVD("Inception", "Christopher Nolan", 148)
    library = LibraryCollection()
    library.add_item(book1)
    library.add_item(dvd1)

    library.list_available()
    print(dvd1)

    print(book1.checkout())
    print(book1.checkout())  # Attempt to checkout again
    print(dvd1.checkout()) 
    library.list_available()
if __name__ == "__main__":    
    run_simple_library()