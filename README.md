\# Personal Expense Tracker \& Analysis



\## 📌 Project Overview



\- This project is a \*\*Python-based Personal Expense Tracker and Analysis System\*\*.

\- It was developed as part of the \*\*Week 4: Data Visualization \& Complete Project\*\*.

\- The project uses a \*\*sales transaction dataset\*\* to perform expense analysis.

\- Python is used to:

&#x20; - Load the dataset

&#x20; - Clean and validate the data

&#x20; - Analyze expenses

&#x20; - Calculate important metrics

&#x20; - Create charts and visualizations

&#x20; - Generate useful insights



\---



\## 🎯 Project Objectives



The main objectives of this project are:



\- Load and analyze transaction data.

\- Check the dataset for missing values.

\- Clean and validate the data.

\- Verify the accuracy of calculated sales values.

\- Calculate the \*\*total amount spent\*\*.

\- Calculate the \*\*total number of items purchased\*\*.

\- Calculate the \*\*average expense per transaction\*\*.

\- Find the \*\*highest-spending product\*\*.

\- Find the \*\*lowest-spending product\*\*.

\- Identify the \*\*month with the highest spending\*\*.

\- Create meaningful data visualizations.

\- Generate automatic insights from the analysis.



\---



\## 🛠️ Technologies Used



The project is developed using the following technologies:



\- \*\*Python\*\* – Main programming language.

\- \*\*Pandas\*\* – Used for data loading, cleaning, and analysis.

\- \*\*Matplotlib\*\* – Used for creating charts and visualizations.



\---



\## 📊 Dataset



The project uses a \*\*CSV dataset\*\* containing transaction information.



The dataset includes the following important columns:



\- \*\*Date\*\* – Date of the transaction.

\- \*\*Product\*\* – Name of the product purchased.

\- \*\*Quantity\*\* – Number of items purchased.

\- \*\*Price\*\* – Price of each item.

\- \*\*Total Sales\*\* – Total amount spent on the transaction.



\### Dataset Size



\- \*\*Total Records:\*\* 100

\- \*\*File Format:\*\* CSV



\---



\## 🔄 Data Analysis Process



The project follows a step-by-step data analysis process:



\### 1. Load the Dataset

\- The CSV file is loaded using Pandas.

\- The program checks whether the dataset can be loaded successfully.



\### 2. Check Dataset Shape

\- The number of rows and columns is checked.

\- This helps understand the size of the dataset.



\### 3. Check Missing Values

\- The dataset is checked for empty or missing values.

\- Missing values are handled before performing the analysis.



\### 4. Convert Date Format

\- The \*\*Date\*\* column is converted into the proper date format.

\- This makes monthly analysis easier.



\### 5. Validate Total Sales

\- The program checks whether the \*\*Total Sales\*\* value is correct.

\- It compares Total Sales with:



\*\*Quantity × Price\*\*



\- If the calculated value is incorrect, the program can recalculate it.



\### 6. Calculate Expense Metrics

The program calculates:



\- Total amount spent

\- Total items purchased

\- Average expense per transaction

\- Highest spending product

\- Lowest spending product



\### 7. Analyze Product Spending

\- Expenses are grouped according to products.

\- This helps identify which products contribute the most and least to total spending.



\### 8. Analyze Monthly Spending

\- Transactions are grouped by month.

\- Monthly spending is calculated.

\- The month with the highest spending is identified.



\### 9. Create Visualizations

The project creates different charts to make the analysis easier to understand.



\### 10. Generate Key Insights

\- The program automatically identifies important findings from the dataset.

\- These findings are useful for understanding spending patterns.



\---



\# 📈 Visualizations



The project contains three main visualizations.



\## 1. 📊 Bar Chart — Expense by Category



\- The bar chart compares spending between different products/categories.

\- It makes it easy to identify products with:

&#x20; - High spending

&#x20; - Low spending



\*\*File:\*\*

`expense\_by\_category.png`



\---



