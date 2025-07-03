import pandas as pd

# Define the path to the Excel file
excel_file_path = 'sample-data.xlsx'

print(f"--- Reading data from {excel_file_path} ---")

try:
    # Read the first sheet of the Excel file into a DataFrame
    # By default, read_excel reads the first sheet.
    df_sheet1 = pd.read_excel(excel_file_path)
    print("\nContent of the first sheet (default read):")
    print(df_sheet1.head())

    # Read a specific sheet by name
    # Assuming there might be a sheet named 'Sheet2' or similar.
    # If 'Sheet2' does not exist, this will raise a ValueError.
    try:
        df_sheet2 = pd.read_excel(excel_file_path, sheet_name='Sheet2')
        print("\nContent of 'Sheet2':")
        print(df_sheet2.head())
    except ValueError:
        print("\n'Sheet2' not found. Skipping reading specific sheet by name.")

    # Read a specific sheet by index (0-indexed)
    # This reads the second sheet if it exists.
    try:
        df_second_sheet = pd.read_excel(excel_file_path, sheet_name=1)
        print("\nContent of the second sheet (by index 1):")
        print(df_second_sheet.head())
    except IndexError:
        print("\nSecond sheet (index 1) not found. Skipping reading specific sheet by index.")
    except ValueError:
        print("\nOnly one sheet found. Skipping reading specific sheet by index.")

    # Read a specific range from a sheet
    # This example assumes the first sheet and reads data from columns A to C, rows 1 to 5.
    # Note: 'header=None' if your range includes headers that you don't want pandas to interpret.
    # 'usecols' can also be used with column letters or a list of integers (0-indexed).
    try:
        df_range = pd.read_excel(excel_file_path, sheet_name='Sheet1', usecols="A:C", skiprows=0, nrows=5)
        print("\nContent of a specific range (Sheet1, columns A-C, first 5 rows):")
        print(df_range)
    except Exception as e:
        print(f"\nCould not read specific range. Error: {e}")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found. Please ensure it's in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- Finished reading data ---")
