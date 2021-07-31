p = int(input("Masukkan panjang : "))
l = int(input("Masukkan lebar : "))
t = int(input("Masukkan tinggi : "))
Vair = (p * l * t) * 3//4
Vair_sehari = Vair * 2
Vair_sebulan = Vair_sehari * 30
print("Jadi air yang digunakan perbulan adalah ", Vair_sebulan, "liter")

def BubbleSort(n, A):
    # n = panjang list
    # A = list itu sendiri

    #variabel untuk menyimpan data list sementara
    # variabel untuk menampung data hasil yg ditukar
    swap = False 

    #algoritmanya
    while not swap:
        
        # keadaan true artinya harus di check dengan loopingan
        swap = True

        # looping mulai dari 1 sampai n atau 1 - 5, 4x
        # Keadaan List: 11, 334, 523, 12, 12
        for j in range(1, n): # loop sebanyak 4x
            if A[j-1] > A[j]: # membandingkan 0 > 1
                swap = False
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp

                # Disaat loop 1 / j=1
                # A[j-1] / A[1-1] > A[j] / A[1]
                    # 11 > 334, false
                # jika false maka tidak swap/tukar 
                # Keadaan List: 11, 334, 523, 12, 12

                # Disaat loop 2 / j=2
                # A[j-1] / A[2-1] > A[j] / A[2]
                    # 334 > 523, false
                # jika false maka tidak swap/tukar 
                # Keadaan List: 11, 334, 523, 12, 12

                # Disaat loop 3 / j=3
                # A[j-1] / A[3-1] > A[j] / A[3]
                    # 523 > 12, true
                # jika true maka swap/tukar
                # temp = A[j] / A[3]
                    # temp = 12
                # A[j] / A[3] = A[j-1] / A[3-1]
                    # A[3] = 523
                # A[j-1] / A[2] = temp
                    # A[2] = 12
                # Keadaan List: 11, 334, 12, 523, 12

                # Disaat loop 4 / j=4
                # A[j-1] / A[4-1] > A[j] / A[4]
                    # 523 > 12, true
                # jika true maka swap/tukaR
                # temp = A[j] / A[4]
                    # temp = 12
                # A[j] / A[4] = A[j-1] / A[4-1]
                    # A[4] = 523
                # A[j-1] / A[3] = temp
                    # A[3] = 12
                # Keadaan List: 11, 334, 12, 12, 523

                # Disaat loop 1 / j=1
                # A[j-1] / A[1-1] > A[j] / A[1]
                    # 11 > 334, false
                # Keadaan List: 11, 334, 12, 12, 523

                # Disaat loop 2 / j=2
                # A[j-1] / A[2-1] > A[j] / A[2]
                    # 334 > 12, true
                # jika true maka swap/tukaR
                # temp = A[j] / A[2]
                    # temp = 12
                # A[j] / A[2] = A[j-1] / A[2-1]
                    # A[2] = 334
                # A[j-1] / A[1] = temp
                    # A[1] = 12
                # Keadaan List: 11, 12, 334, 12, 523

                # Disaat loop 3 / j=3
                # A[j-1] / A[3-1] > A[j] / A[3]
                    # 334 > 12, true
                # jika true maka swap/tukaR
                # temp = A[j] / A[3]
                    # temp = 12
                # A[j] / A[3] = A[j-1] / A[3-1]
                    # A[3] = 334
                # A[j-1] / A[2] = temp
                    # A[2] = 12
                # Keadaan List: 11, 12, 12, 334, 523

                # Disaat loop 4 / j=4
                # A[j-1] / A[4-1] > A[j] / A[4]
                    # 334 > 523, false
                # Keadaan List: 11, 12, 12, 334, 523
                   
    return A

def bubblesort():
    print("Bubble Sort") #menampilkan kalimat
    A = [int(x) for x in input("Masukkan List untuk bubble sort : ").split()]
        #untuk menginputkan beberapa nilai dalam bentuk list
    n = len(A) #untuk menghitung jumlah karakter pada list
    print("List setelah input : ", A) #untuk menampilkan list setelah diinputkan
    print("Setelah diurutkan menjadi : ", BubbleSort(n,A)) #untuk menampilkan list setelah diurutkan
    print("\n") #untuk memberi jarak pada output
bubblesort()

