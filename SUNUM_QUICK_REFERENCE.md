# 🎤 SUNUM QUICK REFERENCE - Hızlı Bakış Kartı

**Çıktı:** Jüri önünde rahat konuşmak için taşınabilir bir cheat sheet.

---

## ⏱️ SUNUM SAATİ DAĞILIMI (7-9 dakika)

```
Slayt 1  (15 san)  │█          │ BAŞLIK
Slayt 2  (45 san)  │██         │ PROBLEM
Slayt 3  (45 san)  │██         │ VERİ SETİ
Slayt 4  (1 dk)    │███        │ TEMIZLEME + FE
Slayt 5  (1 dk)    │███        │ MODELLEME
Slayt 6  (1 dk)    │███        │ SONUÇLAR
Slayt 7  (1 dk)    │███        │ ABLATION TESTİ
Slayt 8  (1 dk)    │███        │ FEATURE IMP.
Slayt 9  (1 dk)    │███        │ SINIRLAMALAR
Slayt 10 (1 dk)    │███        │ SONUÇ & Q&A
─────────────────────────────────
TOPLAM:  ~9 dk     █████████  ✅
```

---

## 🎯 HER SLAYTA 1 CÜMLELİK ÖZET

| # | Başlık | Mesaj |
|---|--------|-------|
| 1 | BAŞLIK | "Bugün SampleSuperstore'un kârlılığını tahmin edebilen bir model göstereceğim" |
| 2 | PROBLEM | "Kârlılığı tahmin etmek neden zor? Çünkü doğrusal değil ve çok değişken var" |
| 3 | VERİ | "9.994 satır, 13 kolon: satış, kar, indirim, kategori ve bölge bilgisi" |
| 4 | TEMIZLEME | "Boşlukları doldurdum, outlier'ları tespit ettim ve yeni özellikler türettim" |
| 5 | MODEL | "İki model denedim: basit linear regression ve güçlü random forest" |
| 6 | SONUÇ | "LinearRegression başarısız (R²<0), RandomForest %49 doğruluk sağlıyor" |
| 7 | ABLATION | "Coğrafi özellikler çıkarınca model daha da iyileşti (R² 0.49→0.72)!" |
| 8 | ÖNEM | "En önemli 3: Sales, sales_per_item, discounted_sales - satış kalitesi önemli" |
| 9 | SINIRLAMA | "Tarih yok, dış faktörler yok, ama model genelleme yapıyor (drop_geo test)" |
| 10 | SONUÇ | "Kârlılık karmaşık, agaç modelleri uygun, indirim/kategori kritik" |

---

## 💬 SLAYT 2-10 AÇIKLAMA ŞABLONU (30 saniye per slide)

```
[SLAYT GÖSTER]
"Burada şunu görebiliyorsunuz: [BAŞLIK]"

[2-3 madde noktasını oku]
- "Birincisi ... [açıklama]"
- "İkincisi ... [açıklama]"
- "Üçüncüsü ... [açıklama]"

"Bu önemli çünkü [İŞ AÇIKLAMASI]"

[SONRAKI SLAYTA GEÇ]
```

---

## 🔥 KRITIK NOKTALAR (Bunları unutma!)

### 1️⃣ **Ablation Testi** (Slayt 7)
- R² 0.49 → 0.72 (%46 artış!)
- RMSE 156 → 116 (%27 azalış)
- **Mesaj:** "City/State kolonları modeli overfit ettiriyordu!"

### 2️⃣ **LinearRegression Başarısızlığı** (Slayt 6)
- R² = **-0.115** (ortalamadan KÖTÜ)
- **Mesaj:** "Bu veri doğrusal değil, ağaç modeli gerekli"

### 3️⃣ **Top 3 Features** (Slayt 8)
1. Sales (21.2%)
2. sales_per_item (17.8%)
3. discounted_sales (17.2%)
- **Mesaj:** "Kâr sadece satış miktarına değil, kalitesine de bağlı"

### 4️⃣ **Feature Engineering** (Slayt 4)
- sales_per_item, discounted_sales, is_high_discount
- **Mesaj:** "Veriyi sadece temizlemedim, anlam da kattım"

---

## ❓ OLASI SORULAR & HAZIR CEVAPLAR

### **S1: "R² neden bu kadar düşük (0.49)?"**

**Cevap (3 cümle):**
"İyi soru. R² 0.49 demek modelin varyansın %49'unu açıkladığı anlamı var. Profit, pek çok dış faktöre bağlı - sezon, pazar durumu, rekabet gibi şeyler veri setinde yok. Ama 0.49, basit bir perakende modeli için makul bir performans."

---

### **S2: "City/State kolonlarını neden çıkardınız?"**

**Cevap (3 cümle):**
"Ablation testi yaptığımızda, City ve Postal Code gibi coğrafi detaylar modeli overfit ettiriyordu. Bu özellikler eğitim verisi için çok spesifik veriler içeriyor - belki Lancaster şehrindeki satışlar tesadüfen karlıydı. Onları çıkarınca model daha genellenebilir hale geldi (R² 0.72)."

