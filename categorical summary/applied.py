import pandas as pd

def clean_data(data):
  """
  Cleans data by:
    - Removing rows with invalid time values in the "Apply Date" column (using errors='coerce').
    - Removing rows with NaT values in the "Apply Date" column (indicating invalid dates).

  Args:
    data (pandas.DataFrame): The DataFrame containing the data.

  Returns:
    pandas.DataFrame: The cleaned DataFrame with invalid rows removed.
  """

  # Attempt conversion with errors='coerce' (returns NaT for invalid values)
  data['Apply Date'] = pd.to_datetime(data['Apply Date'], errors='coerce')

  # Identify and remove rows with NaT in "Apply Date" (invalid dates)
  data = data.dropna(subset=['Apply Date'])  # Drop rows with NaT in "Apply Date"
  return data

def calculate_percentage_applied_dates_per_month(cleaned_data):
  """
  Calculates the percentage of applied dates for each month in the cleaned data.

  Args:
    cleaned_data (pandas.DataFrame): The cleaned DataFrame containing application dates.

  Returns:
    pandas.Series: A Series with month (index) and percentage of applied dates (values).
  """

  # Extract month as a numerical representation (1-12)
  cleaned_data['Month'] = cleaned_data['Apply Date'].dt.month

  # Count applications per month
  monthly_applications = cleaned_data['Month'].value_counts()

  # Calculate total applications (handle potential empty Series)
  total_applications = len(cleaned_data) if len(cleaned_data) > 0 else 0

  # Calculate percentages for each month and ensure no division by zero
  percentage_applied_dates_per_month = (monthly_applications / total_applications) * 100
  percentage_applied_dates_per_month = percentage_applied_dates_per_month.fillna(0)

  return percentage_applied_dates_per_month

# Read CSV data and clean it
data = pd.read_csv('opertunity.csv')
cleaned_data = clean_data(data.copy())

# Calculate and optionally print the percentage of applied dates per month
percentage_applied_dates_per_month = calculate_percentage_applied_dates_per_month(cleaned_data)
print(percentage_applied_dates_per_month)

# Further analysis (optional):
# - Plot the percentage distribution using matplotlib.pyplot.bar()
# - Group and analyze data by other relevant columns

