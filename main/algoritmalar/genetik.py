import random, model

def mutation(gen):
    # Rastgele iki konum seç (a ve b)
    a, b = random.sample(range(len(gen)), 2)
    # Bu iki konumdaki işlerin yerini değiştir (Swap)
    gen[a], gen[b] = gen[b], gen[a]
    return gen

def crossover(anne, baba):
    cocuk, hedef = anne[:], random.choice(baba)# Çocuk annenin kopyasıdır
    if hedef in cocuk:
        # Babadan rastgele bir gen seçip, çocukta (annede) yer değiştiriyoruz
        i1, i2 = cocuk.index(hedef), cocuk.index(random.choice(cocuk))
        cocuk[i1], cocuk[i2] = cocuk[i2], cocuk[i1]
    return cocuk

def run(isler, tur_sayisi, pop_boy, mutation_rate):
    # Popülasyonu (ilk nesli) rastgele oluştur
    pop = [model.generate_initial(isler, True) for _ in range(pop_boy)]
    best_skor, en_iyi_cozum, gecmis = 9999, [], []
    bulunan_tur = 0
    for tur in range(tur_sayisi):
        # Makespan süresi en düşük (en iyi) olanı listenin en başına (0. indexe) alır.
        pop.sort(key=lambda k: model.makespan(isler, k))
        
        skor = model.makespan(isler, pop[0])
        if skor < best_skor:
            best_skor, en_iyi_cozum = skor, pop[0][:]
            bulunan_tur = tur
            print(f"[GENETIK] Tur {tur} -> {best_skor}")
        gecmis.append((tur, best_skor))
        # ELİTİZM (Elitism): En iyi bireyi (pop[0]) hiç bozmadan yeni nesle aktar.
        yeni_pop = [pop[0]]
        while len(yeni_pop) < pop_boy:
            # SEÇİM (Selection): Anne ve Babayı listenin en iyi kısmından seç.
            anne = pop[random.randint(0, 5)] # 0-5 arası en iyilerdir
            baba = pop[random.randint(0, 10)] #0-10 arası da iyilerdir.
            cocuk = crossover(anne, baba) # Çaprazlama ile çocuk üret
            
            if random.randint(1, 100) <= mutation_rate: cocuk = mutation(cocuk)
            yeni_pop.append(cocuk)
            
            
        pop = yeni_pop # Yeni nesil artık ana popülasyon oldu
    return en_iyi_cozum, best_skor, bulunan_tur, gecmis