import pandas as pd

# Assuming your data is in a CSV file named "signups.csv"
data = pd.read_csv("opertunity.csv")

# Explore data types and missing values (partially shown for brevity)
print("Data Type Summary:")
print(data.dtypes)
print("\nMissing Values:")
print(data.isnull().sum())  # Check for missing values in each column

# Categorical column summaries (example for Gender)
gender_summary = data["Gender"].value_counts(normalize=True) * 100
print("\nGender Summary:")
print(gender_summary.to_string())  # Convert to string for better display

# Opportunity Category summary with percentages
category_summary = (
    data["Opportunity Category"].value_counts(normalize=True) * 100
)
print("\nOpportunity Category Summary (percentages):")
print(category_summary.to_string())


# Opportunity Name summary (showing top 3 and others)
name_summary = data["Opportunity Name"].value_counts().head(3)
others = data["Opportunity Name"].value_counts().sum() - name_summary.sum()
name_summary.loc["Others"] = others
print("\nOpportunity Name Summary (Top 3 and Others):")
print(name_summary.to_string())

# City summary (showing top 3 and others)
city_summary = data["City"].value_counts().head(3)
others = data["City"].value_counts().sum() - city_summary.sum()

# Calculate total number of entries
total_entries = len(data)

# Convert city_summary values to percentages
city_summary = (city_summary / total_entries) * 100

# Add "Others" with calculated percentage
city_summary.loc["Others"] = (others / total_entries) * 100

print("\nCity Name Summary (Top 3 and Others):")
# Iterate through city_summary and format percentages
for city, percentage in city_summary.items():
  formatted_percentage = "{:.1f}%".format(percentage)  # Format with 1 decimal place
  print(f"{city}: {formatted_percentage}")

# State summary (showing top 3 and others)
state_summary = data["State"].value_counts().head(3)
others = data["State"].value_counts().sum() - state_summary.sum()

# Calculate total number of entries
total_entries = len(data)

# Convert state_summary values to percentages
state_summary = (state_summary / total_entries) * 100

# Add "Others" with calculated percentage
state_summary.loc["Others"] = (others / total_entries) * 100

print("\nState Name Summary (Top 3 and Others):")
# Iterate through state_summary and format percentages
for state, percentage in state_summary.items():
  formatted_percentage = "{:.1f}%".format(percentage)  # Format with 1 decimal place
  print(f"{state}: {formatted_percentage}")

# Country summary (showing top 3 and others)
country_summary = data["Country"].value_counts().head(3)
others = data["Country"].value_counts().sum() - country_summary.sum()

# Calculate total number of entries (assuming same data is used)
total_entries = len(data)

# Convert country_summary values to percentages
country_summary = (country_summary / total_entries) * 100

# Add "Others" with calculated percentage
country_summary.loc["Others"] = (others / total_entries) * 100

print("\nCountry Name Summary (Top 3 and Others):")
# Iterate through country_summary and format percentages
for country, percentage in country_summary.items():
  formatted_percentage = "{:.1f}%".format(percentage)  # Format with 1 decimal place
  print(f"{country}: {formatted_percentage}")

 #current student status summary with percentages
category_summary = (
    data["Current Student Status"].value_counts(normalize=True) * 100
)
print("\ncurrent student status Summary (percentages):")
print(category_summary.to_string())

#status discriptionsummary with percentages
category_summary = (
    data["Status Description"].value_counts(normalize=True) * 100
)
print("\nStatus DescriptionSummary (percentages):")
print(category_summary.to_string())
category_summary = (
    data["Current/Intended Major"].value_counts(normalize=True) * 100
)
print("\nCurrent/Intended Major Summary (percentages):")
print(category_summary.to_string())

#status discriptionsummary with percentages
category_summary = (
    data["Reward Amount"].value_counts(normalize=True) * 100
)
print("\nReward Amount Summary (percentages):")
print(category_summary.to_string())

#Skills Earned summary with percentages
category_summary = (
    data["Skills Earned"].value_counts(normalize=True) * 100
)
print("\n Skills Earned Summary (percentages):")
print(category_summary.to_string())