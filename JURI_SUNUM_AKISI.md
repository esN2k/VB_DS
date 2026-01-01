# JÜRİ SUNUM AKIŞI - Konuşma Metni

**Süre:** 7-9 dakika  
**Stil:** Doğal, öğrenci dili, kendine güvenli  
**Format:** Slayt + Canlı Demo

---

## 🎯 SLAYT 1: BAŞLIK (15 saniye)

**Ekran:** Başlık slaytı

**Konuş:**

"Merhaba, ben [İsim]. Bugün size Profit Tahmini projemi sunacağım. SampleSuperstore veri setiyle kârlılığı tahmin eden bir regresyon modeli geliştirdim."

---

## 📊 SLAYT 2: PROBLEM TANIMI (30 saniye)

**Ekran:** Problem tanımı

**Konuş:**

"Problemim şu: Bir perakende şirketinin satış verilerini kullanarak kârlılığı tahmin etmek istiyorum. Bu bir regresyon problemi çünkü sürekli bir değer tahmin ediyoruz."

"Neden önemli? Çünkü şirketler hangi ürünlerin, hangi bölgelerin daha karlı olduğunu bilmek istiyor. Bu da stratejik kararlar için kritik."

---

## 💾 SLAYT 3: VERİ SETİ (45 saniye)

**Ekran:** Veri seti bilgileri

**Konuş:**

"Veri setim SampleSuperstore. 9,994 satır ve 13 kolon var. Sales, Profit, Discount, Quantity gibi sayısal kolonlar ve Category, Region, Segment gibi kategorik kolonlar mevcut."

"İlk işim veriyi temizlemek oldu. Eksik değerleri sayısal kolonlarda median, kategorik kolonlarda mod ile tamamladım. Kategorik alanlarda strip yaparak boşlukları temizledim."

"Outlier'lar için IQR yöntemi kullandım ama silmedim - sadece raporladım. Çünkü gerçek dünyada aykırı satışlar doğal olabilir."

---

## 🔧 SLAYT 4: FEATURE ENGINEERING (1 dakika)

**Ekran:** Feature engineering açıklaması

**Konuş:**

"Feature engineering kısmında veri setinde tarih kolonu olmadığı için şu feature'ları türettim:"

"sales_per_item: Her ürünün birim fiyatı. Sales'i Quantity'ye böldüm."

"discounted_sales: İndirim sonrası net satış. Sales çarpı 1 eksi Discount."

"profit_margin: Kar marjı. Profit'i Sales'e böldüm. Ama dikkat - bu feature'ı leakage yaratacağı için model eğitiminde drop ettim. Çünkü doğrudan hedef değişkenden türetilmiş."

"is_high_discount: İndirim yüzde 30'dan büyükse 1, değilse 0. Binary bir flag."

---

## 🤖 SLAYT 5: MODELLEME (1.5 dakika)

**Ekran:** Model mimarisi

**Konuş:**

"Modelleme kısmında sklearn pipeline kullandım. Kategorik değişkenler için OneHotEncoder, sayısal değişkenler için StandardScaler uyguladım."

"İki model denedim: LinearRegression baseline olarak, RandomForestRegressor daha güçlü bir model olarak."

"Önemli bir nokta: Profit negatif değerler içerebildiği için log dönüşümü direkt uygulanamıyor. Bu yüzden shift + log1p kullandım. Minimum değer negatifse otomatik shift ekledim."

"Train-test split yüzde 80-20 yaptım, random seed 42 ile sabitledi m. Bu sayede sonuçlar tekrar edilebilir."

---

## 📈 SLAYT 6: SONUÇLAR (1.5 dakika)

**Ekran:** Metrik tablosu (Full model)

**Konuş:**

"Sonuçlara bakalım. LinearRegression baseline olarak çok zayıf kaldı - R² negatif çıktı. Bu modelin veri setini açıklayamadığını gösteriyor."

"RandomForest çok daha iyi performans verdi. R² 0.492, MAE 42.15, RMSE 156.9. Yani modelin yüzde 49'luk bir açıklama gücü var."

"Ama asıl ilginç kısım ablation testinde..."

---

## 🔬 SLAYT 7: ABLATION TESTİ (1.5 dakika)

**Ekran:** Full vs No-Geo karşılaştırması

**Konuş:**

"Ablation testi yaptım. City, State ve Postal Code kolonlarını çıkarıp modeli tekrar eğittim. Bunlara 'geo kolonları' diyorum."

"Sonuç şaşırtıcıydı: Model performansı arttı! R² 0.492'den 0.718'e çıktı. MAE de 42'den 26'ya düştü."

"Neden? Çünkü geo kolonları çok yüksek kardinaliteye sahip - yüzlerce benzersiz şehir var. Bu model karmaşıklığını artırıyor ve overfit'e yol açıyor."

"Bu sonuç bana geo bilgisinin bu veri setinde dolaylı etki etse de, Sales, Discount ve türettiğim feature'ların daha güçlü olduğunu gösterdi."

---

## 💡 SLAYT 8: FEATURE IMPORTANCE (1 dakika)

**Ekran:** Top-10 feature importance bar chart

**Konuş:**

"RandomForest bize hangi feature'ların önemli olduğunu söylüyor."

"En önemli üç feature: Sales (0.21), sales_per_item (0.18) ve discounted_sales (0.17). Bunlar benim türettiğim feature'lar ve domain knowledge kullanarak oluşturdum."

