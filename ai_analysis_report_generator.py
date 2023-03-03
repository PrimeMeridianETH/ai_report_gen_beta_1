# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI Analysis Report Generator')
st.subheader('current version : beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter the text material or URL you would like to generate a report from')
if len(article_text) > 5:
    temp = st.slider("temperature", 0.4, 0.6, 0.8)
    if st.button ('Generate Report'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Generate as a professional senior consultant, an empirically true and accurate analysis report. Do not repeat yourself anywhere throughout the resposne. Be incredibly specfic and elaborate contextually if required, but only from supplied information. Always include ALL numerical data points in an orderly cohesive format. Use the following sectional criteria without any text or phrase repeatings within or between sections (very important): Executive Summary, Introduction, Methodology, Results, Discussion, Conclusions, Keywords (only use keywords from supplied text). Use only the text information located here: " + article_text,
            max_tokens = 2000,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
