# SUNUM - Juri Sunum Metni ve Akis

Bu dosya sunumda kullanman icin hazir bir akistir.
Her slayt icin kisa baslik, madde ve konusma notu var.

## Slayt 1: Baslik

**Baslik:** Kar (Profit) Tahmini - SampleSuperstore

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

- Bos degerler: sayisal medyan, kategorik mod
- Kategorikler: stringe cevir + trim
- Tarih varsa: order_month, order_dayofweek, shipping_delay
- Tarih yoksa: sales_per_item, discounted_sales, is_high_discount

Konusma notu:
Sade ama saglam bir temizlik yaptim. Tarih yoksa bile islevsel ozellikler uretiyoruz.

## Slayt 5: Modelleme Akisi

- Is akisi: OneHotEncoder + StandardScaler
- Modeller: LinearRegression (temel), RandomForestRegressor
- Profit hedefinde log1p donusumu (negatif varsa shift)

Konusma notu:
Baslangic icin lineer model kurdum, sonra agac tabanli RF ile guclendirdim.

## Slayt 6: Sonuclar (Metrikler)

| Model | MAE | RMSE | R2 |
| --- | --- | --- | --- |
| LinearRegression | 94.83 | 232.56 | -0.115 |
| RandomForestRegressor | 42.15 | 156.90 | 0.492 |

drop_geo deneyi (City/Postal Code/State cikarildi):
- LinearRegression: MAE 74.62, RMSE 211.84, R2 0.074
- RandomForestRegressor: MAE 25.98, RMSE 116.89, R2 0.718

Konusma notu:
Lineer model zayif kaldi; R2 negatif. Random Forest ile hata ciddi dustu ve R2 0.49 oldu.
Bir de asiri uyum ihtimalini gormek icin drop_geo deneyi yaptim.
City/State/Postal Code kolonlarini cikarinca Random Forest performansi daha da yukseltti:
R2 0.49'dan 0.718'e cikti, RMSE 156'dan 116'ya dustu.

## Slayt 7: Ozellik Onemi

- Sales (0.212), sales_per_item (0.178), discounted_sales (0.172)
- Discount (0.045) ve is_high_discount (0.036)
- City_Lancaster (0.042), Postal Code (0.038)
- Sub-Category_Machines (0.036), Sub-Category_Copiers (0.029)

Konusma notu:
Kar sadece satis miktarina bagli degil. Indirim ve urun tipi fark yaratiyor.
Bolgesel ve kategori kirilimlari da belirgin etki gosteriyor.

## Slayt 8: Sonuc

- Dogrusal model yeterli degil
- Agac tabanli model daha basarili
- Geo kolonlari gerektiginde cikarilabilir

Konusma notu:
Genel sonuc: veri dogrusal degil, agac tabanli model daha uygun. Geo kolonlari ise
asiri uyum yaratabildigi icin kontrollu kullanilmali.

## Slayt 9: Sinirlamalar ve Gelecek Calismalar

- Geo kolonlari asiri uyum riski tasir
- Hiperparametre aramasi performansi artirabilir
- Kategori sadelestirme denenebilir

Konusma notu:
Bu calisma temel bir modelleme. Daha iyi genelleme icin ileri adimlar var.

## Slayt 10: Kapanis

- Sorular?
- Tesekkurler

Konusma notu:
Kisaca ozetledim, sorulari memnuniyetle yanitlarim.
