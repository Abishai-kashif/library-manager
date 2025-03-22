import questionary
from helper.menu_option import MenuOptionsHelper

print('\n\n===============> Welcome to the Library Manager <===============\n\n')


def main():

    while True :
        answer = questionary.select(
            'What do you want to do?',
            choices=['Add a Book', 'Remove a Book', 'Search for a Book', 'Display all Books', 'Display statistics', 'Exit']
        ).ask()

        
        if answer == 'Add a Book':
            MenuOptionsHelper.add_book()
        elif answer == 'Remove a Book':
            MenuOptionsHelper.remove_books()
        elif answer == 'Search for a Book':
            MenuOptionsHelper.search_book()
        elif answer == 'Display all Books':
            MenuOptionsHelper.displayAllBooks()
        elif answer == 'Display statistics':
            MenuOptionsHelper.displayStatistics()
        else:
            break



main()