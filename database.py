import mysql.connector as f
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connect():
    mycon = f.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASSWORD,
        database = DB_NAME )
    cursor = mycon.cursor()
    return mycon , cursor

# to be published in README.md
#    CREATE DATABASE password_vault;

def create_table_users(cursor):
    cursor.execute("""CREATE TABLE users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(30) UNIQUE NOT NULL,
                master_password_encrypted VARCHAR(50) NOT NULL,
                salt_encrypted VARCHAR(20) NOT NULL,
                created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP) AUTO_INCREMENT = 101;""")
    #insert into users(username,master_password_encrypted,salt_encrypted)
    #values('your_username','your password','salt');

def create_table_vault(cursor):
    cursor.execute("""CREATE TABLE vault (
                passwd_id INT AUTO_INCREMENT PRIMARY KEY ,
                user_id INT NOT NULL,
                website_name VARCHAR(100) NOT NULL,
                website_url VARCHAR(400),
                web_username VARCHAR(100) NOT NULL,
                web_password_encrypted VARCHAR(200) NOT NULL,
                web_salt_encrypted VARCHAR(100) NOT NULL,
                note VARCHAR(300) ) AUTO_INCREMENT = 554;""")
