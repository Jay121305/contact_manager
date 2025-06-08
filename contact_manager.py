import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter the contact number to edit: ")) - 1
    if 0 <= idx < len(contacts):
        print("Leave blank to keep current value.")
        name = input(f"New name (current: {contacts[idx]['name']}): ") or contacts[idx]['name']
        phone = input(f"New phone (current: {contacts[idx]['phone']}): ") or contacts[idx]['phone']
        email = input(f"New email (current: {contacts[idx]['email']}): ") or contacts[idx]['email']
        contacts[idx] = {"name": name, "phone": phone, "email": email}
        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        contacts.pop(idx)
        print("Contact deleted successfully.")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()