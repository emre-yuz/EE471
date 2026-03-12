class MediaItem():
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return f"Successful checkout of '{self.title}'."
        else:
            return f"'{self.title}' is already out."

    def __str__(self):
        return f"{self.title} by {self.author} is {'available' if self.is_available else 'not available' }."
    
class Book(MediaItem):
    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (Pages: {self.page_count}) is {'available' if self.is_available else 'not available' }."
    
class DVD(MediaItem):
    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        print("Handle with care: Do not scratch the disc.")
        return f"{super().checkout()} Duration: {self.duration} minutes."
    
class LibraryCollection():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_available(self):
        print("---- Available items in the library: ----")
        for item in self.items:
            if item.is_available:
                print(item)
            else:
                print(f"{item.title} is currently checked out.")