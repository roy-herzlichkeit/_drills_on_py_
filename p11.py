usr = str(input("Username: "))

len = len(usr)
spaces = usr.count(" ")
digits = usr.isalnum() and usr.isalpha()

if len < 13 and not spaces and digits :
    print('Valid Username')
else:
    print('Invalid Username')