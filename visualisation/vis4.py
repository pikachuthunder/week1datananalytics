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

# Count badge name occurrences
badge_counts = data['Badge Name'].value_counts()

# Select top 10 most frequent badge names (or less if fewer than 10 exist)
top_10_badges = badge_counts.head(min(10, len(badge_counts)))

# Choose the visualization type (bar chart or pie chart)
# Option 1: Bar chart (recommended for many categories)
plt.figure(figsize=(10, 6))
top_10_badges.plot(kind='bar', color='navy')
plt.xlabel("Badge Name")
plt.ylabel("Count")
plt.title("Distribution of Top 10 Badge Names")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability (if many badges)
plt.tight_layout()
plt.show()

# Option 2: Pie chart (consider if there are very few badges, less than 5)
# plt.figure(figsize=(8, 8))
# top_10_badges.plot(kind='pie', autopct="%1.1f%%", labels=None)  # Pie chart with percentages
# plt.title("Distribution of Top Badge Names")
# plt.legend(top_10_badges.index, loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
# plt.tight_layout()
# plt.show()

# Choose the visualization type that best suits your data and the number of badges.
