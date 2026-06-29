import pandas as pd
import glob

files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

data = pd.concat(all_data, ignore_index=True)


pink_morsels = data[
    data["product"].str.lower() == "pink morsel"
].copy()


pink_morsels["price"] = (
    pink_morsels["price"]
    .str.replace("$", "", regex=False)
    .astype(float)
)


pink_morsels["Sales"] = (
    pink_morsels["quantity"] *
    pink_morsels["price"]
)


output = pink_morsels[
    ["Sales", "date", "region"]
]


output = output.rename(
    columns={
        "date": "Date"
    }
)

output.to_csv(
    "output.csv",
    index=False
)


print("Data processing completed successfully!")
print(output.head())