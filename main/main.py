import time, model, rapor
from algoritmalar import sa, tabu, genetik, hibrit

dosya, tur_sayisi, algoritma = "ft10.txt", 5000, "SA"

def baslat():
    yol = f"main/test/{dosya}"
    isler = model.dosya_oku(yol)
    if not isler: return print("Dosya yok!")

    print(f"> {algoritma} ({tur_sayisi} Tur) çalışıyor...")
    t1 = time.time()

    # Algoritma seçimi
    if   algoritma == "SA":      sonuc = sa.run(isler, tur_sayisi, 1000, 0.9995)     # Başlangıç Sıcaklığı, Soğutma Katsayısı
    elif algoritma == "TABU":    sonuc = tabu.run(isler, tur_sayisi, 50)             # Tabu Listesi Uzunluğu
    elif algoritma == "GENETIK": sonuc = genetik.run(isler, tur_sayisi, 100, 10)     # Popülasyon Boyutu, Mutasyon Oranı
    elif algoritma == "HIBRIT":  sonuc = hibrit.run(isler, tur_sayisi, 100, 10)      # Popülasyon Boyutu, Mutasyon Oranı 
    else: return print("Hata: Algoritma ismi yanlış!")

    rapor.export(algoritma, yol, isler, sonuc[0], sonuc[1], time.time() - t1, sonuc[2], tur_sayisi, sonuc[3])
baslat()