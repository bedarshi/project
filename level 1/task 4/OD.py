import pandas as pd

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Count the number of restaurants offering online delivery
online_delivery_counts = df["Has Online delivery"].value_counts()

# Calculate the percentage of restaurants offering online delivery
online_delivery_percentage = (online_delivery_counts / len(df)) * 100

# Compare average ratings of restaurants with and without online delivery
avg_rating_with_delivery = df[df["Has Online delivery"] == "Yes"]["Aggregate rating"].mean()
avg_rating_without_delivery = df[df["Has Online delivery"] == "No"]["Aggregate rating"].mean()

# Display results
print("Percentage of restaurants with online delivery:", round(online_delivery_percentage.get("Yes", 0), 2), "%")
print("Percentage of restaurants without online delivery:", round(online_delivery_percentage.get("No", 0), 2), "%")
print("Average Rating (With Online Delivery):", round(avg_rating_with_delivery, 2))
print("Average Rating (Without Online Delivery):", round(avg_rating_without_delivery, 2))
