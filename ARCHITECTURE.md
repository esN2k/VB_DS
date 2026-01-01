# ARCHITECTURE - Proje Mimarisi ve Pipeline Akışı

## 📐 Genel Bakış

VB_DS projesi modüler bir yapıya sahip veri bilimi pipeline'ıdır. Veri yükleme, temizleme, feature engineering, model eğitimi ve değerlendirme adımlarını içerir.

---

## 🔄 Pipeline Akış Diyagramı

```
┌─────────────────────────────────────────────────────────────────┐
│                    VB_DS PROFIT TAHMİNİ PIPELINE                │
└─────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐
    │  Ham Veri        │
    │  SampleSuperstore│
    │  .csv            │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  VERİ YÜKLEME    │
    │  (load_raw)      │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  VERİ TEMİZLEME  │
    │  - Missing: median/mode
    │  - Strip kategorik
    │  - Outlier raporu (IQR)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  FEATURE ENG.    │
    │  - sales_per_item
    │  - discounted_sales
    │  - profit_margin
    │  - is_high_discount
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  KAYDET          │
    │  clean.csv       │
    └────────┬─────────┘
             │
             ├──────────────────┐
             │                  │
             ▼                  ▼
    ┌─────────────────┐  ┌─────────────────┐
    │  MODEL EĞİTİMİ  │  │  MODEL EĞİTİMİ  │
    │  (Full)         │  │  (No-Geo)       │
    │  + Geo kolonlar │  │  - Geo kolonlar │
    └────────┬────────┘  └────────┬────────┘
             │                    │
             ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐
    │  LinearReg      │  │  LinearReg      │
    │  RandomForest   │  │  RandomForest   │
    └────────┬────────┘  └────────┬────────┘
             │                    │
             ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐
    │  Metrikler      │  │  Metrikler      │
    │  metrics_full   │  │  metrics_no_geo │
    │  .csv           │  │  .csv           │
    └─────────────────┘  └─────────────────┘
             │                    │
             └──────────┬─────────┘
                        │
                        ▼
            ┌──────────────────────┐
            │  RAPORLAR            │
            │  - metrics.csv       │
            │  - top10_importance  │
            │  - data_summary.txt  │
            │  - figures/*.png     │
            └──────────────────────┘
```

---

## 📁 Klasör ve Dosya Yapısı

```
VB_DS/
│
├── data/
│   ├── raw/
│   │   └── SampleSuperstore.csv      # Ham veri (9,994 satır)
│   └── processed/
│       └── clean.csv                  # Temizlenmiş veri
│
├── src/
│   ├── __init__.py                    # Python paketi
│   ├── run_pipeline.py                # ★ Ana pipeline (veri + model)
│   ├── preprocess.py                  # Veri temizleme + feature eng.
│   ├── train.py                       # Model eğitimi (kullanılmıyor)
│   ├── evaluate.py                    # Metrik hesaplama
│   ├── audit_repo.py                  # ★ Proje durum raporu
│   ├── app_streamlit.py               # ★ Streamlit uygulaması
│   └── make_figures.py                # ★ EDA görselleri
│
├── notebooks/
│   ├── 01_load_clean.ipynb            # Veri yükleme/temizleme
│   ├── 02_eda.ipynb                   # Keşifsel veri analizi
│   └── 03_model.ipynb                 # Model eğitimi/değerlendirme
│
├── reports/
│   ├── data_summary.txt               # Veri özet istatistikleri
│   ├── metrics.csv                    # Model metrikleri (ana)
│   ├── metrics_full.csv               # Full model metrikleri
│   ├── metrics_no_geo.csv             # No-Geo model metrikleri
│   ├── top10_importance.csv           # Top-10 feature importance
│   └── figures/                       # EDA görselleri (PNG)
│       ├── 01_profit_distribution.png
│       ├── 02_sales_vs_profit.png
│       ├── 03_category_avg_profit.png
│       ├── 04_discount_distribution.png
│       ├── 05_correlation_heatmap.png
│       └── 06_region_profit_boxplot.png
│
├── deliverables/
│   └── teslim_paketi/                 # Teslim dosyaları (ZIP)
│
├── requirements.txt                   # Python bağımlılıkları
├── README.md                          # Proje README
├── RAPOR.md                           # Jüriye teslim raporu
├── OZET_SONUC.md                      # Tek sayfalık özet
├── SUNUM.md                           # Sunum notları
├── SUNUM_SLIDES.pptx                  # PowerPoint sunumu
├── SUNUM_SLIDES.pdf                   # PDF sunumu
├── ADIM_ADIM.md                       # Adım adım talimatlar
├── INSTRUCTIONS.md                    # Basit talimatlar
├── DURUM_RAPORU.md                    # ★ Güncel durum raporu
├── DEMO_SCRIPT.md                     # ★ Canlı demo senaryosu
├── JURI_SUNUM_AKISI.md               # ★ Jüri sunum metni
├── ARCHITECTURE.md                    # ★ Bu dosya
└── CHANGELOG.md                       # ★ Değişiklik günlüğü
```

