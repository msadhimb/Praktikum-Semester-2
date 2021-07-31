def Penjumlahan(angka1,angka2):
    return angka1 + angka2  

def Perkaklian(angka3,angka4):
    return angka3 * angka4

def Pengurangan(angka5,angka6):
    return angka5 - angka6

def Pembagian(angka7, angka8):
    return angka7 / angka8

def main():

    angka1 = int(input("Masukkan angka = "))
    angka2 = int(input("Masukkan angka = "))
    angka3 = int(input("Masukkan angka = "))
    angka4 = int(input("Masukkan angka = "))
    angka5 = int(input("Masukkan angka = "))
    angka6 = int(input("Masukkan angka = "))
    angka7 = int(input("Masukkan angka = "))
    angka8 = int(input("Masukkan angka = "))

    hasil = Penjumlahan(angka1,angka2)
    hasil1 = Perkaklian(angka3,angka4)
    hasil2 = Pengurangan(angka5,angka6)
    hasil3 = Pembagian(angka7,angka8)
    
    print("Hasil penjumlahan adalah ", hasil)
    print("Hasil perkalian adalah ", hasil1)
    print("Hasil pengurangan adalah ", hasil2)
    print("Hasil pembagian adalah ", hasil3)

main()