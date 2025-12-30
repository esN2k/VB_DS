# OZET_SONUC - Tek Sayfalik Ozet + Sonuc

## Ozet (Abstract)

Bu projede hedef degisken olarak **Profit (kar)** secildi ve SampleSuperstore verisi kullanildi.
Veri temizleme adiminda sayisal bosluklar median ile, kategorik bosluklar mod ile tamamlandi.
Kategorik alanlar stringe cevrildi ve trim uygulandi. Tarih yoksa sales_per_item,
discounted_sales ve is_high_discount gibi ek ozellikler uretildi.
Modelleme icin OneHotEncoder + StandardScaler pipeline'i kuruldu ve iki model karsilastirildi:
LinearRegression (baseline) ve RandomForestRegressor. Profit negatif olabildigi icin hedefe
log1p donusumu uygulandi (gerekirse shift).
Son kosuda LinearRegression MAE 94.83, RMSE 232.56, R2 -0.115 verirken,
RandomForestRegressor MAE 42.15, RMSE 156.90, R2 0.492 sonucunu verdi.
Bu nedenle nihai model olarak Random Forest daha basarili kabul edildi.

## Sonuc

Sonuclar, karliligin dogrusal olmayan iliskiler icerdigini ve agac tabanli modellerin
bu veri setinde daha uygun oldugunu gosterdi. En etkili degiskenler Sales,
sales_per_item ve discounted_sales oldu; indirim ile urun alt kategorileri de
kar uzerinde belirgin etki yaratti. Buna karsin City/Postal Code gibi bolgesel
degiskenler overfit riski tasiyabilir. Ileri adim olarak hiperparametre aramasi
ve kategorik sadelestirme ile daha genellenebilir bir model denenebilir.
