import pandas as pd
import matplotlib.pyplot as plt

def visualize_skills_points(csv_file, column_name="Skill Points Earned", num_bins=10, figsize=(10, 6)):
  

  try:
    # Read the CSV file using pandas
    data = pd.read_csv(csv_file)

    # Ensure the specified column exists and is numerical
    if column_name not in data.columns or not pd.api.types.is_numeric_dtype(data[column_name]):
      raise ValueError(f"Column '{column_name}' not found or contains non-numeric values.")

    # Extract the skills points
    skill_points = data[column_name]

    # Create the histogram with navy blue color and black edges
    plt.figure(figsize=figsize)
    plt.hist(skill_points, bins=num_bins, edgecolor='black', color='navy')

    # Add informative labels and title
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {column_name} (from CSV)")

    # Improve readability with grid lines on the y-axis
    plt.grid(axis='y')

    # Display the histogram
    plt.tight_layout()
    plt.show()

  except FileNotFoundError:
    print(f"Error: CSV file '{csv_file}' not found.")
  except ValueError as e:
    print(e)

# Example usage (replace with your actual file path)
csv_file = "opertunity.csv"
visualize_skills_points(csv_file)
