import list_data as data

role = 'bandung_bondowoso' ### ini buat test case

def ubah_tipe_jin():
    """Bandung Bondowoso memiliki wewenang untuk mengubah tipe jin.
    Fungsi mengubah tipe jin yang sudah di summon"""

    global role
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk summon jin!")
        return 0
    else:
        print(">>> ubahjin") ### ini buat test case
        ingin_ubah = input("Masukkan username jin : ")
        
        i = 2
        while i <= (data.N_user):
            if data.users[i][0] == ingin_ubah:
                # Validasi jenis jin dan konfirmasi perubahan
                if data.users[i][2] == 'Pengumpul':
                    konfirmasi = input(f"Jin ini bertipe “{data.users[i][2]}”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        data.users[i][2] = 'Pembangun'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
                # Validasi jenis jin dan konfirmasi perubahan
                elif data.users[i][2] == 'Pembangun':
                    konfirmasi = input(f"Jin ini bertipe “{data.users[i][2]}”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                    if konfirmasi == "Y" or konfirmasi == "y":
                        data.users[i][2] = 'Pengumpul'
                        print("Jin telah berhasil diubah.")
                        break
                    else:
                        print("Batal mengubah tipe jin")
                        break
            elif i == (data.N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1

ubah_tipe_jin()
data.cetak(data.users) ### buat test case

### artinya hanya buat test case dan akan dihapus di main branch agar program berjalan sesuai spesifikasi