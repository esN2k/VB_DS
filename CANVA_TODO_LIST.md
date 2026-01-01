# 📝 CANVA SUNUMU HAZIRLAMA - TODO LIST

**Başlangıç Tarihi:** 2026-01-01  
**Deadline:** Jüri günü sabahı  
**Tahmini Süre:** 2-3 saat

---

## GÖREV 1: İÇERİK VE METINLER
### Amacı: Sunumun yazılı temelini hazırla

- [ ] **JURI_SUNUM_AKISI.md dosyasını oku** (20 min)
  - 7-9 dakikalık konuşma metnini gözden geçir
  - Olası sorular ve cevapları not et
  - Kendi kelimelerin ile uyarlamalar yap

- [ ] **Sunumdaki main mesajları seç** (15 min)
  - Hangi 3 ana noktayı vurgulayacaksın?
  - Her slayt için 1 cümlelik özet yaz
  - **Hazırla:** Bir Word/Notepad dosyası → Bu teknik uyarlar

- [ ] **Konuşma zamanlamasını prova et** (30 min)
  - Akıllı telefonla kendini sesi kaydedip dinle
  - Her slayt için ortalama 1 dakika hedefle
  - Yavaş/hızlı yerleri belirle

---

## GÖREV 2: GÖRSELLERİ TOPLA

### Amacı: Canva'ya yerleştirmek için görselleri hazırla

- [ ] **Hazır görselleri tanımla** (15 min)
  - ✅ Grafikler: `reports/figures/` klasöründe 6 PNG var
    - 01_profit_distribution.png
    - 02_sales_vs_profit.png
    - 03_category_avg_profit.png
    - 04_discount_distribution.png
    - 05_correlation_heatmap.png
    - 06_region_profit_boxplot.png
  - ✅ Metrik tabloları: `reports/*.csv` dosyaları
  - ✅ Veri özeti: `reports/data_summary.txt`

- [ ] **Ek görseller indir** (20 min)
  - [ ] Perakende/satış ilişkili uygun fotoğraf (Unsplash, Pexels)
  - [ ] İşletme/kâr şekilleri (simge, icon)
  - [ ] Veri bilimi teması (grafik, bilim imajı)
  - [ ] Proje logosu (varsa)

- [ ] **Ekstra grafikler oluştur (İsteğe bağlı)** (30 min)
  - Metrik bar chart'ı (Full vs RF)
  - Ablation testi comparison
  - Pipeline diyagramı
  - **Komut:** `python -m src.make_figures` (zaten yapılmış)

- [ ] **Görselleri Canva-uyumlu hale getir** (15 min)
  - [ ] Tüm PNG/JPG dosyalarının boyutunu kontrol et (max 5MB)
  - [ ] Renkler kontrastlı mı? (beyaz arka plan üzerinde okunabilir)
  - [ ] Dosya boyutları optimize mi? (küçük boyut = hızlı yükleme)

---

## GÖREV 3: CANVA'DA SLAYTLARI OLUŞTUR

### Amacı: Profesyonel tasarımla 10 slayt hazırla

- [ ] **Canva'da yeni presentation aç** (5 min)
  - canva.com → "Create a design"
  - "Presentation" → "16:9 Widescreen"
  - Adı: "VB_DS Profit Tahmini - Jüri Sunumu"

- [ ] **Slayt 1: BAŞLIK** (20 min)
  - Başlık: "Profit Tahmini Projesi"
  - Alt başlık: "SampleSuperstore Veri Setiyle"
  - İsim ve tarih ekle
  - Fotoğraf/görsel: Perakende/satış teması
  - Tema renkleri uygula

- [ ] **Slayt 2: PROBLEM TANIMI** (15 min)
  - 4 madde noktası ekle
  - "CANVA_SUNUM_REHBERI.md"'den metni copy-paste et
  - İkon/emoji ekle
  - Arkaplan rengi: açık (contrast)

- [ ] **Slayt 3: VERİ SETİ** (15 min)
  - Tablo: Temel stats
  - "Satır: 9,994 | Kolon: 13 | Yıl: 2011-2015"
  - Veri etsinden örnek görsel
  - Profit dağılım grafiği ekle (01_profit_distribution.png)

- [ ] **Slayt 4: TEMIZLEME & FEATURE ENG.** (15 min)
  - Sol taraf: Temizleme adımları (5 madde)
  - Sağ taraf: Feature Engineering (4 madde)
  - Ikon/renkler: Farklı işlemleri ayırt et
  - Formülleri metin olarak ekle

