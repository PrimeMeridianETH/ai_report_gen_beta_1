# ai_report_gen_beta_1
AI Analysis Report Generator
This is a beta version (0.1) of a Streamlit app that generates an analysis report using OpenAI's GPT-3 language model. The app prompts the user to input text material or a URL, and generates a report with the following sections: Executive Summary, Introduction, Methodology, Results, Discussion, Conclusions, and References.

Dependencies
openai
streamlit
Installation
Before running the script, please make sure to install the dependencies by running the following command:

pip install -r requirements.txt
Usage
Set the OpenAI secret key in the script.
Run the script with the following command:

streamlit run ai_analysis_report_generator.py
Enter the text material or URL you would like to generate a report from.
Use the slider to adjust the temperature parameter.
Click the "Generate Report" button to generate a report.
The report will be displayed in the Streamlit app, and can be downloaded using the "Download result" button.
Note
The app has a minimum length requirement for the input text material.
The app uses OpenAI's API to generate the report, and requires an API key to be set. Please make sure to keep your API key secure.
