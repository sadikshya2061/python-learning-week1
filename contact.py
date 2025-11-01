# contact details management system where users can add, find, list, and delete contacts

def add_contact(contacts):
    """Add a new contact to the contact book"""
    name = input("Enter contact name: ").strip()
    
    if name in contacts:
        print(f"Contact '{name}' already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    
    if not phone.isdigit():
        print(" Phone number must contain only numbers!")
        return
    elif len(phone) != 10:
        print(" Phone number must be exactly 10 digits!")
        return
    
    # Check if phone number already exists for any contact
    if phone in contacts.values():
        print(f" Phone number '{phone}' already exists for another contact!")
        return
        
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")

    
def find_contact(contacts):
    """Find a contact by name"""
    name = input("Enter contact name to find: ").strip()
    
    if name in contacts:
        print(f"Found: {name} - {contacts[name]}")
    else:
        print(f"Contact '{name}' not found!")

def list_contacts(contacts):
    """List all contacts"""
    if not contacts:
        print("Contact book is empty!")
        return
    
    print("\n--- All Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print("--------------------")

def del_contact(contacts):
    """Delete a contact by name"""
    name = input("Enter contact name to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

def main():
    """Main function to run the contact book"""
    contacts = {}  # Dictionary to store contacts
    
    while True:
        print("\n=== Contact Book ===")
        print("1. Add new contact")
        print("2. Find contact")
        print("3. List all contacts")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            find_contact(contacts)
        elif choice == '3':
            list_contacts(contacts)
        elif choice == '4':
            del_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

# Run the program
if __name__ == "__main__":
    main()