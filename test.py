import pandas as pd
import streamlit as st
import pickle
# Vectorization: Creating each movie as a Vector
from sklearn.feature_extraction.text import CountVectorizer
# Calculating Cosine Angle between vectors
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(" rekomender ")

global movies
# movies = 

cv = CountVectorizer(max_features=5000, stop_words="english")

df = pd.read_csv("/home/paul/Mindscope/stream/models/final_data.csv")

model_vector = pd.read_pickle(r"/home/paul/Mindscope/stream/models/similar.pkl"
)
movies = pd.read_pickle(r"/home/paul/Mindscope/stream/models/movies.pkl")
df = df.drop(["Unnamed: 0"], axis=1)


model_vector = cv.fit_transform(df["tags"]).toarray()

similar = cosine_similarity(model_vector)

def reco():
    st.title("M.I Movie Recommender")

# Creating our Recommend function it will return Top 5 movies back
def recommender(movie):
    movie_index = df[df["title"]==movies].index[0]
    distances = model_vector[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    movie_titles = []
    for i in movie_list:
        movie_ttl = df.iloc[i[0]].title 
        print(movie_ttl)
        movie_titles.append(movie_ttl)
        
    return movie_titles


def get_movie_title():
    movie_name = st.text_input("Type movie name here")  
    st.caption("__Try The Butterfly Effect__")

    return movie_name

def show_movies():
    st.subheader(":blue[**RECOMMENDATIONS**]")
    col1, col2 = st.columns(2)
    
    
reco()
show = False
c1, c2 = st.columns([.7, .3])
with c1:
    movie = get_movie_title()
    movie = recommender(movie)
with c2:
    st.caption("")
    st.caption("")
    if movie:
        show = True
    
    if st.button("Search"):
        if movie:
            show = True
            

if show == True:
    show_movies()

