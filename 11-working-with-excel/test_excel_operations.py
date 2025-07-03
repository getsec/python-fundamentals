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
