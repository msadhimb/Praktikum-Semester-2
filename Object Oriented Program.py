class Line:
    
    def __init__(self, Inputid, InputUsername, InputPhotosVideos, Inputpost):
        self.id = Inputid
        self.name = InputUsername
        self.photosvideos = InputPhotosVideos
        self.post = Inputpost

    def Info(self):
        print(f"\n ID : {self.id} \n Username : {self.name} \n Photos and Videos : {self.photosvideos} \n Post : {self.post} \n")
    
    def posting(self, up, status):
        self.post += up
        self.status = status
        print("Status ditambahkan ke beranda \n")
        print(f"{self.name} telah memposting sesuatu yang berbunyi {self.status}")
        print(f"Postingan total diakun anda sekarang berjumlah {self.post} \n")
        
    def getpost(self):
        return self.post

    def photos(self, upp):
        self.photosvideos += upp
        print("Menambahkan gambar dan video")
        print("Gambar dan video telah berhasil diupload \n")
        print(f"{self.name} menambahkan sebuah gambar atau video sejumlah {upp} buah")
        print(f"Total gambar dan video diakun anda adalah {self.photosvideos}, serta total postingan diakun anda adalah {self.post + upp} \n")
adhim = Line("sepatuxx", "hntrzlmn", 6, 7)
salman = Line("sal212", "nmlzrtnh", 1, 100)

adhim.Info()
adhim.posting((int(input("Jumlah post yang anda tulis : "))), str(input("Tulis Status Anda : ")))
adhim.photos(int(input("Masukkan jumlah media yang ingin anda tambahkan : ")))

salman.Info()
salman.posting((int(input("Jumlah post yang anda tulis : "))), str(input("Tulis Status Anda : ")))
salman.photos(int(input("Masukkan jumlah media yang ingin anda tambahkan : ")))