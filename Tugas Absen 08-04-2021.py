def bubblesort(n,A):
    # n = jumlah list
    # A = list
    swap = False
    while not swap:
        swap = True
        for j in range(1,n):
            if A[j-1] > A[j]:
                swap = False
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A

def selectionsort(m,B):
    # m = jumlah list
    # B = list
    i = 0
    while i != m:
        for j in range(i,m):
            if B[i] > B[j]:
                temp = B[j]
                B[j] = B[i]
                B[i] = temp
        i += 1
    return B

def insertionsort(o,C):
    # o = jumlah list
    # C = list
    temp = 0
    for i in range(1,o):
        temp = C[i]
        j = i - 1
        while j >= 0 and temp < C[j]:
            C[j+1] = C[j]
            j -= 1
        C[j+1] = temp
    return C

def binarysearch(k,nmo,D):
    # k = nilai yang akan dicari
    # nmo = jumlah list
    # D = list
    found = False
    bb = 0
    ba = nmo - 1
    while bb <= ba and not found:
        mid = (bb + ba)//2
        if D[mid] == k:
            print("Data found")
            found = True
        else:
            if D[mid] > k:
                ba = mid - 1
            else:
                bb = mid + 1
    if not found:
        print("Data not found")
    return found


def bubblesort_dan_binarysearch():
    print("\n")
    print("Bubble Sort + Binary Search")
    A = [int(x) for x in input("Masukkan List untuk bubble sort : ").split()]
    n = len(A)
    print("List setelah input : ", A)
    print("Setelah diurutkan menjadi : ", bubblesort(n,A))
    k = int(input("Angka yang akan dicari : "))
    print(binarysearch(k,n,A))
    print("\n")

def selectionsort_dan_binarysearch():
    print("Selection Sort + Binary Search")
    B = [int(x) for x in input("Masukkan List untuk selection sort : ").split()]
    m = len(B)
    print("List setelah input : ", B)
    print("Setelah diurutkan menjadi : ", selectionsort(m,B))
    k = int(input("Angka yang akan dicari : "))
    print(binarysearch(k,m,B))
    print("\n")

def insertionsort_dan_binarysearch():
    print("Insertion Sort + Binary Search")
    C = [int(x) for x in input("Masukkan List untuk insertion sort : ").split()]
    o = len(C)
    print("List setelah input : ", C)
    print("Setelah diurutkan menjadi : ", insertionsort(o,C))
    k = int(input("Angka yang akan dicari : "))
    print(binarysearch(k,o,C))
    print("\n")


bubblesort_dan_binarysearch()
selectionsort_dan_binarysearch()
insertionsort_dan_binarysearch()
