import pandas as pd
import streamlit as st
import re
from db_connection import get_sql_connection
import neattext.functions as nfx
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity









RESULT_TEMP = """
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 15px 5px #ccc; background-color: #a8f0c6;
  border-left: 5px solid #6c6c6c;">
<h4>📚 {}</h4>
<p style="color:blue;"><span style="color:black;">🔗 </span><a href="{}",target="_blank">Course Link</a></p>
<p style="color:blue;"><span style="color:black;">🧑‍🎓 Students:</span>{}</p>

</div>
"""



# Search For Course
# @st.cache_data
def search_term_courses(term, df):
    # Extract numeric part from 'VIEWERS' column
    # df['VIEWERS_COUNT'] = df['VIEWERS'].str.extract(r'(\d+)').astype(float)

    # Filter DataFrame based on search term
    # result_df = df[df['TITLE'].str.contains(term)]
    result_df = df[df['TITLE'].str.contains(r'\b{}\b'.format(re.escape(term)), flags=re.IGNORECASE)]

    # Sort DataFrame based on 'VIEWERS' column in descending order
    result_df = result_df.sort_values(by='VIEWERS', ascending=False)
    # result_df = result_df.sort_values(by='VIEWERS_COUNT', ascending=False)

    # Return top x results
    return result_df.head(3)



def recommend(df, course, similarity):
    print("inside recommendation system")
    course_index = df[df['TITLE'] == course].index[0]

    distances = similarity[course_index]
    courses_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_courses_indices = [i[0] for i in courses_list]
    recommended_courses_df = df.iloc[recommended_courses_indices]

    return recommended_courses_df





def main():
    st.sidebar.header('Menu `switcher`')
    st.title("Course Recommendation")

    conn = get_sql_connection()
    sql_query = "SELECT * FROM ADT_COURSES"
    df = pd.read_sql(sql_query, conn)
    df.rename(columns={'course_title': 'TITLE', 'link': 'LINK', 'viewers': 'VIEWERS', 'popularity': 'POPULAR'}, inplace=True)
    df = df.drop_duplicates(subset=['TITLE'])
    # df = pd.read_csv('C:/Users/Bivek/PycharmProjects/NLP/resources/LinkedlnScrappedData.csv')
    df_for_fil = df.copy()

    df_for_fil['TITLE'] = df_for_fil['TITLE'].apply(nfx.remove_stopwords)
    df_for_fil['TITLE'] = df_for_fil['TITLE'].apply(nfx.remove_special_characters)

    cv = CountVectorizer(max_features=3000)
    vectors = cv.fit_transform(df_for_fil['TITLE']).toarray()
    similarity = cosine_similarity(vectors)



    search_term = st.text_input("Search")


    if st.button("Recommend") and search_term is not None:
        try:
            recommended_courses_df = recommend(df, search_term, similarity)

            for index, row in recommended_courses_df.iterrows():
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

        except:
            print("Execption: Executing backup function")
            result_df = search_term_courses(search_term, df)
            # st.write(result_df)
            for index, row in result_df.iterrows():
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



if __name__ == '__main__':
    main()