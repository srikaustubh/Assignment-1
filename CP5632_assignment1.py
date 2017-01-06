__author__ = 'jc449799'

FILE = "books.csv"

def main():
    print("Reading List 1.0 - by Srikaustubh Mandaleeka")
    book_list = []
    load_books(book_list)
    print(book_list)
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            print("Required Books:")
            required_books(book_list)
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
    print("{} books have been saved to {}".format(len(book_list),FILE))
    print("Have a nice day :)")


def display_menu():
# This function is used to display the options Menu

    MENU = "Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark Book as Complete \nQ - Quit"
    print(MENU)



# end of display_menu function

def load_books(book_list):
# load book function is used to load books from file to the list
    book_file = open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    book_file.close()
    # psudocode for load_books() function
    """
    book_file <- open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    ENDFOR
    book_file.close()
"""


def save_books(books):
# This function will help the program to update data into file books.csv
    books_file = open(FILE, 'w')
    for i in books:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file=books_file)
    books_file.close()

# end of save book function

def required_books(book_list):
# This function displays the list of books which need to be read
    total_pages = 0
    flag =0
    count = 0
    print("Required Books:")
    for i in book_list:
        if 'r' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            flag +=1
        count += 1

    if flag ==0:
        print("No required books")
    else:
        print("Total pages for {} books: {}".format(count - 1, total_pages))
    return flag


# end of required_books function

def completed_books(book_list):
# This function is used to print all the completed books
    total_pages = 0
    print("Completed Books:")
    count = 0
    count2 = 0
    for i in book_list:
        if 'c' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count2+=1
        count += 1
    print("Total pages for {} books: {}".format(count2 , total_pages))


# end of completed_books function


def complete_a_book(book_list):
# this function is used to mark a book as complete
    f = required_books(book_list)
    if f >0:
        print("Enter the number of a book to mark as completed")
        flag =0
        while flag == 0:
            try:
                num_of_book = int(input(">>>"))
                if book_list[num_of_book][3] == 'c':
                    print("That book is already completed")
                else:
                    book_list[num_of_book][3] = 'c'
                    print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
                flag=1
            except ValueError:
                print("Invalid input; enter a valid number")
    """
    required_books(book_list)
    write "Enter the number of a book to mark as completed"
    try:
        read num_of_book
        IF book_list[num_of_book][3] = 'c':
            write "That book is already completed"
        ELSE:
            book_list[num_of_book][3] <- 'c'
            save_books(book_list)
            write title and author
    except ValueError:
        write "Invalid input; enter a valid number"
        complete_a_book(book_list)
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
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list.append(book)

# end of add_books function

main()  # calling main funtion