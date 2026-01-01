# DEMO SCRIPT - Jüri Sunumu Canlı Demo Akışı

**Süre:** 5-7 dakika  
**Amaç:** Projenin çalışır halini jüriye göstermek

---

## 📋 Hazırlık (Sunum Öncesi)

### Terminal Hazırlığı
```powershell
# Sanal ortamı aktif et
.venv\Scripts\activate

# Pipeline çalıştır (eğer güncel değilse)
python -m src.run_pipeline

# Streamlit başlat (arka planda)
streamlit run src/app_streamlit.py
```

### Tarayıcı Hazırlığı
- Streamlit app açık olmalı: http://localhost:8501
- Sekme 1: Veri Özeti
- Sekme 2: EDA Grafikleri
- Sekme 3: Model Sonuçları

---

## 🎯 Demo Akışı (5-7 Dakika)

### 1. GİRİŞ (30 saniye)

**Söyle:**
> "Merhaba, ben [İsim]. Bugün size SampleSuperstore verisiyle kâr tahmini projemi göstereceğim. 
> Bu bir regresyon problemi ve amacım satış verilerinden kârlılığı tahmin etmek."

**Ekranda:**
- Streamlit ana sayfa görünüyor
- Başlık: "VB_DS Profit Tahmini Projesi"

---

### 2. VERİ ÖZETİ (1 dakika)

**Söyle:**
> "Öncelikle verimize bakalım."

**Yap:**
1. "Veri Özeti" sekmesini göster
2. Metrikleri işaret et:
   - "9,994 satır veri var"
   - "17 kolon: 9 sayısal, 8 kategorik"
   - "Eksik değer yok - temizleme yaptım"

**Söyle:**
> "Veriye filtre uygulayabilirim. Mesela Technology kategorisine bakalım."

**Yap:**
- Category dropdown → "Technology" seç
- Filtrelenmiş satır sayısını göster
- İlk 10 satırı scroll et

**Süre:** ~1 dakika

---

### 3. EDA GRAFİKLERİ (2 dakika)

**Söyle:**
> "Şimdi veriyi görselleştirelim."

**Yap:**
1. "EDA Grafikleri" sekmesine geç

**Histogram:**
- "Profit" seçili → Dağılımı göster
- **Söyle:** "Profit dağılımı sağa çarpık, bu yüzden log dönüşümü uyguladım."

**Scatter Plot:**
- X: "Sales", Y: "Profit"
- **Söyle:** "Sales arttıkça Profit artıyor ama ilişki tam doğrusal değil. Bu yüzden RandomForest gibi non-linear modeller daha iyi sonuç verdi."

**Korelasyon Matrisi:**
- Scroll down → Heatmap göster
- **Söyle:** "Sales ile Profit arasında güçlü pozitif korelasyon var (0.48). Discount ile Profit negatif korelasyonlu."

**Süre:** ~2 dakika

---

### 4. MODEL SONUÇLARI (2-3 dakika)

**Söyle:**
> "Şimdi modellere bakalım."

**Yap:**
1. "Model Sonuçları" sekmesine geç

**Full Model:**
- Tabloyu göster
- **Söyle:** 
  > "İki model karşılaştırdım: LinearRegression baseline olarak zayıf kaldı (R² negatif).
  > RandomForest çok daha iyi: R² 0.492, MAE 42.15."

**No-Geo Model:**
- Scroll down → No-Geo tablosunu göster
- **Söyle:**
  > "Ablation testi yaptım: City/State/Postal Code kolonlarını çıkarınca model daha genellenebilir oldu.
  > R² 0.492'den 0.718'e çıktı! Bu geo kolonlarının overfit yarattığını gösteriyor."

**Karşılaştırma:**
- Metrik kartlarını göster (MAE/RMSE/R² farkları)
- Yeşil okları işaret et

**Feature Importance:**
- Scroll down → Bar chart göster
- **Söyle:**
  > "En önemli özellikler Sales, sales_per_item ve discounted_sales.
  > Bu feature'ları ben türettim - domain knowledge kullandım."

**Süre:** ~2-3 dakika

---

### 5. TEKNİK DETAYLAR (1 dakika - İsteğe Bağlı)

**Eğer jüri sorarsa:**

**Leakage önlemi:**
> "profit_margin feature'ını modelden drop ettim çünkü doğrudan Profit'ten türetiliyor."

**Log dönüşümü:**
> "Profit negatif olabildiği için shift + log1p kullandım."

**Reproducibility:**
> "Random seed 42 sabitledim, tüm adımlar tek komutla tekrar edilebilir."

**Süre:** ~1 dakika (isteğe bağlı)

---

### 6. KAPANIŞ (30 saniye)

**Söyle:**
> "Özetle: 9,994 satırlık veriyi temizledim, feature engineering yaptım, 
> iki model karşılaştırdım ve ablation testi ile modeli iyileştirdim.
> Final R² 0.718 ile güçlü bir tahmin modeli elde ettim. Teşekkürler!"

**Yap:**
- Streamlit ekranını göster (overview)
- Sorular varsa bekle

**Süre:** ~30 saniye

---

## 📌 Demo Sırasında DİKKAT!

### YAPILACAKLAR ✅
- Yavaş ve net konuş
- Metrikleri işaret et (mouse ile)
- Grafiklere bakarak açıkla
- Jüriye dön, ekrana değil
- Rahat ve kendine güvenli ol

### YAPILMAYACAKLAR ❌
- Kod gösterme (sormadıkça)
- Teknik jargon fazla kullanma
- Streamlit hatalarıyla uğraşma (önceden test et!)
- Acelenin olmasın
- "Bilmiyorum" deme, "Deneyebilirim" de

---

## 🔧 Olası Sorunlar ve Çözümler

### Streamlit Açılmazsa
```powershell
# Port değiştir
streamlit run src/app_streamlit.py --server.port 8502
```

### Veri Yüklenemezse
```powershell
# Pipeline tekrar çalıştır
python -m src.run_pipeline
```

### Grafik Gösterilemezse
```powershell
# Figürleri yeniden oluştur
python -m src.make_figures
```

---

## ⏱️ Zamanlama Özeti

| Bölüm | Süre |
|-------|------|
| Giriş | 30s |
| Veri Özeti | 1dk |
| EDA Grafikleri | 2dk |
| Model Sonuçları | 2-3dk |
| Teknik Detaylar | 1dk (opsiyonel) |
| Kapanış | 30s |
| **TOPLAM** | **5-7dk** |

---

## 📝 Son Kontrol Listesi

Sunum öncesi:
- [ ] Sanal ortam aktif
- [ ] Pipeline çalıştırıldı
- [ ] Streamlit başlatıldı ve test edildi
- [ ] Tarayıcı tam ekran
- [ ] Tüm sekmeler açık ve hazır
- [ ] Ses seviyesi ayarlandı
- [ ] Su bardağı hazır
- [ ] Derin nefes al, rahat ol! 💪
