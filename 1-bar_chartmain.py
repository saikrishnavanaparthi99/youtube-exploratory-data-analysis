import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_player import st_player
import plotly.graph_objects as go
import plotly.figure_factory as ff
#st.set_page_config(
 #   
  #  layout="wide"
   # )

st.markdown(" # 📊 Youtube data analysis on 5 favourite tech youtube channels ")
st.sidebar.markdown("# 📊 Youtube data analysis on 5 favourite tech youtube channels")



# Display Sample Dataframe
st.subheader('1. Displaying channel data related to five channels')
st.markdown("---")
data = pd.read_csv("data/five_channel_data.csv") #path folder of the data file
st.dataframe(data) #displays the table of data

st.subheader('2. Number of Subscribers of each of these channels')
st.markdown("---")

def barPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x = "channel_name", y = "Subscribers", data = data)
    st.pyplot(fig)

barPlot()

st.subheader('3. Total number of views on all these channels')
st.markdown("---")

def barPlot1():
    fig = plt.figure(figsize=(10,4))
    sns.barplot(x = "channel_name",y = "Views",data=data)
    st.pyplot(fig)
    

barPlot1()

st.subheader('4. Total number of videos on all these channels')
st.markdown("---")

def barPlot2():
    fig = plt.figure(figsize=(10,4))
    sns.barplot(x = "channel_name",y = "Total_videos",data=data)
    st.pyplot(fig)

barPlot2()

st.subheader('5. First channel to start publishing videos on youtube ')
st.markdown("---")
first_start = data.sort_values('Published_date',ascending=True).head(1)
st.dataframe(first_start)

st.subheader('6. Last channel to start publishing videos on youtube ')
st.markdown("---")
last_start = data.sort_values('Published_date',ascending=False).head(1)
st.dataframe(last_start)

