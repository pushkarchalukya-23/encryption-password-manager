import random
from database import get_connect
from config import ENCRYPTION_STRING
from validation import checkusernamedb,checkusername
from encryption import encrypt,decrypt,hashpasswd
#user table queries
def register():
    #true means correct
    #false means error
    print("~~~~~~~~ Fill in Your Details ~~~~~~~~")
    print("""Rules for Unique Username:\n~Min & Max Length (8 to 25) characters\n~Contain Letters,Symbols,Digits\n~No Space in between""")
    username = input("Enter a Unique Username : ")
    if checkusername(username) == 1:
        return False
    if checkusernamedb(username) == 1:
        print("Username already exists! Try Something Else")
        return False
    
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
    return True
    
# change_master_password
def verify_password(password,username):
    mycon , cursor = get_connect()
    cursor.execute("""SELECT master_password_encrypted, salt_encrypted, user_id FROM users WHERE username = '{}';""".format(username))
    data = cursor.fetchall()
    master_password_decrypted = decrypt(data[0][0])
    salt_decrypted = decrypt(data[0][1])
    dbpassword = master_password_decrypted.removeprefix(salt_decrypted)
    # [('O86nPy@ZnyD8P[y', '', 102)]
    if dbpassword != password:
        return False
    return data[0][2] #returning user_id if password is correct
