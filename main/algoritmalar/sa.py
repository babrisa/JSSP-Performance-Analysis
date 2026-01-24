import random, math, model

def run(isler, tur_sayisi, sicaklik, sogutma):
    # -----------------------------------------
    # 1. BAŞLANGIÇ DURUMU
    # -----------------------------------------
    mevcut  = model.generate_initial(isler)
    mevcut_skor = model.makespan(isler, mevcut)
    
    # En iyiyi (Rekoru) sakla
    en_iyi_cozum  = mevcut[:]
    best_skor = mevcut_skor
    
    gecmis = [] # Rapor için kayıt listesi

    # -----------------------------------------
    # 2. ANA DÖNGÜ (SOĞUTMA SÜRECİ)
    # -----------------------------------------
    for tur in range(tur_sayisi):
        
        # A. Komşu Üret (Swap Hareketi)
        # Mevcut çözümün kopyasını alıp iki işin yerini değiştiriyoruz
        aday = mevcut[:]
        a, b = random.sample(range(len(aday)), 2)
        aday[a], aday[b] = aday[b], aday[a]
        
        aday_skor = model.makespan(isler, aday)
        
        # B. Kabul Kriteri (Metropolis)
        # Fark < 0 ise (daha iyiyse) KESİN kabul et.
        # Fark > 0 ise (kötüyse) sıcaklığa bağlı bir olasılıkla kabul et.
        fark = aday_skor - mevcut_skor
        
        kabul_olasiligi = math.exp(-fark / sicaklik) if fark > 0 else 1.0
        
        if random.random() < kabul_olasiligi:
            mevcut, mevcut_skor = aday, aday_skor
            
            # Eğer rekor kırıldıysa kaydet
            if mevcut_skor < best_skor:
                en_iyi_cozum, best_skor = mevcut[:], mevcut_skor
                bulunan_tur = tur
        # C. Soğutma ve Kayıt
        sicaklik = sogutma * sicaklik
        gecmis.append((tur, best_skor))
            
    return en_iyi_cozum, best_skor, bulunan_tur, gecmis