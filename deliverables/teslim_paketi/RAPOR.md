# RAPOR - Profit Tahmini (SampleSuperstore)

## 1) Proje Amaci

Bu projede hedef degisken olarak **Profit (kar)** secildi.
Amacim, satis ve kategori bilgilerini kullanarak karliligi tahmin etmek.

## 2) Veri Seti

Dosya: `data/raw/SampleSuperstore.csv`

Beklenen temel kolonlar:
- `Sales`, `Profit`, `Discount`, `Quantity`
- `Category`, `Sub-Category`, `Segment`, `Region`, `State`, `City`, `Ship Mode`
- (Varsa) `Order Date`, `Ship Date`

## 3) Veri Temizleme

- Sayisal bos degerler medyan ile tamamlandi.
- Kategorik bos degerler mod ile tamamlandi.
- Kategorik alanlar stringe cevrildi ve bosluklar temizlendi.
- Aykiri degerler IQR ile **raporlandi**, veri silinmedi.

## 4) Ozellik Muhendisligi

Tarih kolonlari varsa:
- `order_month`, `order_dayofweek`, `shipping_delay`

Tarih kolonlari yoksa:
- `sales_per_item`
- `discounted_sales`
- `profit_margin`
- `is_high_discount`

Not: Profit hedefi kullanildigi icin `profit_margin` egitimde **drop** edildi (leakage onlemi).

## 5) Modelleme

Iki model kuruldu:
- **LinearRegression** (baseline)
- **RandomForestRegressor** (daha guclu, dogrusal olmayan iliskileri yakalar)

Pipeline icinde:
- Kategorik degiskenler One-Hot Encoding
- Sayisal degiskenler StandardScaler

Profit dagilimi carpik olabildigi icin hedefe `log1p` donusumu uygulandi
(negatif deger varsa otomatik shift kullanildi).

## 6) Degerlendirme (Son Kosu)

Metrikler: MAE, RMSE, R2

| Model | MAE | RMSE | R2 |
| --- | --- | --- | --- |
| LinearRegression | 94.83 | 232.56 | -0.115 |
| RandomForestRegressor | 42.15 | 156.90 | 0.492 |

Yorum:
- Linear Regression zayif kaldigi icin R2 negatif cikti.
- Random Forest belirgin sekilde daha iyi; hata dusuyor ve R2 artiyor.

## 7) Feature Importance (Random Forest)

En etkili ozellikler:
- `Sales` (0.212)
- `sales_per_item` (0.178)
- `discounted_sales` (0.172)
- `Discount` (0.045)
- `City_Lancaster` (0.042)
- `Postal Code` (0.038)
- `Sub-Category_Machines` (0.036)
- `is_high_discount` (0.036)
- `Quantity` (0.031)
- `Sub-Category_Copiers` (0.029)

Bu liste, karliligin sadece satis miktariyla degil,
indirim ve urun tipiyle de guclu sekilde iliskili oldugunu gosterir.

## 8) Sonuc ve Ogrenimler

- Karlier iliskiler dogrusal degil; agac tabanli model daha basarili.
- Indirim ve kategori etkisi kritik.
- Leakage riski olan `profit_margin` modeli yapay olarak sisirebilirdi; cikarildi.

## 9) Sinirlamalar ve Gelecek Isler

- Verideki bolgesel degiskenler (City/Postal Code) overfit riski tasiyabilir.
- Hiperparametre aramasi yapilirsa performans artabilir.
- Daha iyi genelleme icin kimi kategoriler sadelestirilebilir.

## 10) Son Not

Bu rapor teslim icin hazir formdadir.
Guncel metrikleri kullanmak istersen `python -m src.run_pipeline` komutunu tekrar calistirabilirsin.
