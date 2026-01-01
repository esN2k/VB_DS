# 🎯 JÜRİ SUNUMU - KONTROL LİSTESİ (SON HAL)

**Hedef:** Jüri sunumunda hiçbir teknik/içerik sorunu yaşamamak  
**Başlangıç:** Bu listeyi 24 saat öncesine başla  
**Tamamlanması:** Salonun kapısından önce ✅

---

## PHASE 1: 24 SAAT ÖNCESI (Hazırlık)

### 📖 DOKÜMANTASYON OKUMA

- [ ] **[CANVA_SUNUM_REHBERI.md](CANVA_SUNUM_REHBERI.md)** - Slayt içeriği (20 min)
- [ ] **[JURI_SUNUM_AKISI.md](JURI_SUNUM_AKISI.md)** - Konuşma metni (30 min)
- [ ] **[SUNUM_QUICK_REFERENCE.md](SUNUM_QUICK_REFERENCE.md)** - Hızlı referans (10 min)
- [ ] **[DEMO_SCRIPT.md](DEMO_SCRIPT.md)** - Canlı demo (15 min) *isteğe bağlı*

### 💾 DOSYA HAZIRLIĞI

- [ ] Canva sunuş PDF indir → `SUNUM_JURI_FINAL.pdf`
  - İndir: Canva > Download > PDF – Print
  - Klasör: `deliverables/` ye kaydet
  
- [ ] Canva sunuş PowerPoint indir (backup)
  - İndir: Canva > Download > PowerPoint
  - Klasör: `deliverables/` ye kaydet

- [ ] USB belleğe kopyala (çift backup)
  - [ ] PDF
  - [ ] PowerPoint
  - [ ] Proje klasörü (ZIP)

- [ ] GitHub push et (son değişiklikler)
  - Komut: `git add . && git commit -m "Sunum hazırlandı"`
  - Komut: `git push origin main`

### 🧪 SUNUŞ PROVA

- [ ] **Mock sunuş yap** (50 dakika)
  - Slaytları baştan sona göster
  - Konuşma metnini takip et
  - Zamanlamayı ölç (7-9 dakika hedef)
  - Video kaydı: Kendini gözlemle

- [ ] **Canlı demo prova** (20 dakika) *isteğe bağlı*
  - Streamlit aç: `python -m src.run_pipeline` → `streamlit run src/app_streamlit.py`
  - "Veri Özeti" → "EDA Grafikleri" → "Model Sonuçları" flow'u
  - WiFi kopunca ne yapacağın bul

- [ ] **Q&A hazırlığı** (15 dakika)
  - Olası 7 soru ve cevaplarını gözden geçir (SUNUM_QUICK_REFERENCE.md)
  - Kendine soruları sor, cevapla

### ⚙️ TEKNİK KONTROLLER

