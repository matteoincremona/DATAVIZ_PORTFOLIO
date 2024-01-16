import pandas as pd
import plotly.express as px
import streamlit
import nbformat

# Load your data
data = pd.read_csv('FAOSTAT_data_en_1-7-2024.csv')

# Create an interactive map using Plotly with a default color scale
fig = px.choropleth(
    data, 
    locations="Area", 
    locationmode="country names",
    color="Value", 
    hover_name="Area", 
    animation_frame="Year",
    color_continuous_scale=px.colors.sequential.Plasma,  
    projection="natural earth",
    title="Average Temperature Change by Country compared to 1960 ",
    range_color=[-1, 2.5]  
)

# Update layout to add a slider for years and improve map aesthetics
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    margin={"r":0,"t":30,"l":0,"b":0},  
    title_x=0.5,  
    coloraxis_colorbar=dict(title='Change in °C')  
)

fig.show()
