# JSSP Algoritma Karşılaştırması (ft10)

Bu projede, meşhur **ft10** veri setini kullanarak Atölye Çizelgeleme Problemini (JSSP) çözmeye çalıştım. 

Amacımız projede gördüğümüz 4 farklı algoritmayı kodlayıp, hangisinin daha hızlı ve daha iyi sonuç verdiğini kendi gözlerimle görmekti.

## 🧪 Neleri Denedim? (Kullandığım Algoritmalar)

Proje içinde şu algoritmaları Python ile yazdım:

* **Simulated Annealing (SA):** Favorim bu oldu. Tek bir çözüm üzerinden gittiği için inanılmaz hızlı çalışıyor.
* **Tabu Search (TS):** Bu da tek çözümle ilerliyor ama "Tabu Listesi" sayesinde sürekli aynı yerlere takılmıyor.
* **Genetic Algorithm (GA):** Popülasyonla (yani kalabalık bir orduyla) çalıştığı için biraz yavaş kalıyor ama mantığı çok sağlam.
* **Hibrit:** GA ve yerel arama (local search) yöntemlerini birleştirmeyi denedim.

## ⚙️ Nasıl Çalıştırılır?

Kodları çalıştırmak için ekstra karmaşık ayarlara gerek yok.

1.  Önce Excel çıktısı alabilmek için gerekli kütüphaneleri kurun:
    ```bash
    pip install pandas openpyxl
    ```

2.  Sonra testi başlatın:
    ```bash
    python main.py
    ```

*Not: `main.py` dosyasının içindeki `SECILEN_ALGORITMA` kısmını değiştirerek diğer algoritmaları da tek tek deneyebilirsiniz.*

## 📊 Aldığım Sonuçlar

Kendi bilgisayarımda yaptığım denemelerde şunları gördüm. Simulated Annealing (SA) hem çok hızlı hem de en iyi sonucu en kısa sürede buluyor.

| Algoritma | Tür | Hız Durumu | En İyi Sonuç (Makespan) |
| :--- | :--- | :--- | :--- |
| **Simulated Annealing** | Tek Çözüm | 🚀 Çok Hızlı | **930** |
| **Tabu Search** | Tek Çözüm | ⚡ Hızlı | 945 |
| **Genetik Algoritma** | Popülasyon | 🐢 Biraz Yavaş | 980 |

---
**Hazırlayan:** Barış Yıldız