**★ = Yeni eklenen dosyalar**

---

## 🔧 Modül ve Fonksiyon Açıklamaları

### 1. `src/run_pipeline.py` (Ana Pipeline)

**Ana Fonksiyon:** `main()`

**Görevler:**
1. Ham veriyi yükle (`load_raw`)
2. Veriyi temizle (`clean_data`)
3. Feature engineering yap (`feature_engineering`)
4. Temizlenmiş veriyi kaydet
5. Veri özetini oluştur
6. Full model eğit (tüm kolonlarla)
7. No-Geo model eğit (City/State/Postal Code hariç)
8. Metrikleri kaydet

**CLI Parametreleri:**
- `--drop-geo`: Geo kolonlarını çıkar
- `--seed`: Random seed (default: 42)
- `--output-dir`: Çıktı dizini (default: reports/)

**Örnek:**
```bash
python -m src.run_pipeline --seed 42
```

---

### 2. `src/preprocess.py` (Veri İşleme)

**Fonksiyonlar:**

- `load_raw(path)`: Ham veriyi CSV'den yükle
- `clean_data(df)`: Veri temizleme
  - Missing: sayısal → median, kategorik → mode
  - Kategorik strip (boşluk temizleme)
  - Tarih dönüşümleri
- `feature_engineering(df)`: Feature türetme
  - `sales_per_item`
  - `discounted_sales`
  - `profit_margin`
  - `is_high_discount`
- `report_outliers(df)`: IQR ile outlier raporu (silmez!)
- `save_processed(df, path)`: Temizlenmiş veriyi kaydet

---

### 3. `src/train.py` (Model Eğitimi)

**Not:** Şu anda kullanılmıyor. Model eğitimi `run_pipeline.py` içinde yapılıyor.

---

### 4. `src/evaluate.py` (Metrik Hesaplama)

**Fonksiyon:** `evaluate_regression(y_true, y_pred)`

**Döndürür:**
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² (Coefficient of Determination)

---

### 5. `src/audit_repo.py` (Proje Durum Raporu)

**Görev:** Projenin güncel durumunu tarar ve DURUM_RAPORU.md oluşturur.

**Kontroller:**
- Dosya varlığı (✓/✗)
- Metrikler (dosyadan okunur)
- Ortam bilgisi (Python versiyon, cwd, timestamp)
- Repo envanteri
- Risk analizi
- P0/P1/P2 eksikler

**Örnek:**
```bash
python -m src.audit_repo
```

---

### 6. `src/app_streamlit.py` (Web Uygulaması)

**Görev:** İnteraktif Streamlit uygulaması (jüri demosu için)

**Sekmeler:**
1. **Veri Özeti:** Shape, missing, kolon tipleri, filtreler
2. **EDA Grafikleri:** Histogram, scatter, korelasyon matrisi
3. **Model Sonuçları:** Metrikler, karşılaştırma, feature importance

**Örnek:**
```bash
streamlit run src/app_streamlit.py
```

---

### 7. `src/make_figures.py` (Görsel Oluşturma)

**Görev:** EDA grafiklerini PNG olarak kaydeder.

**Oluşturulan Grafikler:**
1. Profit dağılımı (histogram)
2. Sales vs Profit (scatter)
3. Category'ye göre avg profit (bar)
4. Discount dağılımı (histogram)
5. Korelasyon matrisi (heatmap)
6. Region'a göre profit (boxplot)

**Örnek:**
```bash
python -m src.make_figures
```

---

## 🎯 Veri Akışı Detayı

### Adım 1: Ham Veri → Temizlenmiş Veri

```
SampleSuperstore.csv (9,994 x 13)
          ↓
[load_raw] Pandas ile yükle
          ↓
[clean_data]
  - Missing imputation
  - Categorical strip
  - Outlier detection (IQR)
          ↓
[feature_engineering]
  - sales_per_item = Sales / Quantity
  - discounted_sales = Sales * (1 - Discount)
  - profit_margin = Profit / Sales
  - is_high_discount = (Discount >= 0.3)
          ↓
clean.csv (9,994 x 17)
```

### Adım 2: Temizlenmiş Veri → Model Metrikleri

