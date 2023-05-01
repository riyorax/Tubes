import tools

user = []
N_user = 3
N_candi = 0

def f_users(file_users):
    users = [['', '', ''] for i in range(103)]
    users = tools.csv_array_user(file_users, users)
    return users

def f_candi(file_candi):
    candi = [['', '', '', '', ''] for i in range(101)]
    candi = tools.csv_array_candi(file_candi, candi)
    return candi

def f_bahan_bangunan(file_bahan_bangunan):
    bahan_bangunan = [['', '', ''] for i in range(4)]
    bahan_bangunan = tools.csv_array_bahan_bangunan(file_bahan_bangunan, bahan_bangunan)
    return bahan_bangunan

def cetak(arr):
    for i in arr:
        print(i)