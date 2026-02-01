# Inventory Control System - Electronics Store

## 📋 Academic Project

This project was developed as a final assignment for the **Algorithms and Computational Logic** course. The objective was to create a functional inventory management system for an electronics store using Python, applying fundamental concepts of computational logic, flow control, and data structures.

## 🎯 Project Challenge

The challenge was to develop a complete inventory control system with the following core functionalities:

- **Add products** to the inventory
- **Update existing products** (price and quantity)
- **Delete products** from the inventory
- **View inventory** with organized product listing
- **Save and exit** with data persistence

## 🛠️ Technologies Used

- **Python 3.x**
- **JSON** for data persistence
- **Type hints** for better code documentation

## 📚 Concepts Applied

### 1. Computational Logic
- Implementation of conditional structures (IF/ELSE)
- Flow control for different system functionalities
- Input validation and error handling

### 2. Data Structures
- **Dictionaries** for efficient product storage
- Normalized keys to avoid duplicates
- Nested dictionaries for product attributes

### 3. Loops and Iterations
- While loops for menu navigation
- For loops for displaying inventory
- Input validation loops

### 4. Best Practices
- Code modularization with clear functions
- Explanatory comments throughout the code
- Clear variable naming conventions
- User-friendly interface with organized menus

## 🚀 Features

### Main Menu
The system presents an interactive menu with the following options:
1. Add product
2. Update product
3. Delete product
4. View inventory
5. Save and exit

### Product Management
Each product contains:
- **Name**: Product identifier
- **Price**: Product price (decimal value)
- **Quantity**: Current stock quantity (integer value)

### Data Persistence
- Inventory data is saved to a JSON file (`inventory.json`)
- Automatic loading on system startup
- Data preservation between sessions

### Input Validation
- Non-empty text validation
- Numeric validation for prices and quantities
- Prevention of negative values
- Duplicate product detection

## 💻 How to Run

1. Ensure Python 3.x is installed on your system
2. Download the `inventory_system.py` file
3. Open terminal/command prompt in the file directory
4. Run the command:
```bash
python inventory_system.py
```

## 📖 Usage Example

```
========================================
  Inventory Control System
========================================
1) Add product
2) Update product
3) Delete product
4) View inventory
5) Save and exit
Choose an option: 1

== Add Product ==
Product name: Laptop
Product price: 1299.99
Quantity in stock: 15
Product added successfully!
```

## 🎓 Learning Outcomes

This project provided hands-on experience with:
- Transforming theoretical knowledge into practical solutions
- Implementing user-friendly command-line interfaces
- Managing data persistence with file systems
- Applying computational thinking to real-world problems
- Writing clean, maintainable, and well-documented code

## 📝 Course Requirements Met

✅ Interactive menu system implementation  
✅ Product addition functionality  
✅ Product update functionality  
✅ Product deletion functionality  
✅ Organized inventory visualization  
✅ Proper use of conditional structures  
✅ Implementation of loops for data iteration  
✅ Appropriate data structure selection  
✅ Code organization with clear comments  
✅ User-friendly interface design  

## 🔍 Code Structure

```
inventory_system.py
├── Input Utilities
│   ├── read_text()      # Text input validation
│   ├── read_float()     # Decimal number validation
│   ├── read_int()       # Integer validation
│   └── normalize_name() # Name normalization
├── File Persistence
│   ├── load_inventory() # Load data from JSON
│   └── save_inventory() # Save data to JSON
├── System Functions
│   ├── add_product()    # Add new products
│   ├── update_product() # Update existing products
│   ├── delete_product() # Remove products
│   └── view_inventory() # Display all products
└── Main Loop
    ├── show_menu()      # Display menu options
    └── execute()        # Main program loop
```

## 👨‍🎓 Academic Context

**Course**: Algorithms and Computational Logic  
**Assignment Type**: Final Project  
**Objective**: Develop a practical inventory management system applying computational logic concepts  
**Deliverable**: Python (.py) file with complete implementation  

## 📄 License

This is an academic project developed for educational purposes.

---

**Note**: This project was created as part of a university assignment to demonstrate understanding of fundamental programming concepts, data structures, and computational logic using Python.