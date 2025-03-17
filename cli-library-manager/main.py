import json

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

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
            with open(self.storage_file, "r") as file:
                data = file.read().strip()  # Read and strip empty spaces
                if data:  # Ensure it's not an empty file
                    self.books_list = json.loads(data)
                else:
                    self.books_list = []
            
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = []


    def save_to_file(self):
        """Save the books data to the storage file."""
        

        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.books_list, file, indent=4)
            print(Fore.GREEN + "✅ Data successfully saved to books_data.json!")
        except Exception as e:
            print(Fore.RED + f"❌ Error saving file: {e}")
    def create_new_book(self):

        """Add a new book to the collection."""
        book_title = input(Fore.YELLOW +"\nEnter book title: ")
        book_author = input(Fore.YELLOW +"Enter book author: ")
        book_year = input(Fore.YELLOW +"Enter book publication year: ")
        book_genre = input(Fore.YELLOW +"Enter book genre: ")
        is_book_read = input(Fore.YELLOW +"Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": book_year,
            "genre": book_genre,
            "is_read": is_book_read
        }
        
        self.books_list.append(new_book)
        self.save_to_file()
        print(Fore.GREEN +f"\nBook '{book_title}' has been added to your collection.")

    def delete_book(self):

            book_title = input(Fore.BLUE +"\nEnter the title of the book to delete: ")

            for book in self.books_list:
                if book["title"].lower() == book_title.lower():
                    self.books_list.remove(book)
                    self.save_to_file()
                    print(Fore.CYAN +f"\nBook '{book_title}' has been deleted from your collection.")
                    return
            print(Fore.RED +f"\nBook with title '{book_title}' not found in your collection.")
                    
    def search_book(self):

        search_book = input(Fore.CYAN+"\nEnter the title of the book to search for: ")

        for book in self.books_list:

            if book["title"].lower() == search_book.lower():
                print(Fore.BLUE+f"\nBook found: \n{book['title']} by {book['author']} ({book['year']})")
                return
        print(Fore.RED +f"\nBook with title '{search_book}' not found in your collection.")

    def display_books(self):

        if not self.books_list:
            print(Fore.RED +"\nYour collection is empty.")
            return
        print(Fore.LIGHTBLUE_EX +"\n📚 Your Book Collection 📚\n\n")
        print("-"*40)
        for book in self.books_list:
            print(Fore.LIGHTGREEN_EX+ f"Title: {book['title']}")
            print(Fore.LIGHTGREEN_EX+ f"Author: {book['author']}")
            print(Fore.LIGHTGREEN_EX+ f"Year: {book['year']}")
            print(Fore.LIGHTGREEN_EX+ f"Genre: {book['genre']}")
            print(Fore.LIGHTGREEN_EX+ f"Read: {'Yes' if book['is_read'] else 'No'}")
            print("-"*40)

    def update_book(self):
        """Modify the details of an existing book in the collection."""
    
        if not self.books_list:
            print(Fore.RED +"\nNo books available in your collection.")
            return
    
        book_title = input(Fore.LIGHTBLACK_EX +"\nEnter the title of the book you want to edit: ").strip().lower()

        for book in self.books_list:
            if book.get("title", "").lower() == book_title:
                print(Fore.RED +"\nLeave blank to keep existing value.")

                new_title = input(Fore.GREEN +f"New title ({book.get('title', 'Unknown')}): ").strip()
                new_author = input(Fore.GREEN +f"New author ({book.get('author', 'Unknown')}): ").strip()
                new_year = input(Fore.GREEN +f"New year ({book.get('year', 'Unknown')}): ").strip()
                new_genre = input(Fore.GREEN +f"New genre ({book.get('genre', 'Unknown')}): ").strip()
                read_status = input(Fore.GREEN +"Have you read this book? (yes/no): ").strip().lower()

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
                    book["is_read"] = read_status == "yes"

                self.save_to_file()
                print(Fore.BLUE +"\nBook updated successfully!\n")
                return

        print(Fore.RED +"\nBook not found!\n")

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        
        total_books = len(self.books_list)
        
        if total_books == 0:
            print(Fore.RED +"\nYour book collection is empty. Start adding books to track your reading progress!\n")
            return

        # Count books marked as 'read'
        completed_books = sum(1 for book in self.books_list if book.get("read", False))
        unread_books = total_books - completed_books

        # Calculate completion rate
        completion_rate = (completed_books / total_books) * 100

        print(Fore.CYAN+f"\n📚 Total books in collection: {total_books}")
        print(Fore.CYAN+f"\n✅ Books read: {completed_books}")
        print(Fore.CYAN+f"\n📖 Books unread: {unread_books}")
        print(Fore.CYAN+f"\n📊 Reading progress: {completion_rate:.2f}%\n")


    def exit(self):
        print(Fore.RED +"\nExiting the application... \n Thank you for using the application! \n")
        self.save_to_file()
        exit()

    def start_application(self):

        while True:
            print(Fore.LIGHTMAGENTA_EX+"\n📚 Welcome to the Book Collection Application 📚\n")
            print(Fore.LIGHTMAGENTA_EX+"1. Add a new book")
            print(Fore.LIGHTMAGENTA_EX+"2. Display all books")
            print(Fore.LIGHTMAGENTA_EX+"3. Delete a book")
            print(Fore.LIGHTMAGENTA_EX+"4. Search for a book")
            print(Fore.LIGHTMAGENTA_EX+"5. Update a book")
            print(Fore.LIGHTMAGENTA_EX+"6. Show reading progress")
            print(Fore.LIGHTMAGENTA_EX+"7. Exit")

            user_choice = input(Fore.RED +"\nEnter your choice(1-7): ")

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
                print(Fore.RED +"\nInvalid choice. Please try again.\n")
                
if __name__ == "__main__":
    app = BookCollection()
    app.start_application()

        
            
