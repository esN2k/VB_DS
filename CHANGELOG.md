# CHANGELOG - Proje Geliştirme Günlüğü

Tüm önemli değişiklikler bu dosyada belgelenmektedir.

---

## [1.1.0] - 2026-01-01 (Jüri Hazırlığı - Final)

### ✨ Yeni Özellikler

#### Uygulama Katmanı
- **Streamlit Uygulaması** (`src/app_streamlit.py`)
  - 3 sekme: Veri Özeti, EDA Grafikleri, Model Sonuçları
  - İnteraktif filtreler (Region/Category/Segment)
  - Gerçek zamanlı veri görselleştirme
  - Metrik karşılaştırma (Full vs No-Geo)
  - Feature importance bar chart
  - Jüri sunumu için hazır

#### Görselleştirme
- **EDA Görselleri Scripti** (`src/make_figures.py`)
  - 6 adet yüksek kaliteli grafik (300 DPI)
  - Profit dağılımı (histogram)
  - Sales vs Profit (scatter plot)
  - Category'ye göre ortalama profit (bar chart)
  - Discount dağılımı
  - Korelasyon matrisi (heatmap)
  - Region'a göre profit (box plot)
  - Otomatik kayıt: `reports/figures/*.png`

#### Kod Kalitesi İyileştirmeleri
- **Logging Sistemi**
  - INFO seviyesinde detaylı loglar
  - Timestamp ile kayıt
  - Kritik adımların izlenmesi
  - Hata mesajları user-friendly

- **CLI Parametreleri** (`argparse`)
  - `--drop-geo`: Geo kolonlarını çıkar
  - `--seed`: Random seed (default: 42)
  - `--output-dir`: Çıktı dizini (default: reports/)

#### Dokümantasyon
- **DEMO_SCRIPT.md**: 5-7 dakikalık canlı demo senaryosu
- **JURI_SUNUM_AKISI.md**: 7-9 dakika konuşma metni (Doğukan ağzıyla)
- **ARCHITECTURE.md**: Pipeline akışı + ASCII diyagram
- **CHANGELOG.md**: Bu dosya
- **README.md**: TL;DR bölümü + uygulama kullanımı

#### Audit İyileştirmeleri
- **DURUM_RAPORU.md** güncellemeleri:
  - Timestamp eklendi
  - Python versiyon bilgisi
  - Çalışma dizini
  - Proje kök dizini

### 🔧 Değişiklikler

#### Dependencies
- Sürüm sabitleme (`requirements.txt`):
  - `pandas==2.3.3`
  - `numpy==2.4.0`
  - `matplotlib==3.10.8`
  - `scikit-learn==1.8.0`
  - `scipy==1.16.3`
- Yeni paketler:
  - `streamlit>=1.28.0`
  - `seaborn>=0.12.0`

#### Proje Yapısı
- `src/app_streamlit.py` eklendi
- `src/make_figures.py` eklendi
- `reports/figures/` klasörü otomatik oluşturuluyor
- 6 adet PNG grafik üretiliyor

---

## [1.0.0] - 2025-12-31 (İlk Teslim)

### ✨ Yeni Özellikler

#### Core Pipeline
- **Ana Pipeline** (`src/run_pipeline.py`)
  - Ham veri yükleme
  - Veri temizleme
  - Feature engineering
  - Model eğitimi (LinearRegression + RandomForest)
  - Full vs No-Geo ablation testi
  - Metrik hesaplama ve kaydetme

#### Veri İşleme
- **Preprocessing** (`src/preprocess.py`)
  - Missing value imputation (median/mode)
  - Kategorik strip (boşluk temizleme)
  - Outlier detection (IQR) - sadece rapor, silme yok
  - Feature engineering:
    - `sales_per_item`
    - `discounted_sales`
    - `profit_margin`
    - `is_high_discount`

#### Model Eğitimi
- **train_models** fonksiyonu
  - sklearn Pipeline (OneHotEncoder + StandardScaler)
  - Log dönüşümü (shift + log1p)
  - Train-test split (80-20, seed=42)
  - Full model (tüm kolonlarla)
  - No-Geo model (City/State/Postal Code hariç)
  - Feature importance (RandomForest)

#### Değerlendirme
- **Metrikler** (`src/evaluate.py`)
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² (Coefficient of Determination)

#### Audit ve Raporlama
- **Repo Auditor** (`src/audit_repo.py`)
  - Dosya varlığı kontrolü (✓/✗)
  - Metrik okuma (dosyadan)
  - Repo envanteri
  - Risk analizi + savunma cümleleri
  - P0/P1/P2 eksikler
  - Öğrenci diliyle özet

#### Notebooks
- `01_load_clean.ipynb`: Veri yükleme ve temizleme
- `02_eda.ipynb`: Keşifsel veri analizi
- `03_model.ipynb`: Model eğitimi ve değerlendirme

#### Dokümantasyon
- **RAPOR.md**: Jüriye teslim raporu
- **OZET_SONUC.md**: Tek sayfalık özet + sonuç
- **SUNUM.md**: Sunum akışı + konuşma notları
- **SUNUM_SLIDES.pptx**: PowerPoint sunumu
- **SUNUM_SLIDES.pdf**: PDF sunumu
- **README.md**: Proje README
- **ADIM_ADIM.md**: Adım adım talimatlar
- **INSTRUCTIONS.md**: Basit talimatlar
- **AUDIT_NASIL_KULLANILIR.md**: Audit kullanım kılavuzu
- **PROJE_AUDIT_SISTEMI.md**: Audit sistemi dokümantasyonu

### 🎯 Sonuçlar

#### Model Performansı
**Full Model (City/State/Postal Code dahil):**
- LinearRegression: R² = -0.115 (zayıf)
- RandomForest: R² = 0.492, MAE = 42.15

**No-Geo Model (City/State/Postal Code hariç):**
- LinearRegression: R² = 0.074
- RandomForest: R² = 0.718, MAE = 25.98

**Bulgu:** Geo kolonlarını çıkarmak modeli iyileştirdi (+46% R² artışı)

#### Feature Importance (Top-3)
1. Sales (0.212)
2. sales_per_item (0.178)
3. discounted_sales (0.172)

### 🐛 Bilinen Sorunlar

- Cross-validation yok (manuel train-test split)
- Grid search / hiperparametre optimizasyonu yapılmadı
- Video sunum hazırlanmadı (plan var)

---

## Versiyon Numaralandırma

Proje [Semantic Versioning](https://semver.org/) kullanır:
- MAJOR.MINOR.PATCH
- Örnek: 1.1.0
  - 1 = Major (büyük değişiklikler)
  - 1 = Minor (yeni özellikler)
  - 0 = Patch (hata düzeltmeleri)

---

## Gelecek Planlar (Roadmap)

### v1.2.0 (İyileştirmeler)
- [ ] Cross-validation ekleme (k-fold)
- [ ] Grid search ile hiperparametre optimizasyonu
- [ ] Ek modeller (XGBoost, LightGBM)
- [ ] Feature selection / PCA

### v2.0.0 (Production)
- [ ] Flask/FastAPI ile REST API
- [ ] Docker containerization
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Unit testler
- [ ] Deployment (Heroku/AWS)

---

**Notlar:**
- Tüm değişiklikler GitHub'da commit history'de mevcut
- Her major değişiklik için commit atıldı
- Reproducibility için random seed sabitleme (seed=42)
- Logging ile tüm adımlar izlenebilir

**Son Güncelleme:** 2026-01-01  
**Yazar:** VB_DS Proje Ekibi
