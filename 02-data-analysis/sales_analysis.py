# BS Data Science Portfolio: Project 02
# Title: Mock Retail Sales Data Analyzer
# Description: Analyzes structured sales data to compute revenue and identify top-performing products.

def analyze_sales_data(sales_records):
    """
    Analyzes a dictionary of sales data and calculates revenue metrics.

    Parameters:
        sales_records (dict): Product sales data

    Returns:
        dict: Summary of total revenue and top product
    """

    if not sales_records:
        print("No sales data available.")
        return None

    total_revenue = 0
    best_selling_product = None
    max_product_revenue = 0

    print("\n--- Product Sales Breakdown ---")

    for product, details in sales_records.items():
        price = details["price"]
        units = details["units_sold"]

        item_revenue = price * units
        total_revenue += item_revenue

        print(f"{product:<12} | Units Sold: {units:<4} | Revenue: ${item_revenue:,.2f}")

        if item_revenue > max_product_revenue:
            max_product_revenue = item_revenue
            best_selling_product = product

    print("--------------------------------")
    print(f"Total Revenue:        ${total_revenue:,.2f}")
    print(f"Top Product:          {best_selling_product}")
    print(f"Top Product Revenue:   ${max_product_revenue:,.2f}")
    print("--------------------------------\n")

    return {
        "total_revenue": total_revenue,
        "top_product": best_selling_product,
        "top_revenue": max_product_revenue
    }


if __name__ == "__main__":
    monthly_sales = {
        "Laptop": {"price": 1200, "units_sold": 15},
        "Smartphone": {"price": 800, "units_sold": 30},
        "Headphones": {"price": 150, "units_sold": 75},
        "Monitor": {"price": 300, "units_sold": 20}
    }

    # Fixed: Added 4 spaces of indentation here
    analyze_sales_data(monthly_sales)
