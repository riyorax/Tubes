def hitung (arr_candi):
    count_candi = 0 
    i = 0
    while True :
        if arr_candi[i] != "-" :
            count_candi += 1 
            i += 1
        else :
            return count_candi
def laporancandi(arr_candi):
    if hitung == 0 :
        print("Total Candi: 0")
        print("Total Pasir yang digunakan: 0")
        print("Total Batu yang digunakan: 0")
        print("Total Air yang digunakan: 0")
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")
    else :
        print("Total Candi:",hitung)
        
        jumlah_pasir = 0
        jumlah_air = 0
        jumlah_batu = 0
        termahal = 0
        termurah = 99999999999999999999999999
        id_termahal = 0
        id_termurah = 0
        i=1
        while True:
            if arr_candi [i] == "-":
                print("Total Pasir yang digunakan:",jumlah_pasir)
                print("Total batu yang digunakan:",jumlah_batu)
                print("Total air yang digunakan:",jumlah_air)
                print(f"ID Candi Termahal: {id_termahal} (Rp {termahal})")
                print(f"ID Candi Termurah: {id_termurah} (Rp {termurah})")
                break
            else : 
                jumlah_pasir += arr_candi[i][2]
                jumlah_batu += arr_candi[i][3]
                jumlah_air += arr_candi[i][4]

            if termahal < (arr_candi [i][2] * 10000 + arr_candi[i][3] * 15000 + arr_candi[i][4] * 7500 ):
                termahal = (arr_candi [i][2] * 10000 + arr_candi[i][3] * 15000 + arr_candi[i][4] * 7500 )
                id_termahal = arr_candi[i][0]
            
            if termurah > (arr_candi [i][2] * 10000 + arr_candi[i][3] * 15000 + arr_candi[i][4] * 7500 ):
                termurah = (arr_candi [i][2] * 10000 + arr_candi[i][3] * 15000 + arr_candi[i][4] * 7500 )
                id_termurah = arr_candi [i][0]