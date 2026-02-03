#pertama membuat fungsi bernama hitung yang menerima dua parameter yaitu a dan b

def hitung(a,b):
    #lalu buat variabel penjumlahan dan pengurangan yang menyimpan hasil dari penjumlahan dan pengurangan dari a dan b
    penjumlahan = a + b
    pengurangan = a - b

    #lalu kembalikan dua nilai dari variabel penjumlahan dan pengurangan menggunakan return
    return penjumlahan, pengurangan

#lalu panggil fungsi hitung dengan nilai a=5 dan b=3

hasil_penjumlahan, hasil_pengurangan = hitung(5, 3)

#terakhir tampilkan hasilnya ke layar menggunakan print()
print('penjuumlahan =', hasil_penjumlahan)
print('pengurangan =', hasil_pengurangan)