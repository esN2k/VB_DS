# 📌 JÜRİ SUNUMU HAZIRLIK - DURUM RAPORU

**Tarih:** 2026-01-01  
**Sunumun Tarihi:** [Buraya Jüri Tarihi Yazılacak]  
**Durum:** ✅ **HAZIR** (Tüm dokümantasyon tamamlandı)

---

## ✅ YAPILMIŞ OLAN İŞLER

### 1. 🎬 SUNUM HAZIRLIK DOKÜMANTASYONU (ÖNCELİKLİ)

| # | Dosya | Durum | Açıklama |
|---|-------|-------|---------|
| 1 | **SUNUM_QUICK_REFERENCE.md** | ✅ | **HEMEN OKU** - 10 dakikalık hızlı referans |
| 2 | **SUNUM_KONTROL_LISTESI.md** | ✅ | Jüri günü öncesi/sonrası tüm kontroller |
| 3 | **CANVA_SUNUM_REHBERI.md** | ✅ | 10 slaytın detaylı içeriği |
| 4 | **CANVA_TODO_LIST.md** | ✅ | Canva'da slaytları oluşturmak için yapılacaklar |
| 5 | **JURI_SUNUM_AKISI.md** | ✅ | 7-9 dakikalık tam konuşma metni |
| 6 | **SUNUM_DOKUMANTASYON_INDEKSI.md** | ✅ | Tüm dokümantasyonun haritası |
| 7 | **DEMO_SCRIPT.md** | ✅ | Streamlit canlı demo senaryosu |
| 8 | **JURI_GUNU_CHECKLIST.md** | ✅ | Jüri günü öncesi/sabahı hazırlığı |

### 2. 🎨 SUNUŞ MATERYALLERI

| Dosya | Durum | Açıklama |
|-------|-------|---------|
| SUNUM_SLIDES.pdf | ✅ Var | PowerPoint sunuş (mevcut) |
| SUNUM_SLIDES.pptx | ✅ Var | PowerPoint editlenebilir versiyon |
| Canva Sunuş | 🔄 YAPILACAK | [Bunu sen oluşturacaksın] |

### 3. 📊 GÖRSELLERİ & VERILER (Canva'da kullan)

| Dosya | Durum | Kullanım |
|-------|-------|---------|
| reports/figures/01_profit_distribution.png | ✅ | Slayt 3 - Profit dağılımı |
| reports/figures/02_sales_vs_profit.png | ✅ | Slayt 6 - Modelleme analizi |
| reports/figures/03_category_avg_profit.png | ✅ | Slayt 8 - Feature importance |
| reports/figures/04_discount_distribution.png | ✅ | Slayt 4 - Temizleme göstergesi |
| reports/figures/05_correlation_heatmap.png | ✅ | Slayt 2 - Problem tanımı |
| reports/figures/06_region_profit_boxplot.png | ✅ | Slayt 7 - Ablation testi |
| reports/metrics_full.csv | ✅ | Metrik tabloları |
| reports/metrics_no_geo.csv | ✅ | Ablation test metrikleri |
| reports/top10_importance.csv | ✅ | Feature importance tablosu |

### 4. 🖥️ UYGULAMALAR (Jüri sunumunda demo için)

| Uygulama | Durum | Komut |
|----------|-------|-------|
| Streamlit İnteraktif Demo | ✅ | `streamlit run src/app_streamlit.py` |
| Pipeline (Veri + Model) | ✅ | `python -m src.run_pipeline` |
| EDA Grafikleri | ✅ | `python -m src.make_figures` |

### 5. 📚 DIĞER DOSYALAR (Referans)

| Dosya | Durum | Amaç |
|-------|-------|------|
| README.md | ✅ Güncellendi | Ana proje dosyası |
| ARCHITECTURE.md | ✅ | Proje mimarisi |
| FINAL_RAPOR.md | ✅ | Jüriye sunacak rapor |
| OZET_SONUC.md | ✅ | 1 sayfalık özet |

---

## 🔄 YAPILACAK OLAN İŞLER

### GÖREV 1: CANVA SUNUŞ OLUŞTUR (Öncelikli)
**Tahmini Zaman:** 3 saat  
**Başlangıç:** Şimdi veya yarın  
**Bitişi:** Sunumdan 1-2 gün öncesi  

