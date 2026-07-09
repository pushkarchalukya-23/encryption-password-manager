import random
from database import get_connect
from config import ENCRYPTION_STRING
from validation import checkusernamedb,checkusername
from encryption import encrypt,decrypt

#user table queries
#registering new user account
def register():
    #true means correct
    #false means error
    print("~~~~~~~~ Fill in Your Details ~~~~~~~~")
    print("""Rules for Unique Username:\n~Min & Max Length (8 to 25) characters\n~Contain LowerCase Letters,Symbols,Digits\n~No Spaces Allowed""")
    username = input("Enter a Unique Username : ")
    if checkusername(username) == 1:
        return False
    print(">>> Checking Availability ...")
    if checkusernamedb(username) == 1:
        print(">>> Username already exists! Try Something Else")
        return False
    else:
        print(">>> Username Available for Use !")
    
    master_password = input("Enter your Master Password : ")

    #check password strength
    #ask whether to use it or change it
    #move forward

    salt = ""
    for i in range(random.randint(3,15)):
        salt += random.choice(ENCRYPTION_STRING)

    master_password_encrypted = encrypt(salt + master_password)
    salt_encrypted = encrypt(salt)
    
    mycon , cursor = get_connect()
    cursor.execute("""INSERT INTO users(username,master_password_encrypted,salt_encrypted)
                   VALUES ('{}','{}','{}')""".format(username,master_password_encrypted,salt_encrypted))
    mycon.commit()
    cursor.execute("""SELECT user_id FROM users WHERE username = '{}';""".format(username))
    data = cursor.fetchall()
    cursor.close()
    mycon.close()
    return data[0][0] #returned user_id if everything went correct

#verify master password
def verify_password(password,username):
    mycon , cursor = get_connect()
    cursor.execute("""SELECT master_password_encrypted, salt_encrypted, user_id FROM users WHERE username = '{}';""".format(username))
    data = cursor.fetchall()
    master_password_decrypted = decrypt(data[0][0])
    salt_decrypted = decrypt(data[0][1])
    dbpassword = master_password_decrypted.removeprefix(salt_decrypted)
    if dbpassword != password:
        cursor.close()
        mycon.close()
        return False
    cursor.close()
    mycon.close()
    return True

#verifying user credentials
def userlogincheck():
    print("~~~~~~~~ Fill in Your Details ~~~~~~~~")
    username = input("Enter your Username : ")
    
    if checkusername(username) == 1:
        return False
    if not checkusernamedb(username):
        print(">>> Account with Username does not exists!")
        return False
    master_password = input("Enter your Master Password : ")
    if not verify_password(master_password,username):
        print(">>> Incorrect Password!")
        return False
    else:
        mycon , cursor = get_connect()
        cursor.execute("""SELECT user_id FROM users WHERE username = '{}';""".format(username))
        data = cursor.fetchall()
        cursor.close()
        mycon.close()
        return data[0][0] #returned user_id if everything went correct
    
    