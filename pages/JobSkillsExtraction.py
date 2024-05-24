import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from run import extract_skills

st.title('Skills Extraction')
st.sidebar.header('Menu `switcher`')

job_description = st.text_input('Enter the job description')

if st.button('Extract Skills'):
    skills = extract_skills(job_description,"true")
    values_to_remove = ['code', 'testing', 'databases', 'database', 'Oracle', 'software development', 'test',
                        'designing', 'engineering', 'coding', 'management', 'Linux', 'debugging', 'Database']
    skills = [skill for skill in skills if skill.lower() not in values_to_remove]
    st.write("The skills extracted from the Job Description are :")
    st.write(skills)