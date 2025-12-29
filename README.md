# VB_DS - Veri Bilimi Proje Iskeleti

Bu repo, SampleSuperstore verisi ile Profit tahmini odakli temel bir veri bilimi calisma akisi icin ornek bir iskelet sunar.
Tum kodlar relatif path kullanir; Windows path'leri gomulu degildir.

## Kurulum

1) Sanal ortam olustur ve aktif et:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2) Kutuphaneleri yukle:

```powershell
pip install -r requirements.txt
```

## Veri Hazirlama

Ham veriyi temizleyip islenmis dosya olustur:

```powershell
python src/preprocess.py --input data/raw/SampleSuperstore.csv --output data/processed/clean.csv
```

## Tek Komutla Pipeline

```powershell
python -m src.run_pipeline
```

Uretilen dosyalar:
- `data/processed/clean.csv`
- `reports/data_summary.txt`
- `reports/metrics.csv`
- `reports/top10_importance.csv`

## Model Egitimi (Profit hedefi)

```powershell
python src/train.py --input data/processed/clean.csv
```

## Notebooks

Notebooks klasorundeki dosyalari sirayla calistirabilirsiniz:
1) `notebooks/01_load_clean.ipynb`
2) `notebooks/02_eda.ipynb`
3) `notebooks/03_model.ipynb`

Olusan grafikler `reports/figures` altina kaydedilir.
