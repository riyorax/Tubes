import random
import tools

bahan_bangunan = [['pasir', 'sand', '0'], ['batu', 'stone', '0'], ['air', 'water', '0']]
def jin_pengumpul(array):
      pasir = random.randint(0,5)
      batu = random.randint(0,5)
      air = random.randint(0,5)
      print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
      a = int(array[0][2])
      a += pasir
      b = int(array[1][2])
      b += batu
      c = int(array[2][2])
      c += air
      array[0][2] = str(a)
      array[1][2] = str(b)
      array[2][2] = str(c)
      tools.write_csv_bahan_bangunan("bahan_bangunan.csv",array)