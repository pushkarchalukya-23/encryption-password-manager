from database import get_connect,create_table_users,create_table_vault
from auth import verify_password
from validation import checkusernamedb
# decide whether to open admin page or user page for different functions
def mainpage():
    print("<------------ MAIN PAGE ------------->")
    print("""1. Admin Login\n2. User Login\n3. Exit""")
    choice = int(input("Enter your Choice : "))
    return choice

def userloginpage():
    print("<------ USER SIGN IN / SIGN UP ------>")
    print("""1. Already Have an Account ?\n2. Register\n3. Back""")
    choice = int(input("Enter your Choice : "))
    return choice

def userlogincheck():
    print("~~~~~~~~ Fill in Your Details ~~~~~~~~")
    username = input("Enter your username : ")
    if checkusernamedb(username) == 0:
        print("Invalid Username!")
        return True
    master_password = input("Enter your password : ")
    if verify_password(master_password,username) == 0:
        print("Incorrect Password!")
        return True
    


def checktables():
    mycon , cursor = get_connect()
    #checking if tables exists or not , otherwise creating them
    cursor.execute("""SHOW TABLES;""")
    data = cursor.fetchall()
    flagu = 0
    flagv = 0
    for i in data:
        if i[0] == 'users' :
            flagu = 1
        if i[0] == 'vault' :
            flagv = 1
    #if it does not exist, function queries is used to create it.
    if flagu == 0:
        create_table_users(cursor)
    if flagv == 0:
        create_table_vault(cursor)
    cursor.close()
    mycon.close()