"Discount da etkili ama Sales kadar değil. City_Lancaster gibi bazı şehirler de önemli çıkmış ama bunlar overfit riski taşıyor."

---

## 🎯 SLAYT 9: CANLIDEPO (2 dakika)

**Ekran:** Streamlit uygulaması

**Konuş:**

"Şimdi size çalışan uygulamayı göstereyim."

[DEMO_SCRIPT.md'deki Demo Akışını Takip Et]

- Veri Özeti sekmesini göster
- EDA grafiklerini göster (Profit dağılımı, Sales vs Profit)
- Model Sonuçlarını göster (Full vs No-Geo karşılaştırma)
- Feature importance grafiğini göster

**Konuş:**

"Görüldüğü gibi proje baştan sona çalışıyor. Tek komutla pipeline çalıştırılabilir, sonuçlar tekrar edilebilir."

---

## 📝 SLAYT 10: SONUÇ VE ÖZET (45 saniye)

**Ekran:** Özet slaytı

**Konuş:**

"Özetlersek:"

"9,994 satırlık veriyi temizledim, feature engineering yaptım. LinearRegression ve RandomForest modellerini karşılaştırdım."

"Ablation testi ile geo kolonlarını çıkarmak modeli iyileştirdi - R² 0.718'e ulaştım."

"Leakage önlemi olarak profit_margin'i eğitimden drop ettim. Outlier'ları sildim yerine raporladım. Log dönüşümü için shift kullandım."

"Proje reproducible - tüm adımlar random seed ile sabitlendive tek komutla çalıştırılabilir."

"Teşekkür ederim. Sorularınızı alabilirim."

---

## ❓ OLASI SORULAR VE CEVAPLAR

### "Overfit riski var mı?"

"RandomForest 200 ağaç kullanıyor ama min_samples_leaf=2 ve max_features='sqrt' ile sınırlandırdım. Test/train split yüzde 80-20 yaptım. No-Geo senaryoda R² artışı overfit azaldığını gösteriyor. Ancak cross-validation yapmadım, bu gelecekte eklenebilir."

### "Neden log dönüşümü kullandınız?"

"Profit dağılımı sağa çarpık ve negatif değerler içeriyor. log1p direkt uygulanamaz negatif değerlere. Bu yüzden minimum değer negatifse otomatik shift ekliyorum. Böylece log dönüşümü çalışır ve çarpık dağılımı düzeltir."

### "Geo kolonlarını neden çıkardınız?"

"Ablation testi yaptım. City/Postal Code gibi alanlar çok fazla benzersiz değer içeriyor - yüksek kardinalite. Bu model karmaşıklığını artırıyor ve genellemeyi zorlaştırıyor. No-Geo'da R² 0.718'e çıktı, yani model daha genellenebilir oldu."

### "Hiperparametre optimizasyonu yaptınız mı?"

"Manuel ayar yaptım ama grid search/random search yapmadım. RandomForest'te n_estimators=200, min_samples_leaf=2, max_features='sqrt' parametrelerini deneme yanılmayla belirledim. Grid search yapılabilir ama zaman kısıtından dolayı manuel yaptım."

### "Cross-validation neden yok?"

"Zaman kısıtı. Ama basit train-test split kullandım ve random seed sabitledim. Cross-validation eklemek sonuçları daha robust yapardı, bu gelecek iyileştirme olarak planlanabilir."

---

## 📌 SUNUM SIRASINDA DİKKAT!

### Beden Dili
- ✅ Jüriye bak, ekrana değil
- ✅ Ellerini doğal kullan
- ✅ Güven içinde dik dur
- ✅ Gülümse, rahat ol

### Konuşma Stili
- ✅ Net ve yavaş konuş
- ✅ Öğrenci dili kullan (robotik değil)
- ✅ "Ben yaptım", "benim yaklaşımım" de
- ✅ Meraklı ve hevesli ol

### Teknik Detaylar
- ✅ Metrikleri tam söyle (R² 0.718, MAE 42.15)
- ✅ Sayıları vurgula (9,994 satır, 200 ağaç)
- ✅ Kod gösterme (sormadıkça)
- ✅ Jargon kullan ama açıkla

---

## ⏱️ ZAMANLAMA KONTROLÜ

| Slayt | Bölüm | Süre |
|-------|-------|------|
| 1 | Başlık | 15s |
| 2 | Problem | 30s |
| 3 | Veri Seti | 45s |
| 4 | Feature Engineering | 1dk |
| 5 | Modelleme | 1.5dk |
| 6 | Sonuçlar | 1.5dk |
| 7 | Ablation | 1.5dk |
| 8 | Feature Importance | 1dk |
| 9 | Canlı Demo | 2dk |
| 10 | Sonuç | 45s |
| **TOPLAM** | | **~9dk** |

---

## 🎬 SON HAZIRLIK

**Sunum öncesi 10 dakika:**
1. Derin nefes al, rahat ol
2. Su iç
3. Slaytları bir kez gözden geçir
4. Streamlit'i test et
5. Güven içinde sahneye çık!

**Unutma:** Sen bu projeyi yaptın, en iyi sen biliyorsun. Jüri seninle tanışmak için burada. Rahat ol, kendine güven, başarısın! 💪🎓
