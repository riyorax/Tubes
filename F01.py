import tools

def login(arr_user,role):
    if role != "" :
        print("Status anda dalam keadaan login, silahkan logout terlebih dahulu!!")
    else:
        inuser = str(input("username :"))
        inpasw = str(input("password :"))
        kode_login = 0
        
        while kode_login != 2:
            kode_login = 0
            for i in range(103):
                if inuser == arr_user[i][0] and inpasw == arr_user[i][1] :
                    kode_login = 2
                    role = arr_user[i][2]
                elif inuser == arr_user[i][0] and inpasw != arr_user [i][1]:
                    kode_login = 1

            if kode_login != 2:
                if kode_login == 0 :
                    print("\nUsername tidak terdaftar! \n")
                elif kode_login == 1 :
                    print("\nPassword salah! \n")
                inuser = str(input("username :"))
                inpasw = str(input("password :"))
        print(f"\nSelamat datang {inuser}!!")
        return role