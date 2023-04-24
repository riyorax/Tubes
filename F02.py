import F01
def logout():
    global F01.role
    if F01.role == "" :
        print("Tidak bisa logout karena belum login")
    else :
        F01.role = ""
        print("keluar dari akun...")

logout()
