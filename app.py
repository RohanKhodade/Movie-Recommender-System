import streamlit as st
import pickle
import pandas
import requests

# loading movies dataset and simialrity model
with open(r"C:\Users\HP\OneDrive\Desktop\Artificial Intellegence\Deep learning\Movie Recommender System\movies.pkl","rb") as file:
    df=pickle.load(file)
    
with open(r"C:\Users\HP\OneDrive\Desktop\Artificial Intellegence\Deep learning\Movie Recommender System\Similarity.pkl","rb") as file:
    similarity=pickle.load(file)
    
movies=df["title"]
st.title("Movies Recommender system")

# function for fetching poster

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    
    

# function for recommendation

def recommend(movie):
    movie_index=df[df["title"]==movie].index[0]
    distances=list(enumerate(similarity[movie_index]))
    m_list=sorted(distances,reverse=True,key=lambda x:x[1])[0:5]
    
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in m_list:
        recommended_movies.append(df.iloc[i[0]].title)
        movie_id=df.iloc[i[0]].movie_id # to fetch poster
        recommended_movies_poster.append(fetch_poster(movie_id))
        
    return recommended_movies,recommended_movies_poster

st.selectbox("How would we contact you",("Email","Phone","Fax",))

movie=st.selectbox("get movie",movies)

search= st.button("Search")




if search:
    result,posters=recommend(movie)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.write(result[0])
        st.image(posters[0])
        
    with col2:
        st.write(result[1])
        st.image(posters[1])
        
    with col3:
        st.write(result[2])
        st.image(posters[2])
        
    with col4:
        st.write(result[3])
        st.image(posters[3])
        
    with col5:
        st.write(result[4])
        st.image(posters[4])