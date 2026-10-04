import streamlit as st

st.set_page_config(
    page_title="Sales Data Calculator",
    page_icon="📊"
)

st.title("📊 Sales Data Calculator")

st.write(
    "Analyze a collection of sales values and calculate "
    "important sales statistics."
)

sales = [1200, 1500, 1800, 1100, 2200,
         2500, 1700, 2000, 1600, 1900]

st.subheader("Sales Data")

st.write(sales)

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

st.subheader("Sales Analysis")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"₹{total_sales:,.2f}")
    st.metric("Highest Sale", f"₹{highest_sale:,.2f}")

with col2:
    st.metric("Average Sale", f"₹{average_sales:,.2f}")
    st.metric("Lowest Sale", f"₹{lowest_sale:,.2f}")

st.subheader("Conclusion")

st.write(
    f"The total sales are ₹{total_sales:,.2f}. "
    f"The average sale is ₹{average_sales:,.2f}. "
    f"The highest sale is ₹{highest_sale:,.2f}, "
    f"while the lowest sale is ₹{lowest_sale:,.2f}."
)