"""
Görsel Oluşturma Scripti - EDA Grafikleri
Reports/figures/ klasörüne PNG grafikleri kaydeder
"""
from __future__ import annotations

import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Stil ayarları
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


def create_figures(clean_csv_path: Path, output_dir: Path) -> None:
    """EDA görsellerini oluştur ve kaydet."""
    
    if not clean_csv_path.exists():
        logging.error(f"Temizlenmiş veri bulunamadı: {clean_csv_path}")
        logging.error("Lütfen önce pipeline'ı çalıştırın: python -m src.run_pipeline")
        return
    
    logging.info(f"Veri yükleniyor: {clean_csv_path}")
    df = pd.read_csv(clean_csv_path)
    
    # Output dizini oluştur
    output_dir.mkdir(parents=True, exist_ok=True)
    logging.info(f"Çıktı dizini: {output_dir}")
    
    # 1. Profit dağılımı (histogram)
    logging.info("Grafik 1: Profit dağılımı...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["Profit"].dropna(), bins=50, edgecolor='black', alpha=0.7, color='steelblue')
    ax.set_xlabel("Profit ($)", fontsize=12)
    ax.set_ylabel("Frekans", fontsize=12)
    ax.set_title("Profit Dağılımı (Histogram)", fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "01_profit_distribution.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Sales vs Profit (scatter)
    logging.info("Grafik 2: Sales vs Profit...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Sales"], df["Profit"], alpha=0.5, edgecolor='k', linewidth=0.5, s=30)
    ax.set_xlabel("Sales ($)", fontsize=12)
    ax.set_ylabel("Profit ($)", fontsize=12)
    ax.set_title("Sales vs Profit İlişkisi", fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "02_sales_vs_profit.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Category'ye göre ortalama Profit (bar chart)
    if "Category" in df.columns:
        logging.info("Grafik 3: Category'ye göre ortalama Profit...")
        cat_profit = df.groupby("Category")["Profit"].mean().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        cat_profit.plot(kind='bar', ax=ax, color='coral', edgecolor='black')
        ax.set_xlabel("Category", fontsize=12)
        ax.set_ylabel("Ortalama Profit ($)", fontsize=12)
        ax.set_title("Category'ye Göre Ortalama Profit", fontsize=14, fontweight='bold')
        ax.grid(True, axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_dir / "03_category_avg_profit.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    # 4. Discount dağılımı (histogram)
    if "Discount" in df.columns:
        logging.info("Grafik 4: Discount dağılımı...")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df["Discount"].dropna(), bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
        ax.set_xlabel("Discount (%)", fontsize=12)
        ax.set_ylabel("Frekans", fontsize=12)
        ax.set_title("Discount Dağılımı", fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / "04_discount_distribution.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    # 5. Korelasyon matrisi (heatmap)
    logging.info("Grafik 5: Korelasyon matrisi...")
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if len(num_cols) > 2:
        corr = df[num_cols].corr()
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                    center=0, vmin=-1, vmax=1, square=True, 
                    linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
        ax.set_title("Korelasyon Matrisi (Heatmap)", fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig(output_dir / "05_correlation_heatmap.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    # 6. Region'a göre Profit box plot (varsa)
    if "Region" in df.columns:
        logging.info("Grafik 6: Region'a göre Profit box plot...")
        fig, ax = plt.subplots(figsize=(10, 6))
        df.boxplot(column='Profit', by='Region', ax=ax, patch_artist=True)
        ax.set_xlabel("Region", fontsize=12)
        ax.set_ylabel("Profit ($)", fontsize=12)
        ax.set_title("Region'a Göre Profit Dağılımı (Box Plot)", fontsize=14, fontweight='bold')
        plt.suptitle("")  # Varsayılan başlığı kaldır
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_dir / "06_region_profit_boxplot.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    logging.info(f"✓ Tüm grafikler kaydedildi: {output_dir}/")
    logging.info(f"Toplam {len(list(output_dir.glob('*.png')))} grafik oluşturuldu.")


def main():
    """Ana fonksiyon."""
    project_root = Path(__file__).resolve().parents[1]
    clean_csv = project_root / "data" / "processed" / "clean.csv"
    figures_dir = project_root / "reports" / "figures"
    
    logging.info("EDA görselleri oluşturuluyor...")
    create_figures(clean_csv, figures_dir)
    logging.info("İşlem tamamlandı!")


if __name__ == "__main__":
    main()
