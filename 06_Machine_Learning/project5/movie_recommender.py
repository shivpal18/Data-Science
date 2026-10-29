import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
import requests



def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": st.secrets["TMDB_API_KEY"],
        "language": "en-US"
    }

    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=20)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return (
                    "https://image.tmdb.org/t/p/w500"
                    + poster_path
                )
            return None
        except requests.exceptions.RequestException:
            if attempt == 2:
                return None


BASE_DIR = Path(__file__).resolve().parent

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances  = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters

movies_dict = pickle.load(open(BASE_DIR / 'movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(BASE_DIR / 'similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.header(name)

            if poster:
                st.image(poster)
            else:
                st.caption("Poster unavailable")