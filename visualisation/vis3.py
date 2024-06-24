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

# Calculate category with highest reward count
category_counts = data['Opportunity Category'].value_counts()
highest_count_category = category_counts.idxmax()
highest_count = category_counts.max()

# Print result
print(f"Opportunity Category with Highest Count of Reward Earned: {highest_count_category} ({highest_count} rewards)")

# Create a bar chart to visualize the distribution
plt.figure(figsize=(8, 6))
category_counts.plot(kind='bar', color='navy')
plt.xlabel("Opportunity Category")
plt.ylabel("Count")
plt.title("Distribution of Reward Earned by Opportunity Category")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
