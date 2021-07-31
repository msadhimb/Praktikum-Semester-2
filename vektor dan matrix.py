#Vektor
Va = [15, 18, 35, 56]
Vb = [5, 6, 7, 8]

def vektor(Va, Vb):
    penjumlahan = []
    perkalian = []
    pengurangan = []
    pembagian = []
   
    if len(Va) != len(Vb): #Jika penjumlahan karakter Va tidak sama dengan Vb maka, berhenti
        return -1
    else:
        for i in range(len(Va)): #Untuk i di area jumlah karakter dari Va (looping/pengurangan)
            penjumlahan.append(Va[i] + Vb[i])
            perkalian.append(Va[i] * Vb[i])
            pengurangan.append(Va[i] - Vb[i])
            pembagian.append(Va[i] // Vb[i])
    print("Hasil penjumlahan 2 vektor = ", penjumlahan)
    print("Hasil perkalian 2 vektor = ", perkalian)
    print("Hasil Pengurangan 2 vektor = ", pengurangan)
    print("Hasil pembagian 2 vektor = ", (pembagian))
    print("\n")
    return pengurangan, perkalian, pembagian, penjumlahan
    
# vektor(Va, Vb)

#Matriks
A = [[80, 20, 40, 60], [80, 100, 120, 140], [160, 180, 200, 210]]
B = [[2, 2, 4, 4], [2, 10, 2, 10], [4, 8, 4, 10]]

def penjumlahanmatrix(A, B):
    baris1 = len(A)
    kolom1 = len(A[0])
    baris2 = len(B)
    kolom2 = len(B[0])

    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        #Jujur pak, saya masih bingung coding dibawah
        C = [0]*baris1
        #Kenapa C = [0] ya pak ?
        for a in range (baris1):
            C[a] = [0] * kolom1
        for a in range(baris1):
            for b in range(kolom2):
                C[a][b] = A[a][b] + B[a][b]
        return C
        #Saya belum paham cara kerja dari coding tersebut pak :', sudah saya coba pahami
        #tapi malah pusing pak :'

def perkalianmatrix(A, B):
    baris1 = len(A)
    kolom1 = len(A[0])
    baris2 = len(B)
    kolom2 = len(B[0])

    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        C = [0]*baris1
        for a in range (baris1):
            C[a] = [0] * kolom1
        for a in range(baris1):
            for b in range(kolom2):
                C[a][b] = A[a][b] * B[a][b]
        return C
        
def penguranganmatrix(A, B):
    baris1 = len(A)
    kolom1 = len(A[0])
    baris2 = len(B)
    kolom2 = len(B[0])

    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        C = [0]*baris1
        for a in range (baris1):
            C[a] = [0] * kolom1
        for a in range(baris1):
            for b in range(kolom2):
                C[a][b] = A[a][b] - B[a][b]
        return C

def pembagianmatrix(A, B):
    baris1 = len(A)
    kolom1 = len(A[0])
    baris2 = len(B)
    kolom2 = len(B[0])

    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        C = [0]*baris1
        for a in range (baris1):
            C[a] = [0] * kolom1
        for a in range(baris1):
            for b in range(kolom2):
                C[a][b] = A[a][b] // B[a][b]
        return C

def main():
    print("\n")
    print("Hasil dari penjumlahan matrix A dan B : ", penjumlahanmatrix(A, B))
    print("Hasil dari perkalian matrix A dan B : ", perkalianmatrix(A, B))
    print("Hasil dari pengurangan matrix A dan B : ", penguranganmatrix(A, B))
    print("Hasil dari pembagian matrix A dan B : ", pembagianmatrix(A, B))
    print("\n")
main()