# 4. Collections: Lists and Tuples

Often, you need to store and work with a collection of items, not just single values. Lists and tuples are two fundamental ways to do this in Python.

## Lists

A list is an **ordered** and **changeable** (mutable) collection of items. They are one of the most versatile data types in Python.

- **Ordered:** The items have a defined order, and that order will not change.
- **Changeable:** You can add, remove, and change items in a list after it has been created.
- **Syntax:** You create lists using square brackets `[]`.

_SQL Analogy:_ A list is like a single column of data from a query result. You can have a list of client names, a list of transaction amounts, etc.

### Accessing Items (Indexing)

You can access an item in a list by referring to its index number. **Important:** Python indexing starts at `0`.

- `my_list[0]` gets the first item.
- `my_list[1]` gets the second item.
- `my_list[-1]` gets the _last_ item.

## Tuples

A tuple is an **ordered** and **unchangeable** (immutable) collection of items.

- **Unchangeable:** Once a tuple is created, you cannot change its values. You cannot add or remove items.
- **Syntax:** You create tuples using round brackets `()`.

### When to use a Tuple?

Use tuples when you have data that you know should not change. For example, the coordinates of a location `(latitude, longitude)` or the RGB values for a color `(255, 0, 0)`. They are slightly more memory-efficient than lists.

For most data analysis tasks where you are collecting and manipulating data, you will use **lists** far more often than tuples.

```python
# Let's explore lists and tuples.

# --- Lists ---

# A list is an ordered and changeable collection.

print("--- Lists ---")

# A list of stock tickers for our portfolio

portfolio_tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
print(f"Original portfolio: {portfolio_tickers}")

# Accessing items by index (remember, index starts at 0)

first_stock = portfolio_tickers[0]
print(f"The first stock is: {first_stock}")

third_stock = portfolio_tickers[2]
print(f"The third stock is: {third_stock}")

# Getting the last item

last_stock = portfolio_tickers[-1]
print(f"The last stock is: {last_stock}")

# Changing an item in the list

portfolio_tickers[2] = "TSLA" # We sold Microsoft and bought Tesla
print(f"Portfolio after selling MSFT for TSLA: {portfolio_tickers}")

# Adding an item to the end of the list

portfolio_tickers.append("NVDA")
print(f"Portfolio after buying NVDA: {portfolio_tickers}")

# Removing an item from the list

portfolio_tickers.remove("GOOGL")
print(f"Portfolio after selling GOOGL: {portfolio_tickers}")

print("-" * 20)

# --- Tuples ---

# A tuple is an ordered and UNCHANGEABLE collection.

print("--- Tuples ---")

# A tuple representing a fixed financial quarter (Year, Quarter Number)

q4_2023 = (2023, 4)
print(f"Financial Period: {q4_2023}")
print(f"Year: {q4_2023[0]}, Quarter: {q4_2023[1]}")

# The following line would cause an error because tuples are immutable:

# q4_2023[0] = 2024 # TypeError: 'tuple' object does not support item assignment
```
