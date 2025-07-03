# Working with Excel Files in Python

This guide provides documentation and examples on how to work with Excel files using Python, specifically focusing on tasks relevant to treasury or statistical analysts. We will be using the `pandas` library, which is a powerful tool for data manipulation and analysis.

This guide is designed for learners who may not have extensive Python experience. Each section will explain a concept and provide Python code snippets that you can run yourself.

## Setup

To follow along with these examples, you need to have Python installed. You will also need to install the `pandas` and `openpyxl` libraries. `openpyxl` is a dependency that `pandas` uses to read and write `.xlsx` files.

You can install them using pip. Open your terminal or command prompt and run:

```bash
pip install pandas openpyxl pytest
```

## Getting Started: Reading Excel Data

The first step is to read your Excel file into a pandas DataFrame. A DataFrame is a table-like data structure that pandas uses to store and manipulate data.

Let's assume your Excel file is named `sample-data.xlsx` and is located in the same directory as your Python script.

```python
import pandas as pd

# Define the path to your Excel file
excel_file_path = 'sample-data.xlsx'

print(f"--- Reading data from {excel_file_path} ---")

try:
    # Read the first sheet of the Excel file into a DataFrame
    # By default, pd.read_excel reads the first sheet.
    df = pd.read_excel(excel_file_path)
    print("\nContent of the first sheet (first 5 rows):")
    print(df.head()) # .head() shows the first 5 rows of the DataFrame

    # You can also read a specific sheet by its name:
    # If your Excel file has multiple sheets, you can specify which one to read.
    # For example, if you have a sheet named 'SalesData', you would use:
    # df_sales = pd.read_excel(excel_file_path, sheet_name='SalesData')
    # print("\nContent of 'SalesData' sheet:")
    # print(df_sales.head())

    # Or by its index (0-indexed, so 0 is the first sheet, 1 is the second, etc.):
    # df_second_sheet = pd.read_excel(excel_file_path, sheet_name=1)
    # print("\nContent of the second sheet:")
    # print(df_second_sheet.head())

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found. Please ensure it's in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- Finished reading data ---")
```

**How to run this code:**

1.  Open a text editor (like VS Code, Notepad, or Sublime Text).
2.  Copy and paste the Python code above into the editor.
3.  Save the file as `read_excel_example.py` (or any other `.py` name) in the same directory as your `sample-data.xlsx` file.
4.  Open your terminal or command prompt, navigate to that directory, and run:
    ```bash
    python read_excel_example.py
    ```

## Filtering and Sorting Data

Once you have your data in a DataFrame, you can easily filter rows based on conditions and sort data by one or more columns.

