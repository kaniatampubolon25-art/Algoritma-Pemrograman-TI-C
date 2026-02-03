#Kita bisa menggunakan tanda petik dalam string selama tanda petiknya berbeda seperti ini
print("aku suka 'apel'.")
#Kita bisa print kalimat beberapa baris dengan menggunakan tanda petik sebanyak 3 kali
#String adalah array, jadi kita bisa mengakses nya melalui indek seperti ini
Apel="enak"
print(Apel[0])
#Kita juga bisa melakukan perulangan seperti ini
for x in Apel:
    print(x)
#Kita bisa mengetahui panjang string dengan cara seperti ini
print(len(Apel))
#Dan kita bisa mengetahui apakah kata yang kita inginkan ada di dalam string menggunakan ini
print("enak" in Apel)
print(Apel.upper())
a = "Apel itu  Enak!"
b = a.split("itu")
print(b)
print(Apel.lower())
print(Apel.replace('n', 'a'))