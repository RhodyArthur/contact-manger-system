import re

def validate_name(name):
    """
    Determine if a string has more than 2 characters
    :param name: string value
    """
    return isinstance(name, str) and len(name) >= 2


def validate_email(email):
    """
    Determine if a string value is an email
    :param email: string value
    """
    if not isinstance(email, str): return False
    if not email:
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """
    Determine if a string value is a phone number
    :param phone: string value
    """
    if not isinstance(phone, str): return False
    if not phone:
        return False
    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone) is not None

def validate_address(address):
    return isinstance(address, str) and len(address) >= 3

def validate_fields(name, email, phone, address):
    if not validate_name(name):
        raise ValueError("Invalid name: must be 2+ characters")
    if not validate_email(email):
        raise ValueError("Invalid email format")
    if not validate_phone(phone):
        raise ValueError("Invalid phone number format")
    if not validate_address(address):
        raise ValueError("Invalid address: must be 3+ characters")
    return True