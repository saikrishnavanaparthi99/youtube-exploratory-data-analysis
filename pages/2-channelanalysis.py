import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_player import st_player
import plotly.graph_objects as go
import plotly.figure_factory as ff
from st_aggrid import AgGrid

st.markdown(" # 📊 Youtube data analysis on Mrwhosetheboss youtube channel")
st.sidebar.markdown("# 📊 Youtube data analysis on Mrwhosetheboss youtube channel")

# Display Sample Dataframe
st.subheader('1. Displaying video data of Mrwhosetheboss youtube channel')
st.markdown("---")
data = pd.read_csv("data/Video_Details_new(Mrwhosetheboss).csv") #path folder of the data file
st.dataframe(data) #displays the table of data

st.subheader('2. Details of the channels first video')
st.markdown("---")
first_video = data.sort_values('Published_date',ascending=True).head(1)
st.dataframe(first_video)

st.subheader('3. Performance in all these years')
st.markdown("---")
data1 = data.groupby('Published_year').mean(numeric_only=True)
fig = px.bar(
    data1,
    x = np.array([2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]),
    y = "Views",
    orientation="v",
    color_discrete_sequence=["#0083B8"] *len(data),
    template="plotly_white",
    width=900, height=600,
  
)

fig.update_layout(
    xaxis_title="Years",
    yaxis_title="",
    legend_title="Performance in all these years",
    font=dict(
        family="Courier New, monospace",
        size=12,
    )
)
st.plotly_chart(fig)

st.subheader('4. Comaparison of Performance for this year to the last two years')
st.markdown("---")

data2 = data.loc[data['Published_year']==2020].groupby('Published_month').mean()
data3 = data.loc[data['Published_year']==2021].groupby('Published_month').mean()
data4 = data.loc[data['Published_year']==2022].groupby('Published_month').mean()

fig = go.Figure()
fig.add_trace(go.Scatter(x=np.array([1,2,3,4,5,6,7,8,9,10,11,12]), y=data2["Views"], name="2020", mode="lines"))
fig.add_trace(go.Scatter(x=np.array([1,2,3,4,5,6,7,8,9,10,11,12]), y=data3["Views"], name="2021", mode="lines"))
fig.add_trace(go.Scatter(x=np.array([1,2,3,4,5,6,7,8,9,10,11,12]), y=data4["Views"], name="2022", mode="lines"))

fig.update_layout(
    title="Performance in all these years", xaxis_title="Year", yaxis_title="Views",width = 1000,height = 600
)
st.plotly_chart(fig)

st.subheader('5. Channels growth with each video')
st.markdown("---")
data_datesort = data.sort_values('Published_date',ascending=True)
xval = np.array(range(1,1489))
fig = go.Figure()
fig.add_trace(go.Scatter(x=xval, y=data_datesort["Views"], name="plot", mode="lines"))
fig.update_layout(
    title="Channels growth with each video", xaxis_title="Videos Number", yaxis_title="Views",width = 1000,height = 600
)
st.plotly_chart(fig)

st.subheader('6. Analysis of channels first viral video')
st.markdown("---")
st.dataframe(data_datesort[461:462])
st.write("The video with the title ","Turn your Smartphone into a 3D Hologram | 4K","is the first viral video which outperformed all the channels previous videos till that time by garnering views of over 24.863 million")

st.subheader('6. Videos Performance - Top 10 videos')
st.markdown("---")
top10_videos = data.sort_values(by='Views',ascending=False).head(10)
st.dataframe(top10_videos)
st.write("Top 10 videos vs views")


fig = px.bar(
    top10_videos,
    x = "Views",
    y = "Title",
    orientation="h",
    color_discrete_sequence=["#0083B8"] *len(top10_videos),
    template="plotly_white",
    width=1000, height=600,
  
)

fig.update_layout(
    xaxis_title="Views",
    yaxis_title="",
    legend_title="Top 10 videos vs views",
    font=dict(
        family="Courier New, monospace",
        size=12,
    )
)
st.plotly_chart(fig)

st.subheader('7. Number of videos uploaded per month')
st.markdown("---")
videos_per_month = data.groupby('Month',as_index=False).size()
sort_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
              'Sep','Oct','Nov','Dec']
videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'],categories=sort_order,ordered=True)
videos_per_month = videos_per_month.sort_index()
st.dataframe(videos_per_month)


