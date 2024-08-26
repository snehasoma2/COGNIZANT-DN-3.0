# contact_management.py

def read_contacts_from_text_file(filename):
    try:
        with open(filename, 'r') as file:
            contacts = file.readlines()
            contacts = [contact.strip() for contact in contacts]
        return contacts
    except FileNotFoundError:
        print(f"{filename} not found. Creating a new file.")
        return []

def write_contacts_to_text_file(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(contact)

def add_contact(filename, contact):
    contacts = read_contacts_from_text_file(filename)
    contacts.append(contact)
    write_contacts_to_text_file(filename, contacts)
    print(f"Contact '{contact}' added.")

def remove_contact(filename, contact):
    contacts = read_contacts_from_text_file(filename)
    if contact in contacts:
        contacts.remove(contact)
        write_contacts_to_text_file(filename, contacts)
        print(f"Contact '{contact}' removed.")
    else:
        print(f"Contact '{contact}' not found.")

import pickle

def save_contacts_to_binary_file(filename, contacts):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(contacts, file)
        print(f"Contacts saved to {filename}.")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def load_contacts_from_binary_file(filename):
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
        return contacts
    except FileNotFoundError:
        print(f"{filename} not found. Returning an empty contact list.")
        return []
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []

def user_interface():
    text_filename = 'contacts.txt'
    binary_filename = 'contacts.dat'

    while True:
        print("\nOptions:")
        print("1. Display contacts (Text file)")
        print("2. Add contact (Text file)")
        print("3. Remove contact (Text file)")
        print("4. Save contacts to binary file")
        print("5. Load contacts from binary file")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            contacts = read_contacts_from_text_file(text_filename)
            display_contacts(contacts)
        elif choice == '2':
            contact = input("Enter contact name: ")
            add_contact(text_filename, contact)
        elif choice == '3':
            contact = input("Enter contact name to remove: ")
            remove_contact(text_filename, contact)
        elif choice == '4':
            contacts = read_contacts_from_text_file(text_filename)
            save_contacts_to_binary_file(binary_filename, contacts)
        elif choice == '5':
            contacts = load_contacts_from_binary_file(binary_filename)
            display_contacts(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    try:
        user_interface()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
