# 2. Variables and Data Types

## What is a Variable?

A variable is a container for storing a value. You give it a name, and you can use that name to refer to the value later. This is fundamental to programming, as it allows you to store and manipulate data.

Think of it like a labeled box where you can put something.

`variable_name = value`

## Common Data Types

Every value in Python has a "type". For a beginner, the most important ones are:

1.  **String (`str`):** Used for text. You create them using single (`'`) or double (`"`) quotes.

    - _SQL Analogy:_ Similar to `VARCHAR` or `TEXT`.
    - Example: `client_name = "ABC Corp"`

2.  **Integer (`int`):** Used for whole numbers (no decimals).

    - _SQL Analogy:_ Similar to `INT` or `BIGINT`.
    - Example: `number_of_trades = 150`

3.  **Float (`float`):** Used for numbers with decimals. The name "float" stands for "floating-point number".

    - _SQL Analogy:_ Similar to `DECIMAL` or `FLOAT`.
    - Example: `interest_rate = 0.025`

4.  **Boolean (`bool`):** Can only have one of two values: `True` or `False`. Booleans are essential for making decisions in your code.
    - _SQL Analogy:_ Similar to `BOOLEAN` or `BIT`.
    - Example: `is_approved = True`

Python is dynamically typed, which means you don't have to declare the type of a variable. Python figures it out automatically based on the value you assign.

## How to Run the Code

Navigate to this directory (`02_variables_and_data_types`) in your terminal and run:

```bash
python variables_and_types.py
```

```python
# Let's explore variables and data types.

# 1. String (str) - for text

# We are assigning the text "Treasury Analysis" to a variable named `project_name`.

project_name = "Treasury Analysis"

# We can print the variable to see its value.

print("Project Name:", project_name)
print("Type of project_name is:", type(project_name)) # `type()` shows the data type
print("-" * 20) # Prints a separator line

# 2. Integer (int) - for whole numbers

portfolio_id = 1025
number_of_securities = 50

print("Portfolio ID:", portfolio_id)
print("Type of portfolio_id is:", type(portfolio_id))
print("-" * 20)

# 3. Float (float) - for numbers with decimals

market_value = 1250500.75
risk_factor = 0.95

print("Market Value:", market_value)
print("Type of market_value is:", type(market_value))
print("-" * 20)

# 4. Boolean (bool) - for True or False values

is_hedged = True
requires_review = False

print("Is the portfolio hedged?", is_hedged)
print("Type of is_hedged is:", type(is_hedged))
```
