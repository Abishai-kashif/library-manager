import questionary
import json
from  helper.utils import add_line, load_books


class MenuOptionsHelper:

    @staticmethod
    def displayAllBooks():

        books = load_books()

        add_line()
        print('__________________ All Books __________________')
        add_line()
        for idx, book in enumerate(books):
            print(f'{idx + 1}. {book["title"]}')
        add_line(2)


            

    @staticmethod
    def add_book():
        book = questionary.form(
            title=questionary.text("Enter the book title: ", validate=lambda res: str(res).strip() != ''),
            author=questionary.text("Enter the author: ", validate=lambda res: str(res).strip() != ''),
            publication_year=questionary.text("Enter the publication year: ", validate=lambda res: str(res).strip().isdigit()),
            genre=questionary.text("Enter the genre: ", validate=lambda res: str(res).strip() != ''),
            read_status=questionary.confirm("Have you read this book? ", default=True),
        ).ask()

        books = load_books()


        books.append(book)


        with open('data/books.json', 'w', encoding="utf-8") as file:
            try:
                json.dump(books, file, indent=4)
            except Exception as e:
                print("Something went wrong! when saving books: ", e)

        add_line(2)
        print('Book added successfully ✅')
        add_line()

    @staticmethod
    def remove_books():
        books = load_books()

        booksToRemove = questionary.checkbox(
            'Choose the books you want to remove: ',
            choices=[book['title'] for book in books]
        ).ask()

        books = list(filter(lambda book: book["title"] not in (booksToRemove or []), books))


        with open('data/books.json', 'w', encoding="utf-8") as file:
            try:
                json.dump(books, file, indent=4)
            except Exception as e:
                print("Something went wrong! when saving books: ", e)



        add_line(2)
        print('Books removed successfully 🚮')
        add_line()

    @staticmethod
    def search_book():
        search_by = questionary.select(
            'search by?',
            choices=['title', 'author', 'genre']
        ).ask()

        search_term = questionary.text(f'Enter the {search_by}: ', validate=lambda res: str(res).strip() != '').ask()

        add_line(2)

        term = search_term.lower().strip()

        books = load_books()
        
        results = [book for book in books if book[search_by].lower().strip().startswith(term)]

        print('Books for query:', search_term)
        add_line()

        for idx, book in enumerate(results):
            print(f'{idx + 1}. {book["title"]}')
        
        add_line()


    @staticmethod
    def displayStatistics():
        books = load_books()

        total_books = len(books)
        
        percentage_read: int = (len([ book for book in books if book['read_status'] ]) / total_books) * 100

        add_line()

        print(f'Total Books: { total_books }')
        print(f'Percentage read: { percentage_read.__round__(2)  }%')
        add_line()