# data = {}

# class datapeternakan:

#     def __init__(self):
#         self.nomorhewan = str(input('Masukkan Nomor Hewan : '))
#         self.namahewan = str(input('Masukkan Nama Hewan : '))
#         self.masukan()

#     def masukan(self):
#         data[self.nomorhewan] = self.namahewan
#         print(data)

# print('\n')
# datapeternakan()
# print('\n')

# class SLL :
#     class node:
#         def __init__(self, element, nextlink = None) :
#             self.element = element
#             self.nextnode = nextlink 

#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def __str__(self):
#         result = " "
#         pointer = self.head
#         while pointer != None:
#             result = result + str(pointer.element) + " "
#             pointer = pointer.nextnode
#         return result

#     def tambah(self, element):   
#         nodebaru = self.node(element)
#         nodebaru.nextnode = self.head
#         self.head = nodebaru
#         self.size += 1
        
#     def __len__(self):
#         return self.size

# def main():
#     Listku = SLL()
#     Listku.tambah(input('Bulan belanja : '))
#     print("\n")
#     print("Single Linked List : ", str(Listku))
#     print("Jumlah Pengeluaran Bulan Ini  : Rp", int(input('Masukkan Jumlah Pengeluaran : ')))
#     print("\n")
# main()
