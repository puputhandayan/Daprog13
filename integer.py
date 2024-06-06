def konversiinteger(teks):
    try:
        nilai_integer = int(teks)
        print(f"Nilai integer adalah {nilai_integer}")
    except ValueError:
        print("Kesalahan: Integer tidak valid")

konversiinteger("123") 
konversiinteger("abc")
