import os

import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
from PIL import Image


# ________________________________________________________________________________________
path = os.path.dirname(__file__)
output_map = path + '/df_coords.csv'
sit_logo = Image.open(path + "/sit_logo_nobg.png")
path_image_html = path + "/topics.html"
twitter_logo = path +"/twitter_logo"

im = Image.open("sit_logo_mini.ico")
goal_icon = Image.open('Icon_Goal.ico')

neg_cloud_1308 = Image.open(path + '/negative_13_08.png')
joana_lkd = Image.open(path + '/joana_lkd.png')
ella_lkd = Image.open(path + '/ella_lkd.png')
naemi_lkd = Image.open(path + '/naemi_lkd.png')

path_churn_html = path + "/churn.html"
path_barchar_html = path + "/fig_barchar.html"
path_classes_html = path + "/personas.html"
path_cluster_html = path + "/fig_Cluster.html"
path_heatmap_html = path + "/fig_heatmap.html"
path_hierarchy_html = path + "/fig_hierarchy.html"
path_manutd_html = path + "/ManUtd_only_1quantile_topics.html"
path_matches_sent_html = path + "/matches_and_sentiment_good_one.html"
path_matches_tweets_html = path + "/matches_and_tweets.html"
path_neg_sent_html = path + "/negative_sentiment.html"
path_10_tweets_html = path + "/top_10_tweets_ManUTd.html"
path_daily_new_html = path + "/daily_followers_added_ManUtd.html"

# ________________________________________________________________________________________


# ________________________________________________________________________________________
st.set_page_config(page_title="Social Media Analytics", page_icon=goal_icon, 
        layout="wide")

# _________________________________________________________________________________________
@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

# ___________Display sidebar________________________________________________

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
                
        </style>
        """, unsafe_allow_html=True)



st.sidebar.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
                
    </style>
    """, unsafe_allow_html=True
)


url_joana = "https://www.linkedin.com/in/joanaduartesantos/"
url_ella = "https://www.linkedin.com/in/mihaela-cucui-642789b5/"
url_naemi = "https://www.linkedin.com/in/naemi-graf-0b434a13a/"

st.sidebar.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<p class="big-font">Date: 18.11.2022</p>', unsafe_allow_html=True)

st.sidebar.image(sit_logo)
# image = Image.open(output_logo)
# st.sidebar.image(image, width=250)
# st.sidebar.header("Capstone Project")

st.sidebar.header("")
st.sidebar.header("")
st.sidebar.subheader("Data Science Consulting Team:")

with st.sidebar:
    st.image(joana_lkd, width=150)
    st.caption(url_joana)

with st.sidebar:
    st.image(ella_lkd, width=175)
    st.sidebar.caption(url_ella)

with st.sidebar:
    st.image(naemi_lkd, width=250)
    st.sidebar.caption(url_naemi)


# _________TOP_____________________________________________________________

col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    st.write("")
    
with col3:
    st.image(sit_logo, width=300)


st.title("Data Science Bootcamp - Capstone Project")
st.header("Group: SiT Autonomous")
st.subheader("Sport Team Fan Base Social Media Analytics")

st.info('Description')
st.write("Professional sports organizations these days aren't only about top game performance, but also about their marketing success. There are examples of underdogs who are healthy from a business perspective because of their active fan base (e.g. West Ham United)."
" We would like to better understand how teams could utilize their social media presence to become more successful in growing and engaging their supporters.")

st.header("")
st.info("Goals")
st.write("""
\n Assess social media presence of a football club;
\n Segment followers by their interests and social activity;
\n Grow & Engage their fans.
""")

# _________Titles___________________________________________________________

# _______Selection box________________________________________________________
st.header("")
st.header("Social Media Analytics")
play_vars = ["Please select one of the options below: ", "Tweet Content and Analysis", "Churn Analysis", "Matches and Sentiment Analysis", "Fanbase Segmentation", "Manchester United"]
var_select = st.selectbox("Please select: ", play_vars)

# _________________________Topics__________________________________________________________________________________________

