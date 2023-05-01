from F14 import *

def exit():
    flag_exit = False
    while flag_exit != True :
        input_save = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"))
        if input_save =="Y" or input_save == "y":
            save()
            flag_exit = True 
        elif input_save =="N" or input_save == "n":
            print("tidak save")
            flag_exit = True
    print("Terima kasih dan sampai jumpa kembali... :)")
    quit()