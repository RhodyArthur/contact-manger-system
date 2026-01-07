from validators.validators import validate_fields

class Contact:
    def __init__(self, name: str, email: str, phone: str, address: str):
        validate_fields(name, email, phone, address)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
