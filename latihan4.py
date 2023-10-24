# fungsi jumlah total
def jumlah_total(daftar_angka, pemisah):
    total = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            total += angka
    return total
 
a = jumlah_total(daftar_angka=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pemisah=2)
print("Jumlah total angka dalam list yang habis dibagi pemisah adalah", a)

b = jumlah_total(daftar_angka=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pemisah=3)
print("Jumlah total angka dalam list yang habis dibagi pemisah adalah", b)
