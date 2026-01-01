# CANVA SLIDESHOW HAZIRLAMA REHBERI
## Jüri Sunumu için Adım Adım Rehber

**Süre:** 7-9 dakika  
**Slayt Sayısı:** 10 slayt  
**Format:** Canva Pro (veya ücretsiz Canva)  
**Tema:** Profesyonel, koyu veya açık background

---

## 📋 SLAYT YAPISI VE İÇERİK

### ⏱️ Zaman Dağılımı
- Slayt 1: 15 saniye
- Slaytlar 2-7: 1 dakika × 6 = 6 dakika
- Slaytlar 8-10: 1 dakika × 3 = 3 dakika
- **Toplam: ~9 dakika**

---

## 🎨 SLAYT DETAYLARI

### **SLAYT 1: BAŞLIK (15 saniye)**

**Başlık:** Profit Tahmini Projesi - SampleSuperstore  
**Alt Başlık:** Veri Bilimi & Machine Learning  
**Görseller:** 
- Proje logosu veya işletme görseli
- Veri setinin örnek verisi

**Konuşacağın:**
"Merhaba, ben [İsmin]. Bugün size Profit Tahmini projemi sunacağım. SampleSuperstore veri setiyle perakende şirketinin kârlılığını tahmin eden bir regresyon modeli geliştirdim."

---

### **SLAYT 2: PROBLEM TANIMI (45 saniye)**

**Başlık:** Problem Nedir?

**Madde Noktaları:**
- ❓ **Soru:** Satış verilerinden kârlılığı tahmin edebilir miyiz?
- 📊 **Problem Türü:** Regresyon (sürekli değer tahmini)
- 💰 **İş Değeri:** 
  - Hangi ürünler daha karlı?
  - Hangi bölgeler daha başarılı?
  - İndirim stratejisi nasıl olmalı?
- 🎯 **Hedef:** Doğru, uygulanabilir bir model oluşturmak

**Görseller:**
- Perakende/satış ilişkili görsel
- Çoklu değişken ilişkisini gösteren basit infografik

**Konuşacağın:**
"Problemim şu: Bir perakende şirketinin satış verilerini kullanarak kârlılığı tahmin etmek istiyorum. Bu regresyon problemidir çünkü sürekli bir değer (Profit) tahmin ediyoruz.

Neden önemli? Çünkü şirketler hangi ürünlerin, hangi bölgelerin daha karlı olduğunu bilmek istiyor. Bu bilgi stratejik kararlar için kritiktir."

---

### **SLAYT 3: VERİ SETİ (45 saniye)**

**Başlık:** Veri Seti: SampleSuperstore

**İstatistikler Box'ı:**
```
📊 TEMEL STATS
━━━━━━━━━━━━━━━
Satır: 9,994
Kolon: 13
Tarih Aralığı: 2011-2015
```

**Veriler:**
| Kategori | Kolon | Örnek |
|----------|-------|--------|
| **Sayısal** | Sales, Profit, Discount, Quantity | 150.23, 25.50, 0.2, 3 |
| **Kategorik** | Category, Region, Segment, State | Office Supplies, East, Consumer, NY |
| **Meta** | Order Date, Ship Mode | 2015-01-05, Same Day |

**Görseller:**
- Veri seti özeti tablosunun ekran görüntüsü
- Profit dağılım grafiği (histogram)

**Konuşacağın:**
"Veri setim SampleSuperstore. 9,994 satır ve 13 kolon var. Sales, Profit, Discount, Quantity gibi sayısal kolonlar; Category, Region, Segment gibi kategorik kolonlar mevcut.

İlk işim veriyi temizlemek oldu. Eksik değerleri sayısal kolonlarda median ile, kategorik kolonlarda mod ile tamamladım. Kategorik alanlarda trim yaparak boşlukları temizledim."

---

### **SLAYT 4: TEMIZLEME & FEATURE ENGINEERING (1 dakika)**

**Başlık:** Veri Hazırlama

**Sol Taraf - Temizleme:**
- ✅ Eksik değerler (Sayısal: Median, Kategorik: Mod)
- ✅ Beyaz alan temizliği (Trim)
- ✅ Outlier analizi (IQR)
- ✅ Veri tipi dönüşümleri

**Sağ Taraf - Feature Engineering:**
- 📌 `sales_per_item`: Sales / Quantity
- 📌 `discounted_sales`: Sales × (1 - Discount)
- 📌 `is_high_discount`: Discount > 0.3 → 1/0
- 📌 `profit_margin`: (Dropped - Leakage)