---

### **S3: "Neden RandomForest seçtiniz?"**

**Cevap (2 cümle):**
"LinearRegression'ı baseline olarak denedim ama R² negatif çıktı - veri doğrusal değil. RandomForest gibi ağaç tabanlı modeller non-linear ilişkileri yakalayabiliyor. Ayrıca feature importance'i doğal olarak veriyor, ki bu açıklanabilirlik için önemli."

---

### **S4: "Log dönüşümü neden uyguladınız?"**

**Cevap (2 cümle):**
"Profit'in negatif değerleri olduğu için direkt log alamıyoruz. log1p kullandım ve gereken yerlerde shift yaptım. Bu, büyük kar farkını küçülterek modeli daha stabil hale getirdi."

---

### **S5: "Streamlit uygulaması nasıl kullanılır?"**

**Cevap (3 cümle):**
"Streamlit uygulaması 3 sekmeye ayrılmış: 'Veri Özeti'nde özet istatistikler ve filtreler, 'EDA Grafikleri'nde dağılım ve korelasyon, 'Model Sonuçları'nda metrikler ve feature importance var. Filtreler sayesinde Region, Category, Segment'e göre veriyi filtreleyebilirsiniz."

---

### **S6: "Gelecek adımlar neler?"**

**Cevap (3 cümle):**
"Hiperparametre optimizasyonu yapabilirim - GridSearch ile max_depth, min_samples gibi parametreleri ayarlayabilirim. XGBoost gibi daha gelişmiş modelleri deneyebilirim. Ayrıca zaman serisi özellik mühendisliği yapılabilir - trend ve seasonality analizi."

---

### **S7: "Model üretimde nasıl kullanılır?"**

**Cevap (2 cümle):**
"Modeli joblib ile pickle halinde kaydedebilirim. Sonra yeni veriler gelince, aynı preprocessing pipeline'ı uygulaması ve model.predict() çağırması yeterli. API olarak Flask/FastAPI'le wrap edebilirim."

---

## 📱 SUNUSU AÇMA KONTROL LİSTESİ

Jüri Salonına girerken kontrol et:
- [ ] Laptop şarjlı (100%)
- [ ] Canva sunuş PDF açıldı (veya PowerPoint)
- [ ] Streamlit uygulaması arka planda hazır
- [ ] WiFi bağlantısı açık
- [ ] Ses çalışıyor (hoparlör/kulaklık)
- [ ] Ekran saat gösteriyor (zamanlamak için)
- [ ] Fare işaretçisi görünüyor

---

## 🎬 SUNUŞ BAŞLAMADAN 1 DAKIKA ÖNCE

**Psikolojik hazırlık:**

"Bu projeyi benim yaptım, ona hakim olan ben'im. Jüri beni merak ediyor, korkmuyor. Açık, net, kendine güvenli konuş. Sesini işit, gözlerini tut. Başarıyla bitireceğim."

**Fiziksel hazırlık:**

- 3 derin nefes al ve ver
- Omuzlarını çöz
- Cümlelerini tekrar et (ilk 30 saniye)
- Gülümse

---

## 🏁 SUNUM SONUNDA SAY ETSİ CÜMLE

"**Kârlılık, sadece satış miktarından daha fazlası. Doğru model seçimi ve veri anlayışı ile işletme kararlarını destekleyebiliriz. Teşekkürler, sorularınızı dinlemek için hazırım.**"

---

## 📞 EN SON ANINDA PANIKLARSAM?

| Sorun | Çözüm |
|-------|-------|
| "Sesi unuttum" | JURI_SUNUM_AKISI.md'yi söz söz oku (bu dosya!) |
| "Hangi slayt sonrası?" | "Sonraki slayta geçelim" de ve ilerlet |
| "Streamlit çalışmıyor?" | "Ekran görüntüsü gösterelim" de, PDF'den devam et |
| "Zaman bitiyor?" | Slayt 9-10'u atlayıp direkt sonuca git |
| "Soru anlamamışım?" | "Harika soru, daha detaylı anlatabilir miyim?" de |

---

## ✅ 24 SAAT ÖNCESI SON MADDE

- [ ] JURI_SUNUM_AKISI.md'yi bir daha oku
- [ ] 10 dakikalık mock sunuş yap
- [ ] Canva PDF'ini bir daha aç ve kontrol et
- [ ] Bu quick reference kartını bastır + yanına al
- [ ] Erken yat ✌️

---

**SON SÖZCÜKLER:**

> "İnsan sunumda mükemmel olmak zorunda değil. Hazırlanmış, samimi, ve konuştuğu şeyi seven biri olmak yeterli. Sen o kişisin. Başarılı olacaksın. 🚀"

**İYİ ŞANSLAR!**
