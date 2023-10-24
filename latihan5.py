# Fungsi penambahan
def tambah(angka1, angka2):
    return angka1 + angka2
# Fungsi pengurangan
def kurang(angka1, angka2):
    return angka1 - angka2
# Fungsi perkalian
def kali(angka1, angka2):
    return angka1 * angka2
# Fungsi pembagian
def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Error: Tidak boleh ada pembagian dengan nol"

# Fungsi menu
def show_menu():
    print("\n")
    print("----------- KALKULATORKU ----------")
    print("Pilih operasi:")
    print("[1] Penambahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Keluar")
    pilihan = input("Masukkan nomor operasi (1-5): ")

    if pilihan == '5':
        print("Terima kasih telah menggunakan program kalkulator kami, keluar.")
        exit()
    elif pilihan in ['1', '2', '3', '4']:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        if pilihan == '1':
            hasil = tambah(angka1, angka2)
            print(f"Hasil penambahan: {hasil}")
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            print(f"Hasil pengurangan: {hasil}")
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            print(f"Hasil perkalian: {hasil}")
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            print(f"Hasil pembagian: {hasil}")
    else:
        print("Pilihan tidak tepat. Silakan pilih kembali nomor yang benar.")

# Main loop program       
if __name__ == "__main__":
    while(True):
        show_menu()