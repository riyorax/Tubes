import tools
import random
from list_data import *

def batchkumpul():
    if role == "bandung_bondowoso":
        count = 0
        i = 0
        while True:
            if role[i] != "-":
                if role[i][2] == "jin_pengumpul":
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
    if role == "bandung_bondowoso":
        count_jin_pembangun = 0
        i = 0
        while True:
            if role[i] != "-":
                if role[i][2] == "jin_pembangun":
                    count_jin_pembangun += 1
            else:
                break
            i += 1
        pasir = 0
        batu = 0
        air = 0
        if count_jin_pembangun == 0:
            print("Kumpul gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
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
                bahan_bangunan[0][2] = str(a)
                bahan_bangunan[1][2] = str(b)
                bahan_bangunan[2][2] = str(c)
                count_candi = 0
                i = 0
                while True:
                    if role[i] != "-":
                        count_candi += 1
                    else:
                        break
                    i += 1
                if (100-count_candi) < count_jin_pembangun:
                    repetition = 100-count_candi
                else:
                    repetition = count_jin_pembangun
                arr_pembuat = ["-" for i in range(repetition)]
                flag = 0
                j = 0
                while (flag < repetition):
                    if role[j] != "-":
                        if role[j][2] == "jin_pembangun":
                            arr_pembuat[flag] = role[j][0]
                            flag +=1
                    j += 1
                for i in range(repetition):
                    pembuat = arr_pembuat[i]
                    pasir = arr_temp_bahan_bangunan[i][0]
                    batu = arr_temp_bahan_bangunan[i][1]
                    air = arr_temp_bahan_bangunan[i][2]
                    id_candi = tools.id_candi(candi)
                    print(id_candi)
                    tools.write_array_candi(candi,id_candi,pembuat,pasir,batu,air)
    else:
        print("Maaf anda tidak memiliki akses untuk fungsi tersebut")