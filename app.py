import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Interview Assistant",layout="centered")
st.title("  AI _INTERVIEW_ASSISTANT")
st.caption("practice interviews with AI generated questions and constructive feedback.")
st.caption("launched by Deepashree")              
st.write("Department of AI & DS")

try:
  client = Groq(api_key=st.secrets["GROQ_API_KEY"])
  st.write("API CONNECTION SUCCESSFULL")
except (keyError, FileNotFoundError):
  st.error("GROQ_API_KEY is missing.add it to streamlitcloud--> App settings secrets")
  st.stop()
                



role = st.selectbox("Select Job Role",[
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Machine learning Engineer",
  "Software Engineer",
  "HR Executive",
])

if st.button("Generate Interview Questions"):

  prompt = "Generate 5 Interview Question for the Role of " + role 
  response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {"role":"system","content":"you are an expert technical interviewer"},
      {"role":"user","content":prompt}
    ]
  )
  output = response.choices[0].message.content
  st.write(output)
      
    
      
