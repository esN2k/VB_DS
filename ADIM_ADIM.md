# ADIM_ADIM - Ogretmen Gibi Anlatim

Bu bolumde bir ogretmen gibi, adim adim ve cok net sekilde anlatim vardir.
Her adimi sirayla uygula; atlama.

## Adim 0: Projeyi Ac

Projeyi bilgisayarinda `VB_DS` klasoru olarak ac.

## Adim 1: Veri Dosyasini Kontrol Et

`data/raw/` klasorune gir.
Orada `SampleSuperstore.csv` dosyasinin oldugundan emin ol.
Yoksa dosyayi oraya kopyala.

## Adim 2: Sanal Ortam Kur

Terminal ac ve su komutlari yaz:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Bu adim, proje icin temiz bir Python ortami olusturur.

## Adim 3: Kutuphaneleri Yukle

```powershell
pip install -r requirements.txt
```

Bu komut olmadan kodlar calismaz.

## Adim 4: Pipeline'i Calistir

```powershell
python -m src.run_pipeline
```

Bu komut su islemleri yapar:
1) Ham veriyi okur
2) Temizler ve ozellik uretir
3) `clean.csv` kaydeder
4) Veri ozeti ve metrik dosyalarini olusturur

## Adim 5: Ciktilari Kontrol Et

Su dosyalarin olusmasi gerekir:
- `data/processed/clean.csv`
- `reports/data_summary.txt`
- `reports/metrics.csv`
- `reports/top10_importance.csv`

`reports/metrics.csv` dosyasini ac ve metrikleri kontrol et.

## Adim 6: (Opsiyonel) Notebooklari Calistir

Grafik uretmek istersen sira ile calistir:
1) `notebooks/01_load_clean.ipynb`
2) `notebooks/02_eda.ipynb`
3) `notebooks/03_model.ipynb`

Grafikler `reports/figures` klasorune kaydolur.

## Adim 7: Rapor ve Sunum Hazirligi

Rapor icin: `RAPOR.md`
Sunum icin: `SUNUM.md`

Bu iki dosya kopyala-yapistir seklinde kullanilabilir.

## Adim 8: Son Kontrol

- Dataset dogru mu?
- Cikti dosyalari olustu mu?
- Rapor ve sunum metni hazir mi?

Hepsi tamamsa teslim edebilirsin.
