import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import time
import numpy as np




# write title to my app
st.title('hello, you ! how are you ?')
st.write("i'm enjoying coding with streamlit")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)
st.dataframe(df_weather.style.highlight_max(axis=0))






# une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.

# barplot continent/ cylinders
st.write('<span style=color:red, font-weight:bold>hist plot montrant la distribution des cylindres en time 60<span/>',
         unsafe_allow_html =True)

my_bar_graph_2 = sns.histplot(df_weather,
                           x='cylinders',
                           y='time-to-60')


st.pyplot(my_bar_graph_2.figure)




# barplot:continent / weightlbs
st.write('<span style=color:red>bar plot montrant la distribution des weightlbs par pays<span/>',
         unsafe_allow_html =True)
my_bar_graph = sns.barplot(df_weather,
                           x='continent',
                           y='weightlbs')


st.pyplot(my_bar_graph.figure)



# corr graph
st.write('<span style=color:red>heatmap montrant la coorelation entre les colomnes d udf<span/>',
         unsafe_allow_html =True)
my_corr_graph = sns.heatmap(df_weather.corr(),
                            vmin=-1,
                            vmax=1,
                            center=0,
                            cmap='Blues',
                            annot=True)
st.pyplot(my_corr_graph.figure)




# des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).






