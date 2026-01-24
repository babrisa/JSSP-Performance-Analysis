import random, model

def swap_move(cozum):
    yeni = cozum[:]
    a, b = random.sample(range(len(yeni)), 2)
    yeni[a], yeni[b] = yeni[b], yeni[a]
    return yeni, tuple(sorted((a, b)))
    # Sadece yeni çözümü değil, hangi işlerin yerini değiştirdiğimizi (a, b) de döndürüyoruz.

def run(isler, tur_sayisi, tabu_uzunlugu):
    # --- 1. BAŞLANGIÇ ---
    mevcut = model.generate_initial(isler, rastgelelik=False)
    best_skor, en_iyi_cozum = model.makespan(isler, mevcut), mevcut[:]
    
    tabu_list, elite_list, gecmis = [], [], []
    stagnation_counter, bulunan_tur = 0, 0

    for tur in range(tur_sayisi):
        # --- 2. KOMŞU ARAŞTIRMASI (20 ADAY) ---
        komsular = []
        for _ in range(20):
            aday, hareket = swap_move(mevcut)
            komsular.append((model.makespan(isler, aday), aday, hareket))
        
        # Filtre: Yasaklı olmayanlar VEYA Rekor kıranlar (Aspiration Criteria)
        # Tabu listesinde olsa BİLE, eğer rekor kırıyorsa (k[0] < best_skor) izin ver.
        gecerli = [k for k in komsular if k[2] not in tabu_list or k[0] < best_skor]

        if gecerli:
            # En iyi komşuya git
            skor, aday, hareket = min(gecerli, key=lambda x: x[0])
            mevcut = aday
            
            # Tabu Listesini Güncelle
            tabu_list.append(hareket)
            #(FIFO - First In First Out)
            if len(tabu_list) > tabu_uzunlugu: tabu_list.pop(0)

            # Rekor Kontrolü
            if skor < best_skor:
                best_skor, en_iyi_cozum, bulunan_tur = skor, aday[:], tur
                elite_list.append(aday[:])
                if len(elite_list) > 10: elite_list.pop(0)
                stagnation_counter = 0; print(f"[TABU] Tur {tur}: Rekor -> {best_skor}")
            else: stagnation_counter += 1

        # --- 3. STAGNATION ---
        if stagnation_counter > 50:
            # A Planı: Hafızandaki en iyi çözümlerden (Elite List) rastgele birine geri dön.
            # B Planı: Liste boşsa tamamen rastgele bir çözümle (Restart) başla.
            mevcut = random.choice(elite_list)[:] if elite_list else model.generate_initial(isler, True)
            stagnation_counter = 0 
            print("[TABU] Geri Sıçrama.")
            
        gecmis.append((tur, best_skor))

    return en_iyi_cozum, best_skor, bulunan_tur, gecmis