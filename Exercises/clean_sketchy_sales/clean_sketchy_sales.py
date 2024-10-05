import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create a synthetic dataset
n_samples = 100

data = {
    "OrderID": range(1, n_samples + 1),
    "Product": np.random.choice(["Widget", "Gadget", "Doodad", None], size=n_samples),
    "Quantity": np.random.randint(1, 10, size=n_samples),
    "Price": np.random.choice([10.99, 15.99, None], size=n_samples),
    "Date": pd.date_range(start="2023-01-01", periods=n_samples, freq="D"),
}

# Introduce some inconsistencies
data["Product"][5] = "gadget"  # Lowercase entry
data["Product"][10] = "Doodad"  # Duplicate entry
# data["Quantity"][20] = None  # Missing value
data["Price"][25] = -5.99  # Invalid price

df = pd.DataFrame(data)
df.loc[10] = df.loc[0]  # Duplicate row for testing

# Save the dataset to a CSV file
df.to_csv("messy_sales_data.csv", index=False)

print("Synthetic Sales Dataset:")
print(df.head(15))
