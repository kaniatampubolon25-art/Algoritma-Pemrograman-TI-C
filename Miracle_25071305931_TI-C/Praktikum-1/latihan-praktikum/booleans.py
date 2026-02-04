# booleans.py

# perbandingan
print(10 > 9)     # True
print(10 == 9)    # False
print(10 < 9)     # False
 
# if statement
a = 200
b = 33

if a > b:
    print("a lebih besar daripada b")

# evaluasi nilai dengan bool()
print(bool("Hello"))    # True
print(bool(15))         # True

# nilai yang bernilai false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# fungsi yang mengembalikan boolean
def my_function():
    return True

print(my_function())