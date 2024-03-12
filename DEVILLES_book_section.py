# BOOK SECTION FUNTIONS

# Add Book
def add_book(book_dict):
    print("_______________________________________________________________________________")
    print("------------------------------------ADD BOOK-----------------------------------")
    print("SYSTEM: A new book Archon? It is my pleasure to add it to the library.\nPlease fill up the information needed.\n")
    book_title = input("BOOK TITLE: ").upper()
    book_author = input("BOOK AUTHOR: ").upper()
    book_date_published = input("DATE PUBLISHED (e.g. 9 Jan 2020): ").upper()
    book_status = "AVAILABLE"
    book_list_of_borrowers = []

    book_num = 1
    while ("B" + str(book_num)) in book_dict:
        book_num += 1
    book_id = "B"+str(book_num)

    # ADDS LOG TO LOGBOOK
    book_dict[book_id] = [[book_title, book_author, book_date_published], book_status, book_list_of_borrowers ]

    print("\nSYSTEM: Book ADDED! Thank you for adding a book to our library!")
    print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)


# Delete Book
def delete_book(book_dict,borrow_dict):
    print("_______________________________________________________________________________")
    print("----------------------------------DELETE BOOK----------------------------------")
    print("SYSTEM: \What book would you like to delete Archon?\nPlease fill up the information needed.\n")
    book_title = input("BOOK TITLE: ").upper()
    book_author = input("BOOK AUTHOR: ").upper()

    is_removed = False
    for book_id in list(book_dict.keys()):
        if book_dict[book_id][0][0] == book_title and book_dict[book_id][0][1] == book_author :
            del book_dict[book_id]
            for borrower in list(borrow_dict.keys()):
                if borrow_dict[borrower][0] not in book_dict:
                    del borrow_dict[borrower]
            is_removed = True
            break

    if is_removed == True:
        print("\nSYSTEM: The book is REMOVED from the library")
        print("===============================================================================")
    else:
        print("\nSYSTEM: The book is NOT REMOVED. Make sure to check if the details\nare correct and if the book exists in our library")
        print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)


# Delete All Books
def delete_all_books(book_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("--------------------------------DELETE ALL BOOK--------------------------------")
    print("SYSTEM: Archon, you are about to delete all books!\nAre you sure that this is what you want?\n")
    print("Direction: Type the number of choice.")
    print("[1] YES. Delete all books")
    print("[2] NO. It was just a mistake. Sorry")
    confirm_delete = input("ARCHON INPUT: ")

    if confirm_delete == "1":
        for book in list(book_dict.keys()):
            del book_dict[book]

            for borrower in list(borrow_dict.keys()):
                if borrow_dict[borrower][0] not in book_dict:
                    del borrow_dict[borrower]



        print("\nSYSTEM: I've DELETED all the books Archon. I hope that there'll\nbe a day that the library will be filled with books once again.")
        print("===============================================================================")

    elif confirm_delete == "2":
        print("\nSYSTEM: Phew! I thought you're really going to delete all books!")
        print("===============================================================================")
    else:
        print("\nERROR: Invalid Choice, Please Choose Again.")
        print("===============================================================================")
        
    # TEST - Delete/Comment Later.
    print(book_dict)


# View Book
def view_book(book_dict,log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("-----------------------------------VIEW BOOK-----------------------------------")
    print("SYSTEM: Searching for a book? I got you Adventurer!\nPlease fill up the information needed.\n")
    book_title = input("BOOK TITLE: ").upper()
    
    for book in book_dict:
        if book_dict[book][0][0] == book_title:
            print("SYSTEM: We found the book! Here are some information about it.")
            print("BOOK ID        : " + book)
            print("BOOK TITLE     : " + book_dict[book][0][0])
            print("BOOK AUTHOR    : " + book_dict[book][0][1])
            print("DATE PUBLISHED : " + book_dict[book][0][2])
            print("BOOK STATUS    : " + book_dict[book][1])

            # List of Borrowers
            borrowers = []
            for borrower in book_dict[book][2]:
                borrower_log_id = borrow_dict[borrower][1]
                borrower_name = log_dict[borrower_log_id][0]
                borrowers.append(borrower_name)

            print(f"BORROWERS      : {borrowers}")
            print("\nSYSTEM: I hope that we satisfied your curiosity Adventurer!")
            print("===============================================================================")
            return
    
    print("\nSYSTEM: Book NOT found. Make sure to check if the details are \ncorrect and if the book exists in our library")
    print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(borrow_dict)


# Edit Book
def edit_book(book_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("-----------------------------------EDIT BOOK-----------------------------------")
    print("SYSTEM: You want to edit a book, Archon? No problem, We can do it!\nPlease fill up the information needed.\n")
    book_title = input("BOOK TITLE: ").upper()
    
    for book in book_dict:
        if book_dict[book][0][0] == book_title:
            print("\nSYSTEM: We found the book! Here's the current information about the book.")
            print("BOOK TITLE     : " + book_dict[book][0][0])
            print("BOOK AUTHOR    : " + book_dict[book][0][1])
            print("DATE PUBLISHED : " + book_dict[book][0][2])

            print("\nSYSTEM: Now you can change some its information.")
            book_dict[book][0][0] = input("BOOK TITLE: ").upper()
            book_dict[book][0][1] = input("BOOK AUTHOR: ").upper()
            book_dict[book][0][2] = input("DATE PUBLISHED (e.g. 9 Jan 2020): ").upper()
            
            print("\nSYSTEM: The book is EDITED. Thank you Archon!")
            print("===============================================================================")
            return
    
    print("\nSYSTEM: Book NOT found. Make sure to check if the details are \ncorrect and if the book exists in our library")
    print("===============================================================================")

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(borrow_dict)


# View Pending
def view_pending(book_dict,log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("===============================================================================")
    print("---------------------------------VIEW PENDING----------------------------------")
    print("SYSTEM: Here are all the books that are currently borrowed by others.")
 
    is_unavailable = 0
    number_of_book = 1
    for book in book_dict:
        if book_dict[book][1] == "UNAVAILABLE":
            print(f"[{number_of_book}.] _________________________________________________")
            print("BOOK ID        : " + book)
            print("BOOK TITLE     : " + book_dict[book][0][0])
            print("BOOK AUTHOR    : " + book_dict[book][0][1])
            print("DATE PUBLISHED : " + book_dict[book][0][2])
            print("STATUS         : " + book_dict[book][1])
            #LAST BORROWER
            borrow_id = book_dict[book][2][-1]
            log_id = borrow_dict[borrow_id][1]
            recent_borrower = log_dict[log_id][0]
            print("DATE OF RETURN : " + borrow_dict[borrow_id][2])
            print("LAST BORROWER  : " + recent_borrower) #THIS WILL BE EDITED ONCE LIST OF BORROWERS ARE MADE

            is_unavailable += 1
            number_of_book += 1

    if is_unavailable == 0:
        print("\nSYSTEM: All books are available. Go and borrow a book, Adventurer!")
        print("===============================================================================")
    else:
        print("\nSYSTEM: They'll return it soon Adventurer. For now, try other books.")
        print("===============================================================================")

    
            
    # TEST - Delete/Comment Later.
    print(book_dict)
    print(borrow_dict)
    

# TESTING AREA

# books_dictionary ={
#     # Book_ID (B#) : [[Title, Author, Date Published], Status, List_of_Borrowers]
# }

# borrow_list_dictionary = {
#     # Borrow_ID (BL#) : [Book_ID, Log_ID, Date Return]
# }

# # add_book(books_dictionary)