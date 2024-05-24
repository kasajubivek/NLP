import pandas as pd
from db_connection import get_sql_connection

def load_data_from_sql():
    conn = get_sql_connection()
    sql_query = "SELECT * FROM ADT_Jobs"
    df = pd.read_sql(sql_query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    data = load_data_from_sql()
    test = pd.read_csv('C:\\Users\\Bivek\\PycharmProjects\\pythonProject\\resources\\filtered_data.csv')
    # new_column_names = {'course_title': 'TITLE', 'link': 'LINK', 'viewers': 'VIEWERS', 'popularity': 'POPULAR'}
    # #
    # # # Rename the columns using the dictionary
    # data.rename(columns=new_column_names, inplace=True)
    # print(data['VIEWERS'].head())
    # print(test['VIEWERS'].head())

print(data.columns)
print(test.columns)