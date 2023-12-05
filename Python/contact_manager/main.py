from contact_manager_app import ContactManager

# Create an instance of ContactManager
contact_manager = ContactManager("contact_list.txt")

# Add contacts
contact_manager.add_contact("John Doe", "555-1234", "john@gmail.com")
contact_manager.add_contact("Alice Smith", "555-5678", "alice@gmail.com")
contact_manager.add_contact("Bob Johnson", "555-9876", "bob@gmail.com")

# Read and display the contact list
print("----- Contact List -----")
contact_manager.read_contact_list()

# Search for a contact
print("\n----- Search Contact -----")
contact_manager.search_contact("Alice Smith")

# Update contact information
print("\n----- Update Contact -----")
contact_manager.update_information("Bob Johnson", "555-1111", "bob@yahoo.com")

# Read and display the updated contact list
print("\n----- Updated Contact List -----")
contact_manager.read_contact_list()
