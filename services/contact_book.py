import json
from ..exceptions.custom_exceptions import DuplicateContactError, ContactNotFoundError
class ContactBook():
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        """
        load all contacts
        """
        try:
            with open('data/data.json') as f:
                self.contacts = json.load(f)
                return self.contacts
        except FileNotFoundError:
            return 'File not found'
        except json.JSONDecodeError:
            return 'Invalid JSON file'
        
    def list_contacts(self):
        """list all contacts"""
        print("Name\tEmail\tPhone\tAddress\n")
        result = ''
        for contact in self.contacts:
            data = f"{contact["name"]}\t{contact["email"]}\t{contact["phone"]}\t{contact["address"]}\n"
            result += data
        return result
    
   


contact = ContactBook()
contact.load_contacts()
print(contact.list_contacts())