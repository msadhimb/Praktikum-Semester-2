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

a2 = [11, 334, 523, 12, 12] #5
print (BubbleSort(5, a2))