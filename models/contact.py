from validators.validators import validate_fields

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
            "phone": self.email,
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
        
    def __str__(self):
        """Human-readable representation"""
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}'