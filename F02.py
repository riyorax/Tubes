import F01_Login
global role
def logout():
    global role
    if role == "" :
        print("Tidak bisa logout karena belum login")
    else :
        role = ""
        print("keluar dari akun...")

logout()
