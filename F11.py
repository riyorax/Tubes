def hancurkancandi(arr_candi):
    id = input("Masukkan ID candi: ")
    yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
    blank_index = 0
    if yakin == "Y" :
        for i in range (101):
            if arr_candi [i][0] == id :
                arr_candi [i]= "-"
                for i in range (101):
                    if arr_candi[i]==("-"):
                        blank_index = i
                        break
                for i in range(blank_index+1 , 101):
                    arr_candi[i - 1] = arr_candi[i]
                    if i == 101:
                        arr_candi[i-1] = '-'    
       
                return arr_candi
            
        
        print("Tidak ada candi dengan ID tersebut.")
        return arr_candi
            
    else : 
        print("Candi tidak jadi dihancurkan")

