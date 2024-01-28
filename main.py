from fastapi import FastAPI, Form
from typing import Annotated
import pandas as pd
import streamlit as st

# Vectorization: Creating each movie as a Vector
from sklearn.feature_extraction.text import CountVectorizer
# Calculating Cosine Angle between vectors
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()
cv = CountVectorizer(max_features=5000, stop_words="english")


df = pd.read_csv("/home/paul/Mindscope/stream/models/final_data.csv")

model_vector = pd.read_pickle(r"/home/paul/Mindscope/stream/models/similar.pkl"
)
movies = pd.read_pickle(r"/home/paul/Mindscope/stream/models/movies.pkl")
df = df.drop(["Unnamed: 0"], axis=1)


model_vector = cv.fit_transform(df["tags"]).toarray()

similar = cosine_similarity(model_vector)


# Creating our Recommend function it will return Top 5 movies back
def recommender(movie):
    movie_index = df[df["title"]==movies].index[0]
    distances = model_vector[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    movie_titles = []
    for i in movie_list:
        movie_ttl = df.iloc[i[0]].title 
        st.info(movie_ttl)
        movie_titles.append(movie_ttl)
        
    return movie_titles


@app.get("/")
async def root():
    return {"rs_api" : "recommendation system api"}

@app.post("/recommender")
async def recommendations(
    movie = Annotated[str, Form()]
    ):
    recom = recommender(movie)
    return {"recom": recom}

