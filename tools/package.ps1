# VB_DS Teslim Paketi Oluşturma Scripti
# PowerShell 5.0+ gerektirir

param(
    [string]$OutputName = "teslim_paketi"
)

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "VB_DS TESLİM PAKETİ OLUŞTURMA" -ForegroundColor Cyan
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

# Timestamp
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$zipName = "${OutputName}_${timestamp}.zip"

Write-Host "[1/5] Timestamp oluşturuldu: $timestamp" -ForegroundColor Green

# Geçici dizin oluştur
$tempDir = "temp_package"
if (Test-Path $tempDir) {
    Remove-Item $tempDir -Recurse -Force
}
New-Item -ItemType Directory -Path $tempDir | Out-Null
Write-Host "[2/5] Geçici dizin oluşturuldu: $tempDir" -ForegroundColor Green

# Dosyaları kopyala
Write-Host "[3/5] Dosyalar kopyalanıyor..." -ForegroundColor Yellow

# Klasörler
$folders = @(
    "src",
    "notebooks",
    "reports",
    "data/raw"
)

foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Write-Host "  - $folder" -ForegroundColor Gray
        Copy-Item -Path $folder -Destination "$tempDir/$folder" -Recurse
    }
}

# Tek dosyalar
$files = @(
    "README.md",
    "RAPOR.md",
    "OZET_SONUC.md",
    "SUNUM.md",
    "SUNUM_SLIDES.pptx",
    "SUNUM_SLIDES.pdf",
    "ADIM_ADIM.md",
    "INSTRUCTIONS.md",
    "DURUM_RAPORU.md",
    "DEMO_SCRIPT.md",
    "JURI_SUNUM_AKISI.md",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "requirements.txt",
    ".gitignore"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "  - $file" -ForegroundColor Gray
        Copy-Item -Path $file -Destination "$tempDir/$file"
    }
}

Write-Host "[3/5] Dosyalar kopyalandı ✓" -ForegroundColor Green

# data/processed varsa kopyala (opsiyonel)
if (Test-Path "data/processed/clean.csv") {
    Write-Host "  - data/processed/clean.csv (opsiyonel)" -ForegroundColor Gray
    if (-not (Test-Path "$tempDir/data/processed")) {
        New-Item -ItemType Directory -Path "$tempDir/data/processed" | Out-Null
    }
    Copy-Item -Path "data/processed/clean.csv" -Destination "$tempDir/data/processed/clean.csv"
}

# ZIP oluştur
Write-Host "[4/5] ZIP arşivi oluşturuluyor..." -ForegroundColor Yellow

# Eski ZIP'i sil (varsa)
if (Test-Path $zipName) {
    Remove-Item $zipName -Force
}

# PowerShell 5.0+ Compress-Archive kullan
Compress-Archive -Path "$tempDir/*" -DestinationPath $zipName -CompressionLevel Optimal

Write-Host "[4/5] ZIP oluşturuldu: $zipName ✓" -ForegroundColor Green

# Geçici dizini temizle
Write-Host "[5/5] Temizlik yapılıyor..." -ForegroundColor Yellow
Remove-Item $tempDir -Recurse -Force
Write-Host "[5/5] Temizlik tamamlandı ✓" -ForegroundColor Green

# Sonuç
Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "✅ TESLİM PAKETİ BAŞARIYLA OLUŞTURULDU!" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host ""

# Dosya bilgileri
$zipInfo = Get-Item $zipName
$sizeMB = [math]::Round($zipInfo.Length / 1MB, 2)

Write-Host "📦 Dosya Adı  : $zipName" -ForegroundColor White
Write-Host "📏 Boyut      : $sizeMB MB" -ForegroundColor White
Write-Host "📁 Konum      : $($zipInfo.FullName)" -ForegroundColor White
Write-Host ""

# İçerik özeti
Write-Host "📋 İçerik Özeti:" -ForegroundColor White
Write-Host "  - Kod (src/, notebooks/)" -ForegroundColor Gray
Write-Host "  - Raporlar (reports/, *.md)" -ForegroundColor Gray
Write-Host "  - Sunumlar (*.pptx, *.pdf)" -ForegroundColor Gray
Write-Host "  - Ham veri (data/raw/)" -ForegroundColor Gray
Write-Host "  - Dokümantasyon (README, RAPOR, vb.)" -ForegroundColor Gray
Write-Host ""

Write-Host "✅ Teslim paketi hazır! Jüriye gönderebilirsiniz." -ForegroundColor Green
Write-Host ""
