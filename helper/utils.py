import json 

def load_books():
    with open('data/books.json', 'r', encoding="utf-8") as file:
        try :
            return list(json.load(file))
        except Exception as e:
            print("Something went wrong! when loading books: ", e)
            return []
        
        
        
def add_line(no_of_lines=1):
    print('\n' * no_of_lines)
