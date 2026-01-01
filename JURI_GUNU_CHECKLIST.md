# JÜRİ GÜNÜ CHECKLIST - Son Kontrol Listesi

## 📅 Jüri Günü Öncesi (Akşam)

### 🖥️ Teknik Hazırlık
- [ ] Laptop tam şarjlı
- [ ] Şarj aleti yanımda
- [ ] Yedek USB bellek hazır (proje ZIP'i içinde)
- [ ] İnternet bağlantısı test edildi
- [ ] Ses seviyesi ayarlandı
- [ ] Ekran parlaklığı uygun

### 📁 Proje Durumu
- [ ] Sanal ortam kurulu (`.venv`)
- [ ] `requirements.txt` yüklendi
- [ ] Pipeline çalıştırıldı: `python -m src.run_pipeline`
- [ ] Audit raporu güncel: `python -m src.audit_repo`
- [ ] Görseller oluşturuldu: `python -m src.make_figures`
- [ ] Streamlit test edildi: `streamlit run src/app_streamlit.py`
- [ ] Tüm çıktılar mevcut:
  - [ ] `data/processed/clean.csv`
  - [ ] `reports/metrics_full.csv`
  - [ ] `reports/metrics_no_geo.csv`
  - [ ] `reports/top10_importance.csv`
  - [ ] `reports/figures/*.png` (6 grafik)
  - [ ] `DURUM_RAPORU.md`

### 📄 Dökümanlar Hazır
- [ ] `RAPOR.md` yazdırıldı (opsiyonel)
- [ ] `SUNUM_SLIDES.pdf` erişilebilir
- [ ] `DEMO_SCRIPT.md` yazdırıldı (yanımda)
- [ ] `JURI_SUNUM_AKISI.md` okundu (ezberledim)
- [ ] Teslim paketi ZIP oluşturuldu: `.\tools\package.ps1`

### 🎯 Sunum Hazırlığı
- [ ] Slaytlar hazır (`SUNUM_SLIDES.pptx`)
- [ ] Streamlit açık ve hazır (arka planda)
- [ ] Demo senaryosu gözden geçirildi
- [ ] Zamanlama prova edildi (7-9 dk)
- [ ] Olası sorulara cevaplar hazır

---

## 📅 Jüri Günü Sabahı (Son 30 Dakika)

### ⚡ Hızlı Kontrol
- [ ] Derin nefes aldım, rahatım
- [ ] Su bardağı hazır
- [ ] Laptop açıldı ve hazır
- [ ] Sanal ortam aktif: `.venv\Scripts\activate`
- [ ] Streamlit çalışıyor: `http://localhost:8501`
- [ ] Slaytlar açık ve ilk sayfada
- [ ] Tarayıcı tam ekran modu
- [ ] Bildirimler kapatıldı (sessiz mod)
- [ ] Telefon sessizde

### 🎬 Demo Hazırlık (5 Dakika Öncesi)
- [ ] Streamlit sekmeleri test edildi:
  - [ ] Veri Özeti açılıyor
  - [ ] EDA Grafikleri yükleniyor
  - [ ] Model Sonuçları gösteriliyor
- [ ] Filtreler çalışıyor (Category dropdown)
- [ ] Grafikler render oluyor
- [ ] Hiçbir hata mesajı yok

---

## 🎯 Sunum Sırasında

### İlk 2 Dakika
- [ ] Kendimi tanıttım (ad, proje adı)
- [ ] Problem tanımını net açıkladım
- [ ] Veri setini tanıttım (9,994 satır, 17 kolon)

### Demo (2-3 Dakika)
- [ ] Streamlit uygulamasını gösterdim
- [ ] Veri Özeti sekmesini gösterdim
- [ ] EDA grafiklerini gösterdim
- [ ] Model sonuçlarını gösterdim
- [ ] Full vs No-Geo karşılaştırmasını vurguladım

### Teknik Detaylar
- [ ] Ablation testini açıkladım (R² 0.492 → 0.718)
- [ ] Leakage önlemini söyledim (profit_margin drop)
- [ ] Log dönüşümünü açıkladım (shift + log1p)
- [ ] Feature engineering örneklerini verdim

### Kapanış
- [ ] Özet yaptım (30 saniye)
- [ ] Teşekkür ettim
- [ ] Sorulara hazırım dedim

---

## ❓ Olası Sorular - Hazır Cevaplar

### "Overfit riski var mı?"
**Cevap:** "RandomForest 200 ağaç kullanıyor ama min_samples_leaf=2 ve max_features='sqrt' ile sınırlandırdım. Test/train split %20 yaptım. No-Geo senaryoda R² artışı overfit azaldığını gösteriyor."

### "Cross-validation yok mu?"
**Cevap:** "Zaman kısıtı nedeniyle basit train-test split kullandım ama random seed sabitledim. Cross-validation eklemek sonuçları daha robust yapardı, gelecek iyileştirme olarak planlanabilir."

### "Neden geo kolonları performansı düşürüyor?"
**Cevap:** "Yüksek kardinalite - çok fazla benzersiz şehir var. Bu model karmaşıklığını artırıyor ve genellemeyi zorlaştırıyor. No-Geo'da R² 0.718'e çıktı."

### "Hiperparametre optimizasyonu?"
**Cevap:** "Manuel ayar yaptım: n_estimators=200, min_samples_leaf=2. Grid search yapılabilir ama zaman kısıtı nedeniyle manuel yaptım."

### "Deployment planı var mı?"
**Cevap:** "Streamlit uygulaması temel bir deployment. İleri adım olarak Flask API veya Docker containerization yapılabilir."

---

## 🔧 Acil Durum Planı

### Streamlit Açılmazsa
```powershell
# Port değiştir
streamlit run src/app_streamlit.py --server.port 8502

# Veya yeniden başlat
Ctrl+C
streamlit run src/app_streamlit.py
```

### Veri Yüklenemezse
```powershell
# Pipeline tekrar çalıştır
python -m src.run_pipeline
```

### Grafik Hatası
```powershell
# Figürleri yeniden oluştur
python -m src.make_figures
```

### Tamamen Çökerse
- Panik yapma!
- "Teknik bir sorun yaşıyoruz, slaytlarla devam edeyim" de
- Slaytları göster
- Kod ve sonuçlardan bahset
- Özür dile, profesyonel kal

---

## 💡 Sunum İpuçları

### Beden Dili
- ✅ Jüriye bak, ekrana değil
- ✅ Ellerini doğal kullan
- ✅ Dik dur, güven içinde
- ✅ Gülümse

### Konuşma
- ✅ Yavaş ve net konuş
- ✅ "Ben", "benim" kullan (sahiplenme)
- ✅ Teknik terimleri açıkla
- ✅ Sayıları vurgula (9,994 satır, R² 0.718)

### Zaman Yönetimi
- ✅ 7-9 dakika sınırında kal
- ✅ Her bölüme eşit zaman ayır
- ✅ Acele etme
- ✅ Sorular için 2-3 dakika ayır

---

## 🎓 Psikolojik Hazırlık

### Gece Öncesi
- [ ] Erken yat (en az 7 saat uyku)
- [ ] Projeni bir kez daha gözden geçir
- [ ] Kendine güven: "Ben bu projeyi yaptım, en iyi ben biliyorum"
- [ ] Pozitif düşün

### Sabah
- [ ] Kahvaltı yap
- [ ] Rahat kıyafet giy
- [ ] Erken git (10-15 dakika önce)
- [ ] Derin nefes al

### Sıranı Beklerken
- [ ] Su iç
- [ ] Derin nefes egzersizi (4-7-8 tekniği)
- [ ] Önemli notları gözden geçir
- [ ] Pozitif self-talk: "Hazırım, yapabilirim!"

---

## ✅ Son Kontrol (5 Dakika Önce)

1. [ ] Laptop şarjda veya tam şarjlı
2. [ ] Streamlit çalışıyor
3. [ ] Slaytlar açık
4. [ ] Su bardağı yanımda
5. [ ] Telefon sessiz
6. [ ] Bildirimler kapalı
7. [ ] DEMO_SCRIPT.md yanımda
8. [ ] Derin nefes aldım
9. [ ] Gülümsedim
10. [ ] Hazırım! 💪

---

## 🎬 Final Mesaj

**Unutma:**
- Sen bu projeyi yaptın
- Tüm detayları biliyorsun
- Jüri seninle tanışmak istiyor
- Hata yapsan bile sorun değil
- Kendine güven
- Rahat ol
- En iyisini yapacaksın!

**Başarılar!** 🎓🚀

---

**Hazırlayan:** VB_DS Proje Ekibi  
**Tarih:** 2026-01-01  
**Durum:** Jüriye Hazır ✅