```python
import pandas as pd

excel_file_path = 'sample-data.xlsx'

try:
    df = pd.read_excel(excel_file_path)
    print("\nOriginal DataFrame (first 5 rows):")
    print(df.head())

    # --- Filtering Data ---

    # Example 1: Filter rows where 'Profit' is greater than 10000
    # This assumes your Excel file has a column named 'Profit'.
    # If not, you will get a KeyError.
    try:
        df_filtered_profit = df[df['Profit'] > 10000]
        print("\nDataFrame filtered by 'Profit' > 10000 (first 5 rows):")
        print(df_filtered_profit.head())
    except KeyError:
        print("\n'Profit' column not found for filtering. Skipping Profit filter example.")

    # Example 2: Filter rows where 'Segment' is 'Government'
    # This assumes your Excel file has a column named 'Segment'.
    try:
        df_filtered_segment = df[df['Segment'] == 'Government']
        print("\nDataFrame filtered by 'Segment' == 'Government' (first 5 rows):")
        print(df_filtered_segment.head())
    except KeyError:
        print("\n'Segment' column not found for filtering. Skipping Segment filter example.")

    # Example 3: Filter rows with multiple conditions
    # (e.g., 'Units Sold' > 2000 AND 'Country' == 'Germany')
    # This assumes 'Units Sold' and 'Country' columns exist.
    try:
        df_multi_filter = df[(df['Units Sold'] > 2000) & (df['Country'] == 'Germany')]
        print("\nDataFrame filtered by 'Units Sold' > 2000 AND 'Country' == 'Germany' (first 5 rows):")
        print(df_multi_filter.head())
    except KeyError:
        print("\n'Units Sold' or 'Country' column not found for multi-filtering. Skipping multi-filter example.")

    # --- Sorting Data ---

    # Example 1: Sort DataFrame by 'Date' column in ascending order
    # This assumes a 'Date' column exists.
    try:
        df_sorted_date_asc = df.sort_values(by='Date', ascending=True)
        print("\nDataFrame sorted by 'Date' (Ascending, first 5 rows):")
        print(df_sorted_date_asc.head())
    except KeyError:
        print("\n'Date' column not found for sorting. Skipping date sort example.")

    # Example 2: Sort DataFrame by 'Gross Sales' column in descending order
    # This assumes a 'Gross Sales' column exists.
    try:
        df_sorted_gross_sales_desc = df.sort_values(by='Gross Sales', ascending=False)
        print("\nDataFrame sorted by 'Gross Sales' (Descending, first 5 rows):")
        print(df_sorted_gross_sales_desc.head())
    except KeyError:
        print("\n'Gross Sales' column not found for sorting. Skipping Gross Sales sort example.")

    # Example 3: Sort DataFrame by multiple columns
    # (e.g., 'Country' then 'Profit', with different ascending/descending orders)
    # This assumes 'Country' and 'Profit' columns exist.
    try:
        df_sorted_multi = df.sort_values(by=['Country', 'Profit'], ascending=[True, False])
        print("\nDataFrame sorted by 'Country' (Asc) then 'Profit' (Desc, first 5 rows):")
        print(df_sorted_multi.head())
    except KeyError:
        print("\n'Country' or 'Profit' column not found for multi-column sorting. Skipping multi-column sort example.")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found. Please ensure it's in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**How to run this code:**

1.  Open a text editor.
2.  Copy and paste the Python code above into the editor.
3.  Save the file as `filter_sort_example.py` in the same directory as your `sample-data.xlsx` file.
4.  Open your terminal or command prompt, navigate to that directory, and run:
    ```bash
    python filter_sort_example.py
    ```

## Aggregating Data

Aggregation allows you to summarize your data, such as calculating sums, averages, counts, minimums, or maximums. This is often done after grouping data by one or more categories.

```python
import pandas as pd

excel_file_path = 'sample-data.xlsx'

