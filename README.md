# VB_DS - Kar Tahmini Veri Bilimi Projesi

Bu proje SampleSuperstore verisiyle kar (Profit) tahmini yapar.
Amac: veriyi temizlemek, ozellik uretmek, modeli egitmek ve raporlamak.

## Hizli Baslangic

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.run_pipeline
```

## Juri Demosu

```powershell
streamlit run src/app_streamlit.py
```

## Ham Veri

- `data/raw/SampleSuperstore.csv`

## Uretilen Ciktilar

- `data/processed/clean.csv`
- `reports/data_summary.txt`
- `reports/metrics.csv`
- `reports/metrics_full.csv`
- `reports/metrics_no_geo.csv`
- `reports/top10_importance.csv`
- `reports/figures/` (opsiyonel)
