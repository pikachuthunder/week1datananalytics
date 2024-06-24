import pandas as pd
import matplotlib.pyplot as plt

# Assuming your CSV file is named "data.csv"
data = pd.read_csv("oppertunity.csv")

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)
# Visualize missing values using bar chart
missing_values.plot(kind='bar')
plt.xlabel("Column Name")
plt.ylabel("Number of Missing Values")
plt.title("Missing Values Distribution in oppertunity data.csv")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
