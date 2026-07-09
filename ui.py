from database import get_connect,create_table_users,create_table_vault
from models import save
# decide whether to open admin page or user page for different functions
def usersigninpage():
    print("<------ USER SIGN IN / SIGN UP ------>")
    print("""1. Already Have an Account ?\n2. Register\n3. Back""")
    choice = input("Enter your Choice : ")
    return choice


def controlpanel(user_id):
    print("======================================")
    print("             MAIN MENU")
    print("======================================")
    print("""[1] SEARCH WEB_PASSWORDS
[2] SAVE NEW WEB_PASSWORD
[3] UPDATE WEB_PASSWORD
[4] DELETE WEB_PASSWORD
[5] RESET MASTER_PASSWORD
[6] DELETE USER ACCOUNT
[7] LOGOUT""")

    choice2 = int(input("Enter your Preference : "))
    if choice2 == 1:
        #search(user_id)
        return True
    elif choice2 == 2:
        save(user_id)
        return True
    elif choice2 == 3:
        #update(user_id)
        return True
    elif choice2 == 4:
        #delete(user_id)
        return True
    elif choice2 == 5:
        #reset(user_id)
        return True
    elif choice2 == 6:
        #deleteacc(user_id)
        return False
    elif choice2 == 7:
        print(">>> Logging Out ...")
        return False
    else:
        print(">>> Invalid Preference !")
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
