import os


# Define the class
class ContactManager:
    # Take the file name as a parameter
    def __init__(self, file_name):
        self.file_name = file_name

    # Add a new contact to the file
    def add_contact(self, name, phone, email):
        # Open the file in append mode
        with open(self.file_name, "a") as file:
            # Write the contact information in a comma-separated line
            file.write(f"{name},{phone},{email}\n")

    # Read the contact list from the file
    def read_contact_list(self):
        # Open the file in read mode
        with open(self.file_name, "r") as file:
            # Print a header
            print("Name\tPhone\tEmail")
            # Loop through each line in the file
            for line in file:
                # Split the line by comma
                values = line.strip().split(",")
                # Check if there are enough values
                if len(values) == 3:
                    # Unpack the values
                    name, phone, email = values
                    # Print the contact information in a tab-separated format
                    print(f"{name}\t{phone}\t{email}")
                else:
                    # Handle the case where there are not enough values
                    print(f"Invalid data: {line.strip()}")

    # Search for a contact by name in the file
    def search_contact(self, name):
        # Open the file in read mode
        with open(self.file_name, "r") as file:
            # Loop through each line in the file
            for line in file:
                # Split the line by comma and assign to variables
                contact_name, phone, email = line.split(",")
                # Check if the contact name matches the input name
                if contact_name == name:
                    # Print the contact information
                    print(f"Name: {contact_name}")
                    print(f"Phone: {phone}")
                    print(f"Email: {email}")
                    # Return from the function
                    return
        # If the loop ends without finding a match, print a message
        print("Contact not found.")

    # Update the information of a contact by name in the file
    def update_information(self, name, new_phone, new_email):
        temp_file_name = "temp.txt"
        with open(self.file_name, "r") as file, open(temp_file_name, "w") as temp_file:
            for line in file:
                # Split the line by comma
                values = line.strip().split(",")
                # Check if there are enough values
                if len(values) == 3:
                    contact_name, phone, email = values
                    if contact_name == name:
                        temp_file.write(f"{contact_name},{new_phone},{new_email}\n")
                    else:
                        temp_file.write(f"{contact_name},{phone},{email}\n")
                else:
                    # Handle the case where there are not enough values
                    print(f"Invalid data: {line.strip()}")

        os.replace(temp_file_name, self.file_name)
        print(f"Contact information for {name} has been updated.")

