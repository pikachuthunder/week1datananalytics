import pandas as pd
import matplotlib.pyplot as plt

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

# Read CSV data and clean it
data = pd.read_csv('opertunity.csv')
data = clean_data(data.copy())

# Convert Apply Date to datetime format (adjust format if needed)
data['Year'] = data['Apply Date'].dt.year  # Extract year for pie charts

# Group by year and calculate category proportions
category_proportions = (
    data.groupby(['Year', 'Opportunity Category'])['Opportunity Category']
    .count()
    .unstack(fill_value=0)
    .div(data.groupby('Year')['Opportunity Category'].count(), axis=0)
)

# Create a subplot grid for multiple pie charts (one per year)
fig, axes = plt.subplots(nrows=len(category_proportions), ncols=1, figsize=(10, len(category_proportions)*3))

# Iterate through each year and create a pie chart
for i, year in enumerate(category_proportions.index):
  axes[i].pie(category_proportions.loc[year], labels=category_proportions.columns, autopct="%1.1f%%")
  axes[i].set_title(f"Opportunity Category Distribution in Year {year}")

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
