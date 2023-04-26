import tools

user = []

users = [['', '', ''] for i in range(103)]
candi = [['', '', '', '', ''] for i in range(101)]
bahan_bangunan = [['', '', ''] for i in range(4)]

users = tools.csv_array_user("user.csv", users)
N_user = 2
candi = tools.csv_array_candi("candi.csv", candi)
N_candi = 0
bahan_bangunan = tools.csv_array_bahan_bangunan("bahan_bangunan.csv", bahan_bangunan)

def cetak(arr):
    for i in arr:
        print(i)