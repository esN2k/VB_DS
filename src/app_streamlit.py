"""
Streamlit Uygulama - VB_DS Profit Tahmini Projesi
Jüri Sunumu için İnteraktif Demo
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# Proje kök dizinini ayarla
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))


def load_data():
    """Temizlenmiş veriyi yükle."""
    clean_path = project_root / "data" / "processed" / "clean.csv"
    
    if not clean_path.exists():
        st.error(f"❌ Temizlenmiş veri bulunamadı: {clean_path}")
        st.info("💡 Lütfen önce pipeline'ı çalıştırın:")
        st.code("python -m src.run_pipeline", language="bash")
        return None
    
    try:
        df = pd.read_csv(clean_path)
        return df
    except Exception as e:
        st.error(f"❌ Veri yüklenirken hata: {e}")
        return None


def load_metrics():
    """Model metriklerini yükle."""
    metrics_full_path = project_root / "reports" / "metrics_full.csv"
    metrics_no_geo_path = project_root / "reports" / "metrics_no_geo.csv"
    top10_path = project_root / "reports" / "top10_importance.csv"
    
    metrics = {}
    
    if metrics_full_path.exists():
        metrics["full"] = pd.read_csv(metrics_full_path)
    
    if metrics_no_geo_path.exists():
        metrics["no_geo"] = pd.read_csv(metrics_no_geo_path)
    
    if top10_path.exists():
        metrics["importance"] = pd.read_csv(top10_path)
    
    return metrics


def main():
    """Ana uygulama."""
    st.set_page_config(
        page_title="VB_DS Profit Tahmini",
        page_icon="📊",
        layout="wide"
    )
    
    # Başlık
    st.title("📊 VB_DS Profit Tahmini Projesi")
    st.markdown("**Hedef:** SampleSuperstore verisiyle kâr (Profit) tahmini")
    st.markdown("---")
    
    # Veriyi yükle
    df = load_data()
    
    if df is None:
        st.stop()
    
    # Sekme yapısı
    tab1, tab2, tab3 = st.tabs([
        "📋 Veri Özeti",
        "📈 EDA Grafikleri",
        "🎯 Model Sonuçları"
    ])
    
    # TAB 1: Veri Özeti
    with tab1:
        st.header("📋 Veri Özeti")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Toplam Satır", f"{len(df):,}")
        
        with col2:
            st.metric("Toplam Kolon", len(df.columns))
        
        with col3:
            missing = df.isna().sum().sum()
            st.metric("Eksik Değer", missing)
        
        st.subheader("Veri Şeması")
        
        # Kolon bilgileri
        col_info = pd.DataFrame({
            "Kolon": df.columns,
            "Tip": df.dtypes.astype(str),
            "Eksik": df.isna().sum(),
            "Benzersiz": [df[col].nunique() for col in df.columns]
        })
        
        st.dataframe(col_info, width='stretch')
        
        # Filtreler
        st.subheader("Veri Filtreleme")
        
        filter_cols = []
        if "Region" in df.columns:
            filter_cols.append("Region")
        if "Category" in df.columns:
            filter_cols.append("Category")
        if "Segment" in df.columns:
            filter_cols.append("Segment")
        
        if filter_cols:
            selected_filters = {}
            cols = st.columns(len(filter_cols))
            
            for idx, col_name in enumerate(filter_cols):
                with cols[idx]:
                    unique_vals = ["Tümü"] + sorted(df[col_name].dropna().unique().tolist())
                    selected = st.selectbox(f"{col_name}", unique_vals)
                    if selected != "Tümü":
                        selected_filters[col_name] = selected
            
            # Filtrelenmiş veri
            filtered_df = df.copy()
            for col_name, value in selected_filters.items():
                filtered_df = filtered_df[filtered_df[col_name] == value]
            
            st.info(f"Filtrelenmiş Satır Sayısı: {len(filtered_df):,}")
            
            # İlk 10 satırı göster
            st.subheader("Örnek Veri (İlk 10 Satır)")
            st.dataframe(filtered_df.head(10), width='stretch')
        else:
            # İlk 10 satırı göster
            st.subheader("Örnek Veri (İlk 10 Satır)")
            st.dataframe(df.head(10), width='stretch')
    
    # TAB 2: EDA Grafikleri
    with tab2:
        st.header("📈 EDA Grafikleri")
        
        # Sayısal kolonlar
        num_cols = df.select_dtypes(include=["number"]).columns.tolist()
        
        if num_cols:
            st.subheader("Histogram - Dağılım Grafikleri")
            
            # Kolon seçimi
            selected_col = st.selectbox("Kolon Seçin", num_cols)
            
            if selected_col:
                import matplotlib.pyplot as plt
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.hist(df[selected_col].dropna(), bins=50, edgecolor='black', alpha=0.7)
                ax.set_xlabel(selected_col)
                ax.set_ylabel("Frekans")
                ax.set_title(f"{selected_col} Dağılımı")
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                
                # İstatistikler
                st.subheader(f"{selected_col} İstatistikleri")
                stats = df[selected_col].describe()
                st.dataframe(stats.to_frame().T, width='stretch')
        
        # Scatter plot
        if len(num_cols) >= 2:
            st.subheader("Scatter Plot - İlişki Grafiği")
            
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("X Ekseni", num_cols, index=0)
            with col2:
                y_col = st.selectbox("Y Ekseni", num_cols, index=min(1, len(num_cols)-1))
            
            if x_col and y_col:
                import matplotlib.pyplot as plt
                
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(df[x_col], df[y_col], alpha=0.5, edgecolor='k', linewidth=0.5)
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"{x_col} vs {y_col}")
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
        
        # Korelasyon matrisi
        if len(num_cols) > 2:
            st.subheader("Korelasyon Matrisi")
            
            import matplotlib.pyplot as plt
            import numpy as np
            
            corr = df[num_cols].corr()
            
            fig, ax = plt.subplots(figsize=(12, 10))
            im = ax.imshow(corr, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
            
            # Eksen etiketleri
            ax.set_xticks(np.arange(len(corr.columns)))
            ax.set_yticks(np.arange(len(corr.columns)))
            ax.set_xticklabels(corr.columns, rotation=45, ha='right')
            ax.set_yticklabels(corr.columns)
            
            # Değerleri göster
            for i in range(len(corr.columns)):
                for j in range(len(corr.columns)):
                    text = ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                                   ha="center", va="center", color="black", fontsize=8)
            
            plt.colorbar(im, ax=ax)
            ax.set_title("Korelasyon Matrisi (Heatmap)")
            st.pyplot(fig)
    
    # TAB 3: Model Sonuçları
    with tab3:
        st.header("🎯 Model Sonuçları")
        
        metrics = load_metrics()
        
        if not metrics:
            st.warning("⚠️ Model metrikleri bulunamadı. Pipeline'ı çalıştırın.")
            st.code("python -m src.run_pipeline", language="bash")
            st.stop()
        
        # Full Model Metrikleri
        if "full" in metrics:
            st.subheader("📊 Full Model Metrikleri (Tüm Kolonlar)")
            st.dataframe(metrics["full"], width='stretch')
            
            # En iyi modeli vurgula
            best_model_full = metrics["full"].loc[metrics["full"]["r2"].idxmax()]
            st.success(f"✅ En İyi Model (Full): **{best_model_full['model']}** - R² = {best_model_full['r2']:.4f}")
        
        st.markdown("---")
        
        # No-Geo Model Metrikleri
        if "no_geo" in metrics:
            st.subheader("📊 No-Geo Model Metrikleri (City/State/Postal Code Hariç)")
            st.dataframe(metrics["no_geo"], width='stretch')
            
            # En iyi modeli vurgula
            best_model_no_geo = metrics["no_geo"].loc[metrics["no_geo"]["r2"].idxmax()]
            st.success(f"✅ En İyi Model (No-Geo): **{best_model_no_geo['model']}** - R² = {best_model_no_geo['r2']:.4f}")
        
        # Karşılaştırma
        if "full" in metrics and "no_geo" in metrics:
            st.markdown("---")
            st.subheader("📊 Full vs No-Geo Karşılaştırması")
            
            # RandomForest karşılaştırması
            rf_full = metrics["full"][metrics["full"]["model"] == "RandomForestRegressor"]
            rf_no_geo = metrics["no_geo"][metrics["no_geo"]["model"] == "RandomForestRegressor"]
            
            if not rf_full.empty and not rf_no_geo.empty:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    mae_diff = rf_no_geo["mae"].values[0] - rf_full["mae"].values[0]
                    st.metric(
                        "MAE Farkı",
                        f"{mae_diff:.2f}",
                        delta=f"{mae_diff:.2f}",
                        delta_color="inverse"
                    )
                
                with col2:
                    rmse_diff = rf_no_geo["rmse"].values[0] - rf_full["rmse"].values[0]
                    st.metric(
                        "RMSE Farkı",
                        f"{rmse_diff:.2f}",
                        delta=f"{rmse_diff:.2f}",
                        delta_color="inverse"
                    )
                
                with col3:
                    r2_diff = rf_no_geo["r2"].values[0] - rf_full["r2"].values[0]
                    st.metric(
                        "R² Farkı",
                        f"{r2_diff:.4f}",
                        delta=f"{r2_diff:.4f}",
                        delta_color="normal"
                    )
                
                if r2_diff > 0:
                    st.info("✅ Geo kolonlarını çıkarmak modelin genelleme yeteneğini artırdı!")
        
        st.markdown("---")
        
        # Feature Importance
        if "importance" in metrics:
            st.subheader("📊 Top-10 Feature Importance (RandomForest)")
            
            import matplotlib.pyplot as plt
            
            top10 = metrics["importance"].head(10)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(top10["feature"], top10["importance"], color="steelblue", edgecolor="black")
            ax.set_xlabel("Önem Skoru")
            ax.set_ylabel("Özellik")
            ax.set_title("Top-10 En Önemli Özellikler")
            ax.invert_yaxis()
            ax.grid(True, axis='x', alpha=0.3)
            st.pyplot(fig)
            
            # Tablo olarak da göster
            st.dataframe(top10, width='stretch')
    
    # Footer
    st.markdown("---")
    st.markdown("**VB_DS Profit Tahmini Projesi** | Jüri Sunumu 2026")


if __name__ == "__main__":
    main()
