"""
Inventory Control System - Electronics Store

Work requirements (summary):
- Menu with options: add, update, delete, view and exit.
- Each product has: name, price, quantity.
- Display inventory with organized list.

Data structure:
- We use a dictionary (dict) where the key is the normalized product name
  and the value is another dictionary with "name", "price" and "quantity".
"""

from __future__ import annotations

import json
from typing import Dict, Any

DATA_FILE = "inventory.json"


# =========================
# Input Utilities
# =========================

def read_text(message: str) -> str:
    """Reads a non-empty text from the user."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Invalid input. Enter a non-empty text.")


def read_float(message: str) -> float:
    """Reads a decimal number (float) from the user, validating input."""
    while True:
        text = input(message).strip().replace(",", ".")
        try:
            value = float(text)
            if value < 0:
                print("The value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number (e.g.: 1999.90).")


def read_int(message: str) -> int:
    """Reads an integer (int) from the user, validating input."""
    while True:
        text = input(message).strip()
        if not text.isdigit():
            print("Invalid input. Enter an integer number (e.g.: 10).")
            continue
        value = int(text)
        return value


def normalize_name(name: str) -> str:
    """
    Normalizes the name to use as key:
    - removes extra spaces
    - converts to lowercase
    """
    return " ".join(name.strip().split()).lower()


# =========================
# File Persistence
# =========================

def load_inventory() -> Dict[str, Dict[str, Any]]:
    """Loads the inventory from JSON file. If it doesn't exist, returns empty."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Warning: corrupted inventory file. A new one will be created.")
    return {}


def save_inventory(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Saves the inventory to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)


# =========================
# System Rules
# =========================

def add_product(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Adds a new product to inventory, avoiding duplication by name."""
    print("\n== Add Product ==")
    original_name = read_text("Product name: ")
    key = normalize_name(original_name)

    if key in inventory:
        print("Product already exists in inventory. Use 'Update product'.")
        return

    price = read_float("Product price: ")
    quantity = read_int("Quantity in stock: ")

    inventory[key] = {
        "name": original_name.strip(),
        "price": price,
        "quantity": quantity
    }

    print("Product added successfully!")


def update_product(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Updates price and quantity of an existing product."""
    print("\n== Update Product ==")
    name = read_text("Product name to update: ")
    key = normalize_name(name)

    if key not in inventory:
        print("Product not found in inventory.")
        return

    price = read_float("New product price: ")
    quantity = read_int("New quantity in stock: ")

    inventory[key]["price"] = price
    inventory[key]["quantity"] = quantity

    print("Product updated successfully!")


def delete_product(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Deletes a product from inventory by name."""
    print("\n== Delete Product ==")
    name = read_text("Product name to delete: ")
    key = normalize_name(name)

    if key not in inventory:
        print("Product not found in inventory.")
        return

    removed = inventory.pop(key)
    print(f"Product '{removed['name']}' removed successfully!")


def view_inventory(inventory: Dict[str, Dict[str, Any]]) -> None:
    """Displays the inventory in a clear and organized way."""
    print("\n== Current Inventory ==")

    if not inventory:
        print("Empty inventory.")
        return

    # Sort by product name
    sorted_products = sorted(inventory.values(), key=lambda p: p["name"].lower())

    print("-" * 60)
    print(f"{'Product':30} {'Price ($)':>12} {'Qty':>8}")
    print("-" * 60)

    for p in sorted_products:
        print(f"{p['name'][:30]:30} {p['price']:>12.2f} {p['quantity']:>8}")

    print("-" * 60)


def show_menu() -> None:
    """Displays the main menu."""
    print("\n" + "=" * 40)
    print("  Inventory Control System")
    print("=" * 40)
    print("1) Add product")
    print("2) Update product")
    print("3) Delete product")
    print("4) View inventory")
    print("5) Save and exit")


def execute() -> None:
    """Main system loop (menu)."""
    inventory = load_inventory()

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            add_product(inventory)
        elif option == "2":
            update_product(inventory)
        elif option == "3":
            delete_product(inventory)
        elif option == "4":
            view_inventory(inventory)
        elif option == "5":
            save_inventory(inventory)
            print("Inventory saved. Exiting system...")
            break
        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    execute()
