# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size

    def __str__(self):
        """String representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count

    def __str__(self):
        """String representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


# The following part should be in main.py for testing
if __name__ == "__main__":
    from library_system import Book, EBook, PrintBook, Library

    def main():
        # Create a Library instance
        my_library = Library()

        # Create instances of each type of book
        classic_book = Book("Pride and Prejudice", "Jane Austen")
        digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
        paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

        # Add books to the library
        my_library.add_book(classic_book)
        my_library.add_book(digital_novel)
        my_library.add_book(paper_novel)

        # List all books in the library
        my_library.list_books()

    main()

