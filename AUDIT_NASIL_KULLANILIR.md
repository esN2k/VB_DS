# Audit Script Kullanım Kılavuzu

## Ne İşe Yarar?

`src/audit_repo.py` scripti, projeyi SON HALİYLE inceler ve güncel durum raporu çıkarır.
Bu script bir "Repo Auditor + Data Science Proje Koçu" görevi görür.

## Nasıl Çalıştırılır?

### Adım 1: Bağımlılıkları Yükle

```powershell
pip install -r requirements.txt
```

### Adım 2: Audit Scriptini Çalıştır

```powershell
python -m src.audit_repo
```

### Adım 3: Raporu İncele

Script çalıştırıldıktan sonra:
- Rapor ekrana yazdırılır
- `DURUM_RAPORU.md` dosyası oluşturulur (proje kök dizininde)

## Rapor İçeriği

Rapor şu bölümleri içerir:

### 1) Şu an proje ne durumda?
- Problem tanımı ve hedef değişken
- Kullanılan veri set(ler)i, dosya adları ve yolları
- En son üretilen çıktılar (reports/*, data/processed/*)
- Modeller ve metrikler (dosyadan okunan gerçek değerler)
- Ablation / ek deneyler (drop_geo, grid search vb.)
- Feature engineering özeti
- Rapor ve sunum dosyalarının durumu

### 2) Repo Envanteri
- Ağaç görünümü (src/, notebooks/, reports/, data/)
- Önemli dosyalar ve ne işe yaradığı

### 3) ÇALIŞIYOR mu? Doğrulaması
- Venv kontrol adımları
- `python -m src.run_pipeline` komutu ve beklenen çıktılar
- Notebook durumu

### 4) Riskler ve Hoca Soruları
- Overfit riski
- Leakage (veri sızıntısı)
- log1p + shift kullanımı
- Geo kolonları etkisi
- Outlier yaklaşımı
- Her biri için savunma cümleleri

### 5) Teslim için eksikler (P0/P1/P2)
- P0: Kesin şartlar (olmadan teslim edilmez)
- P1: Puan artıranlar (olması iyi)
- P2: Opsiyonel (bonus)

### 6) Doğukan ağzıyla güncel özet
- Tek paragraf öğrenci diliyle özet

## Örnek Kullanım

```powershell
# Sanal ortamı aktif et (gerekiyorsa)
.venv\Scripts\activate

# Audit yap
python -m src.audit_repo

# Raporu oku
type DURUM_RAPORU.md  # Windows
# cat DURUM_RAPORU.md   # Linux/Mac
```

## Notlar

- Script hiçbir değişiklik yapmaz, sadece okur ve rapor üretir
- Tüm metrikler dosyalardan okunur (varsayım yapılmaz)
- Eksik dosyalar net şekilde işaretlenir (✗)
- Mevcut dosyalar işaretlenir (✓) ve boyutları gösterilir

## Sorun Giderme

**Hata: `ModuleNotFoundError: No module named 'pandas'`**
- Çözüm: `pip install -r requirements.txt` komutunu çalıştır

**Hata: Dosya bulunamadı**
- Scriptin proje kök dizininde (`VB_DS/`) çalıştırıldığından emin ol
- Ham veri dosyasının `data/raw/SampleSuperstore.csv` konumunda olduğunu kontrol et

**Raporda bazı dosyalar eksik görünüyor**
- Normal! Script mevcut durumu gösterir
- Eksik dosyaları oluşturmak için `python -m src.run_pipeline` çalıştır
