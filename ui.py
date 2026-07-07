from database import get_connect,create_table_users,create_table_vault
from auth import verify_password
from validation import checkusernamedb
#gonna add one more table for hashed passwords, separate table for encrypted and hashed ones, create table, diff option for hashing

# decide whether to open admin page or user page for different functions
def usersigninpage():
    print("<------ USER SIGN IN / SIGN UP ------>")
    print("""1. Already Have an Account ?\n2. Register\n3. Back""")
    choice = input("Enter your Choice : ")
    return choice


def controlpanel(user_id):
    print("============= MAIN MENU ==============")
    print("""    [1] SAVE NEW PASSWORD
    [2] SEARCH PASSWORDS
    [3] RESET MASTER_PASSWORD
    [4] UPDATE PASSWORD
    [5] LOGOUT""")
    choice2 = int(input("Enter your Preference : "))
    if choice2 == 1:
        pass
    elif choice2 == 2:
        pass
    elif choice2 == 3:
        pass
    elif choice2 == 4:
        pass
    elif choice2 == 5:
        print(">>> Logging Out ...")
        return False
    
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
