import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a title
st.title("Welcome to My Streamlit App")

# Add some text
st.write("This is a simple demonstration of Streamlit's capabilities.")

# Create a sidebar
st.sidebar.header("Sidebar")
user_input = st.sidebar.text_input("Enter your name", "Guest")
st.sidebar.write(f"Hello, {user_input}!")

# Create a dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

# Display the dataframe
st.subheader("Sample DataFrame")
st.dataframe(df)

# Create a line chart
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# Add a button
if st.button("Click me!"):
    st.balloons()
