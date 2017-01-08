__author__ = 'jc449799'

FILE = "books.csv"


def main():
    print("Reading List 1.0 - by Srikaustubh Mandaleeka")
    book_list = []
    load_books(book_list)
    print("{} books loaded from {}".format(len(book_list), FILE))
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            print("Required Books:")
            num_of_required_books = required_books(book_list)
            if num_of_required_books == 0:
                print("No required books")
        elif choice.lower() == 'c':
            completed_books(book_list)
        elif choice.lower() == 'a':
            add_books(book_list)
        elif choice.lower() == 'm':
            complete_a_book(book_list)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>>")
    save_books(book_list)
    print("{} books have been saved to {}".format(len(book_list), FILE))
    print("Have a nice day :)")
    """
    end of main function
"""


def display_menu():
    # This function is used to display the options Menu
    MENU = "Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark Book as Complete \n" \
           "Q - Quit"
    print(MENU)
    """
    end of display_menu function
"""


def load_books(book_list):
    # this function is used to load the books from file to list
    book_file = open(FILE, 'r')
    for book in book_file:
        book_list.append(book.strip().split(','))
    book_file.close()
    """
        PSUDOCODE:
        book_file <- open(FILE, 'r')
        for book in book_file:
            book_list.append(book.strip().split(','))
        ENDFOR
        book_file.close()
    """
    """
    end of load_books()
"""


def complete_a_book(book_list):
    # This function is used to mark a book as completed in the file
    num_of_required_books = required_books(book_list)
    if num_of_required_books > 0:
        print("Enter the number of a book to mark as completed")
        int_checker = 0
        while int_checker == 0:
            try:
                num_of_book = int(input(">>>"))
                if num_of_book > len(book_list) - 1:
                    print("Book not in file")
                else:
                    if book_list[num_of_book][3] == 'c':
                        print("That book is already completed")
                    else:
                        book_list[num_of_book][3] = 'c'
                        print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
                    int_checker = 1
            except ValueError:
                print("Invalid input; enter a valid number")
    else:
        print("no required books")
    """
        PSUDOCODE:
        num_of_required_books =required_books(book_list)
        IF num_of_required_books > 0
            write "Enter the number of a book to mark as completed"
            int_checker <- 0
            WHILE int_checker == 0:
                TRY:
                    read num_of_book
                    IF book_list[num_of_book][3] = 'c':
                        write "That book is already completed"
                    ELSE:
                        book_list[num_of_book][3] <- 'c'
                        write title and author
                    int_checker = 1
                EXCEPT ValueError:
                    write "Invalid input; enter a valid number"
        ELSE
            write "No required books"
    """
    """
    end of complete_a_book()
"""


def required_books(book_list):
    # This function displays the list of books which need to be read
    total_pages = 0
    num_of_required_books = 0
    num_of_books = 0
    print("Required Books:")
    for book in book_list:
        if 'r' in book[3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(num_of_books, book[0], book[1], book[2]))
            total_pages += int(book[2])
            num_of_required_books += 1
        num_of_books += 1
    if num_of_required_books > 0:
        print("Total pages for {} books: {}".format(num_of_required_books, total_pages))
    return num_of_required_books
    """
    end of required_books function
"""


def completed_books(book_list):
    # This function is used to print all the completed books
    total_pages = 0
    print("Completed Books:")
    num_of_books = 0
    num_of_completed_books = 0
    for book in book_list:
        if 'c' in book[3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(num_of_books, book[0], book[1],
                                                                book[2]))
            total_pages += int(book[2])
            num_of_completed_books += 1
        num_of_books += 1
    if num_of_completed_books == 0:
        print("No completed books")
    else:
        print("Total pages for {} books: {}".format(num_of_completed_books, total_pages))
    """
    end of completed_books function
"""


def add_books(book_list):
    # This function will help us to add books to the file books.csv
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input can not be blank")
        author = input("Author:")
    int_checker = 0
    pages = 0
    while int_checker == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            int_checker = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list.append(book)
    """
    end of add_books function
"""


def save_books(books):
    # This function will help the program to save data into file books.csv
    books_file = open(FILE, 'w')
    for book in books:
        book_data = book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3]
        print(book_data, file=books_file)
    books_file.close()
    """
    end of save book function
"""


main()  # calling main function
