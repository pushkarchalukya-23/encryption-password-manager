from database import get_connect
from encryption import encrypt, decrypt
from config import ENCRYPTION_STRING
import random

# save password
def save(user_id):
    check = 'r'
    while check == 'r':
        print(">>>>>>>> SAVING NEW PASSWORD <<<<<<<<<")
        web_name = input("Enter Website Name : ").upper()
        web_url = input("Enter Website URL : ")
        web_username = input("Enter Website Username : ").lower()
        web_password = input("Enter Website Password : ")

        choice = input("Want to Add a note ? (y/n) : ")
        if choice == 'y': 
            note = input("Enter a Note [Max Length = 300 characters] : ")
        else: 
            note = None
        check = input("Select ~ [s] save it, [r] re-enter : ").lower()
    print(">>> SAVING INFO ...")

    salt = ""
    for i in range(random.randint(3,15)):
        salt += random.choice(ENCRYPTION_STRING)
    salt_encrypted = encrypt(salt)

    web_password_encrypted = encrypt(salt + web_password)

    mycon , cursor = get_connect()
    cursor.execute("""INSERT INTO vault VALUES ({},'{}','{}','{}','{}','{}','{}');""".format(user_id, web_name, web_url, 
    web_username, web_password_encrypted, salt_encrypted, note))
    mycon.commit()
    cursor.close()
    mycon.close()
    return True
    
# get passwords
# delete password
# update password
