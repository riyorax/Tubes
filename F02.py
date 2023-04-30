from list_data import *
def logout():
    global username
    global role
    if role == "" :
        print("Tidak bisa logout karena belum login")
    else :
        role = ""
        username = ""
        print("keluar dari akun...")