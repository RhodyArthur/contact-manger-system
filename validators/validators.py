import re

def validate_name(name):
    """

    """
    if not name:
        return False
    
    if len(name) < 2:
        return 'Name must have 2 or more character'
    return True

def validate_email(email):
    """
    Determine if a string value is an email
    :param s: string value
    """
    if not email:
        return False
    
    if not isinstance(email, str): return False

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    if not phone:
        return False
    
    if not isinstance(phone, str): return False

    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone) is not None