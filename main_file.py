import mysql.connector as sql
import random

mydb = sql.connect(host='localhost',user='root',passwd='admin')    #Public Key.
curs = mydb.cursor()

print("Welcome to Data Encryption And Decryption")
print("All Kind of Characters are allowed")

def file(e):
    file_name = str(input("Enter File Name You Want to store in: "))
    f1 = open(f'{file_name}.txt','w')
    f1.write(e)
    f1.close()
    main_2()

def encryptor():
    data = str(input("Enter Data: "))
    passwod = str(input("Enter Password: "))       #Private Key.
    caps = list(set(list(data)))

    nq = random.randrange(3,8)
    n = int(nq + 3)
    
    curs.execute(f'create table {passwod}(charac varchar(1),code varchar({n}))')

    lst = []
    act = []

    for i in range(0,len(caps)):
        chara = caps[i]
        i = 0
        while i == 0:
            code = str(random.randrange(0,pow(10,nq)))
            oj = random.randrange(0,len(caps))
            alp = str(caps[oj])
            code += alp
            if code in lst:
                i = 0
            else:
                curs.execute(f"insert into {passwod} values('{chara}','{code}')")
                lst.append(code)
                act.append((chara,code))
                i = 1
        

    mydb.commit()

    encr = str()

    for i in range(0,len(data)):
        for k in range(0,len(act)):
            if data[i] == act[k][0]:
                encr += str(act[k][1])
                encr += str('_')
                break
            else:
                pass
            
    file(encr)

def decryptor():
    num = str(input("Enter Values: "))
    passwod = str(input("Enter Password: "))

    try:
        curs.execute(f'select * from {passwod}')
    except:
        print("Wrong Password")
        main_2()
        
    lum = num.split('_')
    act = []

    for kj in curs:
        act.append(kj)
    
    encrp = str()

    for i in range(0,len(lum)-1):
        for k in range(0, len(act)):
            if str(lum[i]) == str(act[k][1]):
                encrp += str(act[k][0])
            else:
                pass

    ss = str(input("Do you want to delete the Key(y/n): "))
    if ss == 'y':
        curs.execute(f'drop table {passwod}')
    else:
        pass
    
    file(encrp)

def main_2():
    print(f"Welcome {username}")
    print("1. Encrpyt Data")
    print("2. Decrypt Data")
    print("3. Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        encryptor()
    elif ch == 2:
        decryptor()
    else:
        exit()

def main():
    global username
    dd = int(input("Are you (1) Existing User or (2) New User: "))
    if dd == 1:
        try:
            username = input("Enter Username: ")
            curs.execute(f'use {username}')
            main_2()
        except:
            print("Invalid Username")
            main()
    elif dd == 2:
        username = str(input("Welcome!!! Please Enter Your Username: "))
        try:
            curs.execute(f'create database {username}')
            main()
        except:
            print("Username already taken! please enter different username.")
            main()
            
main()
