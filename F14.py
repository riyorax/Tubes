import os
import tools
# from list_data import *

def save():
    global role
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
    tools.write_csv_user(f"{folder}/user.csv",role)
    tools.write_csv_bahan_bangunan(f"{folder}/bahan_bangunan.csv",bahan_bangunan)
    tools.write_csv_candi(f"{folder}/candi.csv",candi)
    print(f"Berhasil menyimpan data di folder {path}")
