def Bio(nama, umur, makanan, minuman, hobi, citacita):

    print("Nama anda adalah : ", nama)
    print("Umur anda ditahun ini adalah : ", umur)
    print("Makanan favorit anda adalah : ", makanan)
    print("Minuman favorit anda adalah : ", minuman)
    print("Hobi anda adalah : ", hobi)
    print("Cita - cita anda adalah : ", citacita)

def main():

    nama = str(input("Masukkan nama lengkap anda : "))
    
    x = int(input("Masukkan tahun lahir anda : "))
    y = int(input("Masukkan ditahun berapa anda mengisi formulir ini : "))
    umur = y - x 

    makanan = str(input("Masukkan makanan favorit anda : "))
    minuman = str(input("Masukkan minuman favorit anda : "))
    hobi = str(input("Masukkan hal apa yang paling suka dan sering anda lakukan : "))
    citacita = str(input("Apa harapan anda untuk masa depan anda sendiri : "))

    print("\n")

    Bio(nama, umur, makanan, minuman, hobi, citacita)

    print("\n")

    

main()




