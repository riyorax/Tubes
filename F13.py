import argparse
import os
from list_data import *
import list_data as data


def cari_folder(nama_folder):
    # {Fungsi ini mencari folder pada direktori}
    if nama_folder == None:
        print(f'Tidak ada nama folder yang diberikan!')
        exit()
    else:
        if os.path.exists(nama_folder):
            print("Loading...")
            print("Selamat datang di program “Manajerial Candi”")
            print("Silahkan masukkan username Anda")
            return(True)
        else: 
            print(f'\nFolder "{nama_folder}" tidak ditemukan.')
            exit()

def load():
    # Fungsi ini mengembalikan 
    # setup parser
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str, nargs="?") #positional argument
    args = parser.parse_args()
    
    valid = cari_folder(args.nama_folder)
    nama = args.nama_folder

    if valid:
        fUsers = data.f_users (os.path.join(nama, "user.csv"))
        fCandi = data.f_candi (os.path.join(nama, "candi.csv"))
        fBahan = data.f_bahan_bangunan (os.path.join(nama, "bahan_bangunan.csv"))

        return fUsers,fCandi,fBahan
    else:
        exit()
 
# Cek
# load()