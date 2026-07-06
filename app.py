from ui import mainpage,checktables,usersigninpage,userlogincheck
from auth import register

#main thread
def run():
    checktables()

    while True :
        #checking choice
        choice = mainpage()
        if (choice == 1) : #admin panel
            continue
            #adminlogin()

        elif (choice == 2) : #user panel
            while True :
                choice1 = usersigninpage()

                if choice1 in [1,2]:
                    if choice1 == 1:
                        if not userlogincheck() : #user sign in page
                            continue
                    elif choice1 == 2:
                        if not register() : #user registering page
                            continue
                    #actual user password manager panel

                elif choice1 == 3: 
                    break
                else:
                    print("Invalid Choice !")
        elif (choice == 3) : #exit
            break
        else :
            print("Invalid Choice !")
# git commands
# git add .
# git commit -m "Added password strength validator"
# git push
# pip freeze > requirements.txt