import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini GenAI App")

st.title("🚀 Gemini GenAI Application")

user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
    if user_input:
        response = model.generate_content(user_input)
        st.success(response.text)

