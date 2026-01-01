# 🎯 PROJE DURUM RAPORU SİSTEMİ - KULLANICI KILAVUZU

## 📋 Özet

Bu döküman, VB_DS projesine eklenen **Repo Auditor + Data Science Proje Koçu** sistemini açıklar.
Sistem, projenizi otomatik olarak inceler ve güncel durum raporu oluşturur.

---

## 🚀 Hızlı Başlangıç

### Tek Komutla Rapor Oluştur

```bash
# Bağımlılıkları yükle (ilk sefer)
pip install -r requirements.txt

# Rapor oluştur
python -m src.audit_repo
```

**Sonuç:** `DURUM_RAPORU.md` dosyası oluşturulur.

---

## 📁 Oluşturulan Dosyalar

### 1. `src/audit_repo.py` (Ana Script)
**Boyut:** ~18 KB  
**Amaç:** Proje audit'i yapan ana Python scripti

**Özellikler:**
- Tüm dosyaları tarar ve durumlarını raporlar
- Metrikleri dosyalardan okur (varsayım yapmaz)
- Repo envanteri çıkarır
- Çalışma komutlarını listeler
- Risk analizi ve savunma cümleleri sağlar
- P0/P1/P2 eksiklikleri listeler
- Öğrenci diliyle özet üretir

### 2. `DURUM_RAPORU.md` (Üretilen Rapor)
**Boyut:** ~9 KB  
**Amaç:** Script tarafından otomatik oluşturulan güncel durum raporu

**İçerik:** 6 ana bölüm
1. Şu an proje ne durumda?
2. Repo Envanteri
3. ÇALIŞIYOR mu? Doğrulaması
4. Riskler ve Hoca Soruları
5. Teslim için Eksikler (P0/P1/P2)
6. Doğukan ağzıyla güncel özet

### 3. `AUDIT_NASIL_KULLANILIR.md` (Kullanım Kılavuzu)
**Boyut:** ~2.5 KB  
**Amaç:** Audit scriptinin nasıl kullanılacağını açıklar

### 4. `README.md` (Güncellendi)
**Güncelleme:** Audit scripti bilgisi eklendi

---

## 📊 Rapor Bölümleri Detayı

### 1️⃣ Şu an proje ne durumda?

#### Problem Tanımı ve Hedef Değişken
- Problem türü (Regresyon)
- Hedef değişken (Profit)
- Amaç

#### Kullanılan Veri Set(ler)i
- ✓ Ham veri dosyası ve boyutu
- ✓ Temizlenmiş veri dosyası ve boyutu

#### En Son Üretilen Çıktılar
- ✓/✗ her dosya için durum
- Dosya boyutları
- Lokasyonlar

#### Modeller ve Metrikler
**Dosyadan okunan gerçek değerler:**
- Full model (tüm kolonlarla)
- No-Geo model (City/State/Postal Code hariç)
- MAE, RMSE, R² metrikleri

#### Ablation / Ek Deneyler
- drop_geo testi sonuçları
- R² artış/azalışları
- Grid search durumu

#### Feature Engineering Özeti
- Tarih kolonları varsa/yoksa feature'lar
- Leakage önlemleri
- Missing value stratejisi
- Outlier yaklaşımı

#### Rapor ve Sunum Dosyaları
- ✓/✗ her dokümantasyon dosyası
- Teslim paketi durumu

---

### 2️⃣ Repo Envanteri

#### Ağaç Görünümü
```
src/
  audit_repo.py
  run_pipeline.py
  preprocess.py
  ...
notebooks/
  01_load_clean.ipynb
  ...
reports/
  metrics.csv
  ...
```

#### Önemli Dosyalar
Her dosya için:
- Dosya yolu
- Ne işe yaradığı (1 cümle)

---

### 3️⃣ ÇALIŞIYOR mu? Doğrulaması

#### Venv Kontrolü
```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### Bağımlılıkları Yükle
```powershell
pip install -r requirements.txt
```

#### Ana Pipeline Çalıştır
```powershell
python -m src.run_pipeline
```

**Beklenen çıktılar:**
- clean.csv
- metrics*.csv
- data_summary.txt
- top10_importance.csv

#### Notebook Durumu
- Hangi notebook'lar var?
- Ne zaman kullanılır?

---

### 4️⃣ Riskler ve Hoca Soruları

Her risk için:
- **Soru:** Hoca ne sorabilir?
- **Cevap:** Öğrenci diliyle 2-3 cümle savunma

**Kapsanan konular:**
1. Overfit riski
2. Leakage (veri sızıntısı)
3. log1p + shift kullanımı
4. Geo kolonları etkisi
5. Outlier yaklaşımı

---

### 5️⃣ Teslim için Eksikler (P0/P1/P2)

#### P0 (Kesin Şartlar)
- [x] Yapılmış
- [ ] Yapılmamış

#### P1 (Puan Artıranlar)
- [x] Yapılmış
- [ ] Yapılmamış (iyileştirme önerisi)

#### P2 (Opsiyonel/Bonus)
- [ ] Yapılmamış (opsiyonel)

---

### 6️⃣ Doğukan Ağzıyla Güncel Özet

Tek paragraf, öğrenci diliyle, hocaya göndermek üzere proje özeti.

**Kapsar:**
- Ne yaptın?
- Hangi modelleri kullandın?
- Önemli bulgular neler?
- Ne hazır, ne eksik?
- Proje çalışıyor mu?

---

## 🔍 Teknik Detaylar

### Dosya Tarama Mekanizması
```python
def find_file(project_root: Path, pattern: str) -> list[Path]:
    return list(project_root.rglob(pattern))
