import typing
import random
import tools
import F07
import F06

role = ["*" for i in range(103)]
bahan_bangunan = [['pasir', 'sand', '0'], ['batu', 'stone', '0'], ['air', 'water', '0']]
candi = ["*" for i in range(101)]



while True:
    funct = input("pilih fungsi")
    if funct == "6":
      F06.jin_pembangun("bahan_bangunan.csv","candi.csv",bahan_bangunan,candi,"asep123","asep")
    else:
      F07.jin_pengumpul(bahan_bangunan)
    a = input("continue?")
    if a == "n":
        break