try:
    df = pd.read_excel(excel_file_path)
    print("\nOriginal DataFrame (first 5 rows):")
    print(df.head())

    # --- Basic Aggregation Operations ---

    # Calculate the sum of a numeric column (e.g., 'Profit')
    try:
        total_profit = df['Profit'].sum()
        print(f"\nTotal Profit: {total_profit}")
    except KeyError:
        print("\n'Profit' column not found for sum aggregation. Skipping sum example.")

    # Calculate the average of a numeric column (e.g., 'Units Sold')
    try:
        average_units_sold = df['Units Sold'].mean()
        print(f"Average Units Sold: {average_units_sold}")
    except KeyError:
        print("\n'Units Sold' column not found for average aggregation. Skipping average example.")

    # Count the number of non-null values in a column (e.g., 'Segment')
    try:
        count_entries = df['Segment'].count()
        print(f"Number of Entries: {count_entries}")
    except KeyError:
        print("\n'Segment' column not found for count aggregation. Skipping count example.")

    # Find the maximum value in a column (e.g., 'Gross Sales')
    try:
        max_gross_sales = df['Gross Sales'].max()
        print(f"Maximum Gross Sales: {max_gross_sales}")
    except KeyError:
        print("\n'Gross Sales' column not found for max aggregation. Skipping max example.")

    # Find the minimum value in a column (e.g., 'Discounts')
    try:
        min_discounts = df['Discounts'].min()
        print(f"Minimum Discounts: {min_discounts}")
    except KeyError:
        print("\n'Discounts' column not found for min aggregation. Skipping min example.")

    # --- Grouped Aggregation ---

    # Group by 'Country' and calculate the sum of 'Profit' for each country
    # This assumes 'Country' and 'Profit' columns exist.
    try:
        profit_by_country = df.groupby('Country')['Profit'].sum()
        print("\nTotal Profit by Country:")
        print(profit_by_country)
    except KeyError:
        print("\n'Country' or 'Profit' column not found for group by aggregation. Skipping group by example.")

    # Group by multiple columns (e.g., 'Segment' and 'Product') and calculate average 'Units Sold'
    # This assumes 'Segment', 'Product', and 'Units Sold' columns exist.
    try:
        avg_units_by_segment_product = df.groupby(['Segment', 'Product'])['Units Sold'].mean()
        print("\nAverage Units Sold by Segment and Product:")
        print(avg_units_by_segment_product)
    except KeyError:
        print("\n'Segment', 'Product', or 'Units Sold' column not found for multi-group by aggregation. Skipping multi-group by example.")

    # Perform multiple aggregations at once using .agg()
    # This assumes 'Product', 'Profit', 'Units Sold', and 'Gross Sales' columns exist.
    try:
        multi_agg = df.groupby('Product').agg(
            Total_Profit=('Profit', 'sum'),
            Average_Units_Sold=('Units Sold', 'mean'),
            Max_Gross_Sales=('Gross Sales', 'max')
        )
        print("\nMultiple Aggregations by Product:")
        print(multi_agg)
    except KeyError:
        print("\nRequired columns for multi-aggregation not found. Skipping multi-aggregation example.")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found. Please ensure it's in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**How to run this code:**

1.  Open a text editor.
2.  Copy and paste the Python code above into the editor.
3.  Save the file as `aggregate_example.py` in the same directory as your `sample-data.xlsx` file.
4.  Open your terminal or command prompt, navigate to that directory, and run:
    ```bash
    python aggregate_example.py
    ```

## Data Exploration

Understanding your data's structure, types, and basic statistics is crucial before performing detailed analysis.

```python
import pandas as pd

excel_file_path = 'sample-data.xlsx'

print(f"--- Exploring data from {excel_file_path} ---")

try:
    df = pd.read_excel(excel_file_path)
    print("\nOriginal DataFrame (first 5 rows):")
    print(df.head())

    # --- Basic Data Exploration ---

    # Display basic information about the DataFrame, including data types and non-null values
    print("\nDataFrame Info:")
    df.info()

    # Display descriptive statistics for numeric columns
    print("\nDescriptive Statistics for Numeric Columns:")
    print(df.describe())

    # Get the column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Get the shape of the DataFrame (rows, columns)
    print(f"\nDataFrame Shape (Rows, Columns): {df.shape}")

    # Count unique values in a specific column (e.g., 'Segment')
    # This assumes a 'Segment' column exists.
    try:
        print("\nUnique values in 'Segment' column:")
        print(df['Segment'].unique())
        print("\nValue counts for 'Segment' column:")
        print(df['Segment'].value_counts())
    except KeyError:
        print("\n'Segment' column not found for unique value count. Skipping unique values example.")

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found. Please ensure it's in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- Finished data exploration ---")
```

**How to run this code:**

1.  Open a text editor.
2.  Copy and paste the Python code above into the editor.
3.  Save the file as `data_exploration_example.py` in the same directory as your `sample-data.xlsx` file.
4.  Open your terminal or command prompt, navigate to that directory, and run:
    ```bash
    python data_exploration_example.py
    ```

## Testing Your Understanding

