# BS Data Science Portfolio: Project 03
# Title: Housing Market Exploratory Data Analysis (EDA)
# Description: Processes real estate property records to clean data, segment by location, and compute market insights.

def run_housing_eda(raw_property_data):
    """
    Performs data cleaning, filtering, and statistical profiling on property listings.
    
    Parameters:
        raw_property_data (list): List of dictionaries containing raw property details.
        
    Returns:
        dict: Cleaned data count and average market metrics.
    """
    print("--- 🚀 Starting Housing Market EDA Pipeline ---")
    
    # 1. Data Cleaning: Filter out records with missing data (None)
    clean_data = [item for item in raw_property_data if item["price"] is not None and item["city"] is not None]
    dropped_count = len(raw_property_data) - len(clean_data)
    print(f"[Data Cleaning] Removed {dropped_count} incomplete records.")

    if not clean_data:
        print("[Error] No valid data remaining after cleaning.")
        return None

    # 2. Aggregation: Calculate overall market metrics
    total_listings = len(clean_data)
    prices = [item["price"] for item in clean_data]
    avg_price = sum(prices) / total_listings
    
    print(f"[Market Metrics] Active Clean Listings: {total_listings}")
    print(f"[Market Metrics] Average Market Price:  ${avg_price:,.2f}")

    # 3. Segmentation: Analyze data by City
    city_metrics = {}
    for item in clean_data:
        city = item["city"]
        price = item["price"]
        
        if city not in city_metrics:
            city_metrics[city] = {"total_price": 0, "count": 0}
            
        city_metrics[city]["total_price"] += price
        city_metrics[city]["count"] += 1

    print("\n--- 🏙️ City-by-City Market Analysis ---")
    for city, stats in city_metrics.items():
        city_avg = stats["total_price"] / stats["count"]
        print(f"City: {city:<12} | Listings: {stats['count']:<3} | Avg Price: ${city_avg:,.2f}")
        
    print("----------------------------------------\n")
    
    return {
        "clean_count": total_listings, 
        "avg_price": avg_price
    }


if __name__ == "__main__":
    # Simulating a raw dataset loaded from a CSV file
    raw_listings = [
        {"id": 1, "city": "New York", "price": 850000},
        {"id": 2, "city": "Chicago",  "price": 320000},
        {"id": 3, "city": "Austin",   "price": 450000},
        {"id": 4, "city": "New York", "price": None},   # Missing data to be cleaned
        {"id": 5, "city": "Chicago",  "price": 280000},
        {"id": 6, "city": "Austin",   "price": 510000},
        {"id": 7, "city": None,       "price": 300000},   # Missing data to be cleaned
        {"id": 8, "city": "New York", "price": 990000}
    ]

    # Run the data pipeline
    run_housing_eda(raw_listings)
