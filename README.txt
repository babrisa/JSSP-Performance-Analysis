# JSSP Algoritma Kıyaslaması 🏭

Bu proje, Endüstri Mühendisliği ile ortak aldığımız ders kapsamında, meşhur İş Atölyesi Çizelgeleme problemini çözmek için hazırlandı.

Amacımız: Derste gördüğümüz algoritmaları kodlayıp hangisinin daha hızlı ve verimli çalıştığını test etmekti.

* **Simulated Annealing (SA):** Tek çözümle ilerliyor, inanılmaz hızlı. (Favorim)
* **Tabu Search (TS):** "Tabu Listesi" sayesinde takılmadan ilerliyor.
* **Genetik Algoritma (GA):** Evrim mantığıyla, popülasyonla çalışıyor.
* **Hibrit:** GA ve yerel arama yöntemlerinin karışımı (En güçlüsü ama en ağırı).

## ⚙️ Çalıştırma

Gerekli kütüphaneleri kurup maini çalıştırmanız yeterli:

```bash
pip install pandas openpyxl
python main.py

## 📊 Örnek Sonuçlar (ft10)

Yaptığım testler sonucunda algoritmaların performans karşılaştırması şöyledir:

| Algoritma | Tür | Hız | En İyi Makespan |
| :--- | :--- | :--- | :--- |
| **Simulated Annealing** | Tek Çözüm | 🚀 Çok Hızlı | 930 |
| **Tabu Search** | Tek Çözüm | ⚡ Hızlı | 945 |
| **Genetic Algorithm** | Popülasyon | 🐢 Yavaş | 980 |
| **Hibrit Algoritma** | Karma | 🐢 Yavaş | 928 |
