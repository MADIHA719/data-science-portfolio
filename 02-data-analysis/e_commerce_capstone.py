"""
🏆 BS Data Science Portfolio: Project 09 (Master Capstone)
Title: Production-Scale End-to-End E-Commerce Analytics &
Predictive Machine Learning Pipeline
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score
)

np.random.seed(42)


def generate_production_dataset(n_samples=5000):

    categories = [
        "Electronics",
        "Clothing",
        "Home & Kitchen",
        "Books",
        "Beauty"
    ]

    weights = [0.30, 0.25, 0.20, 0.15, 0.10]

    data = {

        "Order_ID":
        range(10001, 10001 + n_samples),

        "Category":
        np.random.choice(
            categories,
            size=n_samples,
            p=weights
        ),

        "Price_USD":
        np.random.exponential(
            scale=120,
            size=n_samples
        ) + 5,

        "Discount_Applied":
        np.random.choice(
            [0, 1],
            size=n_samples,
            p=[0.65, 0.35]
        ),

        "Rating":
        np.random.normal(
            loc=4.1,
            scale=0.6,
            size=n_samples
        ).clip(1, 5)
    }

    df = pd.DataFrame(data)

    # Missing values

    df.loc[
        df.sample(frac=0.04, random_state=42).index,
        "Price_USD"
    ] = np.nan

    df.loc[
        df.sample(frac=0.06, random_state=24).index,
        "Rating"
    ] = np.nan

    df.loc[
        df.sample(frac=0.02, random_state=12).index,
        "Discount_Applied"
    ] = np.nan

    temp_df = df.copy()

    temp_df["Price_USD"] = temp_df["Price_USD"].fillna(
        temp_df["Price_USD"].median()
    )

    temp_df["Rating"] = temp_df["Rating"].fillna(
        temp_df["Rating"].mean()
    )

    temp_df["Discount_Applied"] = temp_df[
        "Discount_Applied"
    ].fillna(0)

    def conversion_logic(row):

        probability = 0.15

        if row["Discount_Applied"] == 1:
            probability += 0.25

        if row["Rating"] >= 4.3:
            probability += 0.20

        if row["Price_USD"] < 40:
            probability += 0.15

        probability = min(probability, 0.90)

        return np.random.choice(
            [0, 1],
            p=[1 - probability, probability]
        )

    df["Converted_Buyer"] = temp_df.apply(
        conversion_logic,
        axis=1
    )

    return df


def run_e_commerce_capstone():

    print("\n🏆 E-COMMERCE MASTER CAPSTONE")
    print("=" * 70)

    df = generate_production_dataset(5000)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nFirst Five Rows:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Data Cleaning

    df["Price_USD"] = df["Price_USD"].fillna(
        df["Price_USD"].median()
    )

    df["Rating"] = df["Rating"].fillna(
        df["Rating"].mean()
    )

    df["Discount_Applied"] = (
        df["Discount_Applied"]
        .fillna(0)
        .astype(int)
    )

    print("\n✓ Data Cleaning Completed")

    df.to_csv(
        "cleaned_ecommerce_data.csv",
        index=False
    )

    print("✓ Saved: cleaned_ecommerce_data.csv")

    # Feature Engineering

    df["Estimated_Savings"] = (

        df["Price_USD"]

        * df["Discount_Applied"]

        * 0.20

    )

    print("✓ Feature Engineering Completed")

    # EDA

    category_summary = (

        df.groupby("Category")

        .agg(

            Total_Revenue=("Price_USD", "sum"),

            Average_Rating=("Rating", "mean"),

            Conversion_Rate=("Converted_Buyer", "mean")

        )

        .sort_values(

            by="Total_Revenue",

            ascending=False

        )

        .reset_index()

    )

    print("\nCategory Summary:\n")

    print(category_summary)

    category_summary.to_csv(

        "category_summary.csv",

        index=False

    )

    print("\n✓ Saved: category_summary.csv")

    # Visualization

    sns.set_theme(style="darkgrid")

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(15, 6)
    )

    sns.barplot(
        data=category_summary,
        x="Category",
        y="Total_Revenue",
        ax=axes[0]
    )

    axes[0].set_title("Revenue by Category")

    axes[0].tick_params(
        axis="x",
        rotation=15
    )

    sns.boxplot(
        data=df,
        x="Category",
        y="Price_USD",
        ax=axes[1]
    )

    axes[1].set_title(
        "Price Distribution"
    )

    axes[1].tick_params(
        axis="x",
        rotation=15
    )

    plt.tight_layout()

    plt.savefig(
        "capstone_performance_plots.png",
        dpi=300
    )

    plt.show()

    plt.close()

    print("✓ Saved: capstone_performance_plots.png")

    # Machine Learning

    features = [

        "Price_USD",

        "Discount_Applied",

        "Rating",

        "Estimated_Savings"

    ]

    X = df[features]

    y = df["Converted_Buyer"]

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.25,

        random_state=42,

        stratify=y

    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    # Logistic Regression

    lr_model = LogisticRegression(
        random_state=42
    )

    lr_model.fit(
        X_train_scaled,
        y_train
    )

    lr_pred = lr_model.predict(
        X_test_scaled
    )

    lr_acc = accuracy_score(
        y_test,
        lr_pred
    )

    # Random Forest

    rf_model = RandomForestClassifier(

        n_estimators=150,

        max_depth=10,

        random_state=42

    )

    rf_model.fit(
        X_train,
        y_train
    )

    rf_pred = rf_model.predict(
        X_test
    )

    rf_acc = accuracy_score(
        y_test,
        rf_pred
    )

    rf_prob = rf_model.predict_proba(
        X_test
    )[:, 1]

    roc = roc_auc_score(
        y_test,
        rf_prob
    )

    print("\nMODEL PERFORMANCE")
    print("=" * 50)

    print(f"Logistic Regression : {lr_acc:.4f}")
    print(f"Random Forest       : {rf_acc:.4f}")
    print(f"ROC-AUC Score       : {roc:.4f}")

    print("\nClassification Report:\n")

    print(

        classification_report(

            y_test,

            rf_pred,

            target_names=[

                "No Purchase",

                "Purchase"

            ]

        )

    )

    # Feature Importance

    feature_df = pd.DataFrame({

        "Feature": features,

        "Importance":
        rf_model.feature_importances_

    })

    feature_df = feature_df.sort_values(

        by="Importance",

        ascending=False

    )

    print("\nFeature Importance:\n")

    print(feature_df)

    feature_df.to_csv(
        "feature_importance.csv",
        index=False
    )

    print("\n✓ Saved: feature_importance.csv")

    # Business Insights

    top_category = category_summary.loc[
        category_summary["Total_Revenue"].idxmax(),
        "Category"
    ]

    print("\n📈 BUSINESS INSIGHTS")
    print("-" * 40)

    print(f"Top Category : {top_category}")

    print(
        f"Average Rating : "
        f"{df['Rating'].mean():.2f}/5"
    )

    print(
        "ML Insight : Price, Discounts "
        "and Ratings influence customer purchases."
    )

    print("\n🏁 CAPSTONE PROJECT COMPLETED SUCCESSFULLY")


if __name__ == "__main__":

    run_e_commerce_capstone()
