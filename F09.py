import tools

user = ["-" for i in range(103)]
tools.csv_array_user("user.csv",user)
bahan_bangunan = ["-" for i in range(4)]
tools.csv_array_bahan_bangunan("bahan_bangunan.csv",bahan_bangunan)
candi = ["-" for i in range(101)]
tools.csv_array_candi("candi.csv",candi)

def ambil_laporan_jin(arr_user,arr_candi):
    count_jin = 0
    i = 0
    while True:
        if arr_user[i] != "-":
            if arr_user[i][2] == "jin_pengumpul" or arr_user[i][2] == "jin_pembangun":
                count_jin += 1
        else:
            break
        i += 1
    print(f"> Total Jin:{count_jin}")
    count_jin_pengumpul = 0
    i = 0
    while True:
        if arr_user[i] != "-":
            if arr_user[i][2] == "jin_pengumpul":
                count_jin_pengumpul += 1
        else:
            break
        i += 1
    print(f"> Total Jin Pengumpul:{count_jin_pengumpul}")
    count_jin_pembangun = 0
    i = 0
    while True:
        if arr_user[i] != "-":
            if arr_user[i][2] == "jin_pembangun":
                count_jin_pembangun += 1
        else:
            break
        i += 1
    print(f"> Total Jin Pembangun:{count_jin_pembangun}")
    if count_jin_pembangun == 0:
        print("> Jin Terajin: -")
        print("> Jin Termalas: -")
    else:
        arr_jin_jmlhcandi = ["-" for i in range(count_jin_pembangun)]
        idx_jin = 0
        i = 0
        while idx_jin<count_jin_pembangun:
            if arr_user[i] != "-":
                if arr_user[i][2] == "jin_pembangun":
                    arr_jin_jmlhcandi[idx_jin] = [arr_user[i][0],0]
                    idx_jin += 1
            else:
                break
            i += 1
        for x in range(4):
            j = 0
            pembuat = arr_jin_jmlhcandi[x][0]
            count_jmlh_candi = 0
            while True:
                if arr_candi[j] != "-":
                    if arr_candi[j][1] == pembuat:
                        count_jmlh_candi += 1
                else:
                    break
                j += 1
            arr_jin_jmlhcandi[x][1] = count_jmlh_candi
        max_jmlh = arr_jin_jmlhcandi[0][1]
        max_pembuat = arr_jin_jmlhcandi[0][0]
        min_jmlh = arr_jin_jmlhcandi[0][1]
        min_pembuat = arr_jin_jmlhcandi[0][0]
        for i in range(count_jin_pembangun):
            if arr_jin_jmlhcandi[i][1] > max_jmlh:
                if arr_jin_jmlhcandi[i][0] < max_pembuat:
                    max_jmlh = arr_jin_jmlhcandi[i][1]
                    max_pembuat = arr_jin_jmlhcandi[i][0]
            if arr_jin_jmlhcandi[i][1] < min_jmlh:
                if arr_jin_jmlhcandi[i][0] > min_pembuat:
                    min_jmlh = arr_jin_jmlhcandi[i][1]
                    min_pembuat = arr_jin_jmlhcandi[i][0]
        print(max_pembuat)
        print(min_pembuat)
        
print(user)
print(candi)
ambil_laporan_jin(user,candi)