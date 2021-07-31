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

a2 = [11, 334, 523, 12, 12] #5
print (insertionSort(5, a2))