import pandas as pd

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing cuisine information
df = df.dropna(subset=["Cuisines"])

# Split multiple cuisines and count occurrences
cuisine_counts = df["Cuisines"].str.split(", ").explode().value_counts()

# Get the top 3 cuisines
top_cuisines = cuisine_counts.head(3)

# Calculate their percentage
total_restaurants = len(df)
top_cuisines_percentage = (top_cuisines / total_restaurants) * 100

# Combine results into a DataFrame
top_cuisines_df = pd.DataFrame({
    "Cuisine": top_cuisines.index,
    "Count": top_cuisines.values,
    "Percentage": top_cuisines_percentage.values
})

# Display the results
print(top_cuisines_df)