**Görseller:**
- Temizleme adımları infografik
- Feature engineering formülleri

**Konuşacağın:**
"Feature engineering kısmında şu feature'ları türettim:

- **sales_per_item**: Her ürünün birim fiyatı. Sales'i Quantity'ye böldüm.
- **discounted_sales**: İndirim sonrası net satış.
- **is_high_discount**: İndirim yüzde 30'dan büyükse flag.

Dikkat ettim - profit_margin feature'ı leakage yaratacağı için model eğitiminde drop ettim."

---

### **SLAYT 5: MODELLEME (1 dakika)**

**Başlık:** Model Mimarisi

**Pipeline Diyagramı:**

```
┌─────────────────┐
│  Raw Data       │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Cleaning │
    └────┬────┘
         │
  ┌──────┴──────┐
  │              │
┌─▼──┐      ┌───▼────┐
│Num │      │Categor.│
└─┬──┘      └───┬────┘
  │             │
  ▼             ▼
[Standard]  [OneHot]
  Scaler     Encoder
  │             │
  └─────┬───────┘
        │
    ┌───▼─────┐
    │ Pipeline│
    └───┬─────┘
        │
  ┌─────┴────────┐
  │              │
  ▼              ▼
Linear        RandomForest
Regression    Regressor
```

**Modeller:**
- **LinearRegression**: Baseline (basit, hızlı)
- **RandomForestRegressor**: Ana model (güçlü)

**Özel İşlemler:**
- 🔄 Profit dönüşümü: `log1p(shift_if_negative(Profit))`
- 📊 Kategori encoding: OneHotEncoder
- 📐 Sayısal ölçekleme: StandardScaler
- 🔀 Train-Test: 80-20 (Seed=42)

**Konuşacağın:**
"Modelleme kısmında sklearn pipeline kullandım. Kategorik değişkenler için OneHotEncoder, sayısal değişkenler için StandardScaler uyguladım.

İki model denedim: LinearRegression baseline olarak, RandomForestRegressor daha güçlü bir model olarak.

Önemli bir nokta: Profit negatif değerler içerebildiği için log dönüşümü direkt uygulanamıyor. Bu yüzden shift + log1p kullandım."

---

### **SLAYT 6: SONUÇLAR - METRIKLER (1 dakika)**

**Başlık:** Model Performansı

**Grafik 1: Metrik Karşılaştırması**
```
        MAE        RMSE       R²
Linear:  94.83     232.56    -0.115  ❌
RF:      42.15     156.90     0.492  ✅
```

**Görseller:**
- Bar chart: MAE, RMSE, R² değerleri
- Tablo: Tam metrikler

**Açıklamalar:**
- 📉 **LinearRegression**: Çok zayıf (R² negatif = ortalamadan kötü)
- ✅ **RandomForest**: Çok daha iyi (R² 0.49 = %49 açıklama gücü)
- 📊 **Hata Metrikleri**: MAE 42 $ ortalama hata

**Konuşacağın:**
"Sonuçlara bakalım. LinearRegression baseline olarak çok zayıf kaldı - R² negatif çıktı. Bu modelin veri setini açıklayamadığını gösteriyor.

RandomForest çok daha iyi performans verdi. R² 0.492, MAE 42.15, RMSE 156.9. Yani modelin yüzde 49'luk bir açıklama gücü var. Ama asıl ilginç kısım ablation testinde..."

---

### **SLAYT 7: ABLATION TESTİ (1 dakika)**

**Başlık:** City/State Kolonlarının Etkisi

**Grafikler (Yan Yana):**

**Full Model:**
- MAE: 42.15
- RMSE: 156.90
- R²: 0.492

**No-Geo Model:**
- MAE: 25.98 ⬇️
- RMSE: 116.89 ⬇️
- R²: 0.718 ⬆️

**Ok Göstergeleri:**
```
R² 0.49 ➜ 0.72 (+46% artış!) ✅
RMSE 156 ➜ 116 (-27% azalış) ✅
```

