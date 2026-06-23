# BS Data Science Portfolio: Project 04
# Title: Smartphone Market Analysis using Pandas
# Description: End-to-end EDA using Pandas including cleaning, imputation, aggregation, and filtering.

import pandas as pd
import io

def run_pandas_eda():
    print("\n--- 🐼 Starting Professional Pandas EDA Pipeline ---\n")

    # Simulated raw dataset (like real CSV file)
    csv_data = """Brand,Model,Price_USD,Rating,Storage_GB
Apple,iPhone 15,799,4.8,128
Samsung,Galaxy S24,749,4.7,128
Google,Pixel 8,699,,128
Apple,iPhone 15 Pro,999,4.9,256
Xiaomi,Redmi Note 13,,4.2,64
Samsung,Galaxy A55,399,4.5,
Google,Pixel 8 Pro,999,4.8,256
"""

    # 1. Load data
    df = pd.read_csv(io.StringIO(csv_data))

    print("[Step 1] Raw Dataset:")
    print(df, "\n")

    # 2. Clean missing critical values (Price is important)
    df_clean = df.dropna(subset=['Price_USD']).copy()

    print("[Step 2] After Removing Missing Prices:")
    print(df_clean, "\n")

    # 3. Convert columns to numeric (safe practice in real datasets)
    df_clean['Price_USD'] = pd.to_numeric(df_clean['Price_USD'], errors='coerce')
    df_clean['Rating'] = pd.to_numeric(df_clean['Rating'], errors='coerce')
    df_clean['Storage_GB'] = pd.to_numeric(df_clean['Storage_GB'], errors='coerce')

    # 4. Handle missing values (Imputation)
    df_clean['Rating'] = df_clean['Rating'].fillna(df_clean['Rating'].mean())
    df_clean['Storage_GB'] = df_clean['Storage_GB'].fillna(df_clean['Storage_GB'].median())

    print("[Step 3] After Handling Missing Values:")
    print(df_clean, "\n")

    # 5. Brand-level analysis (GroupBy aggregation)
    brand_summary = df_clean.groupby('Brand').agg(
        Average_Price=('Price_USD', 'mean'),
        Total_Models=('Model', 'count'),
        Average_Rating=('Rating', 'mean'),
        Average_Storage=('Storage_GB', 'mean')
    ).reset_index()

    print("[Step 4] Brand Market Summary:")
    print(brand_summary, "\n")

    # 6. Premium segment analysis
    premium_phones = df_clean[df_clean['Price_USD'] > 700]

    print("[Step 5] Premium Smartphones (> $700):")
    print(premium_phones[['Brand', 'Model', 'Price_USD']], "\n")

    # 7. Final summary report (professional touch)
    print("--- 📊 FINAL SUMMARY REPORT ---")
    print(f"Total Clean Records: {len(df_clean)}")
    print(f"Average Market Price: ${df_clean['Price_USD'].mean():.2f}")
    print(f"Most Expensive Phone: ${df_clean['Price_USD'].max():.2f}")
    print(f"Most Affordable Phone: ${df_clean['Price_USD'].min():.2f}")

    print("\n--- EDA Pipeline Completed Successfully ---\n")


if __name__ == "__main__":
    run_pandas_eda()
