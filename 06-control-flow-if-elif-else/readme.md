# 6. Control Flow: `if`, `elif`, `else`

So far, our code has run from top to bottom, executing every line. Control flow statements allow you to make decisions and run specific blocks of code only when certain conditions are met.

This is how you give your program "intelligence" to handle different situations.

## The `if` Statement

The `if` statement is the most basic decision-making statement. It executes a block of code **only if** a specified condition is `True`.

## The `else` Statement

The `else` statement can be combined with an `if` statement. It provides an alternative block of code to execute if the `if` condition is `False`.

## The `elif` Statement

`elif` is short for "else if". It allows you to check for multiple different conditions. You can have as many `elif` statements as you need.

### Structure

_SQL Analogy:_ The `if`/`elif`/`else` structure is very similar to a `CASE WHEN ... THEN ... ELSE ... END` statement in SQL. You are evaluating a series of conditions and choosing an outcome.

This structure is fundamental for tasks like data validation, categorizing data based on values, or implementing business rules.

```python
# Let's explore conditional logic with if/elif/else.

# --- Simple if/else ---

print("--- Simple if/else ---")

portfolio_value = 1500000
risk_threshold = 1000000

if portfolio_value > risk_threshold:
    print("Portfolio value exceeds risk threshold. ACTION REQUIRED.")
else:
    print("Portfolio value is within acceptable risk limits.")

print("-" * 20)

# --- if/elif/else ---

print("--- if/elif/else ---")

# Let's categorize a bond by its credit rating.

credit_rating = "AA"

print(f"Analyzing bond with rating: {credit_rating}")

if credit_rating == "AAA":
    print("Category: Prime Investment Grade")
elif credit_rating == "AA" or credit_rating == "A":
    print("Category: High Investment Grade")
elif credit_rating == "BBB":
    print("Category: Medium Investment Grade")
elif credit_rating == "BB" or credit_rating == "B":
    print("Category: High-Yield (Junk Bond)")
else:
    print("Category: Not Rated or C-grade")

# This is like a CASE WHEN statement in SQL:

# CASE

# WHEN rating = 'AAA' THEN 'Prime'

# WHEN rating IN ('AA', 'A') THEN 'High'

# ...

# END
```