fig = px.bar(
    videos_per_month,
    x = "Month",
    y = "size",
    orientation="v",
    color_discrete_sequence=["#b83500"] *len(videos_per_month),
    template="plotly_white",
    width=1000, height=600,
  
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="",
    legend_title="Number of videos uploaded per month",
    font=dict(
        family="Courier New, monospace",
        size=12,
    )
)
st.plotly_chart(fig)

st.subheader('8. Top 10 worst(viewcount wise) videos that didnt perform relatively well')
st.markdown("---")
top10_least_views = data.sort_values(by='Views',ascending=False).head(10)
st.dataframe(top10_least_views)

fig = px.bar(
    top10_least_views,
    x = "Views",
    y = "Title",
    orientation="h",
    color_discrete_sequence=["#83b800"] *len(top10_least_views),
    template="plotly_white",
    width=1000, height=600,
  
)

fig.update_layout(
    xaxis_title="Views",
    yaxis_title="",
    legend_title="Number of videos uploaded per month",
    font=dict(
        family="Courier New, monospace",
        size=12,
    )
)
st.plotly_chart(fig)


st.subheader('9. comparison between top 10 best performed and worst performed videos duration')
st.markdown("---")
st.write("Data related to top 10 videos")
data.sort_values('Views',ascending=True)[0:10].mean(axis=0,numeric_only=True)
top10 = pd.DataFrame(data.sort_values('Views',ascending=True)[0:10].mean(axis=0,numeric_only=True))
st.dataframe(top10)
st.write("Data related to top 10 worst performed videos")
data.sort_values('Views',ascending=False)[0:10].mean(axis=0,numeric_only=True)
top10_worst = pd.DataFrame(data.sort_values('Views',ascending=False)[0:10].mean(axis=0,numeric_only=True))
st.dataframe(top10_worst)
st.write("1.The average duration of the videos which did not perform well is 2.581 minutes and the average duration of the videos which performed well is 1.575 minutes.")

st.subheader('10. 100 most viewed videos with month of publication')
st.markdown("---")

def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "Published_month", data = data.sort_values(by='Views').head(100), palette="Set1")
    st.pyplot(fig)

countPlot()
st.write("As the channel we are analyzing is basically a tech channel which deals with unboxing and reviewing of various tech products. It can be observed that there are more videos published in june followed by july and august which can be a sign that in these months more smartphones or tech products are released in the market which made more review videos to be posted. So the best month to publish a video for this channel is: June")


st.subheader('11. 100 most viewed videos with day of publication')
st.markdown("---")


def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "Published_day", data = data.sort_values(by='Views').head(100), palette="Set1")
    st.pyplot(fig)

countPlot()
st.write("Most of the 100 most viewed videos are published on Thursday followed by Sunday So the best day to publish a video is: Thursday")


st.subheader('12. 100 most viewed videos with hour of publication')
st.markdown("---")

def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "hour", data = data.sort_values(by='Views').head(100), palette="Set1")
    st.pyplot(fig)

countPlot()
st.write("The best time to post a video can be at : 2:00PM")

st.subheader('13. Corelations')
st.markdown("---")
corr = data[['Views','Likes','Comments','durationSecs','tagCount']].corr()
st.dataframe(corr)

fig, ax = plt.subplots()
sns.heatmap(corr, ax=ax,annot = True,cmap='viridis')
st.write(fig)

st.subheader('14. Views,likes,comment and tags relation')
st.subheader('Number of likes vs. views')
fig = px.scatter(data,x = 'Likes',y= 'Views', trendline='ols',trendline_color_override='red',width=1000,height=600)
st.write(fig)
st.markdown("---")
st.subheader('Number of Tags vs. views')
fig = px.scatter(data,x = 'tagCount',y= 'Views', trendline='ols',trendline_color_override='red',width=1000,height=600)
st.write(fig)
st.markdown("---")

st.subheader('Length of the video and number of views')
fig = px.scatter(data,x = 'durationMin',y= 'Views', trendline='ols',trendline_color_override='red',width=1000,height=600)
st.write(fig)
st.markdown("---")

st.subheader('Length of the title and number of views')
fig = px.scatter(data,x = 'titlelength',y= 'Views', trendline='ols',trendline_color_override='red',width=1000,height=600)
#st.write(fig)
st.plotly_chart(fig)
st.markdown("---")

