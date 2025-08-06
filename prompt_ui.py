from pyexpat import model
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Reasearch Tool")

user_input = st.text_input("Enter your question or prompt")

if st.button("Summarize"):
    result = model.invoke(user_input) 
    st.write(result.content)
