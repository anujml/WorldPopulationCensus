import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import charts as ch
import seaborn as sns

# Set page layout to wide
st.set_page_config(layout="wide")

# Custom CSS to remove margins
st.markdown("""
    <style>
    .css-18e3th9 {padding-top: 0rem;}
    .css-1d391kg {padding-top: 1rem;}
    .css-1offfwp {padding-left: 0rem; padding-right: 0rem;}
    .block-container {padding-top: 1rem;}
    .reportview-container {
        background-color: #2E2E2E;  /* Darker background color */
        color: white;
    }
    h1 {
        text-align: center;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Assuming NewWorldPopulationData is your DataFrame/
NewWorldPopulationData = pd.read_csv('NewWorldPopulationData.csv').drop('Unnamed: 0', axis = 1)

# Sidebar dropdown for continent selection
ContinentDropDown = NewWorldPopulationData['Continent'].unique()

with st.sidebar.expander("Select a Continent", expanded=True):
    selected_continent = st.selectbox('Continent', ContinentDropDown)
    
# Filter data for the selected continent
st.markdown(f'<h1 style="text-align: center; padding-bottom : 70px">World Population Census - {selected_continent}</h1>', unsafe_allow_html=True)

SelectedData = NewWorldPopulationData[NewWorldPopulationData['Continent'] == selected_continent]

# Plot the line chart for the selected continent
if selected_continent:
    col1, col2 = st.columns([6, 4])  # 70% width for col1 and 30% width for col2
    with col1:
        st.markdown(
            f"""
            <h6 style="color: black; text-align: center;">
                {selected_continent} Population Trend
            </h6>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(ch.plot_line(SelectedData,selected_continent), use_container_width=True)
    with col2:
        st.markdown(
            f"""
            <h6 style="color: black; text-align: center;">
                {selected_continent} Population Distribution
            </h6>
            """,
            unsafe_allow_html=True
        )
        st.pyplot(
                ch.plot_hist(SelectedData,
                               NewWorldPopulationData[NewWorldPopulationData['Continent'].str.lower() != 'overall'] ,
                               selected_continent), 
                use_container_width=True
                )
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(
            f"""
            <h6 style="color: black; text-align: center;">
                {selected_continent} Population Map 2022
            </h6>
            """,
            unsafe_allow_html=True
        )
        st.plotly_chart(
                ch.PlotMap(SelectedData,
                            NewWorldPopulationData[NewWorldPopulationData['Continent'].str.lower() != 'overall'] ,
                            selected_continent,
                            column = '2022 Population'), 
                use_container_width=True
                )
        
    with col4:
        st.markdown(
            f"""
            <h6 style="color: black; text-align: center;">
                {selected_continent} Density Map 2022
            </h6>
            """,
            unsafe_allow_html=True
        )
        if selected_continent.lower() != 'overall':
            st.plotly_chart(
                    ch.PlotMap(SelectedData,
                                None,
                                selected_continent,
                                column = 'Density (per km²)',
                                r1 = np.percentile(SelectedData['Density (per km²)'],10),
                                r2 = np.percentile(SelectedData['Density (per km²)'],90)
                    ), 
                                
                    use_container_width=True
                    )
        else:
            overall_data = NewWorldPopulationData[NewWorldPopulationData['Continent'].str.lower() != 'overall']
            st.plotly_chart(
                    ch.PlotMap(SelectedData,
                                overall_data,
                                selected_continent,
                                column = 'Density (per km²)',
                                r1 = np.percentile(overall_data['Density (per km²)'],20),
                                r2 = np.percentile(overall_data['Density (per km²)'],90)
                    ), 
                                
                    use_container_width=True
                    )

    

