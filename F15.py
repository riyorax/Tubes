# from list_data import *
def help () :
    global role
    print("=========== HELP ===========")
    if role == "" :
        print ('1. login',"\nUntuk masuk menggunakan akun")
        print ('2. exit',"\nUntuk keluar dari program dan kembali ke terminal")
        print ("3. save","\nmenyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print ('4. help','\nmenampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain')
    elif role == "bandung_bondowoso" :
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. summonjin',"\nUntuk memanggil jin ")
        print ('3. hapusjin',"\nUntuk menghapus jin yang telah di summon")
        print ('4. ubahjin',"\nUntuk mengubah tipe jin ")
        print ('5. batchkumpul',"\nUntuk menyuruh jin mengumpulkan bahan baku candi ")
        print ('6. batchbangun',"\nUntuk menyuruh jin membangun candi ")
        print ('7. laporanjin',"\nUntuk mengetahui kinerja, jumlah jin , username jin terajin dan termalas dari para jin ")
        print ('8. laporancandi',"\nuntuk mengetahui progress pembangunan candi ")
        print ("9. save","\nmenyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print ('10. help','\nmenampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain')
        print ('11. exit',"\nUntuk keluar dari program dan kembali ke terminal")
    elif role == "roro_jonggrang":
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. hancurkancandi','\nuntuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso')
        print ('3. ayamberkokok','\nuntuk menyelesaikan permainan dengan memalsukan pagi hari')
        print ("4. save","\nmenyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print ('5. help','\nmenampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain')
        print ('6. exit',"\nUntuk keluar dari program dan kembali ke terminal")
    elif role == "jin_pengumpul" :
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. kumpul','\nuntuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi')
        print ("3. save","\nmenyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print ('4. help','\nmenampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain')
        print ('5. exit',"\nUntuk keluar dari program dan kembali ke terminal")
    elif role =='jin_pembangun':
        print ('1. logout',"\nUntuk keluar dari akun yang digunakan sekarang  ")
        print ('2. bangun','\nuntuk membangun candi')
        print ("3. save","\nmenyimpan data yang berada di program sesuai dengan struktur data eksternal.")
        print ('4. help','\nmenampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain')
        print ('5. exit',"\nUntuk keluar dari program dan kembali ke terminal")
