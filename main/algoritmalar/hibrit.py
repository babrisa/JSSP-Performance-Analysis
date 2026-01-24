import random, model

def mutation(gen):
    a, b = random.sample(range(len(gen)), 2)
    gen[a], gen[b] = gen[b], gen[a]
    return gen

def crossover(anne, baba):
    cocuk, hedef = anne[:], random.choice(baba)
    if hedef in cocuk:
        i1, i2 = cocuk.index(hedef), cocuk.index(random.choice(cocuk))
        cocuk[i1], cocuk[i2] = cocuk[i2], cocuk[i1]
    return cocuk

def local_search(gen, isler):
    # 1. ADIM: MEVCUT DURUMU YEDEKLE
    # "Elimizdeki çözüm şimdilik en iyisidir" diyerek bir kopyasını alıyoruz.
    best_g, best_s = gen[:], model.makespan(isler, gen)
    
    # 2. ADIM: 10 HAK TANI (SÖMÜRÜ LİMİTİ)
    # Sonsuza kadar arayamayız, bilgisayar yorulmasın diye 10 deneme hakkı veriyoruz.
    for _ in range(10): 
        
        # 3. ADIM: KOMŞU ÜRET (MUTASYON İLE)
        # Mevcut en iyi çözümün üzerinde ufak bir değişiklik (swap) yapıp "aday" üretiyoruz.
        aday = mutation(best_g[:])
        
        # 4. ADIM: KARŞILAŞTIRMA (TEPE TIRMANMA MANTIĞI)
        # Eğer yeni bulduğumuz aday, elimizdeki 'best'ten daha kısa sürede bitiyorsa (daha iyiyse)...
        if model.makespan(isler, aday) < best_s: 
            
            # ...Onu yeni 'best' ilan et. (Kötüyse hiçbir şey yapma, eskisi kalsın)
            best_g, best_s = aday, model.makespan(isler, aday)
            
    # 5. ADIM: SONUÇ
    # 10 denemenin sonunda elindeki en iyi hali geri döndür.
    return best_g

def run(isler, tur_sayisi, pop_boy, mutation_rate):
    pop = [model.generate_initial(isler, True) for _ in range(pop_boy)]
    best_skor, en_iyi_cozum, gecmis = 9999, [], []
    bulunan_tur = 0
    for tur in range(tur_sayisi):
        pop.sort(key=lambda k: model.makespan(isler, k))
        pop[0] = local_search(pop[0], isler) # --- EKSTRA SATIR ---
        skor = model.makespan(isler, pop[0])
        if skor < best_skor:
            best_skor, en_iyi_cozum = skor, pop[0][:]
            bulunan_tur = tur
            print(f"[HIBRIT] Tur {tur} -> {best_skor}")
        gecmis.append((tur, best_skor))

        yeni_pop = [pop[0]]
        while len(yeni_pop) < pop_boy:
            anne, baba = pop[random.randint(0, 5)], pop[random.randint(0, 10)]
            cocuk = crossover(anne, baba)
            if random.randint(1, 100) <= mutation_rate: cocuk = mutation(cocuk)
            yeni_pop.append(cocuk)
        pop = yeni_pop
    return en_iyi_cozum, best_skor, bulunan_tur, gecmis