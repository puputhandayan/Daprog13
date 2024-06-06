def akseselemen(daftar_list, indeks):
    try:
        elemen = daftar_list[indeks]
        print(f"Elemen di indeks {indeks} adalah {elemen}")
    except IndexError:
        print("Kesalahan: Indeks di luar jangkauan")

list_saya = [1, 2, 3]
akseselemen(list_saya, 1) 
akseselemen(list_saya, 5)