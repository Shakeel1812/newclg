import streamlit as st
from google import genai

Robot = genai.Client(api_key ="AIzaSyDeJd1aD8rLOF0wF_mgUxaKxuYWiajfQPo")

st.title("Shakeel's ChatGPT")

question = st.text_input("Ask Something :")

if st.button("Send"):
    response = Robot.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question)
    st.write(response.text)

