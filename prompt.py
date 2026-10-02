import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    from lan import API_KEY
import os

os.environ["GOOGLE_API_KEY"] = API_KEY

st.title("Langchain PromptTemplate Demo")
st.write("Ask anything")

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=API_KEY
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer this question clearly and simply: {question}"
)

chain = prompt | llm

question = st.text_input("Enter your question:")

if st.button("Generate Answer"):
    if question:
        response = chain.invoke({"question": question})
        st.write("### Answer")
        st.write(response.content)
    else:
        st.warning("Please enter a question.")
