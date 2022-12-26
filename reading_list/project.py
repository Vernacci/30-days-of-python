# day 12 project

reading_list = {}

while True:
    book_title_input = input('Type the book title: ')
    book_author_input = input('Type the author of the book: ')
    year_input = input('type the year of publication: ')
    user_repeat = input('Do you want to add another book? (Y/n)').lower()
    if user_repeat == 'n':
        break
