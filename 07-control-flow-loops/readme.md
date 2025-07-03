# 7. Control Flow: Loops

Loops are used to execute a block of code repeatedly. This is essential for automating repetitive tasks, especially when working with collections of data like lists. Instead of writing the same code for every item, you write it once inside a loop.

## The `for` Loop

A `for` loop is used for **iterating over a sequence** (that is either a list, a tuple, a dictionary, a set, or a string).

This is the most common type of loop you will use in data analysis. For example, you would use a `for` loop to:

- Calculate a metric for every transaction in a list of transactions.
- Check every stock in a portfolio against a certain criterion.
- Clean up every name in a list of client names.

_SQL Analogy:_ A `for` loop is conceptually similar to how SQL processes a `SELECT` statement. SQL applies the operation to every single row that matches the `WHERE` clause. A `for` loop in Python applies a block of code to every single item in a collection.

## The `while` Loop

A `while` loop executes a block of code **as long as a specified condition is true**.

You use a `while` loop when you don't know beforehand how many times you need to loop. For example, you might keep trying to connect to a data source until the connection is successful.

**Caution:** Be careful with `while` loops! If the condition never becomes `False`, the loop will run forever (an "infinite loop").

```python
# Let's explore loops.

# --- The `for` loop ---

# Used to iterate over a sequence (like a list).

print("--- `for` loop ---")

# Let's say we have a list of transaction amounts.

transaction_amounts = [150.25, -35.50, 2000.00, -450.80, 125.00]
total_value = 0.0

# We can loop through each amount and add it to our total.

# The variable `amount` will hold the value of one item from the list at a time.

for amount in transaction_amounts:
    print(f"Processing transaction: {amount}")
    total_value = total_value + amount

print(f"Final total value of all transactions: ${total_value:.2f}") # .2f formats the float to 2 decimal places

print("-" * 20)

# --- The `while` loop ---

# Used to repeat as long as a condition is true.

print("--- `while` loop ---")

# Let's simulate a simple cash flow projection.

# Start with $1000, earn 5% interest per year.

# How many years until we have at least $1500?

capital = 1000
target = 1500
interest_rate = 0.05
years = 0

while capital < target:
    capital = capital * (1 + interest_rate) # Apply interest
    years = years + 1 # Increment the year count
    print(f"Year {years}: Capital is ${capital:.2f}")

print(f"\nIt will take {years} years to reach the target of ${target}.")
```
