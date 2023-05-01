from list_data import *
import tools
import os
import random
import argparse
from list_data import *
import list_data as data
# F01
def login():
    global username
    global role
    global user
    if role != "" :
        print("Status anda dalam keadaan login, silahkan logout terlebih dahulu!!")
    else:
        inuser = str(input("username :"))
        inpasw = str(input("password :"))
        kode_login = 0
        
        while kode_login != 2:
            kode_login = 0
            for i in range(103):
                if inuser == user[i][0] and inpasw == user[i][1] :
                    kode_login = 2
                    role = user[i][2]
                    username = user[i][0]
                elif inuser == user[i][0] and inpasw != user[i][1]:
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
    global user
    global N_user
    N_user = hitung_user()
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk summon jin!")
        return 0
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        if N_user == 103:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        else:
            jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            
            # Cek input jenis jin
            while (not((jenis_jin == "1") or (jenis_jin == "2"))):
                print(f"\nTidak ada jenis jin bernomor “{jenis_jin}”!")
                jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if jenis_jin == "1":
                jenis_jin = "jin_pengumpul"
                print("\nMemilih jin “Pengumpul”.\n")
            elif jenis_jin == "2":
                jenis_jin = "jin_pembangun"
                print("\nMemilih jin “Pembangun”.\n")

            username_jin = input("Masukkan username jin: ")

            # Cek input username jin
            while True:
                for i in range(1, N_user+1):
                    if user[i][0] == username_jin:
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
            N_user += 1
            user[N_user] = [username_jin, password_jin, jenis_jin]

