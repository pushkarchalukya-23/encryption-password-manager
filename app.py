from ui import mainpage,checktables,userloginpage,userlogincheck
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
                choice1 = userloginpage()
                if choice1 == 1:
                    while userlogincheck():
                        pass
                    #actual user page
                elif choice1 == 2:
                    while register():
                        pass
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