```

### Metrik Okuma
```python
def read_metrics_file(path: Path) -> Optional[pd.DataFrame]:
    if path.exists():
        return pd.read_csv(path)
    return None
```

### Dosya Varlığı Kontrolü
```python
def check_file_exists(path: Path, desc: str) -> tuple[bool, str]:
    if path.exists():
        size_kb = path.stat().st_size / 1024
        return True, f"✓ {desc}: {path} ({size_kb:.1f} KB)"
    return False, f"✗ {desc}: {path} (BULUNAMADI)"
```

---

## ⚙️ Özelleştirme

### Kendi Riskini Eklemek

`src/audit_repo.py` dosyasında `risks` listesine ekle:

```python
risks = [
    # ... mevcut riskler ...
    {
        "soru": "Yeni risk sorusu?",
        "cevap": "Öğrenci diliyle cevap...",
    },
]
```

### Yeni Çıktı Dosyası Eklemek

`output_files` listesine ekle:

```python
output_files = [
    # ... mevcut dosyalar ...
    ("yeni_dosya.csv", "Açıklama"),
]
```

---

## 🐛 Sorun Giderme

### Hata: ModuleNotFoundError
**Çözüm:**
```bash
pip install -r requirements.txt
```

### Hata: Dosya bulunamadı
**Kontroller:**
1. Scriptin proje kök dizininde çalıştırıldığından emin ol
2. Ham veri `data/raw/SampleSuperstore.csv` konumunda olmalı

### Raporda eksik dosyalar görünüyor
**Normal!** Script mevcut durumu gösterir.  
**Çözüm:** Pipeline'ı çalıştır:
```bash
python -m src.run_pipeline
```

---

## 📝 Örnek Kullanım Senaryoları

### Senaryo 1: İlk Audit
```bash
# Projeyi klonladın, ne durumda görmek istiyorsun
python -m src.audit_repo
```

### Senaryo 2: Pipeline Çalıştırdıktan Sonra Kontrol
```bash
# Pipeline çalıştır
python -m src.run_pipeline

# Audit ile kontrol et
python -m src.audit_repo
```

### Senaryo 3: Teslim Öncesi Final Kontrol
```bash
# Audit yap
python -m src.audit_repo

# DURUM_RAPORU.md oku
# P0/P1/P2 eksiklikleri kontrol et
# Eksikleri tamamla
```

---

## ✅ Checklist: Script Kullanımı

- [ ] requirements.txt yüklendi
- [ ] `python -m src.audit_repo` çalıştırıldı
- [ ] `DURUM_RAPORU.md` oluşturuldu
- [ ] Rapor incelendi
- [ ] P0 eksikler kontrol edildi
- [ ] Riskler için savunma cümleleri not edildi
- [ ] Doğukan ağzıyla özet okundu

---

## 🎓 Eğitim Amaçlı Notlar

Bu script bir **Repo Auditor + Data Science Proje Koçu** görevi görür.

**Öğrendikleriniz:**
1. Python ile dosya sistemi operasyonları
2. Pandas ile metrik okuma
3. Rapor oluşturma
4. Proje organizasyonu
5. Dokümantasyon standartları
6. Risk analizi
7. Önceliklendirme (P0/P1/P2)

---

## 🔗 İlgili Dökümanlar

- `README.md` - Proje ana README
- `AUDIT_NASIL_KULLANILIR.md` - Audit kullanım kılavuzu
- `RAPOR.md` - Jüriye teslim raporu
- `ADIM_ADIM.md` - Adım adım proje kurulum

---

## 📞 Destek

Sorun yaşarsan:
1. `AUDIT_NASIL_KULLANILIR.md` oku
2. Bu dosyayı tekrar oku
3. Hata mesajlarını kontrol et
4. İhtiyaç halinde kodu incele: `src/audit_repo.py`

---

**Son güncelleme:** 2026-01-01  
**Versiyon:** 1.0  
**Yazar:** GitHub Copilot
