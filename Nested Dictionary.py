buku1 = {
    'Nama Buku':'Tenggelam', 
    'Kode Buku':1921, 
    'Rak Nomor':5
}
buku2 = {
    'Nama Buku':'Terbit', 
    'Kode Buku':1764, 
    'Rak Nomor':12
}
buku3 = {
    'Nama Buku':'Terang', 
    'Kode Buku':1844, 
    'Rak Nomor':7
}
buku4 = {
    'Nama Buku':'Habis', 
    'Kode Buku':1966, 
    'Rak Nomor':10
}
buku5 = {
    'Nama Buku':'Habis Gelap Terbitlah Terang', 
    'Kode Buku':2141, 
    'Rak Nomor':1
}


DataPerpustakaan = {
    1:buku1,
    2:buku2,
    3:buku3,
    4:buku4,
    5:buku5
}

def looping():
    print("\n")
    print("Data Buku Perpustakaan")
    print("\n")
    for i in range(1, 6):
        for j, v in DataPerpustakaan[i].items():
            print(j, " : ", v)
        print("\n")

looping()

