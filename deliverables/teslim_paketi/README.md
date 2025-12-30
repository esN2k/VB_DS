# VB_DS - Profit Tahmini Veri Bilimi Projesi

Bu proje SampleSuperstore verisi ile **Profit (kar)** tahmini yapar.
Amac basit: Veriyi temizle, ozellik uret, modeli egit ve raporla.
Her sey Turkce ve adim adim anlatildi; ilk defa bakan biri bile anlayabilir.

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

## Ne Uretir?

- `data/processed/clean.csv`
- `reports/data_summary.txt`
- `reports/metrics.csv`
- `reports/top10_importance.csv`
- `reports/figures/` (sadece notebook calisirsa)

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

## Dokumantasyon Dosyalari

- `INSTRUCTIONS.md` -> Basit talimatlar (ilk bakan icin)
- `ADIM_ADIM.md` -> Ogretmen gibi adim adim anlatim
- `OZET_SONUC.md` -> Tek sayfalik ozet + sonuc
- `RAPOR.md` -> Juriye teslim raporu
- `SUNUM.md` -> Sunum akisi + konusma notlari
- `SUNUM_SLIDES.pptx` -> Hazir slayt dosyasi
- `SUNUM_SLIDES.pdf` -> Hazir sunum PDF

## Sik Karsilasilan Hatalar

- "SampleSuperstore.csv not found": Dosya `data/raw/` altinda degil.
- "Profit column not found": Veride Profit kolonu eksik.
- Python bulunamadi: `py -3.10 -m venv .venv` ile yeniden kur.
