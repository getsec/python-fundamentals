# 5. Collections: Dictionaries and Sets

Continuing with collections, dictionaries and sets offer different ways to store groups of data, each with unique properties.

## Dictionaries (`dict`)

A dictionary is an **unordered**, **changeable**, and **indexed** collection of data. It stores data in **key-value pairs**.

- **Key-Value Pairs:** Each item in a dictionary has a `key` and a corresponding `value`. You use the key to access the value.
- **Changeable:** You can add, change, and remove items after the dictionary has been created.
- **Syntax:** You create dictionaries using curly braces `{}` with `key: value` items.

_SQL/Data Analogy:_ A dictionary is very much like a **single row of data** or a single record. The keys are like the column headers (`'FirstName'`, `'LastName'`), and the values are the data for that specific row (`'John'`, `'Doe'`). This structure is extremely common when working with data from APIs or databases (like JSON).

Example:
`stock_info = {'ticker': 'AAPL', 'price': 175.50, 'currency': 'USD'}`

## Sets

A set is an **unordered** and **unindexed** collection of **unique** items.

- **Unique:** A set cannot have duplicate members. If you try to add an item that's already there, it will be ignored.
- **Unordered:** The items in a set do not have a defined order. You cannot access items by an index number.
- **Syntax:** You create sets using curly braces `{}`.

### When to use a Set?

The main use for a set is to efficiently check if an item is present in a collection or to get a list of unique items from another collection (like a list). For example, you could get a unique list of all currencies used in a list of transactions.

```python
# Let's explore dictionaries and sets.

# --- Dictionaries ---

# Dictionaries store data in key-value pairs.

print("--- Dictionaries ---")

# A dictionary representing a single trade

trade_record = {
    "trade_id": "T12345",
    "security": "IBM",
    "quantity": 100,
    "price": 145.75,
    "is_buy": True
}

print(f"Original trade record: {trade_record}")

# Accessing values using their keys

print(f"Security traded: {trade_record['security']}")
print(f"Trade price: {trade_record['price']}")

# Changing a value

trade_record['price'] = 146.10 # The price was updated
print(f"Updated trade record: {trade_record}")

# Adding a new key-value pair

trade_record['currency'] = 'USD'
print(f"Record with currency: {trade_record}")

print("-" * 20)

# --- Sets ---

# Sets store unique, unordered items.

print("--- Sets ---")

# Imagine a list of currencies from multiple transactions, with duplicates

transaction_currencies = ['USD', 'EUR', 'USD', 'JPY', 'GBP', 'EUR', 'USD']

# We can use a set to quickly find the unique currencies

unique_currencies = set(transaction_currencies)
print(f"Original list of currencies: {transaction_currencies}")
print(f"Unique currencies in our transactions: {unique_currencies}")
```
