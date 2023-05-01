import tools

user = ["-" for i in range(103)]
candi = ["-" for i in range(101)]
bahan_bangunan = ["-" for i in range(4)]
N_user = 3
N_candi = 0
role = ""
username = ""

def f_users(file_users):
    global user
    user = tools.csv_array_user(file_users, user)
    return user

def f_candi(file_candi):
    global candi
    candi = tools.csv_array_candi(file_candi, candi)
    return candi

def f_bahan_bangunan(file_bahan_bangunan):
    global bahan_bangunan
    bahan_bangunan = tools.csv_array_bahan_bangunan(file_bahan_bangunan, bahan_bangunan)
    return bahan_bangunan

def cetak(arr):
    for i in arr:
        print(i)