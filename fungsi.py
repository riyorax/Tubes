from list_data import *

# F01
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

# F02
def logout():
    global username
    global role
    if role == "" :
        print("Tidak bisa logout karena belum login")
    else :
        role = ""
        username = ""
        print("keluar dari akun...")

# F03
def summonjin():
    """Bandung Bondowoso memiliki wewenang memanggil jin dari dunia lain. 
    fungsi mengambil input username, password, dan jenis jin."""
    global role
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk summon jin!")
        return 0
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        if data.N_user == 103:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            
            # Cek input jenis jin
            while (not((jenis_jin == "1") or (jenis_jin == "2"))):
                print(f"\nTidak ada jenis jin bernomor “{jenis_jin}”!")
                jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if jenis_jin == "1":
                jenis_jin = "Pengumpul"
                print("\nMemilih jin “Pengumpul”.\n")
            elif jenis_jin == "2":
                jenis_jin = "Pembangun"
                print("\nMemilih jin “Pembangun”.\n")

            username_jin = input("Masukkan username jin: ")

            # Cek input username jin
            while True:
                for i in range(1, data.N_user+1):
                    if data.users[i][0] == username_jin:
                        print(f'\nUsername “{username_jin}” sudah diambil!\n')
                        username_jin = input("Masukkan username jin: ")
                        continue
                break

            password_jin = input("Masukkan password jin: ")

            # Cek input password jin
            while True:
                if len(password_jin) < 5 or len(password_jin) > 25:
                    print("\nPassword panjangnya harus 5-25 karakter!\n")
                    password_jin = input("Masukkan password jin: ")
                    continue
                print("Mengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                break

            # Memasukkan input jin baru ke dalam array user csv
            data.N_user += 1
            data.users[data.N_user] = [username_jin, password_jin, jenis_jin]

# F04
def hapusjin():
    """Bandung Bondowoso memiliki wewenang untuk menghapus jin.
    Fungsi menghapus jin dan candi yang dibuat oleh jin tersebut juga ikut terhapus."""
    global role
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk menghapus jin!")
        return 0
    else:
        hapus_jin = input("Masukkan username jin : ")

        i = 0

        while i <= (data.N_user):
            if data.users[i][0] == hapus_jin:
                konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                if konfirmasi == "Y" or konfirmasi == 'y':
                    # Hapus jin
                    for i in range(1, data.N_user+1):
                        if data.users[i][0] == hapus_jin:
                            data.users[i] = ['', '', '']
                            for j in range(i, data.N_user):
                                data.users[j] = data.users[j+1]
                            break 
                    # Hapus candi jin
                    for i in range (data.N_candi):
                        if data.users[i][1] == hapus_jin:
                            data.users[i] = ['', '', '','','']
                            for j in range(i, data.N_user):
                                data.users[j] = data.users[j+1]
                            break    
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    break
                else: # Konfirmasi == "N" or "n"
                    break
            elif i == (data.N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1

# F05
def ubahjin():
    """Bandung Bondowoso memiliki wewenang untuk mengubah tipe jin.
    Fungsi mengubah tipe jin yang sudah di summon"""
    global role
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk mengubah tipe jin!")
        return 0
    else:
        ingin_ubah = input("Masukkan username jin : ")
        
        i = 2
        while i <= (data.N_user):
            if data.users[i][0] == ingin_ubah:
                # Validasi jenis jin dan konfirmasi perubahan
                if data.users[i][2] == 'Pengumpul':
                    konfirmasi = input(f"Jin ini bertipe “{data.users[i][2]}”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        data.users[i][2] = 'Pembangun'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
                # Validasi jenis jin dan konfirmasi perubahan
                elif data.users[i][2] == 'Pembangun':
                    konfirmasi = input(f"Jin ini bertipe “{data.users[i][2]}”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        data.users[i][2] = 'Pengumpul'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
            elif i == (data.N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1