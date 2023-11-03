import psycopg2
from psycopg2 import sql
import os
import json
from dotenv import load_dotenv
load_dotenv()

# DB = os.getenv("DB")
# USER = os.getenv("USER")
# PASS = os.getenv("PASS")
# HOST = os.getenv("HOST")
# PORT = os.getenv("PORT")
# Establish a connection to the PostgreSQL database

conn = psycopg2.connect(
    database="mehrab_evan",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)


def insert_knowledge(id, msg_history):
    try:
        with conn.cursor() as cursor:
            # Email and password combination does not exist, insert the new user
            cursor.execute("""
                INSERT INTO knowledge (id, know)
                VALUES (%s, %s)
            """, (id, msg_history))
            conn.commit()
            return "OK"
    except psycopg2.Error as e:
        # Handle any database errors here
        print(f"Error inserting user message: {e}")
        return "Error"


def get_knowledge(id):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT know
            FROM knowledge
            WHERE id = %s
        """, (id,))
        user_data = cursor.fetchone()
        # return user_data
        if user_data:
            user_msg = user_data[0]
            return user_msg
        else:
            return None
