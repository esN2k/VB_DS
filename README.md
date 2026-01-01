# VB_DS - Profit Tahmini Veri Bilimi Projesi

Bu proje SampleSuperstore verisi ile **Profit (kar)** tahmini yapar.
Amac basit: Veriyi temizle, ozellik uret, modeli egit ve raporla.
Her sey Turkce ve adim adim anlatildi; ilk defa bakan biri bile anlayabilir.

## 🚀 TL;DR - Hızlı Başlangıç (3 Komut)

```powershell
# 1. Pipeline çalıştır (veri + model)
python -m src.run_pipeline

# 2. Durum raporu oluştur
python -m src.audit_repo

# 3. Streamlit uygulaması başlat (jüri demosu)
streamlit run src/app_streamlit.py
```

## 0) 3 Adimda Calistir

1) Sanal ortam:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

2) Kutuphaneler:
```powershell
pip install -r requirements.txt
```

3) Tek komutla pipeline:
```powershell
python -m src.run_pipeline
```

## 🎯 Uygulama Çalıştırma (Jüri Demosu)

İnteraktif Streamlit uygulaması ile projeyi jüriye gösterin:

```powershell
streamlit run src/app_streamlit.py
```

**Uygulama özellikleri:**
- 📋 Veri Özeti: Satır/kolon sayısı, veri tipleri, eksik değerler
- 📈 EDA Grafikleri: Histogram, scatter, korelasyon matrisi
- 🎯 Model Sonuçları: Metrikler, karşılaştırma, feature importance
- 🔍 Filtreler: Region/Category/Segment bazlı filtreleme

## 📊 CANVA SUNUMU HAZIRLAMA

**🎓 JÜRİ SUNUMU İÇİN KAPSAMLI REHBERLERİ BİRLEŞTİRİLMİŞTİR!**

Sunuş hazırlaması için **5 temel dokümanda** tüm ihtiyacın var:

### 🔴 **BAŞLA BURADAN** (Hemen oku - 10 dakika)
📍 **[SUNUM_QUICK_REFERENCE.md](SUNUM_QUICK_REFERENCE.md)**
- Her slaytın 1 cümlelik özeti
- Konuşacağın şablonlu metin
- 7 olası soru + hazır cevaplar
- Son dakika panik protokolü

### 🟡 **Detaylı Hazırlık** (1-2 gün öncesi, 1.5 saat)

**1. Slayt İçeriği:** [CANVA_SUNUM_REHBERI.md](CANVA_SUNUM_REHBERI.md)
- 10 slaytın tam detayı (metni, görselleri, tasarımı)
- Canva'da nasıl oluşturacağın adım adım
- Renk, font, layout best practices

**2. Konuşma Metni:** [JURI_SUNUM_AKISI.md](JURI_SUNUM_AKISI.md)
- 7-9 dakikalık tam konuşma (doğal, samimi dille)
- Her slayt için detaylı metin
- Psikolojik hazırlık notları

**3. Yapılacaklar Listesi:** [CANVA_TODO_LIST.md](CANVA_TODO_LIST.md)
- 7 ana görev adım adım (içerik → görseller → slaytlar → tasarım → export → prova → kontroller)
- Takvim (T-2 gün → Sabah)
- Tahmini çalışma saatleri (~7.5 saat)

### 🟢 **Kontroller & Acil Durum** (Jüri günü)

**4. Jüri Günü Kontrol Listesi:** [SUNUM_KONTROL_LISTESI.md](SUNUM_KONTROL_LISTESI.md)
- 5 phase (24 saat öncesi → sunuş sonrası)
- Teknik kontroller
- Acil durum planları
- Sunum esnasında dinamik rehber

**5. Canlı Demo (İsteğe bağlı):** [DEMO_SCRIPT.md](DEMO_SCRIPT.md)
- Streamlit uygulamasını jüri önünde nasıl açacağın
- 5-7 dakikalık demo senaryo
- Olası sorunlar ve çözümler

### 📑 **TÜMSÜRÜ KAPSAYANİNDEKS** 
📍 **[SUNUM_DOKUMANTASYON_INDEKSI.md](SUNUM_DOKUMANTASYON_INDEKSI.md)**
- Hangi dosyayı ne zaman okuyacağını söyler
- Hızlı referans tablosu
- Acil durum planları

---

**⏱️ Hızlı Planlama:**
- **Bugün (T-2):** SUNUM_QUICK_REFERENCE.md oku (10 min) + CANVA_SUNUM_REHBERI.md başlangıç (15 min)
- **Yarın (T-1):** CANVA_TODO_LIST.md takip edip slaytları oluştur (3 saat)
- **Sunum Günü Sabahı:** SUNUM_KONTROL_LISTESI.md + SUNUM_QUICK_REFERENCE.md (30 min)
- **Salonun Kapısında:** SUNUM_QUICK_REFERENCE.md son bakış (5 min)

---

## 📖 EK DOKÜMANTASYON

İhtiyaca göre okuyabileceğin diğer rehberler:

**Not:** Uygulama için önce pipeline çalıştırılmalıdır.

## Ne Uretir?

