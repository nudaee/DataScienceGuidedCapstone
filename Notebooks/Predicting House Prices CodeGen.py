import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Generate synthetic data
num_samples = 100
bedrooms = [random.randint(1, 5) for _ in range(num_samples)]
bathrooms = [random.randint(1, 4) for _ in range(num_samples)]
sqft = [random.randint(800, 3000) for _ in range(num_samples)]
neighborhoods = ["Suburb A", "Suburb B", "Suburb C"]
neighborhood = [random.choice(neighborhoods) for _ in range(num_samples)]
year_built = [random.randint(1980, 2020) for _ in range(num_samples)]
garage_capacity = [random.randint(1, 3) for _ in range(num_samples)]
price = [sqft[i] * 150 + bedrooms[i] * 20000 + bathrooms[i] * 15000 + garage_capacity[i] * 10000 for i in range(num_samples)]

# Create a DataFrame
data = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "sqft": sqft,
    "neighborhood": neighborhood,
    "year_built": year_built,
    "garage_capacity": garage_capacity,
    "price": price
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("house_data.csv", index=False)

print("Dataset saved as 'house_data.csv'")
