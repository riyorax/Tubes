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
            if data.users[i][0] == hapus_jin:
                konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                if konfirmasi == "Y" or konfirmasi == 'y':
                    # Hapus jin
                    for i in range(1, data.N_user+1):
                        if data.users[i][0] == hapus_jin:
                            data.users[i] = ['', '', '']
                            for j in range(i, data.N_user):
                                data.users[j] = data.users[j+1]
                            break 
                    # Hapus candi jin
                    for i in range (data.N_candi):
                        if data.users[i][1] == hapus_jin:
                            data.users[i] = ['', '', '','','']
                            for j in range(i, data.N_user):
                                data.users[j] = data.users[j+1]
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
                
[['id', 'pembuat', 'pasir', 'batu', 'air'], ['1', 'd', '5', '4', '3'], ['2', 'u', '2', '1', '3'], ['3', 'n', '5', '2', '4'], ['4', 'g', '3', '4', '3'], '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
[['id', 'pembuat', 'pasir', 'batu', 'air'], ['1', 'd', '5', '4', '3'], ['2', 'u', '2', '1', '3'], ['3', 'n', '5', '2', '4'], ['4', 'g', '3', '4', '3'], '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']