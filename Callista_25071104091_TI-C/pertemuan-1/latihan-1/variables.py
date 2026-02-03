#cara mendeklarasikan variable
apple=10
#lalu menampilkan nya
print(apple)
#kita bisa merubah tipe data dan isinya kapan saja nanti
apple="enak"
print(apple)
#kita juga bisa mentukan tipe datanya seperti ini
apple=float(3)
print(apple)
#kita bisa mengetahui tipe datanya seperti ini
print(type(apple))

#Camel case
appleEnak=11
#Pascal case
AppleEnak=20
#Snake Case
apple_enak=35


#MULTIPLE VALUE
a,b,c='apel', 'sangat', 'enak'
print(a,b,c)
#MULTIPLE VARIABLES ONE VALUE
A=B=C='APPLE SANGAT ENAKK'
print(A,B,C)
x = "The best fruit ever"

def myfunc():
  print("Apple is " + x)

myfunc()
#kita bisa memakai variabel global dalam fungsi
x = "The best fruit"

def myfunc():
  x = "The best fruit ever"
  print("Apple is " + x)

myfunc()

print("Apple is " + x)
#Jika di dalam fungsi punya variabel yang sama, fungsi akan memakai variabel yang ada di dalamnya
def myfunc():
  global x
  x = "Delicious"

myfunc()

print("Apple is " + x)
#kita juga bisa mendeklarasikan variable dari dalam fungsi juga seperti ini