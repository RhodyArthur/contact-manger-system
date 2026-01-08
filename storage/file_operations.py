import json


def get_contacts(filename="data/data.json"):
    """
    Load and return all contacts from JSON file.
    Raises FileNotFoundError or JSONDecodeError on failure.
    """
    with open(filename, 'r') as f:
        data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Data format invalid: expected a list of contacts")

        return data


def save_contacts(contacts, filename="data/data.json"):
    """
    Save all contacts to JSON file.
    Overwrites existing file.
    """
    if not isinstance(contacts, list):
        raise ValueError("Contacts must be a list")

    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=4)
