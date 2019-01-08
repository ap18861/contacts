import csv

file_name = "contacts.csv"
def get_selection():
    """Enter which function you would like to run."""
    x = input("Please enter your selection: ")
    if x == '1':
        write_file()
    elif x == '2':
        read_file()
    elif x == '3':
        search_file()
    elif x == '4':
        exit()

def welcome():
    """Beginning of the program"""
    welcome_sentence = "|Welcome to your contacts program!|"
    print("-"*len(welcome_sentence))
    print(welcome_sentence)
    print("-"*len(welcome_sentence))
    print("Press 1 to create a new contact.")
    print("Press 2 to read from the csv file.")
    print("Press 3 to search the csv file.")
    print("Press 4 to exit from the program.")
    get_selection()
    
def first_name_entry():
    """First name entry of new contact."""
    first_name = input("Please enter the contact first name: ")
    return first_name

def email_entry():
    """Enter the email of the new contact."""
    email = input("Please enter the email of your contact: ")
    return email

def last_name_entry():
    """Enter the last name of the new contact."""
    last_name = input("Please enter the contact last name: ")
    return last_name

def name_entry():
    """Calls all the functions for new contact entry."""
    first_name = first_name_entry()
    last_name = last_name_entry()
    name = [first_name, last_name]
    return name

def number_entry():
    """Enter the phone number of the new contact."""
    phone_number = input("Please enter the phone number of your contact: ")
    return phone_number

def display_name():
    """Displays the information of the entry."""
    name = name_entry()
    phone_number = number_entry()
    email = email_entry()
    print("Your new contact name is {} {}.".format(name[0], name[1]))
    print("Your new contact phone number is {}.".format(phone_number))
    print("Your new contact email is: {}.".format(email))

def write_file():
    """Writes to the csv file for a new entry."""
    with open('contacts.csv', mode = 'a', newline = '\n') as contacts_file:
        contacts_writer = csv.writer(contacts_file, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        first_name = first_name_entry()
        last_name = last_name_entry()
        phone_number = number_entry()
        email = email_entry()
        contacts_writer.writerow([first_name,last_name,phone_number,email])

    welcome()

def read_file():
    """Reads the file of all the contacts."""
    with open('contacts.csv', mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
                line_count += 1
            else:
               print(f'{", ".join(row)}')

    welcome()

def search_file():
    """Searches for a value in csv file."""    
    value = get_contact_value()
    with open(file_name, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader, None) #skip header
        for row in csv_reader:
            if value in row:
                print(row)
    
    welcome()
def get_contact_value():
    """Gets the value that we want to search."""

    print("For which value would you like to search?")
    print("Press 1 to search by first name.")
    print("Press 2 to search by last name.")
    print("Press 3 to search by phone number.")
    print("Press 4 to search by email.")
    print("Press 5 to go back to the Welcome screen.")
    z = input("Please enter selection: ")
    if z == "1":
        first_name = first_name_entry()
        return first_name
    elif z == "2":
        last_name = last_name_entry()
        return last_name
    elif z == "3":
        phone_number = number_entry()
        return phone_number
    elif z == "4":
        email = email_entry()
        return email
    else:
        print("You have not entered a proper value.")
        welcome()   

welcome()