#### Adımlar:
1. [ ] **Canva.com'a gir**
   - https://www.canva.com
   - Hesap oluştur veya giriş yap
   - "Create a design" → "Presentation" → "16:9 Widescreen"

2. [ ] **CANVA_TODO_LIST.md takip et**
   - Görev 1: İçerik hazırlığı (30 min)
   - Görev 2: Görselleri topla (45 min)
   - Görev 3: Slaytları oluştur (90 min)
   - Görev 4: Tasarımı uygula (30 min)
   - Görev 5: Export et (15 min)
   - Görev 6: Prova et (30 min)
   - Görev 7: Son kontroller (30 min)

3. [ ] **Slaytlara temel içeriği ekle**
   - CANVA_SUNUM_REHBERI.md'den metinleri kopyala
   - Her slayt için başlık, maddeler, görseller

4. [ ] **Görselleri yerleştir**
   - reports/figures/ klasöründen PNG'leri yükle
   - Tablo ve grafikler ekle (CSV'den)

5. [ ] **Tasarımı uygula**
   - Renk şeması: Navy Blue + Yeşil/Orange
   - Fontlar: Bold başlıklar, Regular body text
   - Layout: Whitespace ve alignment kontrolü

6. [ ] **Export et**
   - PDF indir: `SUNUM_JURI_FINAL.pdf`
   - PowerPoint indir: `SUNUM_JURI_FINAL.pptx`
   - deliverables/ klasörüne kaydet

### GÖREV 2: SUNUŞ METNINI PROVA ET (Zorunlu)
**Tahmini Zaman:** 1 saat  
**Başlangıç:** Slaytlar tamamlandıktan sonra  

#### Adımlar:
1. [ ] **JURI_SUNUM_AKISI.md oku** (20 min)
2. [ ] **Yüksek sesle prova et** (30 min)
   - Tüm 10 slaytı konuş
   - Zamanlamayı ölç (7-9 dakika hedef)
   - Video kaydı (kendini gözlemle)
3. [ ] **Hataları düzelt** (10 min)
   - Hızlı bölümleri yavaşla
   - Unuttuğun kısımları tekrar çalış

### GÖREV 3: JÜRİ GÜNÜ HAZIRLIĞINI YAP
**Tahmini Zaman:** 45 dakika (3 aşama)  
**Başlangıç:** Sunum tarihinden 24 saat öncesi  

#### Aşama 1 - 24 saat öncesi (akşam):
1. [ ] SUNUM_KONTROL_LISTESI.md PHASE 1 tamamla
   - Dokümantasyon okuma
   - Dosya hazırlığı
   - Sunuş prova
   - Teknik kontroller

#### Aşama 2 - Sabah (2 saat öncesi):
2. [ ] SUNUM_KONTROL_LISTESI.md PHASE 2 tamamla
   - Sunuş dosyalarını aç
   - Streamlit başlat
   - Fiziksel hazırlık
   - Psikolojik hazırlık

#### Aşama 3 - Salonun kapısında (30 dakika öncesi):
3. [ ] SUNUM_KONTROL_LISTESI.md PHASE 3 tamamla
   - Zamanlamayı kontrol et
   - Ekipmanı yerleştir
   - Sunuş dosyasını aktif et
   - Psikolojik hazırlanma

---

## 📋 AYLAR BAZINDA TAKVIM

### 📅 **Bu Hafta (T-2 gün)**
- [ ] Tüm dokümantasyonu oku (2 saat)
  - [ ] SUNUM_QUICK_REFERENCE.md (10 min)
  - [ ] SUNUM_KONTROL_LISTESI.md (20 min)
  - [ ] CANVA_SUNUM_REHBERI.md (30 min)
  - [ ] Diğer dosyalar (60 min)
- [ ] Hazırlık stratejisini oluştur (30 min)

### 📅 **Yarın (T-1 gün)**
- [ ] Canva slaytlarını oluştur (3.5 saat)
  - CANVA_TODO_LIST.md'yi adım adım takip et
- [ ] Prova et (1 saat)
  - JURI_SUNUM_AKISI.md konuşma metnini oku
  - Slaytları baştan sona sunuş yap
  - Zamanlamayı ölç

### 📅 **Sunum Günü Sabahı (T-0)**
- [ ] SUNUM_KONTROL_LISTESI.md Phase 2 tamamla (45 min)
  - Laptop hazırlığı
  - Dosyaları aç
  - Fiziksel hazırlık
  - Psikolojik hazırlık
- [ ] SUNUM_QUICK_REFERENCE.md son bakış (10 min)

### 📅 **Jüri Salonuna Girişte (T-30 min)**
- [ ] SUNUM_KONTROL_LISTESI.md Phase 3 tamamla
- [ ] SUNUM_QUICK_REFERENCE.md oku (5 min)
- [ ] Psikolojik hazırlanma (5 min)

---

## 🎯 EN ÖNEMLİ 5 ADIM

Bu 5 adımı mutlaka yap:

1. **SUNUM_QUICK_REFERENCE.md oku** (10 min)  
   → Genel fikir elde et

2. **CANVA_TODO_LIST.md takip edip slaytları oluştur** (3.5 saat)  
   → Profesyonel sunuş yap

3. **JURI_SUNUM_AKISI.md konuşmasını prova et** (30 min)  
   → Güvenli konuş

4. **SUNUM_KONTROL_LISTESI.md'yi takip et** (24 saat öncesi + sabah)  
   → Teknik sorundan kaçın

5. **SUNUM_QUICK_REFERENCE.md son bakış** (Salondan 5 min öncesi)  
   → Son dakika panik engelle

---

## 📞 HERHANGİ BİR SORUN MU?

| Sorunu | Çözüm |
|--------|-------|
| "Ne okuyacağım?" | SUNUM_DOKUMANTASYON_INDEKSI.md → Okuma planı |
| "Canva'da nasıl başlayayım?" | CANVA_TODO_LIST.md → Görev 1-3 |
| "Ne konuşacağım?" | JURI_SUNUM_AKISI.md + SUNUM_QUICK_REFERENCE.md |
| "Zamanla nasıl baş edeceğim?" | SUNUM_QUICK_REFERENCE.md → Saat dağılımı |
| "Jüri günü neler yapayım?" | SUNUM_KONTROL_LISTESI.md → Phase 1-5 |
| "Sunuş dosyalarım hazır mı?" | SUNUM_KONTROL_LISTESI.md Phase 2 → Dosya açma |

---

## 🎉 BAŞARIYA GİDEN YOL

```
Şu An            Hazırlık              Sunuş Günü         BAŞARI
   ↓                  ↓                      ↓                ↓
Dokü-       Canva       Prova      Kontroller      7-9 min    ✅
mentasyon   slaytları   & test     & hazır.      profesyonel TAMAMLANDI
oku         oluştur    (1 saat)   (1 saat)       sunuş
(2 saat)    (3 saat)
   ↓            ↓           ↓           ↓             ↓         ↓
```

---

## 📌 DİKKAT!

**Unutma!** Bu dosyaları yanına al:
- [ ] Bu README.md (internet olmadan okumak için)
- [ ] SUNUM_QUICK_REFERENCE.md yazdırı
- [ ] SUNUM_KONTROL_LISTESI.md yazdırı
- [ ] Laptop + şarj
- [ ] USB bellek (yedek)

---

## ✅ TAMAMLANMA KRİTERLERİ

Sunuma hazır kabul edilmen için:

- [ ] Canva sunuş oluşturulmuş (PDF + PPTX)
- [ ] JURI_SUNUM_AKISI.md konuşması 1x prova edilmiş
- [ ] Zamanlamaya uyulmuş (7-9 dakika)
- [ ] Streamlit uygulaması test edilmiş
- [ ] Tüm kontrol listesi takip edilmiş

**Eğer tüm bu kutular işaretlenmişse → Hazırsın! 🚀**

---

**Belge Sürüm:** 1.0  
**Son Güncelleme:** 2026-01-01  
**Durum:** ✅ JÜRIYE HAZIR

---

> **Son Sözcükler:** Hazırlıklı olduğunda, başarılı olursun. Bu dokümantasyonu takip edersen, jüri sunumun kusursuz olacak. Kendine inan. Başarıyla sunacaksın! 💪🎉

