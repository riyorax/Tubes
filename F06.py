import random
import tools
# from list_data import *

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
            count_candi = tools.hitung_candi
            if count_candi<100:
                tools.write_array_candi(candi,id_candi,username,pasir,batu,air)
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-count_candi}")

    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")