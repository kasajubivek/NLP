import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
import re
from db_connection import get_sql_connection

df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/job_postings.csv')
companies_df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/companies.csv')
count_df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/employee_counts.csv')

conn = get_sql_connection()
sql_query = "SELECT * FROM ADT_Jobs AS j INNER JOIN ADT_COMPANIES AS c ON j.company_id = c.company_id;"
merged_df = pd.read_sql(sql_query, conn)
merged_df.rename(columns={'experience_level': 'formatted_experience_level'},inplace=True)



print('Original Size',df.shape)

keywords = ['python', 'react', 'angular', 'java', 'javascript', 'C developer', 'C software', 'C++', 'C#',
    'data scientist', 'full stack', 'fullstack', 'backend', 'back end', 'front end', 'frontend',
    'AI', 'Artificial Intelligence', 'software developer', 'software engineer', 'database',
    'AWS', 'devops', 'vue', 'ios', 'android', 'flutter', 'cyber security', 'HTML', 'CSS', 'node',
    'SQL', 'mongodb', 'django', 'Spring', 'Ruby', '.NET', 'PHP', 'TypeScript', 'Swift', 'Kotlin',
    'Xamarin', 'Unity', 'Bootstrap', 'Flask', 'Express.js', 'Redux', 'GraphQL', 'Docker', 'Kubernetes',
    'Jenkins', 'Git', 'RESTful', 'GraphQL', 'Bash/Shell scripting', 'Linux/Unix', 'MATLAB',
    'Ember.js', 'AngularJS', 'Sass', 'D3.js', 'Three.js', 'Pandas', 'NumPy', 'Scikit-learn',
    'TensorFlow', 'PyTorch', 'Keras', 'Flask', 'Django REST framework', 'GraphQL', 'Apache Kafka',
    'RabbitMQ', 'Apache Spark', 'Hadoop', 'Redux Saga', 'RxJS', 'Webpack', 'Gulp', 'Grunt', 'Puppet'
    ,'Ansible', 'Terraform', 'Elasticsearch', 'Logstash', 'Kibana', 'Prometheus', 'Grafana',
    'Jenkins Pipeline', 'Travis CI', 'CircleCI', 'Heroku', 'Firebase', 'Azure', 'Google Cloud',
    'Microsoft Azure', 'Selenium', 'Graphic design', 'RESTful API', 'Microservices architecture']



pattern = '|'.join(r'\b{}\b'.format(re.escape(keyword)) for keyword in keywords)
mask = df['title'].str.contains(pattern, case=False, regex=True)

filtered_df = df[mask]

print('Filtered Size (IT)',filtered_df.shape)

filtered_df.to_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\filtered_data.csv', index=False)

# merged_df = pd.merge(filtered_df, companies_df, on='company_id', how='inner')
merged_df.to_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\resources\\merged_data.csv', index=False)

# def extract_skills(job_desc):
#     skills_found = [skill for skill in keywords if
#                     re.search(rf'\b{re.escape(skill)}\b', job_desc, re.IGNORECASE)]
#     return ', '.join(skills_found)
#
# merged_df['skills'] = merged_df['description_x'].apply(extract_skills)
#
# merged_df = merged_df.dropna(subset=['max_salary'], how='any')
#
# print('After dropping null',merged_df.shape)
































# print(filtered_df.count().sort_values())

# filtered_df = filtered_df.dropna(subset=['max_salary'], how='any')
# filtered_df.dropna(subset=['max_salary'], inplace=True)
# filtered_df = filtered_df[filtered_df['max_salary'].notna()]
#
# filtered_df.to_csv('C:\\Users\\Bivek\\PycharmProjects\\NLP\\filtered_data.csv', index=False)
#
# print('after filter')
# print( filtered_df.count().sort_values())
#
# print('del Size (IT)',filtered_df.shape)



# Print the filtered DataFrame
# print(filtered_df.to_string())


#
#
# unique_values = filtered_df['title'].unique()
#
# # for value in unique_values:
# #     print(value)
#
#
# print('Unique values size', unique_values.shape)
















#
# import re
#
# keywords = ['python', 'react', 'angular', 'java', 'C', 'C++', 'data scientist', 'full stack', 'backend', 'front end', 'AI', 'Artificial Intelligence']
# departments = ['IT', 'Business', 'Marketing']
#
# title_pattern = '|'.join(r'\b{}\b'.format(re.escape(keyword)) for keyword in keywords)
# department_pattern = '|'.join(r'\b{}\b'.format(re.escape(department)) for department in departments)
#
# title_mask = df['title'].str.contains(title_pattern, case=False, regex=True)
# department_mask = df['department'].str.contains(department_pattern, case=False, regex=True)
#
# # Combine the masks using the logical AND (&) operator
# combined_mask = title_mask & department_mask
#
# # Apply the combined mask to filter the DataFrame
# filtered_df = df[combined_mask]

