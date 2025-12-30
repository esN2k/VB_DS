# SUNUM - Juriye Sunum Metni ve Akis

Bu dosya sunumda kullanman icin hazir bir akistir.
Her slayt icin kisa baslik, madde ve konusma notu var.

## Slayt 1: Baslik

**Baslik:** Profit Tahmini - SampleSuperstore

Konusma notu:
Benim projem, SampleSuperstore verisiyle karlilik tahmini yapmak.
Hedef degisken Profit ve amac en anlasilir, uygulanabilir modeli kurmak.

## Slayt 2: Problem ve Hedef

- Hedef: Profit tahmini (regresyon)
- Neden onemli: karlilik tahmini planlama ve kampanya kararlarini destekler

Konusma notu:
Bu projede Profit'i tahmin ediyoruz. Veri dogrusal degil, bu yuzden uygun modeli secmek kritik.

## Slayt 3: Veri Seti

- Kaynak: SampleSuperstore CSV
- Temel kolonlar: Sales, Profit, Discount, Quantity, Category, Sub-Category, Segment, Region, State, City, Ship Mode
- Tarih varsa: Order Date, Ship Date

Konusma notu:
Veri temel satis ve kategori bilgilerini iceriyor. Tarih varsa ek ozellikler uretiyoruz.

## Slayt 4: Temizleme ve Ozellik Muhendisligi

- Bos degerler: sayisal median, kategorik mod
- Kategorikler: stringe cevir + trim
- Tarih varsa: order_month, order_dayofweek, shipping_delay
- Tarih yoksa: sales_per_item, discounted_sales, is_high_discount

Konusma notu:
Sade ama saglam bir temizlik yaptim. Tarih yoksa bile islevsel ozellikler uretiyoruz.

## Slayt 5: Modelleme Akisi

- Pipeline: OneHotEncoder + StandardScaler
- Modeller: LinearRegression (baseline), RandomForestRegressor
- Profit hedefinde log1p donusumu (negatif varsa shift)

Konusma notu:
Baslangic icin lineer model kurdum, sonra agac tabanli RF ile guclendirdim.

## Slayt 6: Sonuclar (Metrikler)

| Model | MAE | RMSE | R2 |
| --- | --- | --- | --- |
| LinearRegression | 94.83 | 232.56 | -0.115 |
| RandomForestRegressor | 42.15 | 156.90 | 0.492 |

drop_geo testi (City/Postal Code/State cikartildi):
- LinearRegression: MAE 74.62, RMSE 211.84, R2 0.074
- RandomForestRegressor: MAE 25.98, RMSE 116.89, R2 0.718

Konusma notu:
Lineer model zayif kaldi; R2 negatif. Random Forest ile hata ciddi dustu ve R2 0.49 oldu.
Genelleme testi icin City/Postal Code/State cikardigimda RF R2 0.718 seviyesine cikti.

## Slayt 7: Feature Importance

- Sales (0.212), sales_per_item (0.178), discounted_sales (0.172)
- Discount (0.045) ve is_high_discount (0.036)
- City_Lancaster (0.042), Postal Code (0.038)
- Sub-Category_Machines (0.036), Sub-Category_Copiers (0.029)

Konusma notu:
Kar sadece satis miktarina bagli degil. Indirim ve urun tipi fark yaratiyor.
Bolgesel ve kategori kirilimlari da belirgin etki gosteriyor.

## Slayt 8: Sonuc

- Dogrusal model yeterli degil
- Random Forest daha basarili
- Indirim ve kategori bilgisi kritik

Konusma notu:
Bu veri tipi icin agac tabanli model daha uygun. Sonucu bu netlikte gordum.

## Slayt 9: Sinirlamalar ve Ileri Adimlar

- City/Postal Code gibi kolonlar overfit olabilir
- Hiperparametre aramasi ile iyilestirilebilir
- Daha iyi genelleme icin kategorik sadelestirme denenebilir

Konusma notu:
Modeli daha guclu yapmak icin bu iyilestirmeler planlanabilir.
drop_geo testi bu kolonlarin bazen gurultu yaratabilecegini gosterdi.

## Slayt 10: Soru - Cevap

Kisa cevap hazirliklari:
- "R2 neden negatif?" -> Linear model ortalamadan kotu kaldi.
- "Neden RF?" -> Dogrusal olmayan iliskileri yakaliyor.
- "profit_margin neden yok?" -> Leakage onlemek icin cikardim.

## 15 Saniyelik Ozet Cumlesi

"Linear Regression baseline olarak zayif kaldi; R2 negatif cikti. Random Forest ile MAE 94'ten 42'ye dustu ve R2 yaklasik 0.49 oldu. Yani karlilik iliskileri dogrusal degil; indirim ve kategori etkilerini RF daha iyi yakaladi."
