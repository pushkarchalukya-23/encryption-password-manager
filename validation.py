from database import get_connect
#at the time of register n login
def checkusernamedb(username):
    mycon , cursor = get_connect()
    cursor.execute("""SELECT username FROM users;""")
    data = cursor.fetchall()
    flag = 0
    for i in data:
        if username == i[0]:
            flag = 1
    cursor.close()
    mycon.close()
    return flag

def checkusername(username):
    flag = 0
    #checking length
    if (len(username) < 8) or (len(username) > 25):
        print("Inappropriate Character Length!")
        flag = 1
    
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]:;?><,./-= "
    flag1 = 0
    flags = 0
    #checking letters, symbols, digits, and also spaces
    for i in username:
        if i not in string:
            flag = 1
            flag1 = 1
        if i.isspace():
            flag = 1
            flags = 1
    if flag1 == 1:
        print("Inappriate Characters used!")
    if flags == 1:
        print("Spaces not Allowed!")
    return flag


# email
# password
# password match
# website
# notes
# not_empty