- [ ] Laptop
  - [ ] Disk alanı yeterli (en az 2GB boş)
  - [ ] RAM yeterli (Firefox + Streamlit'i açıp test et)
  - [ ] Hiç hata/warning var mı terminalinde? (program başlat/durdur)

- [ ] İnternet
  - [ ] WiFi bağlantısı açık
  - [ ] 4G sinyal gücü kontrol (backup)
  - [ ] Canva.com açılıyor mu (cloud backup için)?

- [ ] Ses & Görüntü
  - [ ] Sistem sesi açık mı? (ses seviyesi 50%)
  - [ ] Kulaklıkları test et (varsa)
  - [ ] Ekran parlaklığını test et (projeksiyonda görülür mü?)

### 🛡️ ACİL DURUM PLANI

- [ ] Scenario: "Streamlit çalışmazsa"
  - Çözüm: Ekran görüntüsü hazırla
  - [ ] Dosya: `reports/figures/` tüm PNG'ler downloaded
  - [ ] Alternative: PDF'de tüm grafikler var mı kontrol et

- [ ] Scenario: "İnternet düşerse"
  - Çözüm: Çevrimdışı sunuş yap
  - [ ] Tüm görüntüler local mi? ✅
  - [ ] Metin dosyaları local mi? ✅
  - [ ] PowerPoint (Canva'ya alternatif) hazır mı? ✅

- [ ] Scenario: "Ekran yansıtması sorun yaşarsa"
  - Çözüm: Telnet/kablolu bağlantıya geç
  - [ ] HDMI kablo yanında mı?
  - [ ] VGA adaptörü var mı (eski projeksiyonlar için)?

- [ ] Scenario: "Zaman biterse"
  - Çözüm: Slayt 9-10'u atlayıp sonuca git
  - [ ] Son 2 slayt birleştir: "İleri adımlar + Sonuç"
  - [ ] Q&A'ya daha az zaman ayır

---

## PHASE 2: SABAH (JÜRİ GÜNÜNDEN 1-2 SAATİ ÖNCESI)

### 🖥️ SUNUŞ DOSYALARINI AÇMA

- [ ] **Canva sunuş aç**
  - URL: Canva.com → Dashboard → "VB_DS Profit Tahmini"
  - VEYA: Dosya aç → `SUNUM_JURI_FINAL.pdf`
  - Test: Tüm slaytlar kaymıyor mu? Görüntüler net mi?

- [ ] **Streamlit başlat** (arka planda)
  ```powershell
  cd d:\Projects\VB_DS
  .venv\Scripts\activate
  python -m streamlit run src/app_streamlit.py
  ```
  - Kontrol: "Local URL: http://localhost:8501" görüntü var mı?
  - Test: Tüm 3 sekme açılıyor mu?

### 👕 FİZİKSEL HAZIRLIK

- [ ] Kıyafet
  - [ ] Profesyonel ancak rahat mi?
  - [ ] Renk kameraya iyi mi görünüyor?
  - [ ] Saç/makyaj? (varsa kontrol)

- [ ] Cisimleri kontrol et
  - [ ] Laptop şarj cihazı (100% pil)
  - [ ] USB bellek (proje + sunum)
  - [ ] Kâğıt + kalem (not almak için)
  - [ ] Bu kontrol listesini yazdır ve yanına al

- [ ] Oda hazırlığı (Zoom/Teams sunumu ise)
  - [ ] Arka fon temiz mi?
  - [ ] Işık yeterli mi? (karşı ışık sorunu var mı?)
  - [ ] Kamera açısı uygun mu?
  - [ ] Mikrofon çalışıyor mu?

### 🧠 PSİKOLOJİK HAZIRLIK

- [ ] **Stres kontrolü**
  - [ ] 5 dakikalık meditasyon/yoga yap
  - [ ] Su içi (dehidrasyona karşı)
  - [ ] Hafif esneme (omuzlar/boyun)

- [ ] **Özgüven söylemi**
  - Tekrar et (yüksek sesle): "Bu projeyi benim yaptım. Hazırlanmışım. Başarılı olacağım."
  - Espri yap (gerginliği kırmak için): "Hadi bakalım, bunun için çalıştım!"

- [ ] **Son sözcükler**
  - Ebeveyinini ara (varsa) ve onları bilgilendir
  - Kendini sevgilendir 💙

---

## PHASE 3: 30 DAKİKA ÖNCESI (Son Kontrol)

### 🚪 SALONUN KAPISINDA

- [ ] **Zamanlamayı kontrol et**
  - Saati sete yönetmen/koordinatöre sor
  - "Başlamak için sinyal ne?" → Cevabı bul

- [ ] **Ekipmanı yerleştir**
  - [ ] Laptop projeksiyona/ekrana bağlı mı?
  - [ ] Fare/trackpad çalışıyor mu?
  - [ ] Ses jürü duyabiliyor mu (test et)?

- [ ] **Sunuş dosyasını aktif et**
  - Presentation mode (Canva): "Present" butonuna basılı mı?
  - PDF: Presentation mode aç (Ctrl+Shift+O)
  - PowerPoint: F5 (slideshow mode)

- [ ] **Jüriye gözlemleri filtrele**
  - [ ] Jüri masasında kaç kişi var?
  - [ ] Kimler not yazıyor (ana kişiler)?
  - [ ] İlginç mi görünüyorlar?

### 🧘 ENERJINI POZİTİF TUTTA

- [ ] Derin nefes (4 kez): İç çek (4 sayı) → Tut (4 sayı) → Çık (4 sayı)
- [ ] Omuz döndürme (10 kez): Hem tarafa
- [ ] Gülümseme prova (5 saniye): Kendine öz-güven güncelle

---

## PHASE 4: SUNUŞ ESNASINDA (0-9 dakika)

### 🎤 İLK 30 SANIYE (Kritik)

- [ ] **Başlıktan hemen önce**
  - [ ] Gözlerinizi eğitim odası içinde çevir (jürüyü seç)
  - [ ] Derin bir nefes al
  - [ ] Gülümse ve sakin görün

- [ ] **Slayt 1: BAŞLIK (Önemli)**
  - [ ] Sesini işit: Açık, belirli, yavaş
  - [ ] Gözlerinizi jürüye bağla
  - [ ] İlk cümleni söyle: "Merhaba, ben [İsim]. Bugün size Profit Tahmini projemi sunacağım..."

### ⏱️ ZAMAN TAKİBİ

Her slayt sonunda (zihinsel olarak kontrol et):
- Slayt 1: 15 san ✅
- Slayt 2: 1 min ✅
- Slayt 3: 1 min ✅
- Slayt 4: 1 min ✅
- Slayt 5: 1 min ✅
- Slayt 6: 1 min ✅
- Slayt 7: 1 min ✅ ← **ABLATION TESTİ (kritik)**
- Slayt 8: 1 min ✅
- Slayt 9: 1 min ✅
- Slayt 10: 1 min ✅

Eğer 6 dakikada Slayt 6'ya varıştıysan → Tamam!  
Eğer 7 dakikada Slayt 7'ye varıştıysan → Acele et

### 📊 SLAYT SUNUŞ TİPİ

Slayt 2-10 için:
1. **Başlığı oku** (mavi başlık)
2. **2-3 madde noktasını açıkla** (her biri 10-15 saniye)
3. **Görsel hakkında 1 yorum** ("Burada görebiliyorsunuz ki...")
4. **Sonraki slayta geç** (ok tuşu/boşluk)

### 🗣️ KONUŞMA KALİTESİ

- [ ] **Hız**: Çok hızlı değil, çok yavaş değil (normal tempo)
- [ ] **Ton**: Monoton değil, dalgalı (vurguyu değiştir)
- [ ] **Boşluk**: "uh", "şey" kullanma, 2 saniye sessizlik hoş değil
- [ ] **Yüz İfadesi**: Samimi, ilgilenen, ama gergin değil

### 🔴 SORUNLA KARŞILAŞIRSE

| Sorun | Anında Çözüm |
|-------|--------------|
| Slayt açılmıyor | "Bir saniye, teknik sorunumuz var" + F5 yada yenile |
| Tabanı unutum | Notlarınıza/QUICK_REFERENCE'e bakın + "Devam edelim" |
| Jüri soru sorunca | Soruyu dinle, 2 saniye düşün, cevap ver (QUICK_REFERENCE'te hazır) |
| Zaman daralırsa | Slayt 9'u hızlıkça oku, Slayt 10'a odaklan |
| Mikrofon patlar | Ses tesatçıyı çağır (30 saniye bekle), devam et |

---

## PHASE 5: SUNUM SONUNDA (Slayt 10)

### 🏁 SON SÖZLER

- [ ] **Slayt 10'da dur** (Sonuç, Bulguları göster)
- [ ] **Son sözcüklerini söyle**:
  > "Kârlılık, sadece satış miktarından daha fazlası. Doğru model seçimi ve veri anlayışı ile işletme kararlarını destekleyebiliriz. **Teşekkürler, sorularınızı dinlemek için hazırım.**"

- [ ] **Jürüye bak** (gülümseme, biraz bekleme)

### ❓ Q&A HAZIRLIĞI

- [ ] "Sorularınız var mı?" diye sor
- [ ] Her soru için:
  - 2 saniye düşün
  - 3-4 cümleyle cevap ver
  - Cevaplandıktan sonra jürüye bak ("Başka soru?")

- [ ] Olası sorular ve hazır cevaplar (SUNUM_QUICK_REFERENCE.md'de var)

### 🎉 SUNUŞ SONRASI

- [ ] **Laptopı kapat** (acele etme)
- [ ] **Jürüye teşekkür et** ("Dikkat için teşekkürler")
- [ ] **Odadan çık** (sakin, profesyonel)
- [ ] **Yapıştır telefonuna:** Sunumu başarıyla bitirdim! 🚀
- [ ] **Sosyal medyaya at** (isteğe bağlı): "Jüri sunumum tamamlandı! #VeriYuhndı #MachineLearning"

---

## ✅ KONTROL LİSTESİ TAMAMLAMA IŞARETI

Tüm aşamaları bitirdin mi?

- [ ] Phase 1: 24 saat öncesi (Hazırlık) ✅
- [ ] Phase 2: Sabah (1-2 saat öncesi) ✅
- [ ] Phase 3: 30 dakika öncesi (Son kontrol) ✅
- [ ] Phase 4: Sunuş esnasında (Canlı) ✅
- [ ] Phase 5: Sonrası (Bitiriş) ✅

---

## 🎬 SUNUMU BAŞARILI YAPMANIN GOLDEN RULES

1. **HAZIR OL** ✅ → Bu kontrol listesini takip ettin
2. **SAMİMİ KON** 💬 → Salaş konuş, samimi ol
3. **SLAYTA BAK** 👁️ → Nota bak, ama jürüye de bak
4. **HİZ AYARLA** ⏱️ → Hızlı/yavaş ayarı yap
5. **SORULARI HOŞ LA** 🤔 → Sorular iyi, cevapla
6. **GÜÇ BITIR** 🏁 → Son sözcüklerini güçlü söyle

---

## 📞 KRIZ NUMARALARI

Jüri gününde sorun mu var?

- **Teknik destek:** Jüri odasındaki koordinatöre sor
- **Stres/panik:** Tuvaleti git, yüzünü sıva, derin nefes al (2 min)
- **Bilmediğin soru:** "Harika soru, daha detaylı araştırmam gerek" de
- **Zaman bitiyor:** Hızlı git, ama tamamla (kesme)

---

## 🚀 BAŞLAMA SİYALİ

Salonun kapısından hemen öncesinde:

**Kendine söyle:**
> "Hazırlanmışım. Bu projeyi bilirim. Jüri beni merak ediyor. Başarılı olacağım. 💪"

**Gülümse** 😊

**Kapıyı aç, girecek.**

---

**İYİ ŞANSLAR! 🎉🚀**

*Bu belge jüri sunumunun en kritik olduğu zamanda yazılmıştır. Başarı sana yakın!*
