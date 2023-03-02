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
            prompt = "Generate a professional, empirically true and accurate analysis report. DO NOT REPEAT ANY WORDS OR PHRASING MULTIPLE TIMES. Be incredibly specfic and elaborate if required. Include numerical data points in an orderly cohesive format. Use the following sectional criteria without any text or phrase redunancies within or between sections (very important): Executive Summary, Introduction, Methodology, Results, Discussion, Conclusions, References. Use only the text information located here: " + article_text,
            max_tokens = 3800,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
