# LIST OF BORROWERS FUNCTIONS
import DEVILLES_logbook_section
# Borrow Book
def borrow_book(book_dict, log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("-----------------------------------BORROW BOOK---------------------------------")
    print("SYSTEM: Fantastic choice Adventurer. It seems like you want to learn!\nPlease fill up the information needed for you to borrow a book.\n")

    # TASK 2 - Ask for book details (title, author)
    print("\nPlease fill up the information needed for you to borrow a book.\n")
    book_title = input("BOOK TITLE: ").upper()
    book_author = input("BOOK AUTHOR: ").upper()
    # TASK 3 - Create borrow list entry

    is_available = 0
    book_id = ""
    for book in book_dict:
        if book_dict[book][0][0] == book_title and book_dict[book][0][1] == book_author and book_dict[book][1] == "AVAILABLE":
            book_id = book
            is_available += 1
            continue
        
        
    if is_available != 0:
        # TASK 4 - Ask date of return
        book_return = input("DATE OF RETURN (e.g. 9 Jan 2020): ").upper()
        # TASK 5 - Produce borrow_id (BL#)

        borrow_num = 1
        while ("BL" + str(borrow_num)) in borrow_dict:
            borrow_num += 1
        borrow_id = "BL"+str(borrow_num)

        # TASK 1 - Create Logbook Entry
        log_id = DEVILLES_logbook_section.visit_library(log_dict)

        # TASK 6 - Append borrow_id to list of borrowers in books_dict

        borrow_dict[borrow_id] = [book_id, log_id, book_return]
        book_dict[book_id][2].append(borrow_id)

        # TASK 7 - Update book status to "Unavailable"
        book_dict[book_id][1] = "UNAVAILABLE"

        print("\nSYSTEM: Book BORROWED! Read It, Enjoy It, and Take Care of It!")
        print("===============================================================================")
    else:
        print("\nSYSTEM: Book NOT found. Make sure to check if the details are \ncorrect and if the book EXISTS or is AVAILABLE in our library")
        print("===============================================================================")
        
    

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(log_dict)
    print(borrow_dict)

# Return Book
def return_book(book_dict, log_dict):
    print("_______________________________________________________________________________")
    print("-----------------------------------RETURN BOOK---------------------------------")
    print("SYSTEM: Returning a book Adventurer? I hope you've read it well!\nPlease fill up the information needed for you to return a book.\n")
    # TASK 1 - Update Status to "Available"
    book_title = input("BOOK TITLE: ").upper()
    book_author = input("BOOK AUTHOR: ").upper()

    is_borrowed = 0
    is_found = False
    for book in book_dict:
        if book_dict[book][0][0] == book_title and book_dict[book][0][1] == book_author:
            if book_dict[book][1] == "AVAILABLE":
                print("\nSYSTEM: Book is NOT borrowed. The book is in our shelves.\nIf you've borrowed a duplicate, please update the details.")
                print("===============================================================================")
                is_found = True
            else:
                book_dict[book][1] = "AVAILABLE"
                DEVILLES_logbook_section.visit_library(log_dict)

                is_borrowed += 1
                is_found = True
        
    if is_borrowed != 0:
        print("\nSYSTEM: Thank you for returning the book, Adventurer!")
        print("===============================================================================")
    if is_found == False:
        print("\nSYSTEM: Book NOT identified. Make sure to check if the details are \ncorrect and if the book exists in our library")
        print("===============================================================================")
        return
        
    # TEST - Delete/Comment Later.
    print(book_dict)
    print(log_dict)
    

# View All Entries
def view_all_entries(book_dict, log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("--------------------------------VIEW ALL ENTRIES-------------------------------")
    print("SYSTEM: It looks like you're interested to see all the people who've\n borrowed a book, Adventurer. Here you go, these are all the data we have.")
    # TASK 1 - Print all borrow_dict entries    
    # TASK 2 - Information to show = borrow_id, title, author, date published, date return, borrower

    is_borrowed = 0
    number_of_borrow = 1
    for borrower in borrow_dict:
        book_id = borrow_dict[borrower][0]
        log_id = borrow_dict[borrower][1]
        if book_id in book_dict and log_id in log_dict:
            print(f"[{number_of_borrow}.] _________________________________________________")
            print(f"BORROW ID      : {borrower}")
            print("BOOK TITLE     : " + book_dict[book_id][0][0])
            print("BOOK AUTHOR    : " + book_dict[book_id][0][1])
            print("DATE PUBLISHED : " + book_dict[book_id][0][2])
            print("DATE OF RETURN : " + borrow_dict[borrower][2])
            print("BORROWER       : " + log_dict[log_id][0])

        is_borrowed += 1
        number_of_borrow += 1
    
    if is_borrowed !=0:
        print("\nSYSTEM: I hope that we've satisfied your curiosity!")
        print("===============================================================================")
    else:
        print("\nSYSTEM: It looks like there is NO history of books borrowed.")
        print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(log_dict)
    print(borrow_dict)





# View Expected Returns
def view_expected_return(book_dict, log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("------------------------------VIEW EXPECTED RETURNS----------------------------")
    print("SYSTEM: Looking for the borrower of a book you want, Adventurer?\nI can show you who'll return a book on a specific date!")
    print("Direction: Enter the expected Date of Return (e.g. 9 Jan 2020)")
    print("-------------------------------------------------------------------------------")
    expected_date = input("USER INPUT: ").upper()

    # TASK - print these information [borrow_id, title, author, date published, status, borrower]
    is_borrowed = 0
    number_of_borrow = 1
    for borrower in borrow_dict:
        book_id = borrow_dict[borrower][0]
        log_id = borrow_dict[borrower][1]
        if expected_date == borrow_dict[borrower][2] and book_dict[book_id][1] == "UNAVAILABLE":
            print(f"[{number_of_borrow}.] _________________________________________________")
            print(f"BORROW ID      : {borrower}" )
            print("BOOK TITLE     : " + book_dict[book_id][0][0])
            print("BOOK AUTHOR    : " + book_dict[book_id][0][1])
            print("DATE PUBLISHED : " + book_dict[book_id][0][2])
            print("STATUS         : " + book_dict[book_id][1])
            print("BORROWER       : " + log_dict[log_id][0])

            is_borrowed += 1
            number_of_borrow += 1

    if is_borrowed != 0:
        print("\nSYSTEM: I hope that we've satisfied your curiosity!")
        print("===============================================================================")
    else:
        print(f"\nSYSTEM: There's NOTHING to be returned on {expected_date}.\nTry checking if you inputted the correct date.")
        print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(log_dict)
    print(borrow_dict)

# TESTING AREA
        
# borrow_list_dictionary = {
#     # Borrow_ID (BL#) : [Book_ID, Log_ID, Date Return]
# }