import pandas as pd
import matplotlib.pyplot as plt
import os


def run_expense_tracker():

    # 1. Ensure output folders exist
    os.makedirs('visualizations', exist_ok=True)
    os.makedirs('report', exist_ok=True)

    # 2. Load the Dataset
    try:
        df = pd.read_csv(
            r'C:\Users\Mansi\OneDrive\Documents\Week 1 submission\Week-4-Data-Visualization\Data\sales_data (1).csv'
        )

        print("[INFO] Dataset successfully loaded. Shape:", df.shape)

    except FileNotFoundError:
        print("[ERROR] sales_data (1).csv not found inside the 'Data' folder.")
        return

    # 3. Data Cleaning & Validation

    missing_count = df.isnull().sum().sum()
    print(f"[INFO] Missing values found: {missing_count}")

    if missing_count > 0:
        print("[WARNING] Dataset contains missing values.")
        df = df.dropna()
    else:
        print("[INFO] No missing values found.")

    # Format Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Validate Total Sales calculation
    calculated_totals = df['Quantity'] * df['Price']

    if not (df['Total_Sales'] == calculated_totals).all():
        print("[WARNING] Total_Sales values were incorrect. Recalculating...")
        df['Total_Sales'] = calculated_totals
    else:
        print("[INFO] Total_Sales validation successful.")

    # 4. Expense Analysis & Metrics

    total_spent = df['Total_Sales'].sum()
    total_items = df['Quantity'].sum()
    avg_expense = df['Total_Sales'].mean()

    print("\n--- EXPENSE SUMMARY METRICS ---")
    print(f"Total Amount Spent: ${total_spent:,.2f}")
    print(f"Total Items Purchased: {total_items:,}")
    print(f"Average Expense per Transaction: ${avg_expense:,.2f}")

    # Group data by Product
    category_expenses = (
        df.groupby('Product')['Total_Sales']
        .sum()
        .reset_index()
    )

    # Group data by Month
    df['Month'] = df['Date'].dt.to_period('M')

    monthly_expenses = (
        df.groupby('Month')['Total_Sales']
        .sum()
        .reset_index()
    )

    monthly_expenses['Month'] = monthly_expenses['Month'].astype(str)

    # 5. Create Visualizations

    # -----------------------------
    # Chart 1: Bar Chart
    # -----------------------------

    plt.figure(figsize=(8, 5))

    plt.bar(
        category_expenses['Product'],
        category_expenses['Total_Sales'] / 1000,
        color='#e74c3c',
        edgecolor='black'
    )

    plt.title(
        'Expense Distribution by Category',
        fontsize=14,
        fontweight='bold'
    )

    plt.xlabel('Expense Category', fontsize=12)
    plt.ylabel('Total Spent ($ in Thousands)', fontsize=12)

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.7
    )

    plt.tight_layout()

    plt.savefig(
        'visualizations/expense_by_category.png',
        dpi=300
    )

    plt.close()

    # -----------------------------
    # Chart 2: Line Chart
    # -----------------------------

    plt.figure(figsize=(9, 5))

    plt.plot(
        monthly_expenses['Month'],
        monthly_expenses['Total_Sales'] / 1000,
        marker='o',
        color='#3498db',
        linewidth=2,
        markersize=8
    )

    plt.title(
        'Monthly Spending Trend (2024)',
        fontsize=14,
        fontweight='bold'
    )

    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Spent ($ in Thousands)', fontsize=12)

    plt.grid(
        True,
        linestyle='--',
        alpha=0.7
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        'visualizations/monthly_spending_trend.png',
        dpi=300
    )

    plt.close()

    # -----------------------------
    # Chart 3: Pie Chart
    # -----------------------------

    plt.figure(figsize=(8, 8))

    plt.pie(
        category_expenses['Total_Sales'],
        labels=category_expenses['Product'],
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title(
        'Expense Distribution by Product',
        fontsize=14,
        fontweight='bold'
    )

    plt.tight_layout()

    plt.savefig(
        'visualizations/expense_distribution.png',
        dpi=300
    )

    plt.close()

    # -----------------------------
    # 6. Generate Meaningful Insights
    # -----------------------------

    highest_product = category_expenses.loc[
        category_expenses['Total_Sales'].idxmax(),
        'Product'
    ]

    highest_product_amount = category_expenses['Total_Sales'].max()

    lowest_product = category_expenses.loc[
        category_expenses['Total_Sales'].idxmin(),
        'Product'
    ]

    lowest_product_amount = category_expenses['Total_Sales'].min()

    highest_month = monthly_expenses.loc[
        monthly_expenses['Total_Sales'].idxmax(),
        'Month'
    ]

    highest_month_amount = monthly_expenses['Total_Sales'].max()

    print("\n--- KEY INSIGHTS ---")

    print(
        f"1. The highest spending product is {highest_product} "
        f"with total spending of ${highest_product_amount:,.2f}."
    )

    print(
        f"2. The lowest spending product is {lowest_product} "
        f"with total spending of ${lowest_product_amount:,.2f}."
    )

    print(
        f"3. The highest spending month is {highest_month} "
        f"with spending of ${highest_month_amount:,.2f}."
    )

    print(
        "\n[INFO] Charts successfully created and saved "
        "to 'visualizations/' folder."
    )

    print("[INFO] Analysis completed successfully.")


# Run the program
if __name__ == "__main__":
    run_expense_tracker()
