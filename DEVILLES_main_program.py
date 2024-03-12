import DEVILLES_book_section
import DEVILLES_list_of_borrower_section
import DEVILLES_logbook_section
import DEVILLES_ascii_art
import os

file_path = 'DEVILLES_library_data.txt'
absolute_path = os.path.abspath(file_path)

print(absolute_path)
print()

# FUNCTIONS

def Enter_Library():
    print(DEVILLES_ascii_art.library_logo)
    print("Welcome to Wishdum Library, The Dwelling Place of Knowledge and Wisdom.\n")
    print("SYSTEM: Let's start your journey! What would you like to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] Visit Library")
    print("[2] Exit Library")
    print("-------------------------------------------------------------------------------")

def Main_Menu():
    print(DEVILLES_ascii_art.menu_logo)
    print("Hello Adventurer, I see that you're interested to learn.")
    print("SYSTEM: Tell me what you want to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] Go to Book Section")
    print("[2] Borrow or Return Book")
    print("[3] See Logbook")
    print("[4] Return to Reception Area")
    print("-------------------------------------------------------------------------------")

def Main_Menu_systemArchon():
    print(DEVILLES_ascii_art.menu_archon)
    print("Welcome back Archon, what is thy request?")
    print("SYSTEM: Tell me what you want to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] Add Book")
    print("[2] Delete Book")
    print("[3] Delete All Book")
    print("[4] Edit Book")
    print("[5] Exit Archon Menu")
    print("-------------------------------------------------------------------------------")

def Book_Section_Menu():
    print(DEVILLES_ascii_art.book_section_logo)
    print("Splendid choice Adventurer! Looking for a book aren't we?")
    print("SYSTEM: Tell me what you want to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] View Book")
    print("[2] View Pending")
    print("[3] Return to Main Menu")
    print("-------------------------------------------------------------------------------")

def Borrow_Return_Menu():
    print(DEVILLES_ascii_art.borrower_section_logo)
    print("I see that you're eager to increase you knowledge Adventurer!")
    print("SYSTEM: Tell me what you want to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] Borrow Book")
    print("[2] Return Book")
    print("[3] View All Entries")
    print("[4] View Expected Return")
    print("[5] Return to Main Menu")
    print("-------------------------------------------------------------------------------")

def Logbook_Menu():
    print(DEVILLES_ascii_art.logbook_section_logo)
    print("It's good to know the past Adventurer. Welcome to Logbook!")
    print("SYSTEM: Tell me what you want to do?")
    print("Direction: Type the number of choice.")
    print("-------------------------------------------------------------------------------")
    print("[1] View Transaction Per Day")
    print("[2] View All Entries")
    print("[3] Return to Main Menu")
    print("-------------------------------------------------------------------------------")

def load_library_data(book_dict, log_dict, borrower_dict):
    fileHandle = open("DEVILLES_library_data.txt", "r")
    for library_data in fileHandle:
        data = library_data[:-1].split("Æ")
        #Borrower_List_Dictionary
        if "BL" in data[0]:
            borrower_id = data[0]
            borrower_book_id = data[1]
            borrower_log_id = data[2]
            borrower_date_return = data[3]

            borrower_dict[borrower_id] = [borrower_book_id, borrower_log_id, borrower_date_return]

        #Book_Dictionary
        elif "B" in data[0]:
            book_id = data[0]
            book_title = data[1]
            book_author = data[2]
            book_date_published = data[3]
            book_status = data[4]

            book_list_of_borrowers = []
            for borrower in range(0, len(data)):
                if borrower >= 5 :
                    if data[borrower] != "":
                        book_list_of_borrowers.append(data[borrower])
                    else:
                        continue

            book_dict[book_id] = [[book_title, book_author, book_date_published], book_status, book_list_of_borrowers]
        # ['[]', 'BL1']

        #Log_Dictionary
        elif "L" in data[0]:
            log_id = data[0]
            log_person = data[1]
            log_date = data[2]
            log_time = data[3]
            log_purpose = data[4]

            log_dict[log_id] = [log_person, log_date, log_time, log_purpose]
        
        else:
            continue

    fileHandle.close()

def save_library_data(book_dict, log_dict, borrower_dict):
    fileHandle = open("DEVILLES_library_data.txt", "w")

    for book in book_dict:
        book_id = book
        book_title = book_dict[book][0][0]
        book_author = book_dict[book][0][1]
        book_date_published = book_dict[book][0][2]
        book_status = book_dict[book][1]
        book_list_of_borrowers = book_dict[book][2]

        fileHandle.write(f"{book_id}Æ{book_title}Æ{book_author}Æ{book_date_published}Æ{book_status}Æ")
        if len(book_list_of_borrowers) == 0:
            fileHandle.write("\n")
        else:
            for borrower in book_list_of_borrowers:
                if borrower != book_list_of_borrowers[-1]:
                    fileHandle.write(f"{borrower}Æ")
                else:
                    fileHandle.write(f"{borrower}\n")

    for log in log_dict:
        log_id = log
        log_person = log_dict[log][0]
        log_date = log_dict[log][1]
        log_time = log_dict[log][2]
        log_purpose = log_dict[log][3]

        fileHandle.write(f"{log_id}Æ{log_person}Æ{log_date}Æ{log_time}Æ{log_purpose}\n")

    for borrower in borrower_dict:
        borrower_id = borrower
        borrower_book_id = borrower_dict[borrower][0]
        borrower_log_id = borrower_dict[borrower][1]
        borrower_date_return = borrower_dict[borrower][2]

        fileHandle.write(f"{borrower_id}Æ{borrower_book_id}Æ{borrower_log_id}Æ{borrower_date_return}\n")

    fileHandle.close()


