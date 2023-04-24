user = [["username","password","role"],["wafi","ganteng","manusia"],["ifrit","neraka","jin"]]
def login():
    inuser = str(input("username :"))
    inpasw = str(input("password :"))
    kode_login = 0
    while kode_login != 2:
        kode_login = 0
        for i in range(1,3):
            if inuser == user[i][0] and inpasw == user[i][1] :
                kode_login = 2
                peran = user[i][2]
            elif inuser == user[i][0] and inpasw != user [i][1]:
                kode_login = 1

        if kode_login != 2:
            if kode_login == 0 :
                print("\nUsername tidak terdaftar! \n")
            elif kode_login == 1 :
                print("\nPassword salah! \n")
            
            inuser = str(input("username :"))
            inpasw = str(input("password :"))
    print(f"\nSelamat datang {inuser}!!")
    return peran       
        
print(login())