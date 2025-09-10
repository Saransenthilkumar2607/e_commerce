from flask import Flask
import mysql.connector

app = Flask(__name__)


def __init__db():
    #to create a database of student if there is not an databases.
    connect = mysql.connector.connect(**db_config)
    #connect the sql object
    cursor = connect.cursor()
    #data tables format of student_details\
    cursor.execute('''create table if not exists students_details(
                        student_id int auto_increment primary key,
                        student_name varchar(100) not null,
                        student_number bigint not null,
                        student_email text not null, 
                        student_course text not null
                   
           )
  ''')
    #save connection
    connect.commit()
    # close the database student_details
    connect.close()