def caesar_encode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    shift_amount = 12
    fileLibraryData = open("DEVILLES_library_data_encoded.txt", "w")
    fileHandle = open("DEVILLES_library_data.txt", "r")

    for data_line in fileHandle:
        end_text = ""
        for char in data_line:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        fileLibraryData.write(f"{end_text}\n")


    fileLibraryData.close()
    fileHandle.close()


def caesar_decode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    shift_amount = 12
    fileLibraryData = open("DEVILLES_library_data_encoded.txt", "r")
    fileHandle = open("DEVILLES_library_data.txt", "w")

    for data_line in fileLibraryData:
        end_text = ""
        shift_amount *= -1
        for char in data_line:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        fileHandle.write(f"{end_text}")
        print(end_text)

    fileLibraryData.close()
    fileHandle.close()


# MAIN PROGRAM


books_dictionary ={
    # Book_ID (B#) : [[Title, Author, Date Published], Status, List_of_Borrowers]
}

logbook_dictionary = {
    # Log_ID (L#) : [Person Name, Date, Time, Purpose]
}

borrow_list_dictionary = {
    # Borrow_ID (BL#) : [Book_ID, Log_ID, Date Return]
}

caesar_decode()
load_library_data(books_dictionary, logbook_dictionary, borrow_list_dictionary)


endProgram = False
while not endProgram:


    Enter_Library()
    enter_library_choice = input("USER INPUT: ")
    if enter_library_choice == "1":
        DEVILLES_logbook_section.visit_library(logbook_dictionary)

        endMainMenu = False
        while not endMainMenu:
            Main_Menu()
            main_menu_choice = input("USER INPUT: ")

            #======ARCHON MENU======
            if main_menu_choice == "!systemArchon":
                endArchonMenu = False
                while not endArchonMenu:
                    Main_Menu_systemArchon()
                    archon_menu_choice = input("ARCHON INPUT: ")
                    if archon_menu_choice == "1":
                        DEVILLES_book_section.add_book(books_dictionary)
                    elif archon_menu_choice == "2":
                        DEVILLES_book_section.delete_book(books_dictionary,borrow_list_dictionary)
                    elif archon_menu_choice == "3":
                        DEVILLES_book_section.delete_all_books(books_dictionary,borrow_list_dictionary)
                    elif archon_menu_choice == "4":
                        DEVILLES_book_section.edit_book(books_dictionary,borrow_list_dictionary)
                    elif archon_menu_choice == "5":
                        endArchonMenu = True
                    else:
                        print("ERROR: Invalid Choice, Please Choose Again.")
                        print("===========================================")

            #======BOOK SECTION MENU======
            elif main_menu_choice == "1":
                endBookSectionMenu = False
                while not endBookSectionMenu:
                    Book_Section_Menu()
                    book_section_menu_choice = input("USER INPUT: ")
                    if book_section_menu_choice == "1":
                        DEVILLES_book_section.view_book(books_dictionary,logbook_dictionary, borrow_list_dictionary)
                    elif book_section_menu_choice == "2":
                        DEVILLES_book_section.view_pending(books_dictionary,logbook_dictionary,borrow_list_dictionary)
                    elif book_section_menu_choice == "3":
                        endBookSectionMenu = True
                    else:
                        print("ERROR: Invalid Choice, Please Choose Again.")
                        print("===========================================")
                        
            #======BORROW RETURN MENU======
            elif main_menu_choice == "2":
                endBorrowReturnMenu = False
                while not endBorrowReturnMenu:
                    Borrow_Return_Menu()
                    borrow_return_menu_choice = input("USER INPUT: ")
                    if borrow_return_menu_choice == "1":
                        DEVILLES_list_of_borrower_section.borrow_book(books_dictionary,logbook_dictionary,borrow_list_dictionary)
                    elif borrow_return_menu_choice == "2":
                        DEVILLES_list_of_borrower_section.return_book(books_dictionary,logbook_dictionary)
                    elif borrow_return_menu_choice == "3":
                        DEVILLES_list_of_borrower_section.view_all_entries(books_dictionary,logbook_dictionary,borrow_list_dictionary)
                    elif borrow_return_menu_choice == "4":
                        DEVILLES_list_of_borrower_section.view_expected_return(books_dictionary,logbook_dictionary,borrow_list_dictionary)
                    elif borrow_return_menu_choice == "5":
                        endBorrowReturnMenu = True
                    else:
                        print("ERROR: Invalid Choice, Please Choose Again.")
                        print("===========================================")

            #======LOGBOOK MENU======
            elif main_menu_choice == "3":
                endLogbookMenu = False
                while not endLogbookMenu:
                    Logbook_Menu()
                    logbook_menu_choice = input("USER INPUT: ")
                    if logbook_menu_choice == "1":
                        DEVILLES_logbook_section.view_transactions_per_day(books_dictionary,logbook_dictionary,borrow_list_dictionary)
                    elif logbook_menu_choice == "2":
                        DEVILLES_logbook_section.view_all_entries_log(logbook_dictionary)
                    elif logbook_menu_choice == "3":
                        endLogbookMenu = True
                    else:
                        print("ERROR: Invalid Choice, Please Choose Again.")
                        print("===========================================")
                        
            #======EXIT MAIN MENU
            elif main_menu_choice == "4":
                endMainMenu = True
            else:
                print("ERROR: Invalid Choice, Please Choose Again.")
                print("===========================================")


    elif enter_library_choice == "2":
        print("SYSTEM: Thank you for journeying with us. We hope to see you again!")
        print(DEVILLES_ascii_art.goodbye_logo)
        endProgram = True


    else:
        print("ERROR: Invalid Choice, Please Choose Again.")
        print("===========================================")


save_library_data(books_dictionary, logbook_dictionary, borrow_list_dictionary)
caesar_encode()
