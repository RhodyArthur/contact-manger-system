# Contact Manager System

A robust, menu-driven Contact Management System built in Python. This project demonstrates Object-Oriented Programming, file persistence, error handling, and user input validation through a practical CLI application.

## Features

- **Add Contact**: Create new contacts with name, email, phone, and address.
- **List Contacts**: View all saved contacts in a readable format.
- **Search Contacts**: Find contacts by name.
- **Update Contact**: Edit contact details.
- **Delete Contact**: Remove contacts by name and phone.
- **Export to CSV**: Save all contacts to a CSV file for external use.
- **Auto-Save**: All changes are automatically saved to a JSON file.

## Technologies Used

- **Python 3.x**
- **OOP Principles**: Encapsulation, validation, custom exceptions
- **File I/O**: JSON and CSV for data persistence
- **CLI**: Menu-driven interface with input validation

## Project Structure

```
contact-manger-system/
│
├── main.py                  # Entry point, CLI logic
├── models/
│   └── contact.py           # Contact class (OOP, validation)
├── services/
│   └── contact_book.py      # ContactBook class (manages contacts)
├── storage/
│   └── file_operations.py   # File I/O for JSON/CSV
├── validators/
│   └── validators.py        # Input validation functions
├── exceptions/
│   └── custom_exceptions.py # Custom error classes
├── data/
│   ├── data.json            # Persistent contact storage
│   └── data.csv             # Exported contacts
└── README.md                # Project documentation
```

## How to Run

1. **Clone the repository**
2. Ensure you have Python 3.x installed
3. Install any required packages (if any)
4. Run the application:

```bash
python main.py
```

## Usage

- Follow the on-screen menu to manage contacts
- All data is saved automatically to `data/data.json`
- Export contacts to CSV via the menu

## Data Model

- **Contact**: Represents a single contact with validation
- **ContactBook**: Manages a list of Contact objects, handles all operations

## Error Handling

- Custom exceptions for duplicate contacts and not found errors
- Graceful handling of file I/O errors
- User-friendly error messages in CLI

## Validation

- Name: At least 2 characters
- Email: Valid email format
- Phone: Valid phone number format
- Address: At least 3 characters

## Extending the Project

- Add more fields to Contact
- Implement import from CSV
- Add unit tests for validation and file operations
- Enhance CLI with more features

## License

This project is for educational purposes.

## Author
Rhoda Arthur