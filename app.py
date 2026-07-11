from ui import checktables,usersigninpage,controlpanel
from auth import register,userlogincheck

#main thread
def run():
    checktables()
    while True :
        choice1 = usersigninpage()
        if choice1 in ['1','2']:
            if choice1 == '1':
                user_id , username = userlogincheck() #user sign in page
                if not user_id : 
                   continue
            elif choice1 == '2':
                user_id , username = register() #user registering page
                if not user_id :
                   continue
            
            while True:
                if not controlpanel(user_id , username):
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