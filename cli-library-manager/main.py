import json

class BookCollection:

    """A class to manage a collection of books and allow user to organize and store their books."""

    def __init__(self):

        """Initialize the BookCollection with an empty list of books and a storage file."""
        self.books_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):

        """Read the books data from the storage file."""
        try:
            with open(self.storage_file,"r") as file:
                self.books_list = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.books_list = []

    def save_to_file(self):

        """Save the books data to the storage file."""
        with open(self.storage_file,"w") as file:
            json.dump(self.books_list,file,indent=4)

    def create_new_book(self):

        """Add a new book to the collection."""
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_year = input("Enter book publication year: ")
        book_genre = input("Enter book genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": book_year,
            "genre": book_genre,
            "is_read": is_book_read
        }
        
        self.books_list.append(new_book)
        self.save_to_file()
        print(f"Book '{book_title}' has been added to your collection.")

    def delete_book(self):

            book_title = input("Enter the title of the book to delete: ")

            for book in self.books_list:
                if book["title"].lower() == book_title.lower():
                    self.books_list.remove(book)
                    self.save_to_file()
                    print(f"Book '{book_title}' has been deleted from your collection.")
                    return
            print(f"Book with title '{book_title}' not found in your collection.")
                    
    def search_book(self):

        search_book = input("Enter the title of the book to search for: ")

        for book in self.books_list:

            if book["title"].lower() == search_book.lower():
                print(f"Book found: \n{book['title']} by {book['author']} ({book['year']})")
                return
        print(f"Book with title '{search_book}' not found in your collection.")

    def display_books(self):

        if not self.books_list:
            print("Your collection is empty.")
            return
        print("\n📚 Your Book Collection 📚\n\n")
        print("-"*40)
        for book in self.books_list:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read: {'Yes' if book['is_read'] else 'No'}")
            print("-"*40)

    def update_book(self):
        """Modify the details of an existing book in the collection."""
    
        if not self.books_list:
            print("No books available in your collection.")
            return
    
        book_title = input("Enter the title of the book you want to edit: ").strip().lower()

        for book in self.books_list:
            if book.get("title", "").lower() == book_title:
                print("\nLeave blank to keep existing value.")

                new_title = input(f"New title ({book.get('title', 'Unknown')}): ").strip()
                new_author = input(f"New author ({book.get('author', 'Unknown')}): ").strip()
                new_year = input(f"New year ({book.get('year', 'Unknown')}): ").strip()
                new_genre = input(f"New genre ({book.get('genre', 'Unknown')}): ").strip()
                read_status = input("Have you read this book? (yes/no): ").strip().lower()

                # Update fields only if a new value is provided
                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                if new_year.isdigit():  # Ensures valid numeric input for the year
                    book["year"] = int(new_year)
                if new_genre:
                    book["genre"] = new_genre
                if read_status in ["yes", "no"]:  # Ensures a valid boolean value
                    book["read"] = read_status == "yes"

                self.save_to_file()
                print("\nBook updated successfully!\n")
                return

        print("\nBook not found!\n")

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        
        total_books = len(self.books_list)
        
        if total_books == 0:
            print("Your book collection is empty. Start adding books to track your reading progress!\n")
            return

        # Count books marked as 'read'
        completed_books = sum(1 for book in self.books_list if book.get("read", False))
        unread_books = total_books - completed_books

        # Calculate completion rate
        completion_rate = (completed_books / total_books) * 100

        print(f"📚 Total books in collection: {total_books}")
        print(f"✅ Books read: {completed_books}")
        print(f"📖 Books unread: {unread_books}")
        print(f"📊 Reading progress: {completion_rate:.2f}%\n")


    def exit(self):
        print("Exiting the application... \n Thank you for using the application! \n")
        self.save_to_file()
        exit()

    def start_application(self):

        while True:
            print("\n📚 Welcome to the Book Collection Application 📚")
            print("1. Add a new book")
            print("2. Display all books")
            print("3. Delete a book")
            print("4. Search for a book")
            print("5. Update a book")
            print("6. Show reading progress")
            print("7. Exit")

            user_choice = input("Enter your choice(1-5): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.display_books()
            elif user_choice == "3":
                self.delete_book()
            elif user_choice == "4":
                self.search_book()
            elif user_choice == "5":
                self.update_book()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.exit()
            else:
                print("Invalid choice. Please try again.\n")
                
if __name__ == "__main__":
    app = BookCollection()
    app.start_application()

        
            
