def pembagian(m, n):
    result = 0
    while m > 0:
        m = m - n
        result += 1
    return result
    # CONTOH 1
    # m = 6, n = 3
    # m > 0, True
    # m = m - n
    #  6 - 3 = 3
        # result = 0 + 1
        # result = 1
    # 3 - 3 = 0
        # result = 1 + 1
        # result = 2
    # return result / return 2

    # CONTOH 2
    # m = 4, n = 2
    # m > 0, True
    # m = m - n
    #  4 - 2 = 2
        # result = 0 + 1
        # result = 1
    # 2 - 2 = 0
        # result = 1 + 1
        # result = 2
    # return result / return 2

def pangkat(o, p):
    if p == 1:
        return o
    else:
        return o * pangkat(o, p-1)
    # CONTOH 1
    # o = 5, p = 2
    # p = 1, False
    # return o * pangkat(o, p-1)
    # return 5 * pangkat(5, 2-1)

    # o = 5, p = 1
    # p = 1, True
    # return 5 * return 5

    # Hasil : 25

    # CONTOH 2
    # o = 4, p = 2
    # p = 1, False
    # return o * pangkat(o, p-1)
    # return 4 * pangkat(4, 2-1)

    # o = 4, p = 1
    # p = 1, True
    # return 4 * return 4

    # Hasil : 16

def faktorial(q):
    if q == 1:
        return q
    else:
        return q * faktorial(q - 1)
    # CONTOH 1
    # q = 3
    # q = 1, False
    # return q * faktorial(q - 1)
    # return 3 * faktorial(3 - 1)
    # return 3 * faktorial(2)
    # Hasil sementara : 6

    # q = 2
    # q = 1, False
    # return q * faktorial(q - 1)
    # return 3 * 2 * faktorial(2 - 1)
    # return 3 * 2 * faktorial(1)
    # Hasil sementara : 6

    # q = 1
    # q = 1, True
    # return 3 * 2 * 1
    # return 3 * 2 * 1
    # Hasil akhir 6
    # return 6

    # CONTOH 2
    # q = 2
    # q = 1, False
    # return q * faktorial(q - 1)
    # return 2 * faktorial(2 - 1)
    # return 2 * faktorial(1)
    # Hasil sementara : 2

    # q = 1
    # q = 1, True
    # return 2 * 1
    # return 2 * 1
    # Hasil akhir 2
    # return 2

def main():
    print("Fungsi Rekursif Pembagian")
    m = int(input("Masukkan angka yang ingin dibagi : "))
    n = int(input("Masukkan angka pembagi : "))
    print("Hasil : ", pembagian(m, n))
    print("\n")
    print("Fungsi Rekursif Perpangkatan")
    o = int(input("Masukkan angka : "))
    p = int(input("Masukkan pangkat : "))
    print("Hasil : ", pangkat(o, p))
    print("\n")
    print("Fungsi Rekursif Faktorial")
    q = int(input("Masukkan angka : "))
    print("Hasil : ", faktorial(q))
main()