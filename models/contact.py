from validators.validators import validate_fields, validate_name, validate_email, validate_address, validate_phone

class Contact:
    def __init__(self, name: str, email: str, phone: str, address: str):
        validate_fields(name, email, phone, address)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self):
        """Convert Contact to dictionary for JSON"""
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Contact from dictionary"""
        return cls(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            address= data["address"])
    
    def update(self, new_name=None, new_email=None, new_phone=None, new_address=None):
        if new_name:
            if not validate_name(new_name):
                raise ValueError("Name must be 2 or more characters")
            self.name = new_name

        if new_email:
            if not validate_email(new_email):
                raise ValueError("Invalid email format")
            self.email = new_email

        if new_phone:
            if not validate_phone(new_phone):
                raise ValueError("Invalid phone number format")
            self.phone = new_phone

        if new_address:
            if not validate_address(new_address):
                raise ValueError("Address must be at least 3 characters")
            self.address = new_address
        
    def __str__(self):
        """Human-readable representation"""
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}'