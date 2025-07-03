# 9. File Handling

A lot of data isn't inside your Python script; it's in external files like text files, CSVs (Comma-Separated Values), or Excel spreadsheets.

To work with this data, you first need to read it into your Python program. You may also want to save the results of your analysis to a new file. This process is called File I/O (Input/Output).

## The `open()` Function

The primary function for working with files in Python is `open()`. It takes two main arguments:

1.  The **file path** (the name and location of the file).
2.  The **mode** (what you want to do with the file).

### Common Modes:

- `'r'` - **Read mode:** Opens the file for reading. This is the default mode. An error will occur if the file does not exist.
- `'w'` - **Write mode:** Opens the file for writing. **It will create the file if it does not exist, or overwrite the entire contents if it does exist.**
- `'a'` - **Append mode:** Opens the file for appending. New data is written to the end of the file. It will create the file if it does not exist.

## The `with` Statement

It is best practice to use the `with` statement when dealing with file objects. It handles closing the file for you automatically, even if errors occur. This is safer and cleaner than manually opening and closing files.

**Next Step:** While this is great for simple text files, for data analysis you will almost always use a library like `pandas` to read structured data from files like CSVs or Excel. This topic is a direct stepping stone to that.

```python
# Let's learn the basics of reading from and writing to files.

# --- Writing to a file ---

# We will use the `with` statement, which is the recommended way to handle files.

# It automatically closes the file for you when you're done.

# 'w' stands for 'write' mode. It will create the file if it doesn't exist,

# or overwrite it completely if it does.

file_path = "sample_data.txt"

print(f"Writing a simple report to '{file_path}'...")
with open(file_path, 'w') as file:
    file.write("Treasury Report\n")
    file.write("Date: 2023-10-27\n")
    file.write("-----------------\n")
    file.write("Cash on hand: 50000\n")
    file.write("Investments: 125000\n")

print("File writing complete.")

print("-" * 20)

# --- Reading from a file ---

# 'r' stands for 'read' mode.

print(f"Reading data from '{file_path}'...")
with open(file_path, 'r') as file: # .read() reads the entire content of the file into a single string.
    content = file.read()

print("File content:\n")
print(content)
```
