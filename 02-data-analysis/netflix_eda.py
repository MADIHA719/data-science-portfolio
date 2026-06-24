# BS Data Science Portfolio: Project 07
# Title: Netflix Content Catalog Exploratory Data Analysis (EDA)
# Description: Professional-level EDA using Pandas with cleaning,
# analysis, and visual insights for entertainment catalog data.

import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns


def run_netflix_eda():

    print("\n--- 🎬 Netflix Catalog Professional EDA Pipeline ---\n")

    # ------------------------------------------------
    # 1. Raw Dataset
    # ------------------------------------------------
    raw_csv_data = """show_id,type,title,director,country,date_added,release_year,rating,duration
s1,Movie,Dick Johnson Is Dead,Kirsten Johnson,United States,"September 25, 2021",2020,PG-13,90 min
s2,TV Show,Blood & Water,,South Africa,"September 24, 2021",2021,TV-MA,2 Seasons
s3,TV Show,Ganglands,Julien Leclercq,,"September 24, 2021",2021,TV-MA,1 Season
s4,Movie,Jailer,,India,,2023,TV-14,160 min
s5,Movie,Kota Factory,,India,"September 24, 2021",2021,TV-MA,2 Seasons
s6,TV Show,Midnight Mass,Mike Flanagan,United States,"September 24, 2021",2021,TV-MA,1 Season
s7,Movie,My Little Pony,Robert Cullen,United States,"September 24, 2021",2021,PG,91 min
s8,Movie,Sankofa,Haile Gerima,United States,"September 24, 2021",1993,TV-MA,125 min
"""

    df = pd.read_csv(io.StringIO(raw_csv_data))

    print(f"[Step 1] Dataset Loaded: {len(df)} Records\n")
    print(df)
    print("\n" + "-" * 60)

    # ------------------------------------------------
    # 2. Missing Values
    # ------------------------------------------------
    print("\n[Step 2] Missing Values Report:\n")
    print(df.isnull().sum())

    # ------------------------------------------------
    # 3. Data Cleaning
    # ------------------------------------------------
    df["director"] = df["director"].fillna("Unknown Director")
    df["country"] = df["country"].fillna("Global Production")
    df["date_added"] = df["date_added"].fillna("Unknown Date")

    df["type"] = df["type"].str.strip()
    df["country"] = df["country"].str.strip()

    print("\n[Step 3] Missing Values Handled Successfully")
    print("-" * 60)

    # ------------------------------------------------
    # 4. Content Type Analysis
    # ------------------------------------------------
    print("\n[Step 4] Content Type Distribution:\n")

    type_counts = df["type"].value_counts()

    for c_type, count in type_counts.items():
        print(f"{c_type:<10} : {count} Titles")

    # ------------------------------------------------
    # 5. Filtering
    # ------------------------------------------------
    print("\n[Step 5] Recent US Content (2020+):\n")

    us_recent = df[
        (df["country"] == "United States") &
        (df["release_year"] >= 2020)
    ]

    print(us_recent[["title", "type", "release_year", "rating"]])

    # ------------------------------------------------
    # 6. VISUALIZATION
    # ------------------------------------------------
    sns.set_theme(style="whitegrid")

    # Chart 1
    plt.figure(figsize=(6, 4))

    type_counts.plot(kind="bar", rot=0)

    plt.title("Netflix Content Type Distribution")
    plt.xlabel("Content Type")
    plt.ylabel("Count")

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()

    plt.savefig("netflix_content_type.png", dpi=300)

    plt.show()
    plt.close()

    # Chart 2
    plt.figure(figsize=(7, 4))

    top_countries = df["country"].value_counts().head(5)

    top_countries.plot(kind="bar", rot=45)

    plt.title("Top Producing Countries on Netflix")
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()

    plt.savefig("netflix_top_countries.png", dpi=300)

    plt.show()
    plt.close()

    # ------------------------------------------------
    # 7. FINAL INSIGHTS
    # ------------------------------------------------
    oldest_year = df["release_year"].min()
    newest_year = df["release_year"].max()

    print("\n--- 📊 FINAL INSIGHTS REPORT ---")

    print(f"Total Catalog Items      : {len(df)}")
    print(f"Content Timeline         : {oldest_year} - {newest_year}")
    print(f"Most Common Country      : {df['country'].mode()[0]}")
    print(f"Movies vs TV Shows       : {type_counts.to_dict()}")

    missing_directors = (df["director"] == "Unknown Director").sum()

    print(f"Missing Directors Fixed  : {missing_directors}")

    print("\n--- 🎯 Netflix EDA Completed Successfully ---")


if __name__ == "__main__":
    run_netflix_eda()
