# contact manger system
## BONUS SECTION: Integrated Mini-Project (10 points)

### Create a Contact Management System

Build a complete contact management system that combines all concepts:

**Requirements:**

1. **Data Model (OOP)**
   - `Contact` class with: name, email, phone, address
   - `ContactBook` class to manage multiple contacts
   - Proper encapsulation and validation

2. **Persistence (File I/O)**
   - Save contacts to JSON file
   - Load contacts from JSON file
   - Auto-save on modifications

3. **Error Handling**
   - Custom exceptions: `DuplicateContactError`, `ContactNotFoundError`
   - Handle file operation errors gracefully

4. **Features**
   - Add contact
   - Search contact by name
   - Update contact
   - Delete contact
   - List all contacts
   - Export contacts to CSV

5. **CLI Interface**
   - Menu-driven interface
   - Input validation with appropriate error messages

```python
# Your implementation here

class Contact:
    pass

class ContactBook:
    pass

def main():
    """
    Main CLI loop
    """
    pass

if __name__ == "__main__":
    main()