================================================================================
REPO AUDITOR + DATA SCIENCE PROJE KOÇU
Güncel Durum Raporu
================================================================================

### Ortam Bilgisi
- **Tarih/Saat:** 2026-01-01 14:45:32
- **Python Versiyonu:** 3.12.3
- **Çalışma Dizini:** /home/runner/work/VB_DS/VB_DS
- **Proje Kök Dizini:** /home/runner/work/VB_DS/VB_DS

## 1) ŞU AN PROJE NE DURUMDA?

### Problem Tanımı ve Hedef Değişken
- Problem: Regresyon (sürekli değer tahmini)
- Hedef değişken: Profit (kâr)
- Amaç: Satış ve kategori bilgilerinden kârlılığı tahmin etmek

### Kullanılan Veri Set(ler)i
- ✓ Ham veri: /home/runner/work/VB_DS/VB_DS/data/raw/SampleSuperstore.csv (1077.2 KB)
- ✓ Temizlenmiş veri: /home/runner/work/VB_DS/VB_DS/data/processed/clean.csv (1392.2 KB)

### En Son Üretilen Çıktılar
- ✓ Veri özet raporu: /home/runner/work/VB_DS/VB_DS/reports/data_summary.txt (0.3 KB)
- ✓ Model metrikleri (ana): /home/runner/work/VB_DS/VB_DS/reports/metrics.csv (0.2 KB)
- ✓ Full model metrikleri: /home/runner/work/VB_DS/VB_DS/reports/metrics_full.csv (0.2 KB)
- ✓ No-Geo model metrikleri: /home/runner/work/VB_DS/VB_DS/reports/metrics_no_geo.csv (0.2 KB)
- ✓ Top-10 feature importance: /home/runner/work/VB_DS/VB_DS/reports/top10_importance.csv (0.4 KB)

### Modeller ve Metrikler (Dosyadan Okunan)

**Full (metrics.csv / metrics_full.csv):**
```
                model       mae       rmse        r2
     LinearRegression 94.826673 232.556256 -0.115443
RandomForestRegressor 42.154774 156.900395  0.492262
```

**No-Geo (metrics_no_geo.csv):**
```
                model       mae       rmse       r2
     LinearRegression 74.621414 211.844511 0.074395
RandomForestRegressor 25.979721 116.891142 0.718191
```

### Ablation / Ek Deneyler
- drop_geo: ✓ City/State/Postal Code çıkarılarak test edildi
- Sonuç: No-Geo modelde RandomForest R² artışı gözlemlendi
  (Full: R²=0.492 → No-Geo: R²=0.718)
- Grid search / hiperparametre optimizasyonu: Yok (manuel ayar var)

### Feature Engineering Özeti
- Tarih kolonları YOKSA:
  * sales_per_item = Sales / Quantity
  * discounted_sales = Sales * (1 - Discount)
  * profit_margin = Profit / Sales
  * is_high_discount = 1 if Discount >= 0.3 else 0
- Leakage önlemi: profit_margin hedef Profit iken modelden drop edilir
- Kategorik normalize: strip() ile temizlik
- Missing handling: sayısal -> median, kategorik -> mode
- Outlier: IQR ile SADECE raporlanır, silinmez

### Rapor ve Sunum Dosyalarının Durumu
- ✓ Ana teslim raporu: /home/runner/work/VB_DS/VB_DS/RAPOR.md (4.3 KB)
- ✓ Tek sayfalık özet + sonuç: /home/runner/work/VB_DS/VB_DS/OZET_SONUC.md (1.3 KB)
- ✓ Sunum akışı + konuşma notları: /home/runner/work/VB_DS/VB_DS/SUNUM.md (3.6 KB)
- ✓ PowerPoint sunumu: /home/runner/work/VB_DS/VB_DS/SUNUM_SLIDES.pptx (40.0 KB)
- ✓ PDF sunumu: /home/runner/work/VB_DS/VB_DS/SUNUM_SLIDES.pdf (114.2 KB)
- ✓ Proje README: /home/runner/work/VB_DS/VB_DS/README.md (5.2 KB)
- ✓ Basit talimatlar: /home/runner/work/VB_DS/VB_DS/INSTRUCTIONS.md (1.5 KB)
- ✓ Adım adım anlatım: /home/runner/work/VB_DS/VB_DS/ADIM_ADIM.md (1.7 KB)

