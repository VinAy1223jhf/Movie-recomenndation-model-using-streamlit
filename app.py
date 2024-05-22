import streamlit as st
import pickle
import requests

st.title('Movie Recommender System')
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_names = movies_list['title'].values


def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f0474e3d6b5a4909d8c625cf387193b&language=en-US")
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']


def recommend(movie):
    movie_index = movies_list[movies_list.title == movie].index[0]
    all_distances = similarity[movie_index]
    top_movies = sorted(list(enumerate(all_distances)), reverse=True, key=lambda x: x[1])[0:11]
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in top_movies:
        movie_id=movies_list.iloc[i[0]].id
        recommended_movie_names.append(movies_list.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


selected_movie = st.selectbox(
    'Search for a movie',
    movies_names
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    # with col6:
    #     st.header(names[5])
    #     st.image(posters[5])
    #
    # with col7:
    #     st.header(names[6])
    #     st.image(posters[6])
    #
    # with col8:
    #     st.header(names[7])
    #     st.image(posters[7])
    #
    # with col9:
    #     st.header(names[8])
    #     st.image(posters[8])
    #
    # with col10:
    #     st.header(names[9])
    #     st.image(posters[9])
