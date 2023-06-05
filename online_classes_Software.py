login=False
join=False
names=['abhinav','aakash','anjali']
passwords=['1234','5678','9012']
print('*' * 30)
print('Not Online Classes application')
print('*' * 30)
print('1.Sign Up',end='   ')
print('2.Log In')

while True:
    
    std=int(input('action:'))
    if std==1:
        s_name=input('name:')
        s_password=input('password:')
        c_password=input('conform password:')
        if s_name in names and s_password in passwords:
            print('your account is already created')
        elif s_password==c_password:
            names.append(s_name)
            passwords.append(s_password)
            print('your account is created')
        else:
            print('Password not matching')
    elif std==2:
        if login==False:
            name=input('student id:')
            password=input('password:')
            if name in names and password in passwords:
                idx1=names.index(name)
                idx2=passwords.index(password)
                if idx1==idx2:
                    print('you are succesfully logedin')
                    print('3.join')
                    login=True
            else:
                print('your are not a existing studend')
                print('OR user id could be wrong')
        else:
            print('your already logedin')
            print('if you want to join the class press action:3')
     
    elif std==3:
        if login==True:
            if join==False:
                print('you joined the class')
                join=True
            else:
                print('already joinded the class')
                print('4.exit')
        else:
            print('cant join the class with out loging in')      
    elif std==4:
        if join==True:
            print('you exited the class')
            break
        else:
            print('cant exit without joining the class')
    else:
        print('invalied or unknown command')
