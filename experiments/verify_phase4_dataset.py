
import pandas as pd

df = pd.read_csv("phase4_scenarios.csv")

print("\n--- Dataset verification ---")
print("Total rows:", len(df))
print("Unique test IDs:", df["test_id"].nunique())
print("Categories:", df["category"].nunique())

print("\n--- Scenarios per category ---")
print(df["category"].value_counts().sort_index())

print("\n--- Missing values ---")
print(df.isnull().sum())

print("\n--- Test ID range ---")
print(df["test_id"].iloc[0], "to", df["test_id"].iloc[-1])

# Validation checks
assert len(df) == 30, "Expected exactly 30 scenarios"
assert df["test_id"].nunique() == 30, "Duplicate test IDs found"
assert df["category"].nunique() == 6, "Expected six categories"
assert not df.isnull().any().any(), "Missing values found"

print("\nSUCCESS: Dataset passed all basic checks.")
