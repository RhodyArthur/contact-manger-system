from ..validators.validators import validate_email, validate_name, validate_phone

class Contact:
    def __init__(self, name: str, email: str, phone: str, address: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.validate_fields()

    def validate_name(self):
        if not validate_name(self.name):
            raise ValueError("Invalid name")
        return self.name
        
        
    def validate_email(self):
        if not validate_email(self.email):
            raise ValueError("Invalid email")
        return self.email
        
        
    def validate_phone(self):
        if not validate_phone(self.phone):
            raise ValueError("Invalid phone number")
        return self.phone
        
        
    def validate_address(self):
        if not isinstance(self.address, str) or len(self.address) < 3:
            raise ValueError("Invalid address")
        return self.address
    
    def validate_fields(self):
        self.validate_name()
        self.validate_email()
        self.validate_phone()
        self.validate_address()
        