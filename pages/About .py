import streamlit as st

st.title("E-COMMERCE DATA ANALYSIS")

st.markdown('''
## Introduction

The "E-COMMERCE DATA ANALYSIS" app is a web-based data analysis tool designed to explore and visualize an e-commerce dataset. 
It provides valuable insights into the sales performance, customer behavior, and product trends of an e-commerce business. 
The app is built using Python and Streamlit, a popular framework for creating interactive web applications.
''')

st.markdown('''
1. 📊 **Bar Chart - Missing Values by Features**

'This chart visualizes the count of missing values for each feature (column) in the dataset. 
The feature with the highest count of missing values is indicated by the tallest bar in the chart, 
while the feature with the lowest or no missing values is indicated by the shortest or absent bar in the chart.'
''', unsafe_allow_html=True)

st.markdown('''
2. 📊 **Bar Chart - Total Sales Revenue**

'This chart displays the total sales revenue over time. 
The peak of the line in the chart represents the highest recorded total sales revenue during the observed period, 
while the lowest point (near zero) on the line represents the minimum or no sales revenue during the observed period.'
''', unsafe_allow_html=True)

st.markdown('''
3. 📊 **Bar Chart - Top 10 Countries by Revenue**

'This chart shows the top 10 countries with the highest total revenue from sales. 
The bar with the highest length represents the country with the highest total revenue among the top 10 countries, 
while the bar with the lowest length or absence of a bar indicates the country with the lowest or no revenue among the top 10 countries.'
''', unsafe_allow_html=True)

st.markdown('''
4. 📊 **Bar Chart - Top 20 Products by Revenue**

'This chart presents the top 20 products by their total revenue generated from sales. 
The bar with the greatest length represents the product with the highest total revenue among the top 20 products, 
while the bar with the smallest length or no bar represents the product with the lowest or no revenue among the top 20 products.'
''', unsafe_allow_html=True)

st.markdown('''
5. 📊 **Bar Chart - Sales Quantity for Top 20 Products**

'This chart displays the sales quantity for the top 20 products based on their revenue. 
The bar with the highest length represents the product with the highest sales quantity among the top 20 products, 
while the bar with the lowest length or no bar represents the product with the lowest or no sales quantity among the top 20 products.'
''', unsafe_allow_html=True)

st.markdown('''
6. 📊 **Bar Chart - Average Unit Price of Top 20 Products Sold**

'This chart illustrates the average unit price for the top 20 products based on their revenue. 
The bar with the greatest length represents the product with the highest average unit price among the top 20 products, 
while the bar with the smallest length or no bar represents the product with the lowest or no average unit price among the top 20 products.'
''', unsafe_allow_html=True)

st.markdown('''
7. 📊 **Bar Chart - Top 10 Customers by Revenue**

'This chart shows the top 10 customers with the highest total revenue from their purchases. 
The bar with the highest length represents the customer with the highest total revenue among the top 10 customers, 
while the bar with the smallest length or no bar represents the customer with the lowest or no revenue among the top 10 customers.'
''', unsafe_allow_html=True)

st.markdown('''
8. 📊 **Bar Chart - Sales Performance by Day**

'This chart displays the total revenue generated on each day of the week. 
The bar with the greatest length represents the day with the highest total revenue, 
while the bar with the smallest length or no bar represents the day with the lowest or no revenue.'
''', unsafe_allow_html=True)

st.markdown('''
9. 📈 **Line Chart - Sales Performance by Hour**

'This chart shows the total revenue generated for each hour of the day. 
The peak of the line represents the hour with the highest total revenue, 
while the lowest point (near zero) on the line represents the hour with the lowest or no revenue.'
''', unsafe_allow_html=True)

st.markdown('''
10. 📈 **Line Chart - Total Sales Revenue Lost (Canceled Orders)**

'This chart displays the total sales revenue lost due to canceled orders over time. 
The peak of the line represents the highest recorded total revenue lost due to canceled orders during the observed period, 
while the lowest point (near zero) on the line represents the minimum or no revenue lost due to canceled orders during the observed period.'
''', unsafe_allow_html=True)
