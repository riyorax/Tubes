import tools
# from list_data import *


def ayamberkokok ():
    global candi
    if tools.hitung_candi(candi) < 100 :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", tools.hitung_candi(candi))
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
    else :
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: ", tools.hitung_candi(candi))
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()