- ✓ Teslim paketi: /home/runner/work/VB_DS/VB_DS/deliverables/teslim_paketi/
  ✓ ZIP arşiv: teslim_paketi.zip (265.2 KB)


## 2) REPO ENVANTERİ

### Ağaç Görünümü
```
src/
  __init__.py (0.0 KB)
  __pycache__/
  app_streamlit.py (11.2 KB)
  audit_repo.py (18.1 KB)
  evaluate.py (0.6 KB)
  make_figures.py (5.4 KB)
  preprocess.py (4.9 KB)
  run_pipeline.py (11.1 KB)
  train.py (7.3 KB)
notebooks/
  01_load_clean.ipynb (5.6 KB)
  02_eda.ipynb (2.8 KB)
  03_model.ipynb (4.2 KB)
reports/
  data_summary.txt (0.3 KB)
  figures/
  metrics.csv (0.2 KB)
  metrics_full.csv (0.2 KB)
  metrics_no_geo.csv (0.2 KB)
  top10_importance.csv (0.4 KB)
data/
  processed/
  raw/
deliverables/
  teslim_paketi/
  teslim_paketi.zip (265.2 KB)
```

### Önemli Dosyalar ve Ne İşe Yaradığı

- **src/run_pipeline.py**: Ana pipeline: veri yükle, temizle, eğit, raporla
- **src/preprocess.py**: Veri temizleme ve feature engineering
- **src/train.py**: Model eğitimi (kullanılmıyorsa ignore)
- **src/evaluate.py**: Metrik hesaplama (MAE, RMSE, R²)
- **notebooks/01_load_clean.ipynb**: Veri yükleme ve temizleme (görsel)
- **notebooks/02_eda.ipynb**: Keşifsel Veri Analizi (EDA)
- **notebooks/03_model.ipynb**: Model eğitimi ve değerlendirme
- **data/raw/SampleSuperstore.csv**: Ham veri seti
- **reports/metrics.csv**: Model performans metrikleri
- **RAPOR.md**: Jüriye teslim raporu
- **requirements.txt**: Python bağımlılıkları


## 3) ÇALIŞIYOR MU? DOĞRULAMASI

### Gerekli Kontroller ve Komutlar

#### 3.1) Venv Kontrolü
```powershell
# Sanal ortam oluştur ve aktif et
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```
**Beklenen:** Prompt'ta (.venv) görünür

#### 3.2) Bağımlılıkları Yükle
```powershell
pip install -r requirements.txt
```
**Beklenen:** pandas, numpy, scikit-learn, matplotlib yüklensin

#### 3.3) Ana Pipeline Çalıştır
```powershell
python -m src.run_pipeline
```
**Beklenen çıktılar:**
- data/processed/clean.csv
- reports/data_summary.txt
- reports/metrics.csv
- reports/metrics_full.csv
- reports/metrics_no_geo.csv
- reports/top10_importance.csv
- Terminal'de: 'OK: outputs generated'

#### 3.4) Notebook Durumu
**Notebook'lar mevcut ama opsiyonel:**
- 01_load_clean.ipynb: Veri yükleme görselleri
- 02_eda.ipynb: EDA grafikleri
- 03_model.ipynb: Model sonuçları ve importance plot

**Not:** Pipeline çalışıyorsa notebook'lara gerek yok. Sadece görsel istiyorsan çalıştır.


## 4) RİSKLER VE HOCA SORULARI

### Overfit riski var mı?
RandomForest 200 ağaç kullanıyor ama min_samples_leaf=2 ve max_features='sqrt' ile sınırlandırdım. Test/train split %20 ile yapıldı. No-Geo senaryoda R² artışı overfit azaldığını gösteriyor. Ancak cross-validation yapmadım, bu iyileştirilebilir.

