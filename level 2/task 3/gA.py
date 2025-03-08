import pandas as pd
import folium

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing latitude or longitude values
df = df.dropna(subset=["Latitude", "Longitude"])

# Create a base map centered around the average location
map_center = [df["Latitude"].mean(), df["Longitude"].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add restaurant locations as markers
for _, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Restaurant Name']} - {row['City']}",
        icon=folium.Icon(color="red", icon="cutlery", prefix="fa")
    ).add_to(restaurant_map)

# Save the map as an HTML file
map_filename = "restaurant_map.html"
restaurant_map.save(map_filename)

print(f"Map has been saved as {map_filename}. Open this file in a browser to view the map.")
