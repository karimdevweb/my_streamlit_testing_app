import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import numpy as np


# how  to check the modules
# streamlit --version 
# pip show matplotlib
# pip show seaborn
# pip show plotly.express
# print(pd. __version__)
# print(np.version.version)



# write title to my app
st.title('hello, you ! how are you ?')
st.write("i'm enjoying coding with streamlit")




link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)

# des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).

container = st.container()

with container:
    df_final = 0
    countries = st.multiselect('choose the country', df_weather['continent'].unique())
    if countries:
        df_final = df_weather.loc[df_weather['continent'].isin(countries)]
        
    else:
        df_final = df_weather
        
      
    col_left, col_right = st.columns([1,5])
    
    
    columns_to_see = []
    
    with col_left:
        columns = df_final.columns.to_list()
        for col in columns:
            col = st.checkbox(col, key=col)
            
            
        col_filters = st.session_state
        for col_if_true in col_filters: 
            if st.session_state[col_if_true] == True:
                columns_to_see.append(col_if_true)
            
        
        
    with col_right:
        if columns_to_see:
            st.dataframe(df_final.loc[:,columns_to_see].style.highlight_max(axis=0))
        else:
            st.dataframe(df_final)
        

















# une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.

# barplot continent/ cylinders
st.write('<span style=color:red>hist plot montrant la distribution des cylindres en time 60 <span/>',''.join(countries),
         unsafe_allow_html =True,
         )

my_bar_graph_2 = sns.histplot(df_final,
                           x='cylinders',
                           y='time-to-60')


st.pyplot(my_bar_graph_2.figure)





# barplot:continent / weightlbs
st.write('<span style=color:red>bar plot montrant la distribution des weightlbs par pays<span/>',''.join(countries),
         unsafe_allow_html =True)
my_bar_graph = sns.barplot(df_final,
                           x='continent',
                           y='weightlbs')


st.pyplot(my_bar_graph.figure)



# corr graph
st.write('<span style=color:red>heatmap montrant la coorelation entre les colomnes du df<span/>',''.join(countries),
         unsafe_allow_html =True)
my_corr_graph = sns.heatmap(df_final.corr(),
                            vmin=-1,
                            vmax=1,
                            center=0,
                            cmap='Blues',
                            annot=True)
st.pyplot(my_corr_graph.figure)