```
clean.csv
    ↓
[train_test_split] 80-20 split, seed=42
    ↓
┌───────────────────┐
│  X (features)     │
│  y (Profit)       │
└─────────┬─────────┘
          │
          ├─────────────────┐
          │                 │
    [Full Model]      [No-Geo Model]
    City/State/PC     Drop City/State/PC
          │                 │
    ┌─────┴─────┐     ┌─────┴─────┐
    │  Pipeline │     │  Pipeline │
    │  - Impute │     │  - Impute │
    │  - Scale  │     │  - Scale  │
    │  - OneHot │     │  - OneHot │
    └─────┬─────┘     └─────┬─────┘
          │                 │
    ┌─────┴─────┐     ┌─────┴─────┐
    │ LinearReg │     │ LinearReg │
    │ RandomFor │     │ RandomFor │
    └─────┬─────┘     └─────┬─────┘
          │                 │
          ▼                 ▼
    metrics_full.csv  metrics_no_geo.csv
```

---

## 🧩 Bağımlılıklar

```
pandas==2.3.3         # Veri manipülasyonu
numpy==2.4.0          # Sayısal hesaplama
matplotlib==3.10.8    # Görselleştirme
scikit-learn==1.8.0   # Makine öğrenmesi
scipy==1.16.3         # Bilimsel hesaplama
streamlit>=1.28.0     # Web uygulaması
seaborn>=0.12.0       # İleri görselleştirme
```

---

## 🚀 Çalıştırma Sırası

### Tam Pipeline (Baştan Sona)

```bash
# 1. Sanal ortam
python -m venv .venv
.venv\Scripts\activate

# 2. Bağımlılıklar
pip install -r requirements.txt

# 3. Pipeline
python -m src.run_pipeline

# 4. Görseller
python -m src.make_figures

# 5. Durum raporu
python -m src.audit_repo

# 6. Streamlit
streamlit run src/app_streamlit.py
```

### Hızlı Test

```bash
# Pipeline + Audit
python -m src.run_pipeline && python -m src.audit_repo
```

---

## 📊 Çıktı Dosyaları ve Rolleri

| Dosya | Boyut | Açıklama |
|-------|-------|----------|
| `clean.csv` | ~1.4 MB | Temizlenmiş veri (9,994 x 17) |
| `metrics.csv` | ~200 B | Model metrikleri (aynı metrics_full ile) |
| `metrics_full.csv` | ~200 B | Full model metrikleri (2 model) |
| `metrics_no_geo.csv` | ~200 B | No-Geo model metrikleri (2 model) |
| `top10_importance.csv` | ~400 B | Top-10 feature importance (RF) |
| `data_summary.txt` | ~300 B | Veri özet istatistikleri |
| `figures/*.png` | ~1.1 MB | 6 adet EDA grafiği (300 DPI) |
| `DURUM_RAPORU.md` | ~9 KB | Güncel proje durumu |

---

## 🔐 Güvenlik ve Reproducibility

### Random Seed Sabitleme
- Train-test split: `random_state=42`
- RandomForest: `random_state=42`
- CLI ile değiştirilebilir: `--seed 123`

### Leakage Önlemi
- `profit_margin` feature'ı model eğitiminde drop edilir
- Çünkü doğrudan hedef (Profit) değişkeninden türetilmiş

### Log Dönüşümü
- Profit negatif olabildiği için `shift + log1p` kullanılır
- `shift = -min_val + 1.0` (negatifse)

---

## 📝 Geliştirme Notları

### Yapıldı ✅
- Veri temizleme ve feature engineering
- LinearRegression ve RandomForest modelleri
- Ablation testi (Full vs No-Geo)
- Logging eklendi (INFO seviyesi)
- CLI parametreleri (argparse)
- Streamlit uygulaması
- EDA görselleri (make_figures)
- Comprehensive dokümantasyon

### Yapılabilir (İyileştirmeler) 🔄
- Cross-validation eklenebilir
- Grid search / hiperparametre optimizasyonu
- Ek modeller (XGBoost, LightGBM)
- Feature selection / PCA
- Deployment (Docker, API)
- CI/CD pipeline

---

## 🎓 Mimari Prensipler

1. **Modülerlik:** Her modül tek sorumlulukta
2. **Reproducibility:** Random seed sabitleme
3. **Logging:** Tüm kritik adımlar loglanır
4. **CLI:** Komut satırı ile esneklik
5. **Dokümantasyon:** Her adım açık ve net
6. **Testable:** Adımlar bağımsız test edilebilir

---

**Son Güncelleme:** 2026-01-01  
**Versiyon:** 1.0  
**Yazar:** VB_DS Proje Ekibi
