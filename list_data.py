import tools

role = ""
username = ""
role = ""
username = ""
role = ["-" for i in range(103)] # Panjang array sebanyak 103 karena maximal jin adalah 100 dan terdapat 3 line bawaan untuk header, bondowoso dan roro
bahan_bangunan = ["-" for i in range(4)] # Panjang array 4 untuk satu line untuk header dan 3 lagi untuk bahan bangunan
candi = ["-" for i in range(101)] # Panjang array 101 karena maximal 100 candi dan satu line untuk header

tools.csv_array_user("user.csv",role)
tools.csv_array_bahan_bangunan("bahan_bangunan.csv",bahan_bangunan)
tools.csv_array_candi("candi.csv",candi)

users = tools.csv_array_user("user.csv", role)
N_user = 2
candi = tools.csv_array_candi("candi.csv", candi)
N_candi = 0
bahan_bangunan = tools.csv_array_bahan_bangunan("bahan_bangunan.csv", bahan_bangunan)

def cetak(arr):
    for i in arr:
        print(i)