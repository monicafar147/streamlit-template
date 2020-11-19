"""
    Streamlit web developer application to classify tweets from twitter.
    Author: Monica Farrell.
"""
# Streamlit dependencies
import streamlit as st

# general
import numpy as np 
import pandas as pd
import dill as pickle

#load model
process_path = "clean_me.pkl"
with open(process_path,'rb') as file:
    clean = pickle.load(file)

#load data
data = pd.read_csv('Tweetid,_Originaltex_1605092859311.csv')

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """
    st.write('-----------------------------------------------')
    st.title("Classify tweets")
    # enter text in here
    st.write('### Enter Your Three Favorite Movies')
    movie_1 = st.selectbox('First Option',data['text'][0:10])

    if st.button("Clean"):
        # call your model
        cleaned_text = clean(movie_1)

        # display results
        st.success(cleaned_text)



if __name__ == '__main__':
    
    main()
