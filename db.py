import mysql.connector

def get_connection():

    connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="Srijakani@01",

        database="examguard"

    )

    return connection