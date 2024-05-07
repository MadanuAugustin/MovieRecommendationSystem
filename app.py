import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    # login to the tmdb website to get the api key of your own
    url = "https://api.themoviedb.org/3/movie/{}?api_key=638e587479641f280f1ec49744fd641e&&language=en-US".format(movie_id)
    data = requests.get(url)
    # whatever the data we have got is in the html format, so we need to convert to json format so that we can access the data using keys
    data = data.json()
    poster_path = data['poster_path']
    # the poster_path obtained is not fullpath, so we need to define fullpath by searching "tmdb image path in google search engine"
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# creating a function to fetch the top five recommended movies
# and we are fetching movie poster using movie id
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# title of the project
st.header('Movie Recommender System Using Machine Learning')

# loading the embeddings from the pickle files
movies = pickle.load(open('artifacts//movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

# fetching the movie titles from the variable "movies"

movie_list = movies['title'].values

# designing the searchbar with placeholder name
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# creating a button
# created a function name "recommend" where it gives recommended_movies_name, recommended_movies_poster
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])