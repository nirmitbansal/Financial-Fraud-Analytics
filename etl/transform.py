import pandas as pd

# --------------------------------------------------
# STEP 1: READ RAW DATA
# --------------------------------------------------
print("Reading raw CSV data...")

# Always use path relative to PROJECT ROOT
df = pd.read_csv("data/raw/creditcard.csv")

print("Raw data loaded")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# --------------------------------------------------
# STEP 2: BASIC TRANSFORMATION
# --------------------------------------------------
print("Starting data transformation...")

# Create a fraud flag (1 = fraud, 0 = normal)
df["is_fraud"] = df["Class"]

# Keep only columns needed for analytics
df = df[["Time", "Amount", "is_fraud"]]

# --------------------------------------------------
# STEP 3: CREATE AMOUNT CATEGORY (BUSINESS LOGIC)
# --------------------------------------------------
df["amount_category"] = pd.cut(
    df["Amount"],
    bins=[0, 50, 200, 1000, df["Amount"].max()],
    labels=["Low", "Medium", "High", "Very High"]
)

# --------------------------------------------------
# STEP 4: CREATE TIME BUCKETS
# --------------------------------------------------
df["time_bucket"] = pd.cut(
    df["Time"],
    bins=[0, 20000, 40000, 60000, df["Time"].max()],
    labels=["Early", "Mid", "Late", "Very Late"]
)

# --------------------------------------------------
# STEP 5: DATA VALIDATION
# --------------------------------------------------
print("Transformed data preview:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nTransformation completed successfully")
