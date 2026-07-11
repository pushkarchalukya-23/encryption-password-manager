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
    cursor.execute("""INSERT INTO vault(user_id, website_name, 
    website_url, web_username, web_password_encrypted, web_salt_encrypted, 
    note) VALUES ({},'{}','{}','{}','{}','{}','{}');""".format(user_id, web_name, web_url, 
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
    username = input("Enter Website Username (eg. @abc): ")
    return username

def but4():
    password = input("Enter Website Password : ")
    salt = ""
    for i in range(random.randint(3,15)):
        salt += random.choice(ENCRYPTION_STRING)
    return encrypt(salt + password), encrypt(salt)

def but5():
    note =  input("Enter a Note [Max Length = 300 characters] : ")
    return note

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
        if i == '1':
            ltwna += "'" + but1() + "',"
            wna = True

        elif i == '2':
            ltwur += "'" + but2() + "',"
            wur = True

        elif i == '3':
            ltwus += "'" + but3() + "',"
            wus = True

        else:
            pass

    query = """SELECT passwd_id, website_name, website_url, web_username, web_password_encrypted,
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
            print("Password ID = " , i[0])
            print("Website Name = " + i[1])
            print("Website URL = " + i[2])
            print("Website Username = " + i[3])
            print("Website Password = " + decrypt(i[4]).removeprefix(decrypt(i[5]))) #web password decypted and removed salt
            print("Note = " + i[6])
            print("==========================================")
    else:
        print("No Results Found!")
        print("==========================================")

    cursor.close()
    mycon.close()
    return True
    
#see all saved passwords
def allpasswd(user_id):
    print("==========================================")
    print("         ALL SAVED PASSWORDS :-") 
    print("==========================================")
    query = """SELECT passwd_id, website_name, website_url, web_username, web_password_encrypted,
            web_salt_encrypted, note FROM vault WHERE user_id = {}""".format(user_id)
    
    mycon , cursor = get_connect()
    cursor.execute(query)
    data = cursor.fetchall()
    if data :
        for i in data:
            print("Password ID = " , i[0])
            print("Website Name = " + i[1])
            print("Website URL = " + i[2])
            print("Website Username = " + i[3])
            print("Website Password = " + decrypt(i[4]).removeprefix(decrypt(i[5]))) #web password decypted and removed salt
            print("Note = " + i[6])
            print("==========================================")
    else:
        print(">>> No Results Found!")
        print("==========================================")
    cursor.close()
    mycon.close()
    return True

# delete password
def delete(user_id):
    print("==========================================")
    print("           DELETING PASSWORD :-") 
    print("==========================================")
    passwd_id = input("Enter Password ID to delete = ")
    #CHECKING IF EXISTS OR NOT
    query = """SELECT website_name, website_url, web_username, web_password_encrypted,
            web_salt_encrypted, note FROM vault WHERE user_id = {} AND passwd_id = {}""".format(user_id,passwd_id)
    
    mycon , cursor = get_connect()
    cursor.execute(query)
    data = cursor.fetchall()
    if data :
        for i in data:
            print("Website Name = " + i[0])
            print("Website URL = " + i[1])
            print("Website Username = " + i[2])
            print("Website Password = " + decrypt(i[3]).removeprefix(decrypt(i[4]))) #web password decypted and removed salt
            print("Note = " + i[5])
            print("==========================================")
            a = input("You wanna delete it ? (y/n) : ").lower()
            if a == "y":
                print(">>> Deleting Password ...")
                query1 = """DELETE FROM vault WHERE user_id = {} AND passwd_id = {};""".format(user_id, passwd_id)
                cursor.execute(query1)
                mycon.commit()
                cursor.close()
                mycon.close()
                return True
            else:
                print(">>> It just Dodged a Bullet !")
                return True
    else:
        print(">>> No Matches Found!")
        print("==========================================")
        return True

# update password
def update(user_id):
    print("==========================================")
    print("           UPDATING PASSWORD :-") 
    print("==========================================")
    passwd_id = input("Enter Password ID to update = ")
    #CHECKING IF EXISTS OR NOT
    query = """SELECT website_name, website_url, web_username, web_password_encrypted,
            web_salt_encrypted, note FROM vault WHERE user_id = {} AND passwd_id = {}""".format(user_id,passwd_id)
    
    mycon , cursor = get_connect()
    cursor.execute(query)
    data = cursor.fetchall()
    if data :
        for i in data:
            print("1) Website Name = " + i[0])
            print("2) Website URL = " + i[1])
            print("3) Website Username = " + i[2])
            print("4) Website Password = " + decrypt(i[3]).removeprefix(decrypt(i[4]))) #web password decypted and removed salt
            print("5) Note = " + i[5])
            print("==========================================")
            a = input("You wanna update it ? (y/n) : ").lower()
            if a == 'y':
                query = """UPDATE vault SET """
                b = input("Enter Fields to update (eg. 4 or 2145) : ")
                count1 = False
                count2 = False
                count3 = False
                count4 = False
                count5 = False
                for i in b:
                    if (i == '1') and not count1:
                        query += "website_name = '{}' , ".format(but1())
                        count1 = True

                    elif (i == '2') and not count2:
                        query += "website_url = '{}' , ".format(but2())
                        count2 = True

                    elif (i == '3') and not count3:
                        query += "web_username = '{}' , ".format(but3())
                        count3 = True

                    elif (i == '4') and not count4:
                        password , salt = but4()
                        query += "web_password_encrypted = '{}' , web_salt_encrypted = '{}' , ".format(password,salt)
                        count4= True

                    elif (i == '5') and not count5:
                        query += "note = '{}' , ".format(but5())
                        count5 = True
                    else:
                        pass
                query = query[:-2] + "WHERE user_id = '{}' AND passwd_id = '{}';".format(user_id, passwd_id)
                print(">>> UPDATING ...")
                cursor.execute(query)
                mycon.commit()
                cursor.close()
                mycon.close()
                return True
            else:
                print(">>> No Updates Done ...")
                return True
    else:
        print(">>> No Matches Found !")