- `data/processed/clean.csv`
- `reports/data_summary.txt`
- `reports/metrics.csv`
- `reports/metrics_full.csv`
- `reports/metrics_no_geo.csv`
- `reports/top10_importance.csv`
- `reports/figures/` (EDA görselleri - make_figures ile)

## 📊 EDA Görselleri Oluşturma

EDA grafikleri oluşturmak için:

```powershell
python -m src.make_figures
```

**Oluşturulan grafikler (reports/figures/):**
- 01_profit_distribution.png - Profit dağılımı (histogram)
- 02_sales_vs_profit.png - Sales vs Profit scatter plot
- 03_category_avg_profit.png - Category'ye göre ortalama profit
- 04_discount_distribution.png - Discount dağılımı
- 05_correlation_heatmap.png - Korelasyon matrisi (heatmap)
- 06_region_profit_boxplot.png - Region'a göre profit box plot

**Not:** Grafikler otomatik olarak yüksek kalitede (300 DPI) kaydedilir.

## Veri Seti ve Beklenen Kolonlar

Dosya: `data/raw/SampleSuperstore.csv`
Beklenen minimum kolonlar:
- `Sales`, `Profit`, `Discount`, `Quantity`
- `Category`, `Sub-Category`, `Segment`, `Region`, `State`, `City`, `Ship Mode`
- (Varsa) `Order Date`, `Ship Date`

## Feature Engineering (Tarih Varsa/Yoksa)

Tarih kolonlari varsa:
- `order_month`, `order_dayofweek`, `shipping_delay`

Tarih kolonlari yoksa:
- `sales_per_item = Sales / max(Quantity, 1)`
- `discounted_sales = Sales * (1 - Discount)`
- `profit_margin = Profit / Sales` (Profit hedefi icin **egitimde drop** edilir)
- `is_high_discount = 1 if Discount >= 0.3 else 0`

Not: Aykiri degerler IQR ile **sadece raporlanir**, silinmez.

## Modelleme Ozet

- Hedef: **Profit**
- Pipeline: `OneHotEncoder` + `StandardScaler`
- Modeller: `LinearRegression` ve `RandomForestRegressor`
- Profit negatif olabildigi icin hedefe `log1p` donusumu uygulanir (gerekirse shift).
- RandomForest icin top-10 feature importance raporlanir.
- Genelleme testi icin drop_geo opsiyonu (City/Postal Code/State disarida).

## Proje Yapisi

```
data/
  raw/                # ham veri
  processed/          # temizlenmis veri
notebooks/            # 01-02-03
reports/              # ozet ve metrikler
  figures/            # grafikler
src/                  # tum python kodlari
```

## Notebooklar (Opsiyonel)

Sira ile calistir:
1) `notebooks/01_load_clean.ipynb`
2) `notebooks/02_eda.ipynb`
3) `notebooks/03_model.ipynb`

## Proje Durum Raporu (YENİ!)

Projenin güncel durumunu görmek için:
```powershell
python -m src.audit_repo
```

Bu komut `DURUM_RAPORU.md` dosyası oluşturur ve şunları gösterir:
- Tüm dosyaların durumu (✓/✗)
- Modellerin gerçek metrikleri
- Eksikler ve riskler
- Hoca sorularına hazır cevaplar

Detaylı kullanım: `AUDIT_NASIL_KULLANILIR.md`

## Dokumantasyon Dosyalari

- `INSTRUCTIONS.md` -> Basit talimatlar (ilk bakan icin)
- `ADIM_ADIM.md` -> Ogretmen gibi adim adim anlatim
- `OZET_SONUC.md` -> Tek sayfalik ozet + sonuc
- `RAPOR.md` -> Juriye teslim raporu
- `SUNUM.md` -> Sunum akisi + konusma notlari
- `SUNUM_SLIDES.pptx` -> Hazir slayt dosyasi
- `SUNUM_SLIDES.pdf` -> Hazir sunum PDF
- `AUDIT_NASIL_KULLANILIR.md` -> Audit scripti kullanim kilavuzu
- `DEMO_SCRIPT.md` -> Canli demo senaryosu (5-7 dk)
- `JURI_SUNUM_AKISI.md` -> Juri sunum metni (7-9 dk)
- `ARCHITECTURE.md` -> Pipeline akisi + mimari
- `CHANGELOG.md` -> Degisiklik gunlugu

## 📦 Teslim Paketi Oluşturma

Jüriye teslim için ZIP paketi oluşturmak:

```powershell
# PowerShell ile
.\tools\package.ps1

# Veya özel isimle
.\tools\package.ps1 -OutputName "DogukanYilmaz_VB_DS"
```

**Oluşturulan paket içeriği:**
- Tüm kod (src/, notebooks/)
- Raporlar ve metrikler (reports/, *.md)
- Sunumlar (*.pptx, *.pdf)
- Ham veri (data/raw/)
- Dokümantasyon

**Çıktı:** `teslim_paketi_YYYYMMDD_HHMMSS.zip`

## Sik Karsilasilan Hatalar

- "SampleSuperstore.csv not found": Dosya `data/raw/` altinda degil.
- "Profit column not found": Veride Profit kolonu eksik.
- Python bulunamadi: `py -3.10 -m venv .venv` ile yeniden kur.
- Streamlit açılmıyor: `pip install streamlit` sonra tekrar dene.
