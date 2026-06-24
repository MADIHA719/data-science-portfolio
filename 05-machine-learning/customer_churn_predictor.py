# BS Data Science Portfolio: Project 08
# Title: Customer Churn Predictive Modeling using Scikit-Learn
# Description: Machine learning pipeline including training, evaluation,
# and feature importance analysis using Random Forest.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def run_churn_pipeline():

    print("\n--- 🧠 Customer Churn ML Pipeline Starting ---\n")
    print("=" * 60)

    # ------------------------------------------------
    # 1. Simulated Customer Dataset
    # ------------------------------------------------
    np.random.seed(42)

    raw_data = {
        "tenure_months": [12, 2, 24, 1, 36, 18, 6, 10, 3, 30, 40, 5],
        "monthly_charges": [85.5, 45.0, 95.0, 20.0, 110.0, 75.5, 65.0, 80.0, 55.5, 90.0, 100.5, 30.0],
        "tech_support_user": [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        "churn_status": [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    }

    df = pd.DataFrame(raw_data)

    print("[Step 1] Dataset Preview:")
    print(df)
    print("-" * 60)

    # ------------------------------------------------
    # 2. Features & Target
    # ------------------------------------------------
    X = df[["tenure_months", "monthly_charges", "tech_support_user"]]
    y = df["churn_status"]

    # ------------------------------------------------
    # 3. Train-Test Split
    # ------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    print(f"[Step 2] Training Samples: {len(X_train)} | Testing Samples: {len(X_test)}")
    print("-" * 60)

    # ------------------------------------------------
    # 4. Model Training
    # ------------------------------------------------
    print("[Step 3] Training Random Forest Model...")

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # ------------------------------------------------
    # 5. Prediction & Evaluation
    # ------------------------------------------------
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n--- 📊 MODEL PERFORMANCE REPORT ---")
    print(f"Model Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)\n")

    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Stayed", "Churned"]))

    print("=" * 60)

    # ------------------------------------------------
    # 6. Feature Importance
    # ------------------------------------------------
    print("\n--- 🔍 Feature Importance ---")

    importances = model.feature_importances_

    for feature, importance in zip(X.columns, importances):
        print(f"{feature:<20} : {importance:.4f}")

    print("=" * 60)

    # ------------------------------------------------
    # 7. Insight (IMPORTANT for portfolio)
    # ------------------------------------------------
    print("\n--- 📌 BUSINESS INSIGHT ---")
    print("Customers with higher tenure and active tech support are less likely to churn.")

    print("\n--- ML PIPELINE COMPLETED SUCCESSFULLY ---")


if __name__ == "__main__":
    run_churn_pipeline()
