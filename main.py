from services.contact_book import ContactBook
from exceptions.custom_exceptions import DuplicateContactError, ContactNotFoundError

def main():
    book = ContactBook()
    book.load_contacts()

    while True:
        print("\n=== Contact Management System ===")
        print("1. List all contacts")
        print("2. Add a new contact")
        print("3. Search contacts")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Export contacts to CSV")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n" + book.list_contacts())

        elif choice == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            address = input("Address: ").strip()

            try:
                book.add_contact({"name": name, "email": email, "phone": phone, "address": address})
                print("Contact added successfully!")
            except DuplicateContactError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Validation error: {e}")

        elif choice == "3":
            name = input("Search by name (leave empty if not needed): ").strip()
            phone = input("Search by phone (leave empty if not needed): ").strip()

            try:
                results = book.search_contact_by_name(name=name, phone=phone)
                for contact in results:
                    print(f'Name: {contact["name"]}, Email: {contact["email"]}, Phone: {contact["phone"]}, Address: {contact["address"]}')
            except ContactNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "4":
            name = input("Current Name of Contact: ").strip()
            phone = input("Current Phone of Contact: ").strip()

            new_name = input("New Name (leave empty to skip): ").strip() or None
            new_email = input("New Email (leave empty to skip): ").strip() or None
            new_phone = input("New Phone (leave empty to skip): ").strip() or None
            new_address = input("New Address (leave empty to skip): ").strip() or None

            try:
                updated = book.update_contact(name, phone, new_name, new_email, new_phone, new_address)
                print(f"Contact updated: {updated}")
            except ContactNotFoundError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Validation error: {e}")

        elif choice == "5":
            name = input("Name of Contact to Delete: ").strip()
            phone = input("Phone of Contact to Delete: ").strip()
            try:
                msg = book.delete_contact(name, phone)
                print(msg)
            except ContactNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "6":
            book.export_to_csv()
            print("Contacts exported to CSV successfully!")

        elif choice == "7":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    main()
