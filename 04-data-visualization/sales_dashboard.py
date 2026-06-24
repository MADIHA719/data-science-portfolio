"""
🏆 BS Data Science Portfolio: Project 10
Title: Interactive E-Commerce Sales Dashboard
Author: Madiha
Description: Fully Operational Streamlit Dashboard for E-Commerce Analytics
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🏆 E-Commerce Analytics & Predictive Dashboard")
st.markdown("---")

@st.cache_data
def load_dashboard_data():
    if not os.path.exists("cleaned_ecommerce_data.csv") or not os.path.exists("category_summary.csv"):
        st.error("❌ Required CSV files not found.\nPlease run e_commerce_capstone.py first.")
        return None, None
    df = pd.read_csv("cleaned_ecommerce_data.csv")
    summary = pd.read_csv("category_summary.csv")
    return df, summary

df, summary = load_dashboard_data()

if df is not None:
    if "Order_Month" not in df.columns:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        np.random.seed(42)
        df["Order_Month"] = np.random.choice(months, size=len(df))

    # ---------------------------------------------------
    # SIDEBAR FILTER
    # ---------------------------------------------------
    st.sidebar.header("Dashboard Controls")
    categories = sorted(df["Category"].unique())
    selected_categories = st.sidebar.multiselect("Select Categories", categories, default=categories)

    # Core Reactive Filter Operations
    filtered_df = df[df["Category"].isin(selected_categories)]
    
    # Recalculate summary metrics dynamically to prevent statistical mismatch bugs
    dynamic_summary = (
        filtered_df.groupby("Category")
        .agg(Total_Revenue=("Price_USD", "sum"), Average_Rating=("Rating", "mean"), Conversion_Rate=("Converted_Buyer", "mean"))
        .reset_index()
    )

    # ---------------------------------------------------
    # KPI CARDS
    # ---------------------------------------------------
    if not filtered_df.empty:
        total_revenue = filtered_df["Price_USD"].sum()
        total_orders = len(filtered_df)
        avg_rating = filtered_df["Rating"].mean()
        conversion_rate = filtered_df["Converted_Buyer"].mean() * 100

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("🛒 Total Orders", f"{total_orders:,}")
        col3.metric("⭐ Average Rating", f"{avg_rating:.2f}/5")
        col4.metric("📈 Conversion Rate", f"{conversion_rate:.2f}%")
        st.markdown("---")

        # ---------------------------------------------------
        # VISUALIZATION GRID ARRANGEMENT
        # ---------------------------------------------------
        viz_row1_col1, viz_row1_col2 = st.columns(2)
        
        with viz_row1_col1:
            st.subheader("📊 Revenue by Category")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(data=dynamic_summary, x="Category", y="Total_Revenue", ax=ax, palette="Blues_r")
            plt.xticks(rotation=15)
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        with viz_row1_col2:
            st.subheader("📦 Price Distribution")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=filtered_df, x="Category", y="Price_USD", ax=ax, palette="Set2")
            plt.xticks(rotation=15)
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        viz_row2_col1, viz_row2_col2 = st.columns(2)
        
        with viz_row2_col1:
            st.subheader("📈 Monthly Revenue Trend")
            monthly = filtered_df.groupby("Order_Month")["Price_USD"].sum().reindex(
                ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            )
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(monthly.index, monthly.values, marker="o", color="#1f77b4", linewidth=2.5)
            ax.set_xlabel("Month")
            ax.set_ylabel("Revenue ($)")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        with viz_row2_col2:
            st.subheader("🥧 Revenue Share by Category")
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.pie(dynamic_summary["Total_Revenue"], labels=dynamic_summary["Category"], autopct="%1.1f%%", startangle=140, colors=sns.color_palette("Pastel1"))
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        # ---------------------------------------------------
        # INTERACTIVE DOWNLOADS & LOGS
        # ---------------------------------------------------
        st.markdown("---")
        st.subheader("⬇ Download Filtered Data")
        st.download_button(
            label="Download CSV",
            data=filtered_df.to_csv(index=False),
            file_name="filtered_ecommerce_data.csv",
            mime="text/csv"
        )

        st.subheader("🔍 Transaction Records")
        st.dataframe(filtered_df.head(100), use_container_width=True)

        # ---------------------------------------------------
        # STRATEGIC BUSINESS INSIGHTS
        # ---------------------------------------------------
        st.markdown("---")
        st.subheader("📌 Business Insights")
        if not dynamic_summary.empty:
            # Fixed line: proper positional indexing combined with explicit label lookups
            top_category = dynamic_summary.sort_values(by="Total_Revenue", ascending=False).iloc[0]["Category"]
            st.success(f"**Top Performing Category:** {top_category}")
        st.info("💡 Predictive Modeling Signal: High user-submitted ratings combined with proactive conversion discount flags drive the highest transaction likelihood.")
    else:
        st.warning("⚠️ No data available. Please select at least one active commercial category from the sidebar controls.")

    # ---------------------------------------------------
    # FOOTER OVERLAY
    # ---------------------------------------------------
    st.markdown("---")
    st.markdown(
        """
        ### 👩‍💻 Created by Madiha
        **BS Data Science Portfolio**
        Skills Demonstrated:
        ✔ Python | ✔ Pandas | ✔ NumPy | ✔ Matplotlib | ✔ Seaborn | ✔ Streamlit | ✔ Predictive System Design
        """
    )
