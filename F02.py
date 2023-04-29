def logout(role,username):
    if role == "" :
        print("Tidak bisa logout karena belum login")
    else :
        role = ""
        username = ""
        print("keluar dari akun...")
    return role, username