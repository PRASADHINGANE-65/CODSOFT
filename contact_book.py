contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name.lower()] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    print("✅ Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts.values():
        print("\n----------------")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts.values():
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        contact = contacts[name]
        phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
        email = input(f"Email ({contact['email']}): ") or contact['email']
        address = input(f"Address ({contact['address']}): ") or contact['address']
        contacts[name] = {
            "name": contact["name"],
            "phone": phone,
            "email": email,
            "address": address
        }
        print("✅ Contact updated.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    if name in contacts:
        del contacts[name]
        print("✅ Contact deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
menu()
