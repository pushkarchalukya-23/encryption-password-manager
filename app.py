from ui import mainpage,checktables,usersigninpage,userlogincheck
from auth import register

#main thread
def run():
    checktables()

    while True :
        #checking choice
        choice = mainpage()
        if (choice == 1) :
            continue
            #adminlogin()

        elif (choice == 2) :
            while True :
                choice1 = usersigninpage()
                if choice1 == 1:
                    while True:
                        if userlogincheck() :
                            continue
                    #actual user page
                elif choice1 == 2:
                    while True:
                        if register() :
                            continue
                    #actual user page
                elif choice1 == 3: 
                    break
                else:
                    print("Invalid Choice !")
        elif (choice == 3) :
            break
        else :
            print("Invalid Choice !")

# git add .
# git commit -m "Added password strength validator"
# git push