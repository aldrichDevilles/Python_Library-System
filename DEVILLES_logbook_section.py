# LOGBOOK SECTION FUNCTIONS

# Visit Library
def visit_library(log_dict):
    print("_______________________________________________________________________________")
    print("SYSTEM: Please fill up the information needed for our Logbook.\n")
    visitor_name = input("NAME: ").upper()
    visitor_date = input("DATE OF VISIT (e.g. 9 Jan 2020): ").upper()
    visitor_time = input("TIME OF VISIT (e.g. 9PM, 10:30AM): ").upper()
    visitor_purpose = input("PURPOSE: ").upper()

    log_num = 1
    while ("L" + str(log_num)) in log_dict:
        log_num += 1
    log_id = "L"+str(log_num)

    # ADDS LOG TO LOGBOOK
    log_dict[log_id] = [visitor_name, visitor_date, visitor_time, visitor_purpose]

    print("\nSYSTEM: Thank you and enjoy your library experience!")
    print("===============================================================================")
    print(log_dict)
    return log_id

# View All Entries
def view_all_entries_log(log_dict):
    print("_______________________________________________________________________________")
    print("----------------------------VIEW ALL LOGBOOK ENTRIES---------------------------")
    print("SYSTEM: It seems like you want to see all logs. I got you Adventurer!\nHere's all the data we've gathered.\n")

    number_of_log = 1
    for log in log_dict:
        print(f"[{number_of_log}.] _________________________________________________")
        print("LOG ID        : " + log)
        print("PERSON NAME   : " + log_dict[log][0])
        print("DATE OF VISIT : " + log_dict[log][1])
        print("TIME OF VISIT : " + log_dict[log][2])
        print("PURPOSE       : " + log_dict[log][3])

        number_of_log += 1

    print("\nSYSTEM: I hope that we've satisfied your curiosity!")
    print("===============================================================================")
# View Transactions Per Day
def view_transactions_per_day (book_dict, log_dict, borrow_dict):
    print("_______________________________________________________________________________")
    print("---------------------------VIEW TRANSACTIONS PER DAY---------------------------")
    print("SYSTEM: Looking a specific transaction, Adventurer?\nI can show you each transactions on a specific date!")
    print("Direction: Enter the Date of Transaction (e.g. 9 Jan 2020)")
    expected_date = input("USER INPUT: ").upper()

    # TASK - print these information [log_id, person, date, time, purpose]
    is_logged = 0
    number_of_log = 1
    for log in log_dict:
        if expected_date == log_dict[log][1]:
            print(f"[{number_of_log}.] _________________________________________________")
            print("LOG ID        : " + log)
            print("PERSON NAME   : " + log_dict[log][0])
            print("DATE OF VISIT : " + log_dict[log][1])
            print("TIME OF VISIT : " + log_dict[log][2])
            print("PURPOSE       : " + log_dict[log][3])

            is_logged += 1
            number_of_log += 1

    if is_logged != 0:
        print("\nSYSTEM: I hope that we've satisfied your curiosity!")
        print("===============================================================================")
    else:
        print(f"\nSYSTEM: NO transaction during {expected_date}. It looks like no\none visited the library that day.\nPlease check the date you've entered as well, Adventurer")
        print("===============================================================================")

            

    # TEST - Delete/Comment Later.
    print(book_dict)
    print(log_dict)
    print(borrow_dict)


# TESTING AREA
            
# logbook_dictionary = {
#     # Log_ID (L#) : [Person Name, Date, Time, Purpose]
# }

# visit_library(logbook_dictionary)