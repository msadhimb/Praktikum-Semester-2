#Muhamad Salman Adhim Baqy
#A11.2020.12641
def SelectionSort(n, A):
    # n = panjang list
    # A = list itu sendiri

    # Set nilai awalan untuk looping dengan index 0
    i = 0
    
    # Algoritma
    while i != n: # jika i tidak sama dengan 0

        # looping j = i
            # j = 0 sampai dengan n / jumlah array
            # 0 sampai 5
        for j in range(i, n):

            # buat perbandingan yg kondisinya harus diswap
            # nilai awal a2 = [11, 334, 523, 12, 12] #5
            if A[i] > A[j]:
                # LOOP 0, i=0 j=i/j=0, index 0 > index 0
                    # A[i] > A[j]
                    # A[0] > A[0]
                    # 11 > 11, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 1, i=0 j=1, index 0 > index 1
                    # A[i] > A[j]
                    # A[0] > A[1]
                    # 11 > 334, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 1, i=0 j=2,  index 0 > index 2
                    # A[i] > A[j]
                    # A[0] > A[2]
                    # 11 > 523, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 1, i=0 j=3,  index 0 > index 3
                    # A[i] > A[j]
                    # A[0] > A[3]
                    # 11 > 12, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 1, i=0 j=4,  index 0 > index 4
                    # A[i] > A[j]
                    # A[0] > A[4]
                    # 11 > 12, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

            # i = i + 1
            # i = 0 + 1
                # LOOP 0, i=1 j=i/j=1, index 1 > index 1
                    # A[i] > A[j]
                    # A[1] > A[1]
                    # 334 > 333, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 1, i=1 j=i/j=2, index 1 > index 2
                    # A[i] > A[j]
                    # A[1] > A[2]
                    # 334 > 523, false
                        # Hasil a2 = [11, 334, 523, 12, 12] #5
                        # j++

                # LOOP 2, i=1 j=i/j=3, index 1 > index 3
                    # A[i] > A[j]
                    # A[1] > A[3]
                    # 334 > 12, true
                        # temp = A[j]
                            # temp = A[3]
                            # temp = 12
                        # A[j] = A[i]
                            # A[3] = A[1]
                            # A[3] = 334
                        # A[i] = temp
                            # A[1] = temp
                            # A[1] = 12
                        # Hasil a2 = [11, 12, 523, 334, 12] #5
                        # j++

                # LOOP 3, i=1 j=i/j=4, index 1 > index 4
                    # A[i] > A[j]
                    # A[1] > A[4]  -> i
                    # 12 > 12, false
                        # Hasil a2 = [11, 12, 523, 334, 12] #5
                        # j++

            # i = i + 1
            # i = 1 + 1
                # LOOP 0, i=2 j=i/j=2, index 2 > index 2
                    # A[i] > A[j]
                    # A[2] > A[2]  -> i
                    # 523 > 523, false
                        # Hasil a2 = [11, 12, 523, 334, 12] #5
                        # j++

                # LOOP 1, i=2 j=i/j=3, index 2 > index 3
                    # A[i] > A[j]
                    # A[2] > A[3]  -> i
                    # 523 > 334, true
                        # temp = A[j]
                            # temp = A[3]
                            # temp = 334
                        # A[j] = A[i]
                            # A[3] = A[1]
                            # A[3] = 523
                        # A[i] = temp
                            # A[2] = temp
                            # A[2] = 334
                        # Hasil a2 = [11, 12, 334, 523, 12] #5
                        # j++

                # LOOP 2, i=2 j=i/j=4, index 2 > index 4
                    # A[i] > A[j]
                    # A[2] > A[4]  -> i
                    # 334 > 12, true
                        # temp = A[j]
                            # temp = A[4]
                            # temp = 12
                        # A[j] = A[i]
                            # A[4] = A[2]
                            # A[4] = 334
                        # A[i] = temp
                            # A[2] = temp
                            # A[2] = 12
                        # Hasil a2 = [11, 12, 12, 523, 334] #5
                        # j++

            # i = i + 1
            # i = 2 + 1
                # LOOP 0, i=3 j=i/j=3, index 3 > index 3
                        # A[i] > A[j]
                        # A[3] > A[3]  -> i
                        # 523 > 523, false
                            # Hasil a2 = [11, 12, 12, 523, 334] #5
                            # j++
                # LOOP 1, i=3 j=i/j=4, index 3 > index 4
                        # A[i] > A[j]
                        # A[3] > A[4]  -> i
                        # 523 > 334, true
                            # temp = A[j]
                                # temp = A[4]
                                # temp = 334
                            # A[j] = A[i]
                                # A[4] = A[3]
                                # A[4] = 523
                            # A[i] = temp
                                # A[3] = temp
                                # A[3] = 334
                            # Hasil a2 = [11, 12, 12, 334, 523] #5
                            # j++

            # i = i + 1
            # i = 3 + 1
                # LOOP 0, i=4 j=i/j=4, index 4 > index 4
                        # A[i] > A[j]
                        # A[4] > A[4]  -> i
                        # 523 > 523, false
                            # Hasil a2 = [11, 12, 12, 334, 523] #5
                            # j++

                temp = A[j]
                A[j] = A[i]
                A[i] = temp
            print(A)
        i=i+1
    return A

a2 = [11, 334, 523, 12, 12] #5
print (SelectionSort(5, a2))

print("\n")
print("Muhamad Salman Adhim Baqy")
print("A11.2020.12641")
print("\n")