\## 2. 📈 Line Chart — Monthly Spending Trend



\- The line chart shows how spending changes over time.

\- It displays monthly spending.

\- It helps identify the month with the highest spending.

\- It also makes spending trends easier to understand.



\*\*File:\*\*

`monthly\_spending\_trend.png`



\---



\## 3. 🥧 Pie Chart — Expense Distribution



\- The pie chart shows the percentage distribution of total spending.

\- Each section represents a different product/category.

\- It helps understand which products contribute most to overall spending.



\*\*File:\*\*

`expense\_distribution.png`



\---



\# 📋 Key Results



The analysis produced the following results:



\- \*\*Total Amount Spent:\*\* $12,365,048.00

\- \*\*Total Items Purchased:\*\* 478

\- \*\*Average Expense per Transaction:\*\* $123,650.48

\- \*\*Highest Spending Product:\*\* Laptop

\- \*\*Lowest Spending Product:\*\* Monitor

\- \*\*Highest Spending Month:\*\* March 2024



\---



\# ✅ Error Handling and Data Validation



The program includes several validation and error-handling features.



\### File Handling



\- Checks whether the dataset file exists.

\- Handles \*\*File Not Found\*\* errors.



\### Missing Values



\- Checks the dataset for missing values.

\- Handles missing values before analysis.



\### Date Validation



\- Converts the Date column into a proper date format.

\- Helps prevent errors during monthly analysis.



\### Sales Validation



\- Checks whether the \*\*Total Sales\*\* value is accurate.

\- The expected sales value is calculated using:



\*\*Total Sales = Quantity × Price\*\*



\- If the existing Total Sales value is incorrect, it can be recalculated.



\---



\# 📁 Project Structure



The project is organized as follows:



```text

Week-4-Data-Visualization/

│

├── main.py

├── README.md

├── requirements.txt

│

├── data/

│   └── sales\_data (1).csv

│

├── visualizations/

│   ├── expense\_by\_category.png

│   ├── monthly\_spending\_trend.png

│   └── expense\_distribution.png

│

└── report/

&#x20;   └── project\_report.md

```



\### 📂 Folder Explanation



\- \*\*main.py\*\*

&#x20; - Contains the main Python program.

&#x20; - Performs data loading, analysis, visualization, and insight generation.



\- \*\*README.md\*\*

&#x20; - Explains the project.

&#x20; - Contains objectives, technologies, results, and project structure.



\- \*\*requirements.txt\*\*

&#x20; - Contains the Python libraries required to run the project.



\- \*\*data/\*\*

&#x20; - Stores the original dataset.



\- \*\*visualizations/\*\*

&#x20; - Stores all generated charts and graphs.



\- \*\*report/\*\*

&#x20; - Contains the detailed project report.



\---



\# 🚀 How to Run the Project



Follow these steps to run the project:



\### Step 1 — Install Python



Make sure Python is installed on your computer.



\### Step 2 — Install Required Libraries



Open the terminal in the project folder and run:



```bash

pip install pandas matplotlib

```



Or, if `requirements.txt` is available:



```bash

pip install -r requirements.txt

```



\### Step 3 — Run the Program



Run:



```bash

python main.py

```



\### Step 4 — Check the Output



After running the program:



\- The analysis results will be displayed in the terminal.

\- The visualization images will be saved in the \*\*visualizations\*\* folder.

\- The report will be available in the \*\*report\*\* folder.



\---



\# 💡 Conclusion



\- This project demonstrates a complete \*\*Python data analysis workflow\*\*.

\- It covers:

&#x20; - Data loading

&#x20; - Data cleaning

&#x20; - Data validation

&#x20; - Data analysis

&#x20; - Data visualization

&#x20; - Insight generation

\- The project helps understand how Python can be used to analyze transaction and expense data.

\- The generated charts make the spending patterns easier to understand.

\- Overall, this project provides practical experience with \*\*Pandas, Matplotlib, and basic data analysis\*\*.