### Leakage (veri sızıntısı) var mı?
Hedef Profit iken profit_margin'i modelden drop ettim. Çünkü profit_margin doğrudan Profit'ten türetiliyor ve leakage yaratır. Diğer feature'lar (sales_per_item, discounted_sales) Sales ve Discount'tan türetilmiş olsa da bunlar hedeften bağımsız.

### log1p + shift neden kullanıldı?
Profit negatif değerler içerebiliyor. log1p doğrudan negatife uygulanamaz. Bu yüzden minimum değer negatifse otomatik shift ekliyorum (min_val + 1). Böylece log dönüşümü çalışır ve çarpık dağılımı düzeltir.

### Geo kolonları (City/State/Postal Code) neden çıkarılınca performans arttı?
Yüksek kardinalite (çok benzersiz değer) model karmaşıklığını artırıyor ve genellemeyi zorlaştırıyor. Geo bilgisi dolaylı etki etse de bu veri setinde Sales, Discount ve türetilmiş feature'lar daha güçlü. No-Geo'da R² 0.492'den 0.718'e çıktı, yani model daha genellenebilir oldu.

### Outlier (aykırı değer) yaklaşımınız nedir?
IQR yöntemiyle aykırı değerleri tespit edip SADECE raporladım, silmedim. Çünkü gerçek dünyada aykırı satışlar/kârlar doğal olabilir ve bunları silmek bilgi kaybına yol açar. Model robust olmalı ve bunları öğrenmeli.


## 5) TESLİM İÇİN EKSİKLER (P0/P1/P2)

### P0 (Kesin Şartlar - Olmadan Teslim Edilmez)
- [x] Ham veri (SampleSuperstore.csv) mevcut
- [x] Pipeline çalışıyor (python -m src.run_pipeline)
- [x] Metrik dosyaları üretiliyor (metrics.csv)
- [x] RAPOR.md hazır
- [x] OZET_SONUC.md hazır
- [x] Sunum dosyası mevcut (PPTX + PDF)
- [x] README.md mevcut ve güncel

### P1 (Puan Artıranlar - Olması İyi)
- [x] Notebook'lar (01/02/03) mevcut
- [x] Feature importance raporu (top10_importance.csv)
- [x] Ablation testi yapılmış (drop_geo)
- [ ] Cross-validation eklenmemiş (İyileştirme önerisi)
- [ ] Grid search / hiperparametre optimizasyonu yapılmamış
- [x] Teslim paketi ZIP'i hazır (deliverables/teslim_paketi.zip)
- [ ] Video sunum hazırlanmamış (SUNUM.md'de plan var)

### P2 (Opsiyonel - Bonus)
- [ ] Ek model denemeleri (XGBoost, LightGBM vb.)
- [ ] Feature selection / PCA
- [ ] Deployment planı / API örneği
- [ ] Docker container
- [ ] CI/CD pipeline


## 6) DOĞUKAN AĞZIYLA GÜNCEL ÖZET

---

Hocam, projem SampleSuperstore verisiyle Profit (kâr) tahmini yapıyor. Veriyi temizledim, sales_per_item, discounted_sales gibi feature'lar türettim ve iki model karşılaştırdım: LinearRegression baseline olarak zayıf kaldı (R² negatif), ama RandomForestRegressor çok daha iyi sonuç verdi (R² 0.492). Önemli bir bulgu da City/Postal Code gibi geo kolonlarını çıkarınca modelin genelleme yeteneği arttı (R² 0.718'e çıktı). Leakage önlemi olarak profit_margin'i modelden çıkardım, outlier'ları sildim yerine sadece raporladım. Tüm kod, rapor, sunum ve teslim paketi hazır. Eksik olan sadece cross-validation ve video sunum ama bunlar opsiyonel. Proje çalışır durumda ve tek komutla (`python -m src.run_pipeline`) tüm çıktıları yeniden üretilebiliyor.

---

================================================================================
RAPOR SONU
================================================================================