**Yorumlar:**
- 🤔 City/State/Postal Code kolonları overfit yaratıyor
- 📈 Model genelleştirme yeteneği artıyor
- 🎯 Daha basit model daha iyi sonuç veriyor (Occam's Razor)

**Konuşacağın:**
"Ablation testi yaptım. City, State ve Postal Code kolonlarını çıkarıp modeli tekrar eğittim.

Sonuç beni şaşırttı! RandomForest performansı daha da iyileşti:
- R² 0.49'dan 0.72'ye çıktı
- RMSE 156'dan 116'ya düştü

Bu bize ne söylüyor? City/Postal Code gibi detaylı konum verisi modeli overfit ettiriyor. Daha basit model daha iyi genelleme yapıyor."

---

### **SLAYT 8: FEATURE IMPORTANCE (1 dakika)**

**Başlık:** En Önemli 10 Özellik

**Bar Chart:**
```
Sales                ████████████░ 21.2%
sales_per_item       ███████████░░ 17.8%
discounted_sales     ███████████░░ 17.2%
Sub-Category_Techn   ████░░░░░░░░  5.6%
Segment_Consumer     ████░░░░░░░░  5.2%
Category_Office      ███░░░░░░░░░  4.7%
Region_West          ███░░░░░░░░░  4.2%
Discount             ██░░░░░░░░░░  4.5%
is_high_discount     ██░░░░░░░░░░  3.6%
Sub-Category_Copier  ██░░░░░░░░░░  3.2%
```

**Görseller:**
- Yatay bar chart (top10_importance.csv'den)
- Renkli gösterim (önemli olanlar farklı renk)

**İnsan Diline:**
- 🏆 **Top 3**: Sales, sales_per_item, discounted_sales (satış türü)
- 💰 **Kategori**: Technology, Office, Consumer önemli
- 🎯 **İndirim**: Yüksek indirim risk faktörü

**Konuşacağın:**
"Feature importance diyecek olursam: Sales, sales_per_item ve discounted_sales en önemli 3 özellik.

Yani kâr sadece satış miktarına bağlı değil. İndirim miktarı ve ürün tipi kritik. Technology sub-kategorisinin ve Consumer segmentinin kârlılıkta önemli rolü var."

---

### **SLAYT 9: SINIRLAMALAR & İLERİ ADIMLAR (1 dakika)**

**Başlık:** Sinirlamalar & Gelecek Planları

**Sınırlamalar:**
- ⚠️ Tarih bilgisi kısıtlı (Order/Ship Date ancak ay düzeyinde)
- ⚠️ Dış faktörler yok (pazar durumu, rekabet, mevsimsel etkiler)
- ⚠️ Coğrafi features overfit riski (drop_geo ile adreslenmiş)
- ⚠️ Küçük ürün kategorileri yeterli veri yok

**İleri Adımlar:**
- 🔬 Hiperparametre optimizasyonu (GridSearch)
- 📈 XGBoost/LightGBM denemeleri
- 🗓️ Zaman serisi analizi (trend, seasonality)
- 🎯 Feature selection ile model sadeleştirme
- 🌐 Cross-validation ve ensemble yöntemleri

**Konuşacağın:**
"Tabii modeli daha iyi yapabiliriz. Hiperparametre araması, XGBoost denemeleri, ve daha detaylı zaman analizi yapılabilir.

Ama şu an için bu basit ama etkili bir çözüm sağlıyor."

---

### **SLAYT 10: SONUÇ & SORU-CEVAP (1 dakika)**

**Başlık:** Sonuç

**Temel Bulguları:**
1. ✅ Kârlılık **doğrusal olmayan** ilişkiler içeriyor
2. ✅ **Agac tabanli modeller** (RandomForest) uygun
3. ✅ **İndirim & kategori** bilgisi kritik
4. ✅ Coğrafi features **dikkatli kullanılmalı**
5. ✅ Model **genelleştirilebilir** (drop_geo test)

**Son Söz:**
"Bu veri seti, kârlılığın sadece satış miktarından daha fazlası olduğunu gösteriyor. Doğru model seçimi ve özellik mühendisliği ile güçlü tahminler yapabiliriz."

**Soru-Cevap:**
- 💬 "R² neden düşük?" → Kâr birçok dış faktöre bağlı (pazar, sezon, vb.)
- 💬 "Neden No-Geo daha iyi?" → Coğrafi features overfit yaratıyor
- 💬 "Model üretimde nasıl kullanılır?" → Pickle/joblib ile deploy edilebilir
- 💬 "Başka veri seti deneyip testiniz mi?" → Benzer yapıdaki e-ticaret verisi uygulanabilir

---

## 🎬 CANVA TASARIMI İPUÇLARI

### Renk Şeması
- **Ana Renk**: Navy Blue (#001f3f) veya Deep Purple (#4a148c)
- **Vurgu**: Accent Green (#2ecc71) veya Orange (#ff6b6b)
- **Arka Plan**: Beyaz veya açık gri (#f8f9fa)
- **Metin**: Koyu gri/siyah okunabilir için

### Font Seçimi
- **Başlıklar**: Bold Sans-serif (Poppins, Montserrat, Roboto Bold)
- **Body Text**: Regular Sans-serif (Open Sans, Lato, Inter)
- **Kod/Teknik**: Monospace (Courier New, Monaco)

### Görseller
- ✅ Charts/Graphs: Matplotlib/Seaborn'dan PNG export (300 DPI)
- ✅ Icons: Flaticon, FontAwesome, emoji
- ✅ Fotoğraflar: Unsplash, Pexels (lisanslı)
- ✅ Veri Tabloları: Temiz, readable tablo yapısı

### Düzen (Layout)
- 📐 **Alignment**: Grid layout, center-aligned başlıklar
- 📏 **Boşluk**: Generous whitespace (overload etme)
- 📊 **Görsel Hiyerarşi**: Başlık > Madde > Detay
- 🎨 **Konsistens**: Her slayt aynı tema

### Animasyon (İsteğe Bağlı)
- ⏱️ Madde noktaları: Appear on click
- 📊 Grafikler: Draw animation
- 🎯 Başlık: Fade in
- ⚠️ Kısa tutun (profesyonel kalabilmesi için)

---

## ✅ CANVA'DA YAPMADAN ÖNCE KONTROL LİSTESİ

- [ ] Slaytlar için gerekli görselleri topla:
  - [ ] Metrik tabloları (CSV'den copy-paste)
  - [ ] Grafikler (reports/figures/ klasöründen)
  - [ ] Logo/branding (varsa)

- [ ] Konuşma metnini hazırla:
  - [ ] `JURI_SUNUM_AKISI.md` oku
  - [ ] Kendi kelimelerin ile uyarla
  - [ ] 7-9 dakika zamanlama yap

- [ ] İnsan okumayan kontrolleri:
  - [ ] Font okunabilir mi? (12pt minimum)
  - [ ] Renkler yeterli kontrast sağlıyor mu?
  - [ ] Slaytlar kalabalık değil mi?

- [ ] Canva ayarları:
  - [ ] Ölçek: Widescreen (16:9) ✅
  - [ ] Export: PDF + PPTX (yedek olarak)

---

## 📥 DOSYALARI CANVA'YA AKTARMA

### Option 1: Canva'da Direkt
1. **Canva.com** → "Create a presentation"
2. "Blank" → 16:9 widescreen seç
3. Slayt başına bir tane ekle
4. Görselleri "Upload" → Dosyalar yükle

### Option 2: PowerPoint → Canva
1. SUNUM_SLIDES.pptx'i aç (varsa)
2. Canva'da "Import" → PPTX yükle
3. Düzenle ve iyileştir

### Option 3: Markdown → Canva (Manuel)
1. Bu rehberi Canva'da slayta slayta dönüştür
2. Metni copy-paste et
3. Görselleri yerleştir

---

## 🚀 SUNUMU BAŞARILI YAPMANIN TAKTIKLERI

### Fiziksel Sunumu Sırasında
1. **Başlayın Güçlü:** Göz teması, gülümseme, net ses
2. **Slayt ile Konuş:** Slaydı okuma, slayd açıklıyor
3. **Hızı Ayarla:** Her slayt 1 dakika (±15 saniye)
4. **Soruları Hoşla:** "Harika soru, X'de açıklanıyor" cevapla
5. **Bitirin Kuvvetli:** Sonuç slaydına dön, teşekkürler, Q&A

### Canlı Demo (İsteğe Bağlı)
- Streamlit başlamadan önce test et
- "Şimdi canlı demo yapayım" deyip aç (8-9 dakika sunum sonrası)
- Basit adımlar: Veri sekmesi → EDA → Model sonuçları

### Acil Durum Planları
- 🔴 Streamlit çalışmazsa → Ekran görüntüsü sunumunda hazırla
- 🔴 Internet düşerse → PDF offline kal
- 🔴 Sesi hisseden demişse → Konuşmayı yavaşla, madde göster

---

## 📞 HALA SORU VAR MI?

Eğer Canva slaytlarını hazırlarken tıkandıysan:
- `JURI_SUNUM_AKISI.md` kontrol et (detaylı metin)
- `DEMO_SCRIPT.md` kontrol et (senaryo)
- `reports/figures/` den görselleri kullan (hazır grafikler)

**Başarılar! 🎉**
