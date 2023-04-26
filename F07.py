import random
# import tools
# bahan_bangunan = ["-" for i in range(4)]
# tools.csv_array_bahan_bangunan("bahan_bangunan.csv",bahan_bangunan)

def jin_pengumpul(array):
      pasir = random.randint(0,5)
      batu = random.randint(0,5)
      air = random.randint(0,5)
      print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
      a = int(array[1][2])
      a += pasir
      b = int(array[2][2])
      b += batu
      c = int(array[3][2])
      c += air
      array[1][2] = str(a)
      array[2][2] = str(b)
      array[3][2] = str(c)

# jin_pengumpul(bahan_bangunan)
# print(bahan_bangunan)