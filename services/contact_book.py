import json
import csv
from exceptions.custom_exceptions import DuplicateContactError, ContactNotFoundError
from validators.validators import validate_fields

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
            self.contacts = []
            return self.contacts
        except json.JSONDecodeError:
            return 'Invalid JSON file'
        
    def list_contacts(self):
        """list all contacts"""
        result = ''
        for contact in self.contacts:
            data = f'Name: {contact["name"]}, Email: {contact["email"]}, Phone: {contact["phone"]}, Address: {contact["address"]}\n'
            result += data
        return result
    
    def add_contact(self, contact):
        """add contact to contact list"""
        for c in self.contacts:
            if contact["name"] == c["name"] and contact["phone"] == c["phone"]:
                raise DuplicateContactError("Contact already exist")
        
        validate_fields(contact["name"], contact["email"], contact["phone"], contact["address"])
        self.contacts.append(contact)

        with open('data/data.json', 'w') as f:
            json.dump(self.contacts, f, indent=4)
        return contact


    def search_contact_by_name(self, name=None, phone=None):
        result = []
        for contact in self.contacts:
            if name.lower() in contact.get('name').lower() or phone in contact.get('phone'):
                result.append(contact)

        if len(result) == 0:
            raise ContactNotFoundError("Contact does not exist")
        return result
    
    def export_to_csv(self, filename="data/data.csv"):
        header = ["name", "email", "phone", "address"]

        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(self.contacts)
        

    
    def update_contact(self, name, phone, new_name=None, new_email=None, new_phone=None, new_address=None):
        
        for contact in self.contacts:
            if name == contact.get("name") and phone == contact.get("phone"):
                validate_fields(name, email, phone, address)
                contact["name"] = contact["name"] or  name
                contact["email"] = contact["email"] | email
                contact["phone"] = contact["phone"] | phone
                contact["address"] = contact["address"] | address
        raise ContactNotFoundError('Contact does not exist')



contact = ContactBook()
contact.load_contacts()
print(contact.list_contacts())