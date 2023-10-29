import streamlit as st
import pickle
import pandas as pd

st.markdown("""
This is a movie recommender system that uses machine learning to recommend movies to you based on your past preferences. To use the system, simply select a movie from the dropdown menu and click the "Show Recommendations" button.
""")


def recommend(movie):
    if movie not in similarity:
        st.error('Movie has not been rated.')
        return []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(movies.iloc[i[0]].title)


    recommended_movies = []
    for i in distances:
        recommended_movies.append(movies.at[i[0], 'title'])
    st.write('Recommended movies:')
    st.write(recommended_movies)
    return recommended_movies



movies_dict = pickle.load(open("movies_d.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    "Search your movie here",
    movie_list
)

if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie_name)
    st.write(recommendations)

