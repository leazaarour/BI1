import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import plotly as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
df = pd.read_csv("/Users/leazaarour/Desktop/BI Test.csv")
sns.lineplot(x="Extract Month",  y = 'Sales Amount (in $)',data =df).set_title("Sales per Month")
sns.barplot(y = df['Sales Amount (in $)'], x = df['Client Name'])
st.set_page_config(layout='wide')
with st.sidebar.header('1.Upload your CSV data'):
        uploaded_file= st.sidebar.file_uploader('Upload your input CSV file')
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title='2.Dive into the dataset',
        options=["Exploratory Data Analysis"],
    )
if selected=="Exploratory Data Analysis":
        warnings.simplefilter(action='ignore', category=FutureWarning)
        #loading the dataset
        df= pd.read_csv('/Users/leazaarour/Desktop/BI Test.csv')
        #Exploratory Data Analysis
        st.title("Exploratory Data Analysis")
        df.iloc[:10].plot.bar(x = 'Client Name', y = 'Sales Amount (in $)', 
                                 color = 'skyblue', 
                                 title = 'Top 10 Sold Products By Quantity')
        st.pyplot()
        df.plot.line(x = 'Extract Month', y = 'Sales Amount (in $)', 
                             color = 'salmon', title = 'Monthly Sales')
        st.pyplot()
    