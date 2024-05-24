import pandas as pd
from run import extract_skills
from db_connection import get_sql_connection

conn = get_sql_connection()
sql_query = "SELECT * FROM ADT_Jobs"
df = pd.read_sql(sql_query, conn)
df.rename(columns={'experience_level': 'formatted_experience_level'},inplace=True)

# df = pd.read_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\filtered_data.csv')

# Applying skill extraction to all rows
df['skills'] = df['description'].apply(extract_skills)

# df.to_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\nlp_data.csv', index=False)


# Flattening the list of skills from all rows into a single list
all_skills = [skill for sublist in df['skills'] for skill in sublist]

# Creating a new DataFrame with the extracted skills
extracted_skills_df = pd.DataFrame({'extracted skills': all_skills})


# Define the values to remove
values_to_remove = ['code', 'testing', 'databases', 'database', 'Oracle', 'software development', 'test',
                        'designing', 'engineering', 'coding', 'management', 'Linux', 'debugging', 'Database']

# Filter out rows containing values to remove
extracted_skills_df = extracted_skills_df[~extracted_skills_df['extracted skills'].isin(values_to_remove)]

extracted_skills_df.to_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\extracted_skills.csv', index=False)
