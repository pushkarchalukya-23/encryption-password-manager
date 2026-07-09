from ui import checktables,usersigninpage,controlpanel
from auth import register,userlogincheck

#main thread
def run():
    checktables()
    while True :
        choice1 = usersigninpage()
        if choice1 in ['1','2']:
            if choice1 == '1':
                x = userlogincheck() #user sign in page
                if not x : 
                   continue
            elif choice1 == '2':
                x = register() #user registering page
                if not x :
                   continue
            
            while True:
                if not controlpanel(x):
                    break

        elif choice1 == '3': 
            print("Thanks For Visiting this Program!")
            break
        else:
            print(">>> Invalid Choice !")

# git commands
# git add .
# git commit -m "Added password strength validator"
# git push
# pip freeze > requirements.txt