import random
from database import get_connect
from config import ENCRYPTION_STRING
from validation import checkusernamedb,checkusername
from encryption import encrypt,decrypt,hashpasswd
#user table queries
def register():
    #true means error
    #means correct
    print("~~~~~~~~ Fill in Your Details ~~~~~~~~")
    print("""Rules for Unique Username:\n~Min & Max Length (8 to 25) characters\n~Contain Letters,Symbols,Digits\n~No Space in between""")
    username = input("Enter a Unique Username : ")
    if checkusername(username) == 1:
        return True
    if checkusernamedb(username) == 1:
        print("Username already exists! Try Something Else")
        return True
    
    salt = ""

    for i in range(10):
        salt += random.choice(ENCRYPTION_STRING)
    
    master_password = input("Enter your Master Password : ")
    master_password_encrypted = encrypt(salt + master_password)
    salt_encrypted = encrypt(salt)
    
    mycon , cursor = get_connect()
    cursor.execute("""INSERT INTO users(username,master_password_encrypted,salt_encrypted)
                   VALUES ('{}','{}','{}')""".format(username,master_password_encrypted,salt_encrypted))
    mycon.commit()
    cursor.close()
    mycon.close()
    return False
    
# change_master_password
def verify_password(master_password,username):
    mycon , cursor = get_connect()
    cursor.execute("""SELECT master_password_encrypted FROM users WHERE username = '{}';""".format(username))
    data = cursor.fetchall()
    flag = 0
    if decrypt(data[0][0]) == master_password:
        flag = 1
    return flag