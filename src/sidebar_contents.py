import streamlit as st
import time

def write_sidebar_contents():
    intro='''
PrepAI is a Generative AI application that allows a user to prepare for background as well as technical interviews. The webapp 
utilises open source ollama model "llama3.1", which is prompt engineered to provide users with accurate and relevant information, 
simulations, and practice questions tailored to their specific interview needs.
    '''
    st.sidebar.info("About the project:")
    st.sidebar.write(intro)
    st.sidebar.info("Developed by:")
    st.sidebar.write("Ayush Saini")