import streamlit as st
st.set_page_config(" rekomender ")

global movies
movies = ["The Butterfly Effect", "The Light Effect", "The Men", "CyberGirl" ]
def reco():
    st.title("M.I Movie Recommender")


def get_movie_title():
    movie_name = st.text_input("Type movie name here")  
    st.caption("__Try The Butterfly Effect__")

    return movie_name

def show_movies():
    st.subheader(":blue[**RECOMMENDATIONS**]")
    col1, col2 = st.columns(2)
    with col1:
        st.caption("**The Butterfly Effect**")
        st.image("movie1.jpg", width=300)
        st.caption("The Men")
        st.image("movie2.jpg", width=300)

    with col2:
        st.caption("The Light Effect")
        st.image("movie3.jpg", width=300)
        st.caption("CyberGirl")
        st.image("movie4.jpg", width=300)

reco()
show = False
c1, c2 = st.columns([.7, .3])
with c1:
    movie = get_movie_title()
with c2:
    st.caption("")
    st.caption("")
    if movie:
            #st.info("Looking for recommendations for {}".format(movie.capitalize()))
            for movi in movies:
                if movi.lower() == movie.lower():
                    show = True
            
    if st.button("Search"):
        if movie:
            #st.info("Looking for recommendations for {}".format(movie.capitalize()))
            for movi in movies:
                if movi.lower() == movie.lower():
                    show = True
            
        
 
                   

if show == True:
    show_movies() 

