import streamlit as st
import pandas as pd
import plotly_express as px

# Load the dataset
df = pd.read_csv("vehicles_us.csv")

# Define the header text
header = st.header("Car Advertisement Dashboard")

# Create a checkbox to filter by condition
show_filtered_data = st.checkbox("Filter by Condition")

# Create a plotly histogram of price
price_hist = px.histogram(df, x="price", nbins=20)

# Create a plotly scatter plot of price vs. odometer
price_vs_odometer = px.scatter(df, x="price", y="odometer", color="condition")

# Display the plotly charts depending on the checkbox state
if show_filtered_data:
    filtered_df = df[df["condition"].isin(["excellent", "good"])]
    st.plotly_chart(px.histogram(filtered_df, x="price", nbins=20))
    st.plotly_chart(px.scatter(filtered_df, x="price", y="odometer", color="condition"))
else:
    st.plotly_chart(price_hist)
    st.plotly_chart(price_vs_odometer)