#F04
def hapusjin():
    """Bandung Bondowoso memiliki wewenang untuk menghapus jin.
    Fungsi menghapus jin dan candi yang dibuat oleh jin tersebut juga ikut terhapus."""
    global role
    global user
    global N_user
    global N_candi
    N_user = hitung_user()
    N_candi = hitung_candi()
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk menghapus jin!")
        return 0
    else:
        hapus_jin = input("Masukkan username jin : ")

        i = 0

        while i <= (N_user):
            if user[i][0] == hapus_jin:
                konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                if konfirmasi == "Y" or konfirmasi == 'y':
                    # Hapus jin
                    for i in range(1, N_user+1):
                        if user[i][0] == hapus_jin:
                            user[i] = "-"
                            for j in range(i, N_user+1):
                                user[j] = user[j+1]
                                if j == N_user:
                                    user[j] == "-"
                            break 
                    # Hapus candi jin
                    for i in range (N_candi+1):
                        if candi[i][1] == hapus_jin:
                            candi[i] = "-"
                            for j in range(i, N_candi+1):
                                candi[j] = candi[j+1]
                                if j == N_user:
                                    user[j] == "-"
                            break    
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    break
                else: # Konfirmasi == "N" or "n"
                    break
            elif i == (N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1

# F05
def ubahjin():
    """Bandung Bondowoso memiliki wewenang untuk mengubah tipe jin.
    Fungsi mengubah tipe jin yang sudah di summon"""
    global role
    global N_user
    global user
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk mengubah tipe jin!")
        return 0
    else:
        ingin_ubah = input("Masukkan username jin : ")
        
        i = 2
        while i <= (N_user):
            if user[i][0] == ingin_ubah:
                # Validasi jenis jin dan konfirmasi perubahan
                if user[i][2] == 'jin_pengumpul':
                    tipe = "Pengumpul"
                    konfirmasi = input(f"Jin ini bertipe “{tipe}”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        user[i][2] = 'jin_pembangun'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
                # Validasi jenis jin dan konfirmasi perubahan
                elif user[i][2] == 'jin_pembangun':
                    tipe = "Pembangun"
                    konfirmasi = input(f"Jin ini bertipe “{tipe}”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        user[i][2] = 'jin_pengumpul'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
            elif i == (N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1

#F06
def bangun():
    global role
    global bahan_bangunan
    global username
    global candi
    if role == "jin_pembangun":
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)
        if int(bahan_bangunan[1][2])- pasir < 0 or int(bahan_bangunan[2][2])- batu < 0 or int(bahan_bangunan[3][2])- air < 0:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:
            a = int(bahan_bangunan[1][2])
            a -= pasir
            b = int(bahan_bangunan[2][2])
            b -= batu
            c = int(bahan_bangunan[3][2])
            c -= air
            bahan_bangunan[1][2] = str(a)
            bahan_bangunan[2][2] = str(b)
            bahan_bangunan[3][2] = str(c)
            id_candi = tools.id_candi(candi)
            count_candi = hitung_candi()
            if count_candi<100:
                tools.write_array_candi(candi,id_candi,username,pasir,batu,air)
            print("Candi berhasil dibangun.")
            count_candi = hitung_candi()
            print(f"Sisa candi yang perlu dibangun: {100-count_candi}")

    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")
#F07
def kumpul():
      global bahan_bangunan
      global role
      if role == "jin_pengumpul":
            pasir = random.randint(0,5)
            batu = random.randint(0,5)
            air = random.randint(0,5)
            print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
            a = int(bahan_bangunan[1][2])
            a += pasir
            b = int(bahan_bangunan[2][2])
            b += batu
            c = int(bahan_bangunan[3][2])
            c += air
            bahan_bangunan[1][2] = str(a)
            bahan_bangunan[2][2] = str(b)
            bahan_bangunan[3][2] = str(c)
      else:
            print("Maaf anda tidak memiliki akses untuk fungsi tersebut")
#F08
def batchkumpul():
    global role
    global bahan_bangunan
    global candi
    if role == "bandung_bondowoso":
        count = 0
        i = 0
        while True:
            if user[i] != "-":
                if user[i][2] == "jin_pengumpul":
                    count += 1
            else:
                break
            i += 1
        pasir = 0
        batu = 0
        air = 0
        if count == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            for i in range(count):
                pasir += random.randint(0,5)
                batu += random.randint(0,5)
                air += random.randint(0,5)
            print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
            a = int(bahan_bangunan[1][2])
            a += pasir
            b = int(bahan_bangunan[2][2])
            b += batu
            c = int(bahan_bangunan[3][2])
            c += air
            bahan_bangunan[1][2] = str(a)
            bahan_bangunan[2][2] = str(b)
            bahan_bangunan[3][2] = str(c)
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")

def batchbangun():
    global role
    global bahan_bangunan
    if role == "bandung_bondowoso":
        count_jin_pembangun = hitung_jin_pembangun()
        pasir = 0
        batu = 0
        air = 0
        if count_jin_pembangun == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            beda_pasir = 0
            beda_batu = 0
            beda_air = 0
            arr_temp_bahan_bangunan = ["-" for i in range(count_jin_pembangun)]
            for i in range(count_jin_pembangun):
                temp_pasir = random.randint(1,5)
                temp_batu = random.randint(1,5)
                temp_air = random.randint(1,5)
                arr_temp_bahan_bangunan[i] = [str(temp_pasir),str(temp_batu),str(temp_air)]
                pasir += temp_pasir
                batu += temp_batu
                air += temp_air
            if int(bahan_bangunan[1][2])- pasir < 0 or int(bahan_bangunan[2][2])- batu < 0 or int(bahan_bangunan[3][2])- air < 0:
                print(f"Mengerahkan {count_jin_pembangun} jin untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, dan {air} air.")
                if int(bahan_bangunan[1][2])- pasir < 0:
                    beda_pasir = pasir - int(bahan_bangunan[1][2])
                if int(bahan_bangunan[1][2])- batu < 0:
                    beda_batu = batu - int(bahan_bangunan[1][2])
                if int(bahan_bangunan[1][2])- air < 0:
                    beda_air = air - int(bahan_bangunan[1][2])
                print(f"Bangun gagal. Kurang {beda_pasir} pasir, {beda_batu} batu, dan {beda_air} air.")
            else:
                a = int(bahan_bangunan[1][2])
                a -= pasir
                b = int(bahan_bangunan[2][2])
                b -= batu
                c = int(bahan_bangunan[3][2])
                c -= air
                bahan_bangunan[1][2] = str(a)
                bahan_bangunan[2][2] = str(b)
                bahan_bangunan[3][2] = str(c)
                count_candi = hitung_candi()
                if (100-count_candi) < count_jin_pembangun:
                    repetition = 100-count_candi
                else:
                    repetition = count_jin_pembangun
                arr_pembuat = ["-" for i in range(repetition)]
                flag = 0
                j = 0
                while (flag < repetition):
                    if user[j] != "-":
                        if user[j][2] == "jin_pembangun":
                            arr_pembuat[flag] = user[j][0]
                            flag +=1
                    j += 1
                for i in range(repetition):
                    pembuat = arr_pembuat[i]
                    pasir = arr_temp_bahan_bangunan[i][0]
                    batu = arr_temp_bahan_bangunan[i][1]
                    air = arr_temp_bahan_bangunan[i][2]
                    id_candi = tools.id_candi(candi)
                    tools.write_array_candi(candi,id_candi,pembuat,pasir,batu,air)
                if repetition < 0:
                    print(f"Jin berhasil membangun total 0 candi.")
                else:
                    print(f"Jin berhasil membangun total {repetition} candi.")
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")
#F09
def laporanjin():
    global role
    if role == "bandung_bondowoso":
        count_jin = hitung_jin_pembangun() + hitung_jin_pengumpul()
        print(f"> Total Jin:{count_jin}")
        count_jin_pengumpul = hitung_jin_pengumpul()
        print(f"> Total Jin Pengumpul:{count_jin_pengumpul}")
        count_jin_pembangun = hitung_jin_pembangun()
        print(f"> Total Jin Pembangun:{count_jin_pembangun}")
        if count_jin_pembangun == 0:
            print("> Jin Terajin: -")
            print("> Jin Termalas: -")
            print(f"> Jumlah Pasir: {bahan_bangunan[1][2]} unit")
            print(f"> Jumlah Air: {bahan_bangunan[2][2]} unit")
            print(f"> Jumlah Batu: {bahan_bangunan[3][2]} unit")
        else:
            arr_jin_jmlhcandi = ["-" for i in range(count_jin_pembangun)]
            idx_jin = 0
            i = 0
            while idx_jin<count_jin_pembangun:
                if i == 103:
                    break
                if user[i] != "-":
                    if user[i][2] == "jin_pembangun":
                        arr_jin_jmlhcandi[idx_jin] = [user[i][0],str(0)]
                        idx_jin += 1
                else:
                    break
                i += 1
            for x in range(count_jin_pembangun):
                j = 0
                pembuat = arr_jin_jmlhcandi[x][0]
                count_jmlh_candi = 0
                while True:
                    if j == 101:
                        break
                    if candi[j] != "-":
                        if candi[j][1] == pembuat:
                            count_jmlh_candi += 1
                    else:
                        break
                    j += 1
                arr_jin_jmlhcandi[x][1] = str(count_jmlh_candi)
            max_jmlh = arr_jin_jmlhcandi[0][1]
            max_pembuat = arr_jin_jmlhcandi[0][0]
            min_jmlh = arr_jin_jmlhcandi[0][1]
            min_pembuat = arr_jin_jmlhcandi[0][0]
            for i in range(count_jin_pembangun):
                if arr_jin_jmlhcandi[i][1] > max_jmlh:
                    max_jmlh = arr_jin_jmlhcandi[i][1]
                    max_pembuat = arr_jin_jmlhcandi[i][0]
                if arr_jin_jmlhcandi[i][1] == max_jmlh:
                    if arr_jin_jmlhcandi[i][0] < max_pembuat:
                        max_jmlh = arr_jin_jmlhcandi[i][1]
                        max_pembuat = arr_jin_jmlhcandi[i][0]
                if arr_jin_jmlhcandi[i][1] < min_jmlh:
                    min_jmlh = arr_jin_jmlhcandi[i][1]
                    min_pembuat = arr_jin_jmlhcandi[i][0]
                if arr_jin_jmlhcandi[i][1] == min_jmlh:
                    if arr_jin_jmlhcandi[i][0] > min_pembuat:
                        min_jmlh = arr_jin_jmlhcandi[i][1]
                        min_pembuat = arr_jin_jmlhcandi[i][0]
            print("> Jin Terajin:",max_pembuat)
            print("> Jin Termalas:",min_pembuat)
            print(f"> Jumlah Pasir: {bahan_bangunan[1][2]} unit")
            print(f"> Jumlah Air: {bahan_bangunan[2][2]} unit")
            print(f"> Jumlah Batu: {bahan_bangunan[3][2]} unit")
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")
#F10
def laporancandi():
    global candi
    if hitung_candi() == 0 :
        print("Total Candi: 0")
        print("Total Pasir yang digunakan: 0")
        print("Total Batu yang digunakan: 0")
        print("Total Air yang digunakan: 0")
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")
    else :
        print("Total Candi:",hitung_candi())
        
        jumlah_pasir = 0
        jumlah_air = 0
        jumlah_batu = 0
        termahal = 0
        termurah = 99999999999999999999999999
        id_termahal = 0
        id_termurah = 0
        i=1
        while True:
            if i == 101:
                print("Total Pasir yang digunakan:",jumlah_pasir)
                print("Total batu yang digunakan:",jumlah_batu)
                print("Total air yang digunakan:",jumlah_air)
                print(f"ID Candi Termahal: {id_termahal} (Rp {termahal})")
                print(f"ID Candi Termurah: {id_termurah} (Rp {termurah})")
                break
            if candi [i] == "-":
                print("Total Pasir yang digunakan:",jumlah_pasir)
                print("Total batu yang digunakan:",jumlah_batu)
                print("Total air yang digunakan:",jumlah_air)
                print(f"ID Candi Termahal: {id_termahal} (Rp {termahal})")
                print(f"ID Candi Termurah: {id_termurah} (Rp {termurah})")
                break
            else : 
                jumlah_pasir += int(candi[i][2])
                jumlah_batu += int(candi[i][3])
                jumlah_air += int(candi[i][4])

            if termahal < (int(candi [i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500 ):
                termahal = (int(candi [i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500 )
                id_termahal = candi[i][0]
            
            if termurah > (int(candi [i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500 ):
                termurah = (int(candi [i][2]) * 10000 + int(candi[i][3]) * 15000 + int(candi[i][4]) * 7500) 
                id_termurah = candi [i][0]
            i+=1
#F11
def hancurkancandi():
    global candi
    global role
    if role == "roro_jonggrang":
        id = input("Masukkan ID candi: ")
        yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
        blank_index = 0
        if yakin == "Y" :
            for i in range (101):
                if candi [i][0] == id :
                    candi [i]= "-"
                    for i in range (101):
                        if candi[i]==("-"):
                            blank_index = i
                            break
                    for i in range(blank_index+1 , 101):
                        candi[i - 1] = candi[i]
                        if i == 101:
                            candi[i-1] = '-'
                    return candi
                
            
            print("Tidak ada candi dengan ID tersebut.")
            return candi
                
        else : 
            print("Candi tidak jadi dihancurkan")
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")
        
#F12
def ayamberkokok ():
    if hitung_candi() <= 100 :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", hitung_candi())
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
    else :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", hitung_candi())
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()
#F13
def cari_folder(nama_folder):
    # {Fungsi ini mencari folder pada direktori}
    if nama_folder == None:
        print(f'Tidak ada nama folder yang diberikan!')
        exit()
    else:
        if os.path.exists(nama_folder):
            print("Loading...")
            print("Selamat datang di program “Manajerial Candi”")
            print("Silahkan masukkan username Anda")
            return(True)
        else: 
            print(f'\nFolder "{nama_folder}" tidak ditemukan.')
            exit()

def load():
    # Fungsi ini mengembalikan 
    # setup parser
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str, nargs="?") #positional argument
    args = parser.parse_args()
    
    valid = cari_folder(args.nama_folder)
    nama = args.nama_folder

    if valid:
        fUsers = data.f_users (os.path.join(nama, "user.csv"))
        fCandi = data.f_candi (os.path.join(nama, "candi.csv"))
        fBahan = data.f_bahan_bangunan (os.path.join(nama, "bahan_bangunan.csv"))

        return fUsers,fCandi,fBahan
    else:
        quit()

#F14
def save():
    global user
    global bahan_bangunan
    global candi
    folder = str(input("Masukkan nama folder :"))
    print("\nsaving...\n")

    ## prosedur mengecek data dan membuat folder
    path = "save/" + folder

    ## mengecek folder save
    if os.path.exists("save"):
        pass # folder save ada
        if os.path.exists(path):
            pass   #folder ada

        else: #folder tidak ada
            print(f"membuat folder {path}... \n")
            os.mkdir(path) # buat folder di dalam folder save

    else: # folder tidak ditemukan, maka membuat folder save
        print(f"membuat folder save...\n")
        os.mkdir("save") #membuat folder save
        print(f"membuat folder {path}...\n")
        os.mkdir(path) # membuat folder

    # menyimpan data array ke csv 
    tools.write_csv_user(f"{path}/user.csv",user)
    tools.write_csv_bahan_bangunan(f"{path}/bahan_bangunan.csv",bahan_bangunan)
    tools.write_csv_candi(f"{path}/candi.csv",candi)
    print(f"Berhasil menyimpan data di folder {path}")

#F15
def help () :
    global role
    print("=========== HELP ===========")
    if role == "" :
        print ('1. login',"\nUntuk masuk menggunakan akun")
        print ('2. exit',"\nUntuk keluar dari program dan kembali ke terminal")
        print ("3. save","\n menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
    elif role == "bandung_bondowoso" :
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. summonjin',"\nUntuk memanggil jin ")
        print ('3. hapusjin',"\nUntuk menghapus jin yang telah di summon")
        print ('4. ubahjin',"\nUntuk mengubah tipe jin ")
        print ('5. batchkumpul',"\nUntuk menyuruh jin mengumpulkan bahan baku candi ")
        print ('6. batchbangun',"\nUntuk menyuruh jin membangun candi ")
        print ('7. laporanjin',"\nUntuk mengetahui kinerja, jumlah jin , username jin terajin dan termalas dari para jin ")
        print ('8. laporancandi',"\nuntuk mengetahui progress pembangunan candi ")
        print ("9. save","\n menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
    elif role == "roro_jonggrang":
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. hancurkancandi','\nuntuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso')
        print ('3. ayamberkokok','\nuntuk menyelesaikan permainan dengan memalsukan pagi hari')
        print ("4. save","\n menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
    elif role == "jin_pengumpul" :
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. kumpul','\nuntuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi')
        print ("3. save","\n menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
    elif role =='jin_pembangun':
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. bangun','\nuntuk membangun candi')
        print ("3. save","\n menyimpan data yang berada di program sesuai dengan struktur data eksternal.")
#F16
def exit():
    flag_exit = False
    while flag_exit != True :
        input_save = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"))
        if input_save =="Y" or input_save == "y":
            save()
            flag_exit = True 
        elif input_save =="N" or input_save == "n":
            print("tidak save")
            flag_exit = True
    print("Terima kasih dan sampai jumpa kembali... :)")
    quit()

def hitung_candi ():
    global candi
    count_candi = -1
    for i in range(101):
        if candi[i] != "-" :
            count_candi += 1 
    return count_candi
    
def hitung_user ():
    global user
    count_user = -1
    for i in range(103):
        if user[i] != "-" :
            count_user += 1
    return count_user

def hitung_jin_pembangun():
    global user
    count_jin_pembangun = 0
    for i in range(103):
        if user[i] == "-":
            return count_jin_pembangun
        if user[i][2] == "jin_pembangun" :
            count_jin_pembangun += 1
    return count_jin_pembangun

def hitung_jin_pengumpul():
    global user
    count_jin_pengumpul = 0
    for i in range(103):
        if user[i] == "-":
            return count_jin_pengumpul
        if user[i][2] == "jin_pengumpul" :
            count_jin_pengumpul += 1
    return count_jin_pengumpul

def cek():
    print(user)
    print(bahan_bangunan)
    print(candi)
    print(username)
    print(role)
    print(f"banyak user {hitung_user()}")
    print(f"banyak candi {hitung_candi()}")
    

def run(fungsi):
    if fungsi == "login":
        login()
    if fungsi == "logout":
        logout()
    if fungsi == "summonjin":
        summonjin()
    if fungsi == "bangun":
        bangun ()
    if fungsi == "kumpul":
        kumpul ()
    if fungsi == "ubahjin":
        ubahjin()
    if fungsi == "batchkumpul":
        batchkumpul ()
    if fungsi == "batchbangun":
        batchbangun ()
    if fungsi == "help":
        help ()
    if fungsi == "save":
        save ()
    if fungsi == "ayamberkokok":
        ayamberkokok ()
    if fungsi == "hapusjin":
        hapusjin ()
    if fungsi == "hancurkancandi":
        hancurkancandi ()
    if fungsi == "laporanjin":
        laporanjin ()
    if fungsi == "laporancandi":
        laporancandi ()
    if fungsi == "exit":
        exit()
    if fungsi == "cek":
        cek()