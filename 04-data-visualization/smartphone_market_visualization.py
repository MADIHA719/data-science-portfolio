# BS Data Science Portfolio: Project 06
# Title: Smartphone Market Data Visualization
# Description: Professional data visualization project using Pandas,
# Matplotlib, and Seaborn to analyze smartphone market trends.

import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns


def generate_market_plots():

    print("\n--- 📊 Smartphone Market Data Visualization ---\n")

    # -------------------------------
    # 1. Dataset
    # -------------------------------
    csv_data = """Brand,Model,Price_USD,Rating,Storage_GB
Apple,iPhone 15,799,4.8,128
Samsung,Galaxy S24,749,4.7,128
Google,Pixel 8,699,4.4,128
Apple,iPhone 15 Pro,999,4.9,256
Xiaomi,Redmi Note 13,249,4.2,64
Samsung,Galaxy A55,399,4.5,128
Google,Pixel 8 Pro,999,4.8,256
"""

    df = pd.read_csv(io.StringIO(csv_data))

    print("[Step 1] Dataset Loaded:\n")
    print(df)
    print("\n" + "-" * 50)

    # -------------------------------
    # 2. Theme setup
    # -------------------------------
    sns.set_theme(style="whitegrid")

    # ============================================================
    # CHART 1: Average Price by Brand (Bar Chart)
    # ============================================================

    brand_avg = (
        df.groupby("Brand")["Price_USD"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=brand_avg,
        x="Brand",
        y="Price_USD",
        palette="Blues"
    )

    plt.title("Average Smartphone Price by Brand", pad=15)
    plt.xlabel("Brand")
    plt.ylabel("Average Price (USD)")
    plt.tight_layout()

    plt.savefig("brand_price_comparison.png", dpi=300)
    print("✓ Saved: brand_price_comparison.png")

    plt.show()

    # ============================================================
    # CHART 2: Price vs Rating (Scatter Plot)
    # ============================================================

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Price_USD",
        y="Rating",
        hue="Brand",
        style="Storage_GB",
        s=120
    )

    plt.title("Price vs Customer Rating", pad=15)
    plt.xlabel("Price (USD)")
    plt.ylabel("Rating")

    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()

    plt.savefig("price_rating_correlation.png", dpi=300)
    print("✓ Saved: price_rating_correlation.png")

    plt.show()

    # ============================================================
    # CHART 3: Market Share (Pie Chart)
    # ============================================================

    brand_counts = df["Brand"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        brand_counts,
        labels=brand_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Smartphone Brand Market Share")

    plt.savefig("market_share.png", dpi=300)
    print("✓ Saved: market_share.png")

    plt.show()

    # -------------------------------
    # 4. Final Summary Report
    # -------------------------------
    print("\n--- FINAL SUMMARY REPORT ---")
    print(f"Total Smartphones: {len(df)}")
    print(f"Average Market Price: ${df['Price_USD'].mean():.2f}")
    print(f"Highest Price: ${df['Price_USD'].max():.2f}")
    print(f"Lowest Price: ${df['Price_USD'].min():.2f}")

    # Insight (very important for portfolio)
    print("\nInsight: Apple and Google dominate the premium smartphone segment.")

    print("\n--- Visualization Project Completed Successfully ---")


if __name__ == "__main__":
    generate_market_plots()
