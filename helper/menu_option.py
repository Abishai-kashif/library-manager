import questionary

books = [
    {'title': 'the fellowship of the ring', 'author': 'j.r.r. tolkien', 'publication_year': 1954, 'genre': 'fantasy', 'read_status': True},
    {'title': 'the two towers', 'author': 'j.r.r. tolkien', 'publication_year': 1955, 'genre': 'fantasy', 'read_status': True},
    {'title': 'the return of the king', 'author': 'j.r.r. tolkien', 'publication_year': 1956, 'genre': 'fantasy', 'read_status': True},
    {'title': 'the hobbit', 'author': 'j.r.r. tolkien', 'publication_year': 1937, 'genre': 'fantasy', 'read_status': False},
    {'title': 'the hunger games', 'author': 'suzanne collins', 'publication_year': 2008, 'genre': 'dystopian', 'read_status': False},
]


class MenuOptionsHelper:

    @staticmethod
    def displayAllBooks():
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

        books.append(book)

        add_line(2)
        print('Book added successfully ✅')
        add_line()

    @staticmethod
    def remove_book():
        title = questionary.select(
            'Select the book you want to remove',
            choices=[book['title'] for book in books]
        ).ask()

        books.remove([book for book in books if book['title'] == title][0])

        add_line(2)
        print('Book removed successfully 🚮')
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
        
        results = [book for book in books if book[search_by].lower().strip().startswith(term)]

        print('Books for query:', search_term)
        add_line()

        for idx, book in enumerate(results):
            print(f'{idx + 1}. {book["title"]}')
        
        add_line()


    @staticmethod
    def displayStatistics():
        total_books = len(books)
        # This will calculate the percentage of books that have been read
        # by dividing the number of books that have been read by the total number of books
        # and then multiplying by 100
        percentage_read: int = (len([ book for book in books if book['read_status'] ]) / total_books) * 100

        add_line()

        print(f'Total Books: { total_books }')
        print(f'Percentage read: { percentage_read.__round__(2)  }%')
        add_line()


def add_line(no_of_lines=1):
    print('\n' * no_of_lines)
