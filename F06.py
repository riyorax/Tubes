import random
import tools

def jin_pembangun(file1,file2,array1,array2,id,pembuat):
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    array = tools.csv_array_bahan_bangunan("bahan_bangunan.csv",array1)
    if int(array1[0][2])- pasir < 0 or int(array1[1][2])- batu < 0 or int(array1[2][2])- air < 0:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    else:
        a = int(array1[0][2])
        a -= pasir
        b = int(array1[1][2])
        b -= batu
        c = int(array1[2][2])
        c -= air
        array[0][2] = str(a)
        array[1][2] = str(b)
        array[2][2] = str(c)
        tools.write_csv_candi(file2,array2,id,pembuat,pasir,batu,air)
        tools.write_csv_bahan_bangunan(file1,array1)