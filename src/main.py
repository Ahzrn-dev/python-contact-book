from typing import TypedDict


class Contact(TypedDict):
    phone: str
    email: str
    address: str


class ContactBook:
    """Manage contacts stored in memory."""

    def __init__(self) -> None:
        self.contacts: dict[str, Contact] = {}

    def add_contact(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
    ) -> bool:
        """Add a new contact if the name does not already exist."""

        if name in self.contacts:
            return False

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address,
        }

        return True

    def view_contacts(self) -> None:
        """Display all saved contacts."""

        if not self.contacts:
            print("No contacts found.")
            return

        for name, info in self.contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 24)

    def delete_contact(self, name: str) -> bool:
        """Delete a contact by name."""

        if name not in self.contacts:
            return False

        del self.contacts[name]
        return True

    def edit_contact(
        self,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
    ) -> bool:
        """Update an existing contact."""

        if name not in self.contacts:
            return False

        if phone is not None:
            self.contacts[name]["phone"] = phone

        if email is not None:
            self.contacts[name]["email"] = email

        if address is not None:
            self.contacts[name]["address"] = address

        return True


def main() -> None:
    """Run the Contact Book command-line application."""

    book = ContactBook()

    while True:
        print("\n--- Contact Book Application ---")
        print("1. Add contact")
        print("2. Edit contact")
        print("3. View contacts")
        print("4. Delete contact")
        print("5. Quit")

        user_choice = input("\nPlease choose an option: ").strip()

        if user_choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone: ").strip()
            email = input("Enter contact email: ").strip()
            address = input("Enter contact address: ").strip()

            if book.add_contact(name, phone, email, address):
                print("Contact added successfully.")
            else:
                print("Contact already exists.")

        elif user_choice == "2":
            name = input("Enter the contact name to edit: ").strip()
            phone = input(
                "Enter a new phone number or press Enter to keep unchanged: "
            ).strip()
            email = input(
                "Enter a new email or press Enter to keep unchanged: "
            ).strip()
            address = input(
                "Enter a new address or press Enter to keep unchanged: "
            ).strip()

            updated = book.edit_contact(
                name,
                phone or None,
                email or None,
                address or None,
            )

            if updated:
                print("Contact updated successfully.")
            else:
                print("Contact not found.")

        elif user_choice == "3":
            book.view_contacts()

        elif user_choice == "4":
            name = input("Enter the contact name to delete: ").strip()

            if book.delete_contact(name):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif user_choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()