To verify your understanding and implementation, you can use the `pytest` framework. First, ensure `pytest` is installed (see Setup section).

Create a file named `test_excel_operations.py` in the `11-working-with-excel/` directory with the following content:

```python
import pandas as pd
import pytest

# Define the path to the Excel file
excel_file_path = 'sample-data.xlsx'

# Fixture to load the DataFrame once for all tests
@pytest.fixture(scope='module')
def sample_dataframe():
    try:
        df = pd.read_excel(excel_file_path)
        return df
    except FileNotFoundError:
        pytest.fail(f"Test setup failed: '{excel_file_path}' not found. Please ensure it's in the same directory.")
    except Exception as e:
        pytest.fail(f"Test setup failed: An error occurred while reading the Excel file: {e}")

def test_dataframe_loading(sample_dataframe):
    # Test if the DataFrame loaded successfully and is not empty
    assert sample_dataframe is not None
    assert not sample_dataframe.empty, "DataFrame should not be empty"
    assert isinstance(sample_dataframe, pd.DataFrame), "Object should be a pandas DataFrame"

def test_expected_columns_exist(sample_dataframe):
    # Test if essential columns exist based on the provided schema
    expected_columns = ["Segment", "Country", "Product", "Units Sold", "Manufacturing Price",
                        "Sale Price", "Gross Sales", "Discounts", " Sales", "COGS", "Profit",
                        "Date", "Month Number", "Month Name", "Year"]
    for col in expected_columns:
        assert col in sample_dataframe.columns, f"Column '{col}' not found in DataFrame"

def test_filter_profit_greater_than_10000(sample_dataframe):
    # Test filtering for 'Profit' greater than 10000
    if 'Profit' in sample_dataframe.columns:
        df_filtered = sample_dataframe[sample_dataframe['Profit'] > 10000]
        assert (df_filtered['Profit'] > 10000).all(), "Filtering by Profit failed"
        assert not df_filtered.empty, "No data found for Profit > 10000, check sample data or filter logic"
    else:
        pytest.skip("Column 'Profit' not found, skipping filter test.")

def test_aggregate_total_gross_sales_by_country(sample_dataframe):
    # Test aggregation: sum of 'Gross Sales' grouped by 'Country'
    if 'Country' in sample_dataframe.columns and 'Gross Sales' in sample_dataframe.columns:
        gross_sales_by_country = sample_dataframe.groupby('Country')['Gross Sales'].sum()
        assert 'Canada' in gross_sales_by_country.index, "Country 'Canada' not found in aggregated data"
        assert gross_sales_by_country['Canada'] > 0, "Total Gross Sales for 'Canada' should be greater than 0"
    else:
        pytest.skip("Columns 'Country' or 'Gross Sales' not found, skipping aggregation test.")

def test_sort_by_units_sold_descending(sample_dataframe):
    # Test sorting by 'Units Sold' in descending order
    if 'Units Sold' in sample_dataframe.columns:
        df_sorted = sample_dataframe.sort_values(by='Units Sold', ascending=False)
        # Check if the 'Units Sold' column is indeed sorted in descending order
        assert df_sorted['Units Sold'].is_monotonic_decreasing, "DataFrame is not sorted by Units Sold in descending order"
    else:
        pytest.skip("Column 'Units Sold' not found, skipping sort test.")

# You can add more tests here for other operations like:
# - test_data_types_correctness(sample_dataframe): Check if columns have expected data types
# - test_missing_values(sample_dataframe): Check for expected missing values
# - test_specific_sheet_reading(sample_dataframe): If you have multiple sheets and want to test reading a specific one
```

**How to run the tests:**

1.  Save the code above as `test_excel_operations.py` in the `11-working-with-excel/` directory.
2.  Open your terminal or command prompt, navigate to the `11-working-with-excel/` directory, and run:
    ```bash
    pytest test_excel_operations.py
    ```
    Pytest will discover and run the tests, reporting any failures.
