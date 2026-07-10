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
        web_username = input("Enter Website Username (eg. @abc): ")
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

def but1():
    name = input("Enter Website Name : ").upper()
    return name

def but2():
    url = input("Enter Website URL : ")
    return url

def but3():
    username = input("Enter Website Username : ")
    return username

def search(user_id):
    print(":::::::::::::::::::::::::::::::::::::::::::::::")
    print("Searching on the basis of ?")
    print("""1) Website Name\n2) Website URL\n3) Website Username""")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")
    ch = input("Enter your choice (eg. 1 or 2213) :")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    #query building
    wna = False
    wur = False
    wus = False

    ltwna = "("
    ltwur = "("
    ltwus = "("
    
    for i in ch:
        i = int(i)
        if i == 1:
            ltwna += "'" + but1() + "',"
            wna = True

        elif i == 2:
            ltwur += "'" + but2() + "',"
            wur = True

        elif i == 3:
            ltwus += "'" + but3() + "',"
            wus = True

        else:
            pass

    query = """SELECT website_name, website_url, web_username, web_password_encrypted,
            web_salt_encrypted, note FROM vault WHERE user_id = {}""".format(user_id)
    
    fwna = ltwna[:-1] + ")"
    fwur = ltwur[:-1] + ")"
    fwus = ltwus[:-1] + ")"

    if wna:
        query += """ AND website_name IN {}""".format(fwna)
    if wur:
        query += """ AND website_url IN {}""".format(fwur)
    if wus:
        query += """ AND web_username IN {}""".format(fwus)

    mycon , cursor = get_connect()
    cursor.execute(query)
    data = cursor.fetchall()
    if data :
        print("==========================================")
        print("         Search Results are :-") 
        print("==========================================")
        for i in data:
            print("Website Name = " + i[0])
            print("Website URL = " + i[1])
            print("Website Username = " + i[2])
            print("Website Password = " + decrypt(i[3]).removeprefix(decrypt(i[4]))) #web password decypted and removed salt
            print("Note = " + i[5])
            print("==========================================")
    else:
        print("No Results Found!")
        print("==========================================")

    cursor.close()
    mycon.close()
    return True
    
# get passwords
# delete password
# update password