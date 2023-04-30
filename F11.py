def hancurkancandi(arr_candi):
    id = int(input("Masukkan ID candi: "))
    yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
    i = 0 
    while True :
        if arr_candi [i][0] == id :
            arr_candi [i]= [0,0,0,0,0]
            return arr_candi
        if arr_candi [i] == "-" :
            print("Tidak ada candi dengan ID tersebut.")
            return arr_candi