if var_select == "Tweet Content and Analysis":
    st.title("")
    st.title("")
    st.subheader("Tweet Content - Key Topics Identified Based on Topic Modelling")
    st.title("")
    st.subheader("Tweets collected based on they key hashtags")

    st.title("")
    with open(path_image_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 500, scrolling = True)

# ____________________________MUFC_Topics_______________________________________________________________________________________

    st.title("")
    st.title("")
    with open(path_manutd_html,'r') as f: 
        html_data = f.read()

    st.subheader("Manchester United - official Twitter account")
    st.components.v1.html(html_data, height = 500, scrolling = True)

# _________________________Topics__________________________________________________________________________________________

    st.title("")
    st.title("")
    with open(path_barchar_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, height = 750, scrolling = True)



# _____________________________Hierarchy______________________________________________________________________________________

    st.title("")
    st.title("")
    st.subheader("Hierarchical clustering of the topics obtained")
    with open(path_hierarchy_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, height = 1100, width = 1000)

# _____________________________Top_10______________________________________________________________________________________
if var_select == "Manchester United":
    st.title("")
    st.subheader("Top Tweets")
    with open(path_10_tweets_html,'r') as f: 
        html_data = f.read()
    st.components.v1.html(html_data, height = 500, width = 1000)

# ____________________________MUFC_Topics_______________________________________________________________________________________

    with open(path_manutd_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.subheader("Manchester United - official Twitter account")
    st.components.v1.html(html_data, height = 500, scrolling = True)

# _____________________________Daily_Followers______________________________________________________________________________________

    st.subheader("Followers Acquisition Over Time")
    with open(path_daily_new_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 700, width = 900)


# _________________________Churn__________________________________________________________________________________________

if var_select == "Churn Analysis":
    st.title("")
    st.title("")
    st.subheader("Churn analysis based on interaction with the key hashtags over time")

    with open(path_churn_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 500, scrolling = True)


# ___________________________Matches_+_Sentiment________________________________________________________________________________________

if var_select == "Matches and Sentiment Analysis":
    st.title("")
    st.title("")
    st.subheader("Tweets - sentiment analysis")
    st.write(f"Daily tweet count with sentiment analysis: 1.1M english tweets. Overall 46% of tweets are positive , 18% negative and 40% neutral.")
    st.write("Matches played during the six months period: in orange matches won, in grey matches lost. ") 
    st.write("Size of the bar for each match represents the number of tweets generated during the match (with a 1h window period before and after the match)")
    with open(path_matches_sent_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 600, scrolling = True)
    
# ___________________________________________________________________________________________________________________

    st.header("")
    st.header("")
    st.subheader("Negative word cloud")
    st.write("Wordcloud generated based on the tweets posted on 13.08.2022, where a spike of activity can be perceived in the charts.")
    st.header("")
    st.image(neg_cloud_1308, width = 700)

# ___________________________________________________________________________________________________________________
    st.title("")
    st.title("")
    st.subheader("Sentiment Analysis - Top topics that reflect *negative* sentiment")
    st.title("")
    with open(path_neg_sent_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 500)

# ___________________________________________________________________________________________________________________

# _________________________MAP__________________________________________________________________________________________

if var_select == "Fanbase Segmentation":
    # st.subheader("Users' distribution based on hashtag interaction (3 core hashtags - #MUFC, #manunited, #manchesterunited)")
    st.title("")
    st.title("")
    st.subheader("Fanbase geographical distribution")
    st.write("Location available in 90034 users' profiles (out of 138k unique users).")

    df_map = pd.read_csv("df_coords.csv")
    df_map = df_map.dropna()
    st.map(df_map, zoom = 1)

    # _________________________Classes__________________________________________________________________________________________

    st.title("")
    st.title("")
    st.subheader("Fanbase segmentation based on Twitter profile description")
    # st.subheader("Classes")
   
    st.write("From the 50 clusters generated by Bertopic, 20 classes were manually created by combining some of the clusters.")

    st.title("")
    with open(path_classes_html,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 700, scrolling = True)

