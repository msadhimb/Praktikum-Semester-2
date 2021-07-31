z = 1
a = 1
b = 1
c = 1
print("\n")
print("Data Harga Hewan Peternakan")
print("\n")

sapi = {
    'Sapi Supreme' : 'Rp 20.000.000',
    'Sapi Belanda' : 'Rp 15.000.200',
    'Sapi Kekar' : 'Rp 10.000.000',
    'Sapi Jawa' : 'Rp 5.000.000',
    'Sapi Kurus' : 'Rp 2.000.000'
}

kambing = {
    'Kambing Supreme' : 'Rp 15.000.000',
    'Kambing Belanda' : 'Rp 12.000.200',
    'Kambing Kekar' : 'Rp 10.000.000',
    'Kambing Jawa' : 'Rp 3.500.000',
    'Kambing Kurus' : 'Rp 1.000.000'
}

ayam = {
    'Ayam Jago Supreme Berbulu Ungu' : 'Rp 5.000.000',
    'Ayam Kuning Kemerah-Merahan' : 'Rp 3.500.000',
    'Ayam Hitam Untuk Sesajen' : 'Rp 2.250.666',
    'Ayam Kampung' : 'Rp 500.000'
}

lele = {
    'Lele Makan Nasi' : 'Rp 800.000',
    'Lele Sebesar Tangan Yang Makan Tinja' : 'Rp 400.000',
    'Lele Biasa' : 'Rp 100.000'
}

                

for i, v in sapi.items():
    print("SAPI")
    print(z, ".",i, " : ", v)
    z += 1
print("\n")
for i, v in kambing.items():
    print("Kambing")
    print(a, ".",i, " : ", v)
    a += 1
print("\n")
for i, v in ayam.items():
    print("Ayam")
    print(b, ".",i, " : ", v)
    b += 1
print("\n")
for i, v in lele.items():
    print("Lele")
    print(c, ".",i, " : ", v)
    c += 1
print("\n")

# Nested Dictionary
datapeternakan = {
    1:sapi,
    2:kambing,
    3:ayam,
    4:lele
}

def looping():
    z = 1
    a = 1
    b = 1
    c = 1
    print("\n")
    print("Data Harga Hewan Peternakan")
    for j in range(1, 5):
        print("\n")
        if j == 1:
            print("SAPI")
            for i, v in datapeternakan[j].items():
                print(z, ".",i, ":", v)
                z += 1
        elif j == 2:
            print("Kambing")
            for i, v in datapeternakan[j].items():
                print(a, ".",i, ":", v)
                a += 1
        elif j == 3:
            print("Ayam")
            for i, v in datapeternakan[j].items():
                print(b, ".", i, ":", v)
                b += 1
        elif j == 4:
            print("Lele")
            for i, v in datapeternakan[j].items():
                print(c, ".",i, ":", v)
                c += 1
    print("\n")
looping()

