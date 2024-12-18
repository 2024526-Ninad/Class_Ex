import streamlit as st
import plotly.express as px

# Streamlit Dashboard
st.title("Dairy Export Analysis Dashboard")

# Select product and country
selected_product = st.selectbox("Select Product", filtered_data['Item'].unique())
selected_country = st.selectbox("Select Country", ['Ireland', 'France', 'Germany'])

# Filter data
filtered_dashboard_data = filtered_data[
    (filtered_data['Item'] == selected_product) &
    (filtered_data['Area'] == selected_country)
]

# Visualize data
fig = px.line(filtered_dashboard_data, x='Year', y='Value', title=f"{selected_product} Export Trends in {selected_country}")
st.plotly_chart(fig)
