import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'Phone Number': phone_number, 'Email': email}
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone Number: {info['Phone Number']}, Email: {info['Email']}")
        else:
            print("No contacts found!")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}, Phone Number: {info['Phone Number']}, Email: {info['Email']}")
        else:
            print(f"Contact '{name}' not found!")

    def edit_contact(self, name):
        if name in self.contacts:
            print(f"Editing contact '{name}':")
            phone_number = input("Enter new phone number (leave empty to keep current): ")
            email = input("Enter new email (leave empty to keep current): ")

            if phone_number:
                self.contacts[name]['Phone Number'] = phone_number
            if email:
                self.contacts[name]['Email'] = email

            print("Contact updated successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print("Contacts saved successfully!")

def main():
    contact_manager = ContactManagementSystem()

    while True:
        print("\nWelcome to Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)

        elif choice == '4':
            name = input("Enter name to edit: ")
            contact_manager.edit_contact(name)

        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            filename = input("Enter filename to save contacts: ")
            contact_manager.save_contacts(filename)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
