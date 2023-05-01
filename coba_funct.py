
from list_data import *
import os
import tools

def save(arr_user,arr_bahan_bangunan,arr_candi):
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
    tools.write_csv_user(f"{folder}/user.csv",arr_user)
    tools.write_csv_bahan_bangunan(f"{folder}/bahan_bangunan.csv",arr_bahan_bangunan)
    tools.write_csv_candi(f"{folder}/candi.csv",arr_candi)
    print(f"Berhasil menyimpan data di folder {path}")

def save1():
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
    f = open(f"{path}/aa.txt",'w')
    f.write("-adfasf--")
    f.close()
    print(f"Berhasil menyimpan data di folder {path}")
save1()