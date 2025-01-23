import pandas as pd
import numpy as np

np.random.seed(0)

data = {
    "product_id": np.arange(1, 101),
    "product_name": np.random.choice(
        ["Widget A", "widget-a", "Widget A Large", "Gadget B", "gadget-b"], 100
    ),
    "weight": np.random.choice(["2 lbs", "0.9 kg", "3 lbs", "1.4 kg", np.nan], 100),
    "description": np.random.choice(
        [
            "A very useful widget that performs a variety of functions and tasks, suitable for home and office use.",
            "A compact gadget, easy to store and very efficient for small tasks.",
            "An advanced widget with extended features, ideal for professional use.",
            "A large-sized gadget offering high performance and durability.",
            np.nan,
        ],
        100,
    ),
}


# Convert weights to kilograms
def convert_to_kg(weight):
    if pd.isna(weight):
        return np.nan
    weight = str(weight).lower()
    if "kg" in weight:
        return float(weight.replace("kg", "").strip())
    elif "lbs" in weight:
        # Convert pounds to kilograms (1 lb = 0.45359237 kg)
        return float(weight.replace("lbs", "").strip()) * 0.45359237
    return np.nan


df = pd.DataFrame(data)


duplicate_ids = np.random.choice(df["product_id"], 10)
df = pd.concat([df, df[df["product_id"].isin(duplicate_ids)]])

# Check the first few rows
df.head()
df["product_name"] = df["product_name"].str.lower().replace(r"-", " ", regex=True)

df["weight"] = df["weight"].apply(convert_to_kg)

# Trim descriptions to max 50 characters and add ellipsis if truncated
df["description"] = df["description"].apply(
    lambda x: x[:47] + "..." if pd.notna(x) and len(x) > 50 else x
)

df.to_csv("product_listing_df.csv", index=False)
