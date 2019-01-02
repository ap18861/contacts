import csv

def get_selection():
    """Enter which function you would like to run."""
    x = input("Please enter if you would like to add a contact or read the file: ")
    if x == '1':
        write_file()
    elif x == '2':
        read_file()
    elif x == '3':
        exit()

def welcome():
    """Beginning of the program"""
    welcome_sentence = "|Welcome to your contacts program!|"
    print("-"*len(welcome_sentence))
    print(welcome_sentence)
    print("-"*len(welcome_sentence))
    print("Press 1 to create a new contact.")
    print("Press 2 to read from the csv file.")
    print("Press 3 to exit from the program.")
    get_selection()
    
def first_name_entry():
    """First name entry of new contact."""
    first_name = input("Please enter the new contact first name: ")
    return first_name

def email_entry():
    """Enter the email of the new contact."""
    email = input("Please enter the email of your new contact: ")
    return email

def last_name_entry():
    """Enter the last name of the new contact."""
    last_name = input("Please enter the new contact last name: ")
    return last_name

def name_entry():
    """Calls all the functions for new contact entry."""
    first_name = first_name_entry()
    last_name = last_name_entry()
    name = [first_name, last_name]
    return name

def number_entry():
    """Enter the phone number of the new contact."""
    phone_number = input("Please enter the phone number of your new contact: ")
    return phone_number

def display_name():
    """Displays the information of the new entry."""
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

welcome()

#write_file()
# read_file()
