# Best_Buy

Warehouse-style store simulation project in Python.

---

## Overview

Best_Buy is a simple Python project that models a store warehouse.  
It provides:

- a `Product` class to represent items with name, price, quantity, and active status  
- a `Store` class to manage collections of products (add/remove, compute totals, placing orders)  
- a `main.py` script / user interface to interact via a simple menu

---

## Project Structure

Best_Buy/
├── main.py # Entry script — provides menu to list, order, etc.
├── products.py # Definition of Product class and its behavior
├── store.py # Definition of Store class managing multiple products
├── README.md # This file
└── requirements.txt # Project dependencies

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/fcuriel66/Best_Buy.git
   cd Best_Buy

## Usage

python main.py

 You will be presented with a menu:

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit



