from list_data import *
def hancurkancandi():
    global candi
    id = int(input("Masukkan ID candi: "))
    yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
    i = 0 
    while True :
        if candi [i][0] == id :
            candi [i]= [0,0,0,0,0]
            return candi
        if candi [i] == "-" :
            print("Tidak ada candi dengan ID tersebut.")
            return candi
