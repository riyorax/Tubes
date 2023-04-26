def exit():
    flag_exit = False
    while flag_exit != True :
        input_save = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"))
        if input_save in ['Y','y']:
            print("save") # masukin fungsi save disini
            flag_exit = True 
        elif input_save in ['N','n']:
            print("tidak save")
            flag_exit = True
    print("Terima kasih dan sampai jumpa kembali... :)")
