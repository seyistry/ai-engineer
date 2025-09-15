# import neccesary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("imported successes ")

sales = pd.read_excel('sales Data.xlsx')

print(sales.head())

print("========================")

sales['Revenue'] = sales['Amount'] * sales['Boxes']

print(sales.head())
print("========================")

sales['Date'] = pd.to_datetime(sales['Date'])

print(sales.head())

print("========================")

# lets just plot  this, its not important though.


sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month_name()
sales["Week"] = sales["Date"].dt.day_name()

# print("=================")
# print(sales.head())

"""
#2.0 Steps to Analysis
**Note:** This is after you have followed the ETL(Extract Transform Load) frame work, this is you importing your dataset, cleaning and preparing it for analysis

### A. Work on the KPI's (Key performance index of this data)
1. Total units sold
2. Total Revenue
3. Average Revenue per unit
4. Numbers of products
5. Numbers of Sales Agents

### B. Work on the insights by creating models(Note that creating models in data analysis is different from building models in machine learning)
1. Total monthly revenue by Year
2. Total revenue by branch
3. Total revenue by products
4. Total revenue by sales agent
5. Total revenue by week
6. Total revenue by month
7. Trends of sales

### C. Build your dash board
1. Add the title of your analysis.
2. Add the business/company
3. Add your KPI's
4. Add Charts with appropriate labelling
5. Add your slicer if you are working with streamlit or excel or PowerBi or Tableau to make your dashboard interactive(if not, exclude it)

### C. Report your insights
1. Start with the an executive summary briefly explaining what you and briefly introducing the KPI's.
2. Explain your insights in a narative and relatable way using your visuals.

### D. Make recommendation
1. What should the business owner to increase monthly sales
2. Which of the brannches should be given more attention
3. Which products should be removed from the stock, which products should be purchased more
4. Which of the sales agents should be given more incentives/promoted to sales managers position
"""

Total_goods_sold = sales["Boxes"].sum()
print(f"Total goods sold: {Total_goods_sold} Boxes")

Total_revenue = sales["Revenue"].sum()
print(f"Total revenue: {Total_revenue} N")

# Average Revenue per unit
Average_revenue_per_unit = round(
    Total_revenue / Total_goods_sold if Total_goods_sold > 0 else 0)
print(f"Average revenue per unit: N{Average_revenue_per_unit}")

# Numbers of products
number_of_product = sales['Product'].nunique()
print(f"Total number of product is: {number_of_product}")

"""
1. Total monthly revenue by Year
2. Total revenue by branch
3. Total revenue by products
4. Total revenue by sales agent
5. Total revenue by week
6. Total revenue by month
7. Trends of sales
"""

sales.set_index("Date", inplace=True)
print(sales.head(3))

sales.Year.unique()

sales_by_year = sales.Year.unique()

sales_2021 = sales[sales["Year"] == 2021]

Total_monthly_revenue = sales_2021.groupby(
    ["Month"])["Revenue"].sum().reset_index()
print("===========================")
print(Total_monthly_revenue.head(3))


# Total_monthly_revenue.plot(kind="bar", xlabel="Month", ylabel="Revenue(N)")
plt.plot(Total_monthly_revenue['Month'], Total_monthly_revenue[["Revenue"]])
# plt.xlabel("Month")
# plt.ylabel("Revenue(N)")
# plt.title("Monthly Revenue in 2021")
plt.xticks(rotation=45)
plt.show()
