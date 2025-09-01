import streamlit as st 
import os 
from google import genai

st.write("Hello, Mustafa!")
st.file_uploader("Upload data", type=["csv", "txt"])

# Create a single client object
client = genai.Client()