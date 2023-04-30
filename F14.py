import os
import tools

def save(arr_user,arr_bahan_bangunan,arr_candi):
    folder = str(input("Masukkan nama folder :"))
    ## prosedur mengecek data dan membuat folder
    path = folder
    print(path)
    if os.path.exists(path): # Jika folder ada
        pass
    else: # folder tidak ditemukan, maka membuat folder
        os.makedirs(path)

    # menyimpan data array ke csv 
    print("saving...")
    tools.write_csv_user(f"{folder}/user.csv",arr_user)
    tools.write_csv_bahan_bangunan(f"{folder}/bahan_bangunan.csv",arr_bahan_bangunan)
    tools.write_csv_candi(f"{folder}/candi.csv",arr_candi)
    print(f"Berhasil menyimpan data di folder {folder}")
    #f = open(f"{folder}/aa.txt",'w')
    #f.write("asdasda")
    #f.close()
