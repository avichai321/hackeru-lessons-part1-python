print('into ex_lists_users_login.py')

users_email = ['gal@hackeru.co.il', 'dan@hackeru.co.il', 'ran@hackeru.co.il']
users_logins = ['gal@hackeru.co.il']

def register():
    new_email = input("Enter new e-mail")
    if new_email not in users_email:
        users_email.append(new_email)
        print('היוזר התווסף בהצלחה')
    else:
        print("היוזר קיים, נסה לבחור שם אחר")

def login():
    email = input("Enter your e-mail")
    if email in users_email:
        if email in users_logins:
            print('הינך מחובר במכשיר אחר - יש להתנתק קודם')
        else:
            users_logins.append(email)
            print('ברוך הבא - הנך מחובר למערכת')
    else:
        print("המנוי אינו קיים יש להרשם קודם")

def logout():
    pass

def delete():
    pass

def info():
    print(users_email)
    print(users_logins)


def play():
    op = input('****** Enter Option ****** \n'
               '0 - Stop | '
               '1 - register | '
               '2 - login | '
               '3 - logout | '
               '4 - delete | '
               '100 - Info | '
               '\n >>>')
    if op == '0':
        return
    elif op == '1':
        register()
    elif op == '2':
        login()
    elif op == '3':
        logout()
    elif op == '4':
        delete()
    elif op == '100':
        info()
    play()

play()
