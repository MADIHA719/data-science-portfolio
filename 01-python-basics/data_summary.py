# BS Data Science Portfolio: Project 01
# Title: Data Summary Statistics Analyzer
# Description: A simple script that calculates key statistical summaries from a list of numbers.

def calculate_summary_statistics(data_list):
    """
    Calculates basic summary metrics from a list of numbers.
    
    Parameters:
        data_list (list): List of numerical values
    
    Returns:
        dict: Dictionary containing summary statistics
    """
    
    if not data_list:
        print("The data list is empty.")
        return None

    # Calculations
    total_sum = sum(data_list)
    count = len(data_list)
    average = total_sum / count
    max_value = max(data_list)
    min_value = min(data_list)

    # Result dictionary (useful for future projects like pandas/ML)
    results = {
        "count": count,
        "sum": total_sum,
        "mean": average,
        "max": max_value,
        "min": min_value
    }

    # Display report
    print("\n--- Data Summary Report ---")
    print(f"Total Elements:        {results['count']}")
    print(f"Sum of Elements:       {results['sum']}")
    print(f"Mean (Average):        {results['mean']:.2f}")
    print(f"Maximum Value:         {results['max']}")
    print(f"Minimum Value:         {results['min']}")
    print("---------------------------\n")

    return results


# Run only if file is executed directly
if __name__ == "__main__":
    # Sample dataset for testing
    student_test_scores = [85, 90, 78, 92, 88, 74, 95, 81]

    # Call function
    calculate_summary_statistics(student_test_scores)
