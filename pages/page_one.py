import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import time
import numpy as np






st.title("i'm the first page in the forlder pages, and you ?")


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# read the csv by pd
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



# data is loading
data_load_state = st.text('Loading data...')

#load
my_uber_df = load_data(10000)

if st.checkbox('show raw data'):
    st.subheader('raw data')
    my_uber_df  


data_load_state.text("Done! (using st.cache)")


# draw a hist
st.subheader('Number of pickups by hour')

his_values = np.histogram(
                    my_uber_df[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
                )[0]

st.bar_chart(his_values)

# Plot data on a map
# st.subheader('Map of all pickups')

# st.map(my_uber_df)



# Filter results with a slider
hour_to_filter = st.slider('hour',0,23,17)

filtered_data = my_uber_df[my_uber_df[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


