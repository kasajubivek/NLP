import pandas as pd
import pypyodbc


def get_sql_connection():
    SERVER_NAME = 'LAPTOP-C38N2OPU\\SQLEXPRESS'
    DATABASE_NAME = 'LinkedIn'

    conn = pypyodbc.connect("""
        Driver={{SQL Server}};
        Server={0};
        Database={1};
        Trusted_Connection=yes;""".format(SERVER_NAME, DATABASE_NAME))

    return conn
#
# sql_query = "SELECT * FROM ADT_COMPANIES"  # Corrected SQL query string
#
# df = pd.read_sql(sql_query, conn)

# print(df)
#
# def get_sql_connection():
#     server = 'LAPTOP-C38N2OPU\SQLEXPRESS'
#     database = 'LinkedIn'
#     username = 'LAPTOP-C38N2OPU\Bivek'
#     password = ''
#     # conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
#     # return pyodbc.connect(conn_str)
#     return pyodbc.connect("""Driver={SQL SERVER NATIVE CLIENT 11.0}; Server='LAPTOP-C38N2OPU\SQLEXPRESS; Database=python; Trusted_connection=yes;""")
#