# RAPOR - Kar Tahmini (SampleSuperstore)

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

Not: Profit hedefi kullanildigi icin `profit_margin` egitimde **drop** edildi (veri sizintisi onlemi).

## 5) Modelleme

Iki model kuruldu:
- **LinearRegression** (temel)
- **RandomForestRegressor** (daha guclu, dogrusal olmayan iliskileri yakalar)

Is akisi icinde:
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

## 6.1) Ablasyon Deneyi: Geo Kolonlarini Cikarmanin Etkisi (drop_geo)

Modelin bazi sehir/posta kodu gibi yuksek kardinaliteli alanlari
"ezberleyip ezberlemedigini" gormek icin kucuk bir ablasyon testi yaptim.
Bu amacla Random Forest modelini iki senaryoda karsilastirdim:

1. **Tam**: Tum kolonlar (City/State/Postal Code dahil)
2. **Geo Yok (drop_geo)**: City/State/Postal Code cikarilarak

Asagidaki metrikler test seti uzerinde alinmistir:

| Senaryo           | Model                 |   MAE |   RMSE |    R2 |
| ----------------- | --------------------- | ----: | -----: | ----: |
| Tam               | RandomForestRegressor | 42.15 | 156.90 | 0.492 |
| Geo Yok (drop_geo)| RandomForestRegressor | 25.98 | 116.89 | 0.718 |

Bu sonuclara gore geo kolonlarini cikardigimda model performansi belirgin
sekilde artti. Bunu iki sekilde yorumluyorum:

- City/Postal Code gibi alanlar cok fazla benzersiz deger icerdigi icin
  modeli gereksiz boyutta buyutup gurultu katabiliyor ve genellemeyi
  zorlastirabiliyor.
- Geo kirilimi bazen kara dolayli etki etse de, bu veri setinde kari daha cok
  Sales, Discount, Quantity ve turetilmis ozellikler (sales_per_item,
  discounted_sales gibi) acikliyor gibi gorunuyor.

Bu nedenle final yorumlarda "geo alanlari cikarildiginda modelin daha
genellenebilir hale geldigi" not edildi.

## 7) Ozellik Onemi (Random Forest)

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
Ozellik onemi listesinde Sales, sales_per_item ve discounted_sales gibi
degiskenlerin ustte cikmasi; indirim ve adet etkisinin karlilik uzerinde
dogrudan belirleyici oldugunu destekledi.

## 8) Sonuc ve Ogrenimler

- Kar iliskileri dogrusal degil; agac tabanli model daha basarili.
- Indirim ve kategori etkisi kritik.
- Veri sizintisi riski olan `profit_margin` modeli suni sekilde sisirebilirdi; cikarildi.

## 9) Sinirlamalar ve Gelecek Isler

- Verideki bolgesel degiskenler (City/Postal Code) asiri uyum riski tasiyabilir.
- Hiperparametre aramasi yapilirsa performans artabilir.
- Daha iyi genelleme icin kimi kategoriler sadelestirilebilir.

## 10) Son Not

Bu rapor teslim icin hazir formdadir.
Guncel metrikleri kullanmak istersen `python -m src.run_pipeline` komutunu tekrar calistirabilirsin.
Ek/Appendix: `reports/metrics_full.csv` ve `reports/metrics_no_geo.csv` dosyalari uretildi.