# n adalah panjang array
# A adalah array yang dimasukkan
def insertionSort(n,A):
    temp = 0 # menyimpan temporary data
    for i in range(1, n): # looping dari 1 sampai ke n=5
        temp = A[i]
        # temp = A[1]
            # temp = 334
        
        j = i -1
        # j = 1 -1
            # j = 0
        while j >= 0 and temp < A[j]:
            # temp = A[1]
                # temp = 334
            # j = i - 1
                # j = 1 -1
                    # j = 0
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[0]
                    # 0 >= 0 and 334 < 11 False, tidak tukar
            # Kondisi Array a2 = [11, 334, 523, 12, 12]

            # i++, i=1+1=2
            # temp = A[i]
                # temp = A[2]
                    #temp = 523
            # j = i - 1
                # j = 2 - 1
                    # j = 1
            # j >= 0 and temp < A[j]
                # 1 >= 0 and 523 < A[1]
                    # 1 >= 0 and 523 < 334 False, tidak tukar
            # Kondisi Array a2 = [11, 334, 523, 12, 12]

            # i++, i=2+1=3
            # temp = A[i]
                # temp = A[3]
                    # temp = 12
            # j = i - 1
                # j = 3 - 1
                    # j = 2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 12 < A[2]
                    # 2 >= 0 and 12 < 523 True, tukar
            # A[j+1] = A[j]
                # A[2+1] = A[2]
                    # A[3] = A[2]
                        # A[3] = 523
            # j = j - 1
                # j = 2 - 1
                    # j = 1
            # i = i - 2
                # i = 3-2
                    # i = 1
            # A[1+1] = temp
                # A[2] = 12
            # Kondisi Array a2 = [11, 334, 12, 523, 12]
            
            # i++, i= 1 +1=2
            # temp = A[i]
                # temp = A[2]
                    # temp = 12
            # j = i - 1
                # j = 2 - 1
                    # j = 1
            # j >= 0 and temp < A[j]
                # 1 >= 0 and 12 < A[1]
                    # 1 >= 0 and 12 < 334 True, tukar
            # A[j+1] = A[j]
                # A[1+1] = A[1]
                    # A[2] = 334
            # j = j - 1
                # j = 1 - 1
                    # j = 0
            # i = i - 2
                # i = 0
            # A[j+1] = temp
                # A[0+1] = 12
                    # A[1] = 12
            # Kondisi Array a2 = [11, 12, 334, 523, 12]

            # i++, i=0+1=1
            # temp = A[i]
                # temp = A[1]
                    # temp = 12
            # j = i - 1
                # j = 1 - 1
                    # j = 0
            # j >= 0 and temp < A[j]
                # 0 >= 0 and 12 < A[0]
                    # 0 >= 0 and 12 < 11 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 334, 523, 12]

            # i++, i=1+1=2
            # temp = A[2]
                # temp = A[2]
                    # temp = 334
            # j = i - 1
                # j = 2 - 1
                    # j = 1
            # j >= 0 and temp < A[j]
                # 1 >= 0 and 334 < A[1]
                    # 1 >=0 and 334 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 334, 523, 12] 
                    

            # i++, i=2+1=3
            # temp = A[i]
                # temp = A[3]
                    # temp = 523
            # j = i - 1
                # j = 3 - 1
                    # j = 2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 523 < A[2]
                    # 2 >= 0 and 523 < 334 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 334, 523, 12] 

            # i++, i=3+1=4
            # temp = A[i]
                # temp = A[4]
                    # temp = 12
            # j = i - 1
                # j = 4 - 1
                    # j = 3
            # j >= 0 and temp < A[j]
                # 3 >= 0 and 12 < A[3]
                    # 3 >= 0 and 12 < 523 True, tukar
            # A[j+1] = A[j]
                # A[3+1] = A[3]
                    # A[4] = A[3]
                        # A[4] = 523
            # j = 3 - 1=2
            # i = 4 - 2=2
            # A[j+1]=temp
                # A[2+1] = 12
                    # A[3] = 12
            # Kondisi Array a2 = [11, 12, 334, 12, 523]

            # i++, i=2+1=3
            # temp = A[i]
                # temp = A[3]
                    # temp = 12
            # j = i - 1
                # j = 3 - 1=2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 12 < A[2]
                    # 2 >= 0 and 12 < 334 True, tukar
            # A[j+1] = A[j]
                # A[2+1] = A[2]
                    # A[3] = 334
            # j = 2 - 1=1
            # i = 3 - 2=1
            # A[j+1]=temp
                # A[1+1] = 12
                    # A[2] = 12
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=1+1=2
            # temp = A[i]
                # temp = 12
            # j = i - 1
                # j = 1
            # j >= 0 and temp < A[j]
                # 1 >= 0 and 12 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=2+1=3
            # temp = A[i]
                # temp = 334
            # j = i - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # 2 >= 0 and 334 < 12 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=3+1=4
            # temp = A[i]
                # temp = 523
            # j = i - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # 3 >= 0 and 523 < 334 False, tidak tukar
            # Kondisi Array a2 = [11, 12, 12, 334, 523]

            # i++, i=4+1=5
            # temp = A[5]
                # temp = error, maka out looping

            A[j+1] = A[j]
            j = j-1
            i = i-2
        A[j+1]=temp
    return A

def binarysearch(k,nmo,D):
    # k = nilai yang akan dicari
    # nmo = jumlah list
    # D = list
    found = False 
    bb = 0 # set batas bawah = 0
    ba = nmo - 1 # batas atas = jumlah karakter dalam list - 1
    while bb <= ba and not found: #buat perbandingan jika batas atas lebih kecil sama dengan batas bawah dan data tidak ditemukan maka,
        mid = (bb + ba)//2 # mid = (batas bawah + batas atas) dibagi 2
        if D[mid] == k: #jika list[mid] = data yang akan dicari
            print("Data found") # tampilkan data found
            found = True
        else:
            if D[mid] > k: #jika list[mid] > data yang akan dicari maka,
                ba = mid - 1 #batas atas = mid - 1
            else: #jika list[mid] < data yang akan dicari maka,
                bb = mid + 1 #batas bawah + 1
    if not found: # jika pada akhirnya data tetap tidak ditemukan maka
        print("Data not found") # tampilkan data not found
    return found

def insertionsort_dan_binarysearch():
    print("Insertion Sort + Binary Search") #menampilkan kalimat
    C = [int(x) for x in input("Masukkan List untuk insertion sort : ").split()] # menginputkan beberapa nilai yang langsung diubah ke list
    o = len(C) # menghitung jumlah karakter list
    print("List setelah input : ", C) #menampilkan list setelah diinputkan
    print("Setelah diurutkan menjadi : ", insertionSort(o,C)) #menampilkan list setelah diurutkan
    k = int(input("Angka yang akan dicari : ")) #mencari angka
    print(binarysearch(k,o,C)) #menampilkan dan memanggil fungsi binary search
    print("\n") # memberikan jarak pada output

insertionsort_dan_binarysearch()