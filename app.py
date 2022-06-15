import pickle
import streamlit as st
import requests

st.image('https://www.reliancedigital.in/wp-content/uploads/2019/02/netflix_movies_cover.jpg')
st.title('Movie Recommender System')
st.write('Recommendation systems play an important role in our everyday life. Starting from movie/music streaming sites like Netflix or Spotify to the most basic search engines, the core component is comprised of recommendation systems. Even the technology giant Google is known for its search engine above everything else. To emphasize its importance we aim to build a simple recommendation system using the TMDB movie database')


st.write('The Content Based movie Recomendation System uses the scikit-learn python library, to match with the input movie with corresponding movies in the dataset with the highest similarity score. Its frontend is designed using Streamlit and it is deployed on Heroku. We aim to demystify the magic behind a recommendation system and provide an introduction to natural language processing also on the way.')

st.header('Bag of Words- NLP')
st.write('Bag of words is a Natural Language Processing technique of text modelling. In technical terms, we can say that it is a method of feature extraction with text data. This approach is a simple and flexible way of extracting features from documents. A bag of words is a representation of text that describes the occurrence of words within a document. We just keep track of word counts and disregard the grammatical details and the word order. It is called a “bag” of words because any information about the order or structure of words in the document is discarded. The model is only concerned with whether known words occur in the document, not where in the document.')