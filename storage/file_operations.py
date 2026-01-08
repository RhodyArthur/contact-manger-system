import json
def get_contacts(filename="data/data.json"):
    """
    load all contacts
    """
    try:
        with open(filename) as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        data = []
        return data
    except json.JSONDecodeError:
        return 'Invalid JSON file'
        
def save_contacts(obj, filename="data/data.json"):
    with open(filename, 'w') as f:
       json.dump(obj, f, indent=4)
