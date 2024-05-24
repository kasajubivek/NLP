import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pages.CourseRecommendation import search_term_courses
from db_connection import get_sql_connection

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

st.title('LinkedIn Job Postings Analysis')

conn = get_sql_connection()
coursesQuery = "SELECT * FROM ADT_COURSES"
courses = pd.read_sql(coursesQuery, conn)
courses.rename(columns={'course_title': 'TITLE', 'link': 'LINK', 'viewers': 'VIEWERS', 'popularity': 'POPULAR'}, inplace=True)


mergedQuery = "SELECT * FROM ADT_Jobs AS j INNER JOIN ADT_COMPANIES AS c ON j.company_id = c.company_id;"
df = pd.read_sql(mergedQuery, conn)
df.rename(columns={'experience_level': 'formatted_experience_level'}, inplace=True)


extractedSkillsQuery = "SELECT * FROM extracted_skills"
data = pd.read_sql(extractedSkillsQuery, conn)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# st.title('LinkedIn Job Postings Analysis')
st.sidebar.header('Menu `switcher`')


# data = pd.read_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\extracted_skills.csv')
# courses = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/LinkedlnScrappedData.csv')

# Defining the values to remove
values_to_remove = ['code', 'testing', 'databases','database','Oracle',
                    'software development','test','designing','engineering','coding','management', 'Linux','debugging', 'Database']

# data = data[~data['extracted skills'].isin(values_to_remove)]
data = data[~data['extracted skills'].apply(lambda x: x in values_to_remove)]

# st.write(data)

skill_counts = data['extracted skills'].value_counts()
skill_counts = skill_counts.sort_values(ascending=False)
top_20_skills = skill_counts.head(20)
top_5_skills = skill_counts.head(5)



search_terms = top_5_skills.index.tolist()
all_results = []

for term in search_terms:
    result_df = search_term_courses(term, courses)
    all_results.append(result_df)

course_rec = pd.concat(all_results, ignore_index=True)







col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 20 Trending Skills")
    st.bar_chart(top_20_skills)


    # Extract skill names and counts
    skill_names = top_5_skills.index.tolist()
    skill_counts = top_5_skills.values.tolist()

    # st.markdown('### Top 5 Skills')
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(skill_names[0], skill_counts[0])
    with c2:
        st.metric(skill_names[1], skill_counts[1])
    with c3:
        st.metric(skill_names[2], skill_counts[2])
    with c4:
        st.metric(skill_names[3], skill_counts[3])
    with c5:
        st.metric(skill_names[4], skill_counts[4])

    with st.expander("Click here to get Recommended Courses"):
        for index, row in course_rec.iterrows():
            rec_title = row['TITLE']
            rec_url = row['LINK']
            rec_num_sub = row['VIEWERS']

            st.write("")
            st.markdown(
                f'<div style="background-color: #252928; padding: 10px; border-radius: 5px;">'
                f'<h3 style="margin: 0;font-size: 18px;">📚<a href="{rec_url}">{rec_title}</a></h3>'
                f'<p style="margin: 0;">🎓{rec_num_sub}</p>'
                f'</div>',
                unsafe_allow_html=True
            )

with col2:
    st.subheader("Top 5 Tech Hubs")
    # job roles
    # df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/merged_data.csv')
    countries_df = df['city'].value_counts()
    countries_df = countries_df.head(5).sort_values(ascending=False)

    # Creating labels and values for the chart
    labels = countries_df.index.tolist()
    values = countries_df.values.tolist()

    # Creating donut chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

    # Displaying donut chart
    st.plotly_chart(fig)

cl1, cl2= st.columns(2)
with cl1:
    st.subheader("Work Type Demand")
    # df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/merged_data.csv')
    work_type_df = df['work_type'].value_counts()
    work_type_df = work_type_df.head(3).sort_values(ascending=False)

    st.bar_chart(work_type_df)
with cl2:
    st.subheader("Top 10 Job Roles")
    # job roles
    # df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/merged_data.csv')
    job_title = df['title'].value_counts()
    top_10_job_titles = job_title.head(10).sort_values(ascending=False)

    # Creating labels and values for the chart
    labels = top_10_job_titles.index.tolist()
    values = top_10_job_titles.values.tolist()

    # Creating donut chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

    # Displaying donut chart
    st.plotly_chart(fig)