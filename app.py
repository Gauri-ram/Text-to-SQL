from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model= genai.GenerativeModel('gemini-pro')
    response= model.generate_content([prompt[0], question])
    return response.text

def get_sql_query(sql,db):  
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(sql)
    rows=c.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt= [
    """
    You are an expert at converting English questions to SQL query!
    You have been given a question and you need to convert it to a SQL query.
    The database contains NAME (varchar(25)), CLASS (varchar(25)), SECTION (varchar(25)) AND MARKS (int).
    Questions could be of the type 
    example1- Give me all students in the school which should have query -> 'Select * from STUDENT'
    example2- Give me all student names in the school which have a mark greater than 80 should -> 'Select name from student where marks>80'
    example3-  Give me student names in ECE class -> 'Select name from student where class='ECE'
    Based on question you can use in, orderby etc and sql query should not have ''' in the beginning and end
    """
]

st.set_page_config(page_title="SQL query getter")
st.header("Retrive using english commands")

question= st.text_input("Input: ", key=input)
submit= st.button("Ask the question")

if submit:
    response= get_gemini_response(question,prompt)
    print(response)
    data= get_sql_query(response, "student.db")
    st.subheader("Output: ")
    for row in data:
        print(row)
        stripped_row = str(row).strip("(), ")
        st.subheader(stripped_row)
