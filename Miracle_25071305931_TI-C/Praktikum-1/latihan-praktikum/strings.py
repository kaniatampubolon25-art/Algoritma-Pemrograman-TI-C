# strings.py

# membuat string
teks = "python"
print(teks)

# akses karakter
print(teks[0])

# panjang string
print(len(teks))

# Loop string
for huruf in teks:
    print(huruf)

# cek kata
print ("py" in teks)

# Slicing
print(teks[1:4])

# Modifikasi string
print(teks.upper())
print(teks.lower())
print(teks.replace("p","j"))

# format string
umur = 18
print(f"umur saya {umur} tahun")