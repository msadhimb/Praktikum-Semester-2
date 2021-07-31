jam = int(input("Jam berapa sekarang : "))

if 7 <= jam < 12:
    print("Pagi")
elif 12 <= jam < 15:
    print("Siang")
elif 15 <= jam < 18:
    print("Sore")
elif 18 <= jam < 24:
    print("Malam")