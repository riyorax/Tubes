import list_data as data

def hapusjin():
    """Bandung Bondowoso memiliki wewenang untuk menghapus jin.
    Fungsi menghapus jin dan candi yang dibuat oleh jin tersebut juga ikut terhapus."""
    global role
    if (not(role =='bandung_bondowoso')):
        print("Anda tidak memiliki wewenang untuk menghapus jin!")
        return 0
    else:
        hapus_jin = input("Masukkan username jin : ")

        i = 0

        while i <= (data.N_user):
            if data.user[i][0] == hapus_jin:
                konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                if konfirmasi == "Y" or konfirmasi == 'y':
                    # Hapus jin
                    for i in range(1, data.N_user+1):
                        if data.user[i][0] == hapus_jin:
                            data.user[i] = "-"
                            for j in range(i, data.N_user):
                                data.user[j] = data.user[j+1]
                            break 
                    # Hapus candi jin
                    for i in range (data.N_candi):
                        if data.user[i][1] == hapus_jin:
                            data.user[i] = "-"
                            for j in range(i, data.N_user):
                                data.user[j] = data.user[j+1]
                            break    
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    break
                else: # Konfirmasi == "N" or "n"
                    break
            elif i == (data.N_user):
                print("Tidak ada jin dengan username tersebut.")
                break
            else:
                i += 1

# [[asep,asep,jin_..],[asep,asep,jin_..],[asep,asep,jin_..],"-",["-","-","-"],]
# [[asep,asep,jin_..],[asep,asep,jin_..],[asep,asep,jin_..],"-","-","-","-"]
# [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'], ['asep1', 'asepo123', 'jin_pembangun'], ['asep2', 'asepo123', 'jin_pembangun'], ['asep3', 'asepo123', 'jin_pembangun'], ['asep4', 'asepo123', 'jin_pembangun'], ['asep5', 'asepo123', 'jin_pengumpul'], ['asep6', 'asepo123', 'jin_pengumpul'], ['asep7', 'asepo123', 'jin_pengumpul'], ['asep8', 'asepo123', 'jin_pengumpul'], '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']