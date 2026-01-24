import random

def dosya_oku(yol):
    # Verilen yol üzerinden metin dosyasını okur.
    #Her satırı (Makine No, İşlem Süresi) çiftlerinden oluşan bir listeye çevirir.
    try:
        with open(yol, 'r') as f: satirlar = f.readlines()
        return [[(int(s.split()[i]), int(s.split()[i+1])) for i in range(0, len(s.split()), 2)] for s in satirlar[1:]]
    except FileNotFoundError: return []

def generate_initial(isler, rastgelelik=True):
    cozum = [i for i, ops in enumerate(isler) for _ in ops]
    if rastgelelik: random.shuffle(cozum)
    return cozum

def makespan(isler, en_iyi_cozum):
    m = {} # Makinelerin ne zaman boşa çıkacağı
    j = {} # İşlerin hazır olma durumu
    c = {} # Sayaç

    for i in en_iyi_cozum:
        # Walrus ile 'op' değerini alıyoruz
        if (op := c.get(i, 0)) < len(isler[i]):
            paket = isler[i][op]   
            
            mac  = paket[0]        
            sure = paket[1]        
            
            bitis_zamani = max(m.get(mac, 0), j.get(i, 0)) + sure
            
            m[mac] = bitis_zamani  # Makineyi güncelle
            j[i]   = bitis_zamani  # İşi güncelle
            
            c[i] = op + 1 

    return max(m.values()) if m else 9999