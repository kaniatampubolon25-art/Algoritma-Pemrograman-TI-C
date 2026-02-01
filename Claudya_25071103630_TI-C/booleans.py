# Program menentukan pemberian akses berdasarkan umur minimal

usia_minimal = 21
input_usia = int(input("Masukkan usia : ")) # input dari user
diberi_akses = input_usia >= usia_minimal # penggunaan boolean untuk mengecek data

print(f"Status akses : {diberi_akses}")

if diberi_akses :
    print("Halo! Selamat datang.")
else :
    print("Maaf, anda belum memenuhi batas usia.")
