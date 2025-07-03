# 8. Functions

## What is a Function?

A function is a reusable block of code that performs a specific task. You define the code once and can then "call" (use) the function whenever you need to perform that task.

Using functions helps you:

- **Stay DRY (Don't Repeat Yourself):** Avoid writing the same code over and over.
- **Organize Your Code:** Break down a complex problem into smaller, manageable, and logical pieces.
- **Improve Readability:** Well-named functions make your code easier to understand.

## Defining a Function

You define a function using the `def` keyword, followed by a function name, parentheses `()`, and a colon `:`. The code block within the function is indented.

## Parameters (Arguments)

A function can accept inputs, which are called **parameters** or **arguments**. These are variables listed inside the parentheses in the function definition. This allows you to pass data into the function, making it more flexible.

## The `return` Statement

A function can send a value back to the code that called it. This is done with the `return` statement. A function can return any type of data: a string, a number, a list, a dictionary, etc.

## Why are Functions Important for Data Analysis?

In data analysis, you will constantly perform the same set of operations: calculating a specific metric, cleaning a piece of text, validating a row of data, etc.

By putting these operations into functions, you create a personal toolkit of reusable components. This makes your analysis scripts much cleaner, more reliable, and easier to debug and modify.

```python
# Let's learn how to create and use functions.

# --- A simple function without any inputs ---

def greet_user():
    """This is a docstring. It explains what the function does."""
    print("Hello! Welcome to the Treasury Analysis tool.")

# "Calling" the function to execute its code

greet_user()

print("-" * 20)

# --- A function with parameters (inputs) ---

def calculate_future_value(present_value, rate, periods):
    """Calculates the future value of an investment."""
    future_value = present_value * (1 + rate) ** periods
    return future_value

# Now we can use this function to perform the calculation.

pv = 10000 # Present Value
r = 0.05 # Rate of 5%
n = 10 # 10 years

# Call the function and store the result in a variable

fv = calculate_future_value(pv, r, n)

print(f"The future value of ${pv} invested for {n} years at {r*100}% is ${fv:.2f}")

print("-" * 20)

# --- A function that returns a dictionary ---

def create_trade_record(trade_id, security, quantity, price):
    """Creates a structured dictionary for a trade."""
    record = {
        "id": trade_id,
        "ticker": security,
        "amount": quantity,
        "execution_price": price
    }
    return record

trade1 = create_trade_record("T54321", "MSFT", 200, 305.50)
print("Created trade record:")
print(trade1)
```
