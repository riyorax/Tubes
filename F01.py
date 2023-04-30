# from list_data import *

def login():
    global username
    global role
    if role != "" :
        print("Status anda dalam keadaan login, silahkan logout terlebih dahulu!!")
    else:
        inuser = str(input("username :"))
        inpasw = str(input("password :"))
        kode_login = 0
        
        while kode_login != 2:
            kode_login = 0
            for i in range(103):
                if inuser == role[i][0] and inpasw == role[i][1] :
                    kode_login = 2
                    role = role[i][2]
                    username = [i][0]
                elif inuser == role[i][0] and inpasw != role [i][1]:
                    kode_login = 1

            if kode_login != 2:
                if kode_login == 0 :
                    print("\nUsername tidak terdaftar! \n")
                elif kode_login == 1 :
                    print("\nPassword salah! \n")
                inuser = str(input("username :"))
                inpasw = str(input("password :"))
        print(f"\nSelamat datang {inuser}!!")