import streamlit as st
from langchain_imp import getAnswerChain, createVectorDatabase

st.title("Health Lifestyle Nutrition Q&A 🌱")

st.header("Question:")
question = st.text_input(label= ".")

if question:
    chain = getAnswerChain()
    response = chain(question)

    st.header("Answer:")
    st.write(response["result"])



