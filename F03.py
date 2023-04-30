import list_data as data
# from list_data import *

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