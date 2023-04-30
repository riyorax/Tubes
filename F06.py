import random
import tools

def jin_pembangun(arr_bahan_bangunan,arr_candi,pembuat):
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    array = tools.csv_array_bahan_bangunan("bahan_bangunan.csv",arr_bahan_bangunan)
    if int(arr_bahan_bangunan[1][2])- pasir < 0 or int(arr_bahan_bangunan[2][2])- batu < 0 or int(arr_bahan_bangunan[3][2])- air < 0:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    else:
        a = int(arr_bahan_bangunan[1][2])
        a -= pasir
        b = int(arr_bahan_bangunan[2][2])
        b -= batu
        c = int(arr_bahan_bangunan[3][2])
        c -= air
        arr_bahan_bangunan[0][2] = str(a)
        arr_bahan_bangunan[1][2] = str(b)
        arr_bahan_bangunan[2][2] = str(c)
        id_candi = tools.id_candi(arr_candi)
        flag = False
        for i in range(101):
            if arr_candi[i] == "-":
                flag = True
        if flag:
            tools.write_array_candi(arr_candi,id_candi,pembuat,pasir,batu,air)