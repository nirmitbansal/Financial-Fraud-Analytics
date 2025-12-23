import pandas as pd
from sqlalchemy import create_engine

print("Starting LOAD process...")

# --------------------------------------------------
# STEP 1: READ TRANSFORMED DATA AGAIN
# (Simple approach: re-transform inside load)
# --------------------------------------------------
df = pd.read_csv("data/raw/creditcard.csv")

# Create fraud flag
df["is_fraud"] = df["Class"]

# Select only required columns
df = df[["Time", "Amount", "is_fraud"]]

# Create amount category
df["amount_category"] = pd.cut(
    df["Amount"],
    bins=[0, 50, 200, 1000, df["Amount"].max()],
    labels=["Low", "Medium", "Medium-High", "High"]
)

print("Data prepared for loading")
print("Rows:", df.shape[0])

# --------------------------------------------------
# STEP 2: CONNECT TO MYSQL
# --------------------------------------------------
engine = create_engine(
    "mysql+pymysql://nirmitbansal:nirmit2708@localhost:3306/fraud_analytics"
)

print("Connected to MySQL")

# --------------------------------------------------
# STEP 3: LOAD DATA INTO TABLE
# --------------------------------------------------
df.to_sql(
    name="transactions",
    con=engine,
    if_exists="replace",   # overwrite table if exists
    index=False
)

print("Data loaded successfully into MySQL table: transactions")
