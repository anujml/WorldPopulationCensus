import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# line chart
def plot_line(SelectedData,continent):    
    # Select relevant population data columns and sum across years
    SelectedDataPopulation = SelectedData.select_dtypes(include=['int64', 'float64']).drop(
        ['Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage', 'Rank'], axis=1)
    
    SelectedDataPopulation = pd.DataFrame(SelectedDataPopulation.sum().iloc[::-1])
    SelectedDataPopulation.columns = ['Population']
    SelectedDataPopulation.index.name = 'Year'
    SelectedDataPopulation.reset_index(inplace=True)
    
    # Create a line chart using Plotly
    fig = px.line(
        SelectedDataPopulation,
        x = [i[:4] for i in SelectedDataPopulation['Year'].values],
        y ='Population',
        title = '--'
    )
    
    fig.update_layout(
        height = 300,  # Increase height to occupy more space vertically
        title_x= 0.5,  # Center the title

    )
    
    fig.update_xaxes(title_text = 'year')

    return fig

# Histogram
def plot_hist(SelectedData:pd.DataFrame,OverallData:pd.DataFrame,continent:str):
    # Create a Matplotlib figure and axis
    if continent.lower() != 'overall':
        fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size as needed
        sns.histplot(SelectedData['2022 Population'], kde=True, ax=ax)  # seaborn's histplot (alternative to distplot)
        
        # Set titles and labels if needed
        # ax.set_title(f'{continent} Population Distribution')
        ax.set_xlabel('Population')
        ax.set_ylabel('Frequency')
        return fig
    else:
        fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size as needed
        sns.histplot(OverallData['2022 Population'], kde=True, ax=ax)  # seaborn's histplot (alternative to distplot)
        
        # Set titles and labels if needed
        # ax.set_title(f'{continent} Population Distribution')
        ax.set_xlabel('Population')
        ax.set_ylabel('Frequency')
        return fig
    
# MapChart
def PlotMap(SelectedData:pd.DataFrame,OverallData:pd.DataFrame,continent:str,column:str,r1:int = 0,r2:int = 1500000000):
    # Create a Matplotlib figure and axis
    if continent.lower() != 'overall':
        fig = px.choropleth(
                    SelectedData,
                    locations="CCA3",  # ISO 3166-1 alpha-3 codes
                    color=column,  # Data to be color-coded
                    hover_name="Country/Territory",  # Column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    range_color=(r1,r2),
                    projection="natural earth"
                   )
        return fig
    else:
        fig = px.choropleth(
                    OverallData,
                    locations="CCA3",  # ISO 3166-1 alpha-3 codes
                    color=column,  # Data to be color-coded
                    hover_name="Country/Territory",  # Column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    range_color=(r1,r2),
                    projection="natural earth"
                   )
        return fig
