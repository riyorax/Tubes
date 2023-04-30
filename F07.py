import random
# from list_data import *

def kumpul():
      global bahan_bangunan
      global role
      if role == "jin_pengumpul":
            pasir = random.randint(0,5)
            batu = random.randint(0,5)
            air = random.randint(0,5)
            print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
            a = int(bahan_bangunan[1][2])
            a += pasir
            b = int(bahan_bangunan[2][2])
            b += batu
            c = int(bahan_bangunan[3][2])
            c += air
            bahan_bangunan[1][2] = str(a)
            bahan_bangunan[2][2] = str(b)
            bahan_bangunan[3][2] = str(c)
      else:
            print("Maaf anda tidak memiliki akses untuk fungsi tersebut")