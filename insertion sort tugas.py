listsekarang = [12, 9, 2003, 111, 90, 91, 92, 10000]

def insertionsort(n,A):
    temp = 0
    for i in range(1, n):
        temp = A[i]
            # temp = A[i]
            # temp = A[1]
                # temp = 9
        j = i - 1
            # j = 1 - 1
                # j = 0
        while j >= 0 and temp < A[j]:
            # temp = A[1]
                # temp = 9
            # j = i -1
                # j = 1 - 1 
                # j = 0 
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[0]
                # 0 >= 0 and 9 < 12 True, tukar
            # kondisi listsekarang = [9, 12, 2003, 111, 90, 91, 92, 10000]

            # i++, i = 1 + 1 = 2
            # temp = A[i]
                # temp = A[2]
                # temp = 2003
            # j = i -1
                # j = 2 - 1 
                # j = 1
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[1]
                # 1 >= 0 and 2003 < 12 False, tidak tukar
            # kondisi listsekarang = [9, 12, 2003, 111, 90, 91, 92, 10000]

            #i++, i = 2 + 1 = 3
            # temp = A[i]
                # temp = A[3]
                # temp = 111
            # j = i - 1
                # j = 3 - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[2]
                # 2 >= 0 and 111 < 2003 True, tukar
            # A[j+1] = A[j]
                # A[2+1] = A[2]
                # A[3] = A[2]
                # A[3] = 2003
            # j = j - 1
                # j = 2 - 1
                # j = 1
            # i = i - 2
                # i = 3-2
                # i = 1
            # A[1+1] = temp
                # A[2] = 111
            # kondisi listsekarang = [9, 12, 111, 2003, 90, 91, 92, 10000]  

           #i++, i = 1 + 1 = 2
            # temp = A[i]
                # temp = A[2]
                # temp = 111
            # j = i - 1
                # j = 2 - 1
                # j = 1
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[1]
                # 1 >= 0 and 111 < 12 False, tidak tukar
            # kondisi listsekarang = [9, 12, 111, 2003, 90, 91, 92, 10000]

            #i++, i = 2 + 1 = 3
            # temp = A[i]
                # temp = A[3]
                # temp = 2003
            # j = i - 1
                # j = 3 - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[2]
                # 2 >= 0 and 2003 < 111 False, tidak tukar
            # kondisi listsekarang = [9, 12, 111, 2003, 90, 91, 92, 10000]

            #i++, i = 3 + 1 = 4
            # temp = A[i]
                # temp = A[4]
                # temp = 90
            # j = i - 1
                # j = 4 - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[3]
                # 3 >= 0 and 2003 < 90 True, tukar
            # A[j+1] = A[j]
                # A[3+1] = A[3]
                # A[4] = A[3]
                # A[4] = 2003
            # j = j - 1
                # j = 3 - 1
                # j = 2
            # i = i - 2
                # i = 4 - 2
                # i = 2
            # A[2+1] = temp
                # A[3] = 90
            # kondisi listsekarang = [9, 12, 111, 90, 2003, 91, 92, 10000] 

            #i++, i = 2 + 1 = 3
            # temp = A[i]
                # temp = A[3]
                # temp = 90
            # j = i - 1
                # j = 3 - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[2]
                # 2 >= 0 and 90 < 111 True, tukar
            # A[j+1] = A[j]
                # A[2+1] = A[2]
                # A[3] = A[2]
                # A[3] = 111
            # j = j - 1
                # j = 2 - 1
                # j = 1
            # i = i - 2
                # i = 3 - 2
                # i = 1
            # A[1+1] = temp
                # A[2] = 90
            # kondisi listsekarang = [9, 12, 90, 111, 2003, 91, 92, 10000] 

            #i++, i = 1 + 1 = 2
            # temp = A[i]
                # temp = A[2]
                # temp = 90
            # j = i - 1
                # j = 2 - 1
                # j = 1
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[1]
                # 1 >= 0 and 90 < 12 False, tidak tukar
             # kondisi listsekarang = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 2 + 1 = 3
            # temp = A[i]
                # temp = A[3]
                # temp = 111
            # j = i - 1
                # j = 3 - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[2]
                # 2 >= 0 and 111 < 90 False, tidak tukar
             # kondisi listsekarang = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 3 + 1 = 4
            # temp = A[i]
                # temp = A[4]
                # temp = 2003
            # j = i - 1
                # j = 4 - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[3]
                # 3 >= 0 and 2003 < 111 False, tidak tukar
             # kondisi listsekarang = [9, 12, 90, 111, 2003, 91, 92, 10000]

            #i++, i = 4 + 1 = 5
            # temp = A[i]
                # temp = A[5]
                # temp = 91
            # j = i - 1
                # j = 5 - 1
                # j = 4
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[4]
                # 4 >= 0 and 91 < 2003 True, tukar
            # A[j+1] = A[j]
                # A[4+1] = A[4]
                # A[5] = A[4]
                # A[5] = 2003
            # j = j - 1
                # j = 4 - 1
                # j = 3
            # i = i - 2
                # i = 5 - 2
                # i = 3
            # A[3+1] = temp
                # A[4] = 91
            # kondisi listsekarang = [9, 12, 90, 111, 91, 2003, 92, 10000]

            #i++, i = 3 + 1 = 4
            # temp = A[i]
                # temp = A[4]
                # temp = 91
            # j = i - 1
                # j = 4 - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[3]
                # 3 >= 0 and 91 < 111 True, tukar
            # A[j+1] = A[j]
                # A[3+1] = A[3]
                # A[4] = A[3]
                # A[4] = 111
            # j = j - 1
                # j = 3 - 1
                # j = 2
            # i = i - 2
                # i = 4 - 2
                # i = 2
            # A[2+1] = temp
                # A[3] = 91
            # kondisi listsekarang = [9, 12, 90, 91, 111, 2003, 92, 10000]

            #i++, i = 2 + 1 = 3
            # temp = A[i]
                # temp = A[3]
                # temp = 91
            # j = i - 1
                # j = 3 - 1
                # j = 2
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[2]
                # 2 >= 0 and 91 < 90 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 111, 2003, 92, 10000] 

            #i++, i = 3 + 1 = 4
            # temp = A[i]
                # temp = A[4]
                # temp = 111
            # j = i - 1
                # j = 4 - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[3]
                # 3 >= 0 and 111 < 91 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 111, 2003, 92, 10000] 

            #i++, i = 4 + 1 = 5
            # temp = A[i]
                # temp = A[5]
                # temp = 2003
            # j = i - 1
                # j = 5 - 1
                # j = 4
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[4]
                # 4 >= 0 and 2003 < 111 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 111, 2003, 92, 10000] 

            #i++, i = 5 + 1 = 6
            # temp = A[i]
                # temp = A[6]
                # temp = 92
            # j = i - 1
                # j = 6 - 1
                # j = 5
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[5]
                # 5 >= 0 and 92 < 2003 True, tukar
            # A[j+1] = A[j]
                # A[5+1] = A[5]
                # A[6] = A[5]
                # A[6] = 2003
            # j = j - 1
                # j = 5 - 1
                # j = 4
            # i = i - 2
                # i = 6 - 2
                # i = 4
            # A[4+1] = temp
                # A[5] = 92
            # kondisi listsekarang = [9, 12, 90, 91, 111, 92, 2003, 10000] 

            #i++, i = 4 + 1 = 5
            # temp = A[i]
                # temp = A[5]
                # temp = 92
            # j = 5 - 1
                # j = 5 - 1
                # j = 4
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[4]
                # 4 >= 0 and 92 < 111 True, tukar
            # A[j+1] = A[j]
                # A[4+1] = A[4]
                # A[5] = A[4]
                # A[5] = 111
            # j = j - 1
                # j = 4 - 1
                # j = 3
            # i = i - 2
                # i = 5 - 2
                # i = 3
            # A[3+1] = temp
                # A[4] = 92
            # kondisi listsekarang = [9, 12, 90, 91, 92, 111, 2003, 10000] 

            #i++, i = 3 + 1 = 4
            # temp = A[i]
                # temp = A[4]
                # temp = 92
            # j = i - 1
                # j = 4 - 1
                # j = 3
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[3]
                # 3 >= 0 and 92 < 91 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++, i = 4 + 1 = 5
            # temp = A[i]
                # temp = A[5]
                # temp = 111
            # j = i - 1
                # j = 5 - 1
                # j = 4
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[4]
                # 4 >= 0 and 111 < 92 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++, i = 5 + 1 = 6
            # temp = A[i]
                # temp = A[6]
                # temp = 2003
            # j = i - 1
                # j = 6 - 1
                # j = 5
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[5]
                # 5 >= 0 and 2003 < 111 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 92, 111, 2003, 10000]

            #i++, i = 6 + 1 = 7
            # temp = A[i]
                # temp = A[7]
                # temp = 10000
            # j = i - 1
                # j = 7 - 1
                # j = 6
            # j >= 0 and temp < A[j]
                # j >= 0 and temp < A[6]
                # 6 >= 0 and 2003 < 10000 False, tidak tukar
            # kondisi listsekarang = [9, 12, 90, 91, 92, 111, 2003, 10000]

            A[j + 1] = A[j]
            j = j - 1
            i = i - 2
        A[j + 1] = temp
    return A
print("\n")
print(insertionsort(8, listsekarang))
print("\n")