# INSTRUCTIONS - Proje Talimatlari (Basit Dille)

Bu dosya projeyi ilk kez acan biri icin yazildi. En basit haliyle ne yapman gerektigini anlatir.

## 1) Veri Dosyasini Dogru Yere Koy

- Dosya adi: `SampleSuperstore.csv`
- Dogru klasor: `data/raw/`
- Tam yol: `data/raw/SampleSuperstore.csv`

## 2) Ortam Kurulumu

Terminal ac ve sirayla yaz:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 3) Tek Komutla Pipeline Calistir

```powershell
python -m src.run_pipeline
```

Bu komut tum sureci calistirir ve otomatik cikti uretir.

## 4) Ciktlari Kontrol Et

Olusan dosyalar:
- `data/processed/clean.csv` -> temizlenmis veri
- `reports/data_summary.txt` -> kisa veri ozeti
- `reports/metrics.csv` -> model metrikleri
- `reports/top10_importance.csv` -> en onemli 10 ozellik
- `reports/figures/` -> grafikler (notebook calisirsa)

## 5) Notebooklar (Opsiyonel)

Sadece gormek ve gorsel uretmek istersen:
1) `notebooks/01_load_clean.ipynb`
2) `notebooks/02_eda.ipynb`
3) `notebooks/03_model.ipynb`

## 6) Hazir Dokumanlar (Teslim Icin)

- `RAPOR.md` -> teslim raporu metni
- `OZET_SONUC.md` -> tek sayfalik ozet + sonuc
- `SUNUM.md` -> sunum akisi + konusma notlari
- `SUNUM_SLIDES.pptx` -> hazir slayt dosyasi
- `SUNUM_SLIDES.pdf` -> hazir sunum PDF

## 7) Sorun Giderme

- "SampleSuperstore.csv not found": Dosya yanlis yerde.
- "Profit column not found": Veride Profit kolonu yok.
- Python bulunamadi: `py -3.10 -m venv .venv` ile yeniden kur.
