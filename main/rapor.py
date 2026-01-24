import pandas as pd
import matplotlib.pyplot as plt
import random
import os

# ========================================================
# 1. DOSYA VE KLASÖR YAPILANDIRMASI
# ========================================================
def klasor_hazirla(algoritma, dosya, tur_sayisi):
    instance_name = os.path.splitext(os.path.basename(str(dosya)))[0]
    yol = os.path.join("Raporlar", f"{tur_sayisi}_{algoritma}_{instance_name}")
    os.makedirs(yol, exist_ok=True)
    return os.path.join(yol, f"Sonuc_{tur_sayisi}_{algoritma}_{instance_name}"), instance_name

# ========================================================
# 2. GANTT VERİSİNİ HESAPLA
# ========================================================
def prepare_gantt_data(isler, en_iyi_cozum):
    data, m_times, j_times, op_counts = [], {}, {}, {}

    for job_id in en_iyi_cozum:
        op_idx = op_counts.get(job_id, 0); op_counts[job_id] = op_idx + 1
        if op_idx >= len(isler[job_id]): continue

        machine, duration = isler[job_id][op_idx]
        
        start = max(m_times.get(machine, 0), j_times.get(job_id, 0))
        end = start + duration
        
        m_times[machine] = j_times[job_id] = end
        
        data.append({
            "Job_ID": job_id,
            "Op_ID": op_idx,
            "Machine_ID": machine, 
            "Duration": duration,
            "Start_Time": start,
            "End_Time": end
        })
    return data

# ========================================================
# 3. TXT RAPORU OLUŞTUR
# ========================================================
def txt_olustur(yol, info, sequence):
    metin = f"""
    =========================================
              SONUÇ RAPORU (RESULT)
    =========================================
    Instance Name   : {info['dosya']}
    Algorithm       : {info['algo']}
    Total Iteration : {info['t_tur']}
    Best Makespan   : {info['skor']}
    Found At        : {info['b_tur']}
    Time (sec)      : {info['sure']:.2f}
    =========================================
    Sequence:
    {sequence}
    =========================================
    """
    print(metin)
    with open(f"{yol}.txt", "w", encoding="utf-8") as f: f.write(metin)

# ========================================================
# 4. GANTT ŞEMASI ÇİZ (MATPLOTLIB)
# ========================================================
def grafik_ciz(yol, gantt_data, makespan):
    plt.figure(figsize=(12, 6))
    random.seed(42)
    colors = {d["Job_ID"]: f"#{random.randint(0, 0xFFFFFF):06x}" for d in gantt_data}

    for d in gantt_data:
        plt.barh(d["Machine_ID"], d["Duration"], left=d["Start_Time"], 
                 color=colors[d["Job_ID"]], edgecolor='black')
        
        if d["Duration"] > 2:
            plt.text(d["Start_Time"] + d["Duration"]/2, d["Machine_ID"], 
                     str(d["Job_ID"]), color='white', ha='center', va='center', fontsize=8)

    plt.title(f"Gantt Chart (Makespan: {makespan})")
    plt.xlabel("Time"); plt.ylabel("Machine")
    plt.savefig(f"{yol}.png")
    plt.close()

# ========================================================
# 5. EXCEL ÇIKTISI OLUŞTUR
# ========================================================
def excel_olustur(yol, gantt_data, gecmis):
    with pd.ExcelWriter(f"{yol}.xlsx") as writer:
        pd.DataFrame(gecmis, columns=["Iteration", "Best_Makespan"]).to_excel(writer, sheet_name="History", index=False)
        pd.DataFrame(gantt_data).to_excel(writer, sheet_name="Schedule", index=False)

# ========================================================
# 6. ANA FONKSİYON (MAIN TARAFINDAN ÇAĞRILIR)
# ========================================================
def export(algo, dosya, isler, en_iyi_cozum, makespan, sure, found_iter, tur_sayisi, gecmis):
    
    # A. Dosya yolunu hazırla
    save_path, instance_name = klasor_hazirla(algo, dosya, tur_sayisi)
    
    # B. Gantt verisini hesapla (Yeni fonksiyon ismiyle)
    gantt_data = prepare_gantt_data(isler, en_iyi_cozum)
    
    # C. Bilgileri paketle
    info = {
        "algo": algo,
        "dosya": instance_name,
        "skor": makespan,
        "b_tur": found_iter,
        "t_tur": tur_sayisi,
        "sure": sure
    }
    
    # D. Çıktıları üret
    txt_olustur(save_path, info, en_iyi_cozum)
    grafik_ciz(save_path, gantt_data, makespan)
    excel_olustur(save_path, gantt_data, gecmis)
    
    print(f">> Files saved: {save_path}.*")