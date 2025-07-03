# 3. Basic Operators

Operators are special symbols in Python that carry out arithmetic or logical computation. The values that the operator works on are called operands.

## Arithmetic Operators

These are used to perform mathematical operations like addition, subtraction, etc.

- `+` : Addition (`10 + 5` is 15)
- `-` : Subtraction (`10 - 5` is 5)
- `*` : Multiplication (`10 * 5` is 50)
- `/` : Division (`10 / 5` is 2.0) - Note: Division in Python 3 always results in a float.
- `%` : Modulus (remainder of a division: `10 % 3` is 1)
- `**`: Exponent (`10 ** 2` is 100)

## Comparison (Relational) Operators

These are used to compare two values. They return either `True` or `False`.

- `==`: Equal to (`10 == 5` is `False`)
- `!=`: Not equal to (`10 != 5` is `True`)
- `>` : Greater than (`10 > 5` is `True`)
- `<` : Less than (`10 < 5` is `False`)
- `>=`: Greater than or equal to (`10 >= 10` is `True`)
- `<=`: Less than or equal to (`10 <= 5` is `False`)

## Logical Operators

These are used to combine conditional statements.

- `and`: Returns `True` if both statements are true.
- `or` : Returns `True` if one of the statements is true.
- `not`: Reverses the result, returns `False` if the result is true.

These operators are the building blocks for calculations and decision-making in your programs.

```python
# Let's explore basic operators in Python.

cash_on_hand = 50000
investment = 35000

# --- Arithmetic Operators ---

print("--- Arithmetic Operators ---")

remaining_cash = cash_on_hand - investment
print(f"Remaining Cash: {remaining_cash}") # The f"" is an f-string, an easy way to embed variables in text.

portfolio_value = 1200000
annual_return_rate = 0.075
annual_gain = portfolio_value * annual_return_rate
print(f"Expected Annual Gain: {annual_gain}")

num_assets = 25
num_analysts = 4
assets_per_analyst = num_assets / num_analysts
print(f"Assets per Analyst: {assets_per_analyst}")

print("-" * 20)

# --- Comparison Operators ---

print("--- Comparison Operators ---")

required_capital = 50000
available_capital = 65000

print(f"Is available capital sufficient? {available_capital >= required_capital}")

last_year_profit = 12000
this_year_profit = 11500
print(f"Did profit increase? {this_year_profit > last_year_profit}")

print("-" * 20)

# --- Logical Operators ---

print("--- Logical Operators ---")
is_liquid = True
is_profitable = False
print(f"Can we invest (must be liquid AND profitable)? {is_liquid and is_profitable}")
print(f"Should we review (liquid OR profitable)? {is_liquid or is_profitable}")
print(f"Is it NOT profitable? {not is_profitable}")
```