- [ ] **Slayt 5: MODELLEME** (20 min)
  - Pipeline diyagramı (ASCII'den Canva şekline dönüştür)
  - Modeller: LinearRegression vs RandomForest
  - Özel işlemler kutusu (log1p, scaling, encoding)
  - Renkler: Modelleri farklı renkle göster

- [ ] **Slayt 6: SONUÇLAR - METRIKLER** (20 min)
  - Tablo: MAE, RMSE, R² değerleri
  - ❌ Linear, ✅ Random Forest vurgulama
  - Bar chart veya tablo görseli
  - Açıklaması: "RF çok daha iyi"

- [ ] **Slayt 7: ABLATION TESTİ** (25 min)
  - Yan yana iki kutu: Full vs No-Geo
  - MAE, RMSE, R² değerleri göster
  - ⬆️/⬇️ oklar ile değişimleri göster
  - Bulut: "City/State overfit yaratıyor"
  - Vurgu: "R² 0.49 → 0.72 (%46 artış!)"

- [ ] **Slayt 8: FEATURE IMPORTANCE** (15 min)
  - Bar chart: top10_importance.csv'den
  - 10 özelliği renkli barlarla göster
  - Üst 3'ü öne çıkar (daha koyu renk)
  - %ler metin olarak göster

- [ ] **Slayt 9: SINIRLAMALAR & İLERİ ADIMLAR** (15 min)
  - Sol taraf: 4 sınırlama (⚠️ ikonları)
  - Sağ taraf: 5 ileri adım (🔬 ikonları)
  - Renkler: Sınırlama=kırmızı, İleri=yeşil

- [ ] **Slayt 10: SONUÇ & Q&A** (20 min)
  - 5 ana bulgu (✅ ikonları)
  - Son söz: Kuvvetli bir cümle
  - Q&A hazırlaması: 4 soru ve cevap
  - "Teşekkürler!" kapama

---

## GÖREV 4: TASARIM VE POLİSH

### Amacı: Slaytları profesyonel ve okunabilir yap

- [ ] **Renk şemasını uygula** (10 min)
  - Ana renk: Navy Blue veya Deep Purple
  - Vurgu: Yeşil veya Orange
  - Tüm slaytlarda tutarlı kul
  - Kontrastı kontrol et (beyaz text + koyu bg)

- [ ] **Font'ları standardize et** (10 min)
  - Başlıklar: Bold Sans-serif (Poppins, Montserrat)
  - Body: Regular Sans-serif (Open Sans, Lato)
  - Minimum boyut: 18pt (başlık), 14pt (body)
  - Kod/teknike: Monospace yazı

- [ ] **Düzen ve boşluk kontrol et** (15 min)
  - Hiçbir slayt kalabalık mı? (whitespace yeterli mi)
  - Tüm öğeler hizalı mı? (left/center/right)
  - Görseller uygun boyutta mı?
  - Metin kenar boşluğundan yeterli uzakta mı?

- [ ] **Görsel uyumluluğu kontrol et** (10 min)
  - Grafikler Canva temasına mı uyuyor?
  - Tüm PNG'ler aynı kalitede mi?
  - Fotoğraflar profesyonel mi?
  - İkonlar tutarlı stillendirme mi?

- [ ] **Yazım ve dilbilgisi** (10 min)
  - Türkçe yazım hatalarını kontrol et
  - Başlıklar büyük harfle mi başlıyor?
  - Noktalama işaretleri var mı?
  - Tutarlı dil (formak vs. günlük) seçilmiş mi?

---

## GÖREV 5: EXPORT VE YEDEK

### Amacı: Sunumu jüri gününde açmak için hazırla

- [ ] **Canva'da PDF'e çevir** (5 min)
  - "Download" → "PDF – Print" seç
  - Dosya adı: `SUNUM_JURI_FINAL.pdf`
  - `deliverables/` klasörüne kaydet

- [ ] **Canva'da PowerPoint'e çevir** (5 min)
  - "Download" → "PowerPoint" seç (Canva Pro gerekli)
  - Dosya adı: `SUNUM_JURI_FINAL.pptx`
  - `deliverables/` klasörüne kaydet

- [ ] **Sunumu Canva'da linkle** (5 min)
  - Canva'daki slaytı paylaş → Share link
  - Link: `https://www.canva.com/...`
  - Bunu README.md'ye ekle (backup olarak)

- [ ] **Yedek kopyalarını oluştur** (10 min)
  - PDF'i USB belleğe koy
  - PowerPoint'i emailed to self (backup)
  - İki farklı bilgisayardan erişebil mi test et

- [ ] **Mobil uyumlu su test** (5 min)
  - PDF tablet/telefondan açılıyor mu?
  - Metinler okunabilir mi mobile'da?
  - Görseller düzgün görünüyor mu?

---

## GÖREV 6: SUNUYU PROVA ET

### Amacı: Jüri günü öncesi genel deneme yap

- [ ] **Tam sunum geçişini yap** (45 min)
  - Tüm 10 slaytı baştan sona konuş
  - Önceden hazırlanmış konuşma metnini takip et
  - Zamanlamayı ölç (7-9 dakika hedef)
  - Sessiz video çek (kendini gözlemle)

- [ ] **Presentation mode test et** (10 min)
  - Canva canlı sunuş modu ("Present" butonu)
  - Klavye navigasyonu (ok tuşları, boşluk)
  - Pointer/spotlight araçları test et

- [ ] **Soruları yanıtla prova** (15 min)
  - Olası 5 soruyu sor kendi kendine
  - Cevapları hazırla (3-4 cümle/soru)
  - "Bilmiyorum ama inceleyebilirim" deyin hazırla

- [ ] **Canlı demo prova** (20 min, İsteğe bağlı)
  - Streamlit uygulamasını aç
  - "Veri Özeti" tabına tıkla (1 dakika)
  - "EDA Grafikleri" tabına geç (2 dakika)
  - "Model Sonuçları" tabında dur (3 dakika)
  - Network problemi varsa qr kod veya video adım

- [ ] **A/V ekipmanını test et** (10 min)
  - Sesi test et: sistem sesi yeterli mi?
  - Ekran yansıtmasını test et (HDMI/wireless)
  - Mouse/gösterici çalışıyor mu?
  - Işık/aydınlatma yeterli mi?

---

## GÖREV 7: GÜN ÖNCESI KONTROLLER

### Amacı: Jüri günü sabahı hiçbir sürpriz olmasın

- [ ] **Dokümanlara son bakış** (15 min)
  - `JURI_GUNU_CHECKLIST.md` kontrol et
  - "Jüri Günü Öncesi" bölümünü tamamla
  - "Sabahı" adımlarını kontrol et

- [ ] **Teknik kontrolleri tamamla** (20 min)
  - [ ] Laptop tamamen şarjlı (100%)
  - [ ] Şarj cihazı yanımda
  - [ ] Canva sunuş linkinin veya PDF'in açılıp açılmadığı test et
  - [ ] İnternet bağlantısı açık (WiFi + 4G backup)
  - [ ] Ekran yansıtması test edildi (varsa)

- [ ] **Akıl sağlığı hazırlaması** (10 min)
  - Kendini hazır hisset mi?
  - Stres seviyesi kontrol et
  - Gerekirse sakin olmak için meditasyon/yoga yap
  - Uyku düzeniniz iyi mi? (son gece erken yat)

- [ ] **Final kontroller** (5 min)
  - Oda temiz mi? (arka plan neyin görüneceği)
  - Giysi uygun mu? (profesyonel ancak rahat)
  - Kulaklık/mikrofon gerekli mi test et
  - Saat kontrol et (15 dakika erken git)

---

## 🎯 BAŞARILI SUNUMDAKI İPUÇLARI

### Jüri Sunumu Sırasında:
1. **İlk 30 saniye kritik** → Göz teması, gülümseme, güven
2. **Slayt saat gibi** → Her slayt ~1 dakika (±15 saniye)
3. **Slaytı oku değil, AÇIKLA** → Slayt destek, sen ana
4. **Konu dışı gelmezsen** → Soruların hoşlan
5. **Vizyon göster** → Sadece bugün değil, gelecek de

### Taktikler:
- 🎤 Konuş, sayılmaz. Dinleyin.
- 👁️ Göz teması jürü ile
- 🎯 Hedef her slayt ile göster
- 📊 Veri ile konuş (duygusal değil)
- 🏁 Güçlü sonuç ile bitir

---

## ✅ TAMAMLANDIKTAN SONRA

Tüm görevleri bitirdikten sonra:
1. Dosyaları **deliverables/** klasörüne koy
2. `DURUM_RAPORU.md` güncelle
3. GitHub'a push et (commit: "Sunum hazırlandı")
4. Kendine pat at 🎉

---

## 📅 TAKVIM ÖNERISI

| Gün | Görev | Süre |
|-----|-------|------|
| T-2 gün | Görev 1-2 (İçerik + Görseller) | 2.5 saat |
| T-1 gün | Görev 3-4 (Slayt oluştur + Tasarım) | 3 saat |
| Gün öncesi (Akşam) | Görev 5-6 (Export + Prova) | 1.5 saat |
| Sabah | Görev 7 (Final kontroller) | 30 min |

**TOPLAM: ~7.5 saatlik çalışma**

İyi şanslar! 🚀
