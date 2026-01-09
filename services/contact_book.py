import csv
from exceptions.custom_exceptions import DuplicateContactError, ContactNotFoundError
from storage.file_operations import get_contacts, save_contacts
from models.contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        try:
            self.contacts = [Contact.from_dict(contact) for contact in get_contacts()]
        except FileNotFoundError:
            self.contacts = []
        
    def list_contacts(self):
        """list all contacts"""
        result = []
        for contact in self.contacts:
            data = f'Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}, Address: {contact.address}'
            result.append(data)
        return "\n".join(result)
    
    def add_contact(self, contact: Contact):
        """add contact to contact list"""
        for c in self.contacts:
            if contact.name.lower() == c.name.lower() and contact.phone == c.phone:
                raise DuplicateContactError("Contact already exist")
        
        self.contacts.append(contact)

        save_contacts([c.to_dict() for c in self.contacts])
        return contact


    def search_contact_by_name(self, name):
        result = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                result.append(contact)

        if len(result) == 0:
            raise ContactNotFoundError("Contact does not exist")
        return result
    
    def export_to_csv(self, filename="data/data.csv"):
        header = ["name", "email", "phone", "address"]

        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            data = [c.to_dict() for c in self.contacts]
            writer.writerows(data)
        

    
    def update_contact(self, name, phone, new_name=None, new_email=None, new_phone=None, new_address=None):
        contact = self.__find_contact(name, phone)
        contact.update(new_name, new_email, new_phone, new_address)
        save_contacts([c.to_dict() for c in self.contacts])
        return contact               
    

    def delete_contact(self, name: str, phone: str):
        """
        Delete a contact by name and phone.
        Raises ContactNotFoundError if no matching contact is found.
        """
        contact = self.__find_contact(name, phone)
        self.contacts.remove(contact)
        save_contacts([c.to_dict() for c in self.contacts])
        return f"Contact {name} ({phone}) deleted successfully"
    
    def __find_contact(self, name: str, phone: str)-> Contact :
        for contact in self.contacts:
            if contact.name.lower() == name.lower() and contact.phone == phone:
                return contact
        raise ContactNotFoundError("Contact does not exist")
