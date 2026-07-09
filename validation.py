from database import get_connect

def checkusernamedb(username):
    mycon , cursor = get_connect()
    cursor.execute("""SELECT username FROM users;""")
    data = cursor.fetchall()
    for i in data:
        if i[0] == username :
            cursor.close()
            mycon.close()
            return True #found
    return False #otherwise not found

def checkusername(username):
    flag = 0 #for overall error

    #checking lowercase
    if not username.islower():
        print(">>> Only LowerCase Letters Allowed!")
        flag = 1

    #checking length
    if (len(username) < 8) or (len(username) > 25):
        print(">>> Inappropriate Character Length!")
        flag = 1
    
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]:;?><,./-= "
    flag1 = 0 #for Characters
    flags = 0 #for space

    #checking letters, symbols, digits, and also spaces
    for i in username:
        if i not in string:
            flag = 1
            flag1 = 1
        if i.isspace():
            flag = 1
            flags = 1
    if flag1 == 1:
        print(">>> Inappriate Characters used!")
    if flags == 1:
        print(">>> Spaces not Allowed!")
    return flag

