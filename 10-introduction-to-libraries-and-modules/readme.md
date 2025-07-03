# 10. Introduction to Libraries and Modules

You don't have to write everything from scratch in Python. The Python community has created a vast collection of pre-written code packages that you can use in your own projects.

## Modules

A **module** is simply a Python file (`.py`) with functions, classes, and variables that you can use in other Python scripts. Think of it as a code library. Python comes with many built-in modules (the "standard library").

To use a module, you use the `import` statement.

`import math`

After importing it, you can use its functions by typing `module_name.function_name()`.

`math.sqrt(16)` # Calculates the square root of 16

## Libraries (or Packages)

A **library** (or package) is a collection of related modules. For data analysis, you will rely heavily on external libraries that you need to install.

### `pip`: The Package Installer

`pip` is the standard package manager for Python. You use it from your command line to install and manage libraries. For example, to install the most important library for data analysis, `pandas`, you would run:

`pip install pandas`

## The Next Step: Key Libraries for Data Analysis

- **`pandas`**: The single most important library for data analysis in Python. It provides a powerful object called a **DataFrame**, which is essentially a table (like a spreadsheet or SQL table) that you can easily manipulate, clean, analyze, and visualize. Your journey into real data analysis starts here.
- **`numpy`**: The fundamental package for numerical computation. `pandas` is built on top of it. It's incredibly fast for mathematical operations on large arrays of numbers.
- **`matplotlib` / `seaborn`**: Libraries for creating charts and visualizations.

Congratulations on completing the fundamentals! You are now ready to `import pandas` and start analyzing data.

```python
# A module is a file containing Python code.

# We can import code from other files to use in our own.

# Python has a "standard library" full of useful built-in modules.

# Let's import the `math` module, which contains many mathematical functions.

import math

print("--- Using the `math` module ---")

loan_principal = 50000

# Let's say we need the square root for a risk calculation.

sqrt_principal = math.sqrt(loan_principal)
print(f"The square root of the principal is: {sqrt_principal}")

print(f"The value of Pi is: {math.pi}")

# This concept of `import` is the gateway to data analysis.

# Your next step will be to install and import a powerful, external library

# like pandas:

# `import pandas as pd`
```
