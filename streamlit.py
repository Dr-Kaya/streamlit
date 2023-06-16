import streamlit as st
from langchain.llms import OpenAI

st.title('Quick Start app for LLMS')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature = 0.7, openai_api_key  = openai_api_key)
    st.info(llm(input_text))

with st.form(key='my_form'):
    text = st.text_area(label='Enter your text here')
    submitted = st.form_submit_button('Generate response')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key in the sidebar')
    elif submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
        

