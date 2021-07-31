def sum(x): 
    res = 0 
    # res adalah variable untuk menyimpan angka yang dijumlahkan
    # T = 1, karena ada sebuah assignment
    for i in range(x + 1):
        # melooping i dari x + 1, misal x = 2, maka
        # for i in range(2 + 1)
        # akan terdapat 3 kali looping dari 0 sampai 2
        res += i
        # looping 1
        # res += i
        # res = 0 + 0 = 0
        # T = 2, karena terdapat 1 assignment dan 1 operasi
        # return 0
        # T = 1, karena terdapat 1 assignment

        # looping tersebut diulang sampai 3 kali, maka
        # menjadi T = 2 dikali 3 kali looping
        # dan T = 1 dikali 3 kali looping untuk return
    return res
    # untuk loop dari for i in range(2 + 1), memiliki T = 3
    # maka rumusnya adalah (3 * 3) + 1 atau 1 + 3x


        