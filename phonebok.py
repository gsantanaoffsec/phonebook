from time import sleep

PHONEBOOK = dict()


def show_contacts():
    if len(PHONEBOOK) > 0:
        for contacts in PHONEBOOK:
            search_contacts(contacts)
    else:
        print('Empty phonebook.')


def search_contacts(name):
    try:
        print('----------------------------------------')
        print(f'Name: {name}')
        print(f'Telephone: {PHONEBOOK[name]["telephone"]}')
        print(f'Email: {PHONEBOOK[name]["email"]}')
        print(f'Address: {PHONEBOOK[name]["address"]}')
        print('----------------------------------------')
    except KeyError:
        print(f'The contact "{name}" does not exist!')


def read_contact_details():
    telephone = input('Telephone: ')
    email = input('Email: ')
    address = input('Address: ')
    return telephone, email, address


def include_edit_contact(contact, telephone, email, address):
    PHONEBOOK[contact] = {
        'telephone': telephone,
        'email': email,
        'address': address,
    }
    save_phonebook()
    print()
    print(f'> The contact "{contact}" was successfully added/edited!')
    print()


def delete_contact(name):
    try:
        PHONEBOOK.pop(name)
        save_phonebook()
        print()
        print(f'> The contact "{name}" was successfully deleted!')
        print()
    except KeyError:
        print()
        print(f'The contact "{name}" does not exist!')


def export_phonebook(filename):
    try:
        with open(filename, 'w') as file:
            for contacts in PHONEBOOK:
                telephone = PHONEBOOK[contacts]['telephone']
                email = PHONEBOOK[contacts]['email']
                address = PHONEBOOK[contacts]['address']
                file.write(f'{contacts}, {telephone}, {email}, {address}\n')
            print('> Phonebook exported successfully!')
    except SyntaxError:
        print('Some error occurred!')


def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                telephone = details[1]
                email = details[2]
                address = details[3]
                include_edit_contact(name, telephone, email, address)
    except FileNotFoundError:
        print('> File not found!')


def save_phonebook():
    export_phonebook('database.csv')


def load():
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                telephone = details[1]
                email = details[2]
                address = details[3]

                PHONEBOOK[name] = {
                    'telephone': telephone,
                    'email': email,
                    'address': address,
                }
        print('> Database loaded successfully!')
        print(f'contacts loaded: {len(PHONEBOOK)}')
    except FileNotFoundError:
        print('> File not found!')
    # except Exception as error:
    # print('Algum erro inesperado ocorreu!')


def print_menu():
    print('----------------------------------------')
    print('[1] Show all contacts in the contact book.')
    print('[2] Look for contact.')
    print('[3] Include contact.')
    print('[4] Edit contact.')
    print('[5] Delete contact.')
    print('[6] Export phonebook.')
    print('[7] Import contact.')
    print('[0] Shutdown contact book.')
    print("----------------------------------------")


# Program start

load()

while True:

    print_menu()

    option = int(input('Choose an option: '))

    if option == 1:
        print('Option [1] selected!')
        print('Showing all contacts in the phonebook.')
    elif option == 2:
        print('Option [2] selected!')
        search_contacts(str(input('Contact name: ').capitalize()))
    elif option == 3:
        print('Option [3] selected!')
        contact = input('Contact name: ').capitalize()
        try:
            var = PHONEBOOK[contact]
            print(f'Contact already "{contact}" exists!')
        except KeyError:
            telephone, email, address = read_contact_details()
            include_edit_contact(contact, telephone, email, address)
    elif option == 4:
        print('Option [4] selected!')
        contact = input('Contact name: ').capitalize()
        try:
            var = PHONEBOOK[contact]
            print(f'Editing contact: {contact}')
            telephone, email, address = read_contact_details()
            include_edit_contact(contact, telephone, email, address)
        except KeyError:
            print('> Non-existent contact.')
    elif option == 5:
        print()
        print('Option [5] selected!')
        print()
        delete_contact(str(input('Contact name: ').capitalize()))
    elif option == 6:
        export_phonebook(filename=input('Filename: '))
    elif option == 7:
        filename = input('Enter the name of the file to be imported: ')
        import_contacts(filename)
    elif option == 0:
        print('Please wait, terminating the program...')
        sleep(2)
        quit('> Closed!')
    else:
        print('> Invalid option!')
        quit()

    show_contacts()
