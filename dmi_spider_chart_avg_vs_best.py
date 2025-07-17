"""
Spider Chart Perbandingan Tingkat Kematangan Digital: Rata-rata vs Klinik Terbaik
=================================================================================

Script ini menghasilkan visualisasi spider chart (radar chart) untuk membandingkan 
rata-rata tingkat kematangan digital klinik dengan klinik dengan tingkat kematangan 
digital tertinggi di Kabupaten Ponorogo dari 7 dimensi dengan skala 5.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from style_guide import (
    apply_style,
    save_figure,
    get_color_palette,
    COLORS
)

def get_average_digital_maturity_data() -> Dict[str, float]:
    """
    Data rata-rata tingkat kematangan digital klinik dari 7 dimensi.
    """
    return {
        'Tata Kelola & Kepemimpinan': 4.21,
        'Manusia, Keterampilan & Perilaku': 4.18,
        'Perawatan Berpusat pada Pasien': 4.06,
        'Strategi': 4.03,
        'Analisis Data': 4.01,
        'Kapabilitas TI': 3.88,
        'Interoperabilitas': 3.83
    }

def get_top_clinic_data() -> Dict[str, float]:
    """
    Data tingkat kematangan digital klinik terbaik (Klinik A) dari 7 dimensi.
    """
    return {
        'Tata Kelola & Kepemimpinan': 5.00,
        'Manusia, Keterampilan & Perilaku': 4.92,
        'Perawatan Berpusat pada Pasien': 5.00,
        'Strategi': 5.00,
        'Analisis Data': 5.00,
        'Kapabilitas TI': 5.00,
        'Interoperabilitas': 5.00
    }

def create_comparison_spider_chart(
    avg_data: Dict[str, float], 
    top_data: Dict[str, float], 
    save_path: str = 'digital_maturity_comparison_spider'
) -> None:
    """
    Membuat spider chart perbandingan antara rata-rata dan klinik terbaik.
    
    Args:
        avg_data: Dictionary dengan dimensi dan nilai rata-rata
        top_data: Dictionary dengan dimensi dan nilai klinik terbaik
        save_path: Path untuk menyimpan figure
    """
    # Persiapan data
    categories = list(avg_data.keys())
    avg_values = list(avg_data.values())
    top_values = list(top_data.values())
    
    # Tambahkan nilai pertama di akhir untuk menutup polygon
    avg_values += avg_values[:1]
    top_values += top_values[:1]
    
    # Hitung sudut untuk setiap kategori
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))
    
    # Warna konsisten: rata-rata menggunakan warna primary yang sama seperti chart lain
    avg_color = COLORS['primary']  # Konsisten dengan chart rata-rata lainnya
    top_color = '#3498DB'  # Warna biru profesional untuk klinik terbaik (dari style guide)
    
    # Plot data rata-rata
    ax.plot(angles, avg_values, 'o-', linewidth=3, 
           label='Rata-rata Klinik Ponorogo', 
           color=avg_color, markersize=8, 
           markerfacecolor=avg_color, markeredgecolor='white', markeredgewidth=2)
    ax.fill(angles, avg_values, alpha=0.15, color=avg_color)
    
    # Plot data klinik terbaik
    ax.plot(angles, top_values, 's-', linewidth=3, 
           label='Klinik Terbaik (Klinik A)', 
           color=top_color, markersize=8,
           markerfacecolor=top_color, markeredgecolor='white', markeredgewidth=2)
    ax.fill(angles, top_values, alpha=0.15, color=top_color)
    
    # Kustomisasi grid dan skala
    ax.set_xticks(angles[:-1])
    
    # Buat label yang lebih pendek untuk readability
    short_labels = [
        'Tata Kelola &\nKepemimpinan',
        'Manusia, Keterampilan\n& Perilaku', 
        'Perawatan Berpusat\npada Pasien',
        'Strategi',
        'Analisis Data',
        'Kapabilitas TI',
        'Interoperabilitas'
    ]
    ax.set_xticklabels(short_labels, fontsize=11)
    
    # Set skala radial (0-5)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Tambahkan garis referensi untuk nilai rata-rata keseluruhan
    avg_overall = float(np.mean(avg_values[:-1]))
    top_overall = float(np.mean(top_values[:-1]))
    ax.axhline(y=avg_overall, color=avg_color, linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(y=top_overall, color=top_color, linestyle='--', alpha=0.5, linewidth=1)
    
    # Tambahkan nilai pada setiap titik untuk rata-rata
    for angle, avg_val, top_val in zip(angles[:-1], avg_values[:-1], top_values[:-1]):
        # Nilai rata-rata
        ax.text(angle, avg_val + 0.2, f'{avg_val:.2f}', 
               horizontalalignment='center', 
               verticalalignment='center',
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                        edgecolor=avg_color, alpha=0.9))
        
        # Nilai klinik terbaik
        ax.text(angle, top_val + 0.35, f'{top_val:.2f}', 
               horizontalalignment='center', 
               verticalalignment='center',
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                        edgecolor=top_color, alpha=0.9))
    
    # Kustomisasi tampilan
    ax.set_title('Perbandingan Tingkat Kematangan Digital:\nRata-rata vs Klinik Terbaik di Kabupaten Ponorogo', 
                size=16, fontweight='bold', pad=40)
    
    # Tambahkan legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=12)
    
    # Tambahkan informasi statistik
    plt.figtext(0.02, 0.08, f'Rata-rata Keseluruhan: {avg_overall:.2f}/5.00', 
               fontsize=12, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], 
                        edgecolor=avg_color, alpha=0.9))
    
    plt.figtext(0.02, 0.05, f'Klinik Terbaik: {top_overall:.2f}/5.00', 
               fontsize=12, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], 
                        edgecolor=top_color, alpha=0.9))
    
    # Hitung selisih rata-rata
    gap = top_overall - avg_overall
    plt.figtext(0.02, 0.02, f'Selisih: {gap:.2f} | Skala: 1-5', 
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light_gray'], 
                        edgecolor=COLORS['neutral'], alpha=0.7))
    
    # Simpan figure
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    
    plt.tight_layout()
    plt.show()

def create_detailed_comparison_table(
    avg_data: Dict[str, float], 
    top_data: Dict[str, float]
) -> pd.DataFrame:
    """
    Membuat tabel perbandingan detail antara rata-rata dan klinik terbaik.
    
    Args:
        avg_data: Dictionary dengan dimensi dan nilai rata-rata
        top_data: Dictionary dengan dimensi dan nilai klinik terbaik
        
    Returns:
        DataFrame dengan perbandingan detail
    """
    df = pd.DataFrame({
        'Dimensi': list(avg_data.keys()),
        'Rata-rata': list(avg_data.values()),
        'Klinik Terbaik': list(top_data.values())
    })
    
    df['Selisih'] = df['Klinik Terbaik'] - df['Rata-rata']
    df['Selisih (%)'] = ((df['Klinik Terbaik'] - df['Rata-rata']) / df['Rata-rata'] * 100).round(2)
    
    # Urutkan berdasarkan selisih terbesar
    df = df.sort_values('Selisih', ascending=False).reset_index(drop=True)
    
    return df

def print_summary_statistics(avg_data: Dict[str, float], top_data: Dict[str, float]) -> None:
    """
    Mencetak statistik ringkasan untuk perbandingan data kematangan digital.
    
    Args:
        avg_data: Dictionary dengan dimensi dan nilai rata-rata
        top_data: Dictionary dengan dimensi dan nilai klinik terbaik
    """
    avg_values = list(avg_data.values())
    top_values = list(top_data.values())
    
    avg_overall = np.mean(avg_values)
    top_overall = np.mean(top_values)
    
    print("\n" + "="*80)
    print("PERBANDINGAN TINGKAT KEMATANGAN DIGITAL: RATA-RATA VS KLINIK TERBAIK")
    print("="*80)
    
    # Tabel perbandingan
    df = create_detailed_comparison_table(avg_data, top_data)
    print("\nPERBANDINGAN PER DIMENSI:")
    print("-"*80)
    print(f"{'Dimensi':<30} {'Rata-rata':<10} {'Terbaik':<10} {'Selisih':<10} {'Selisih %':<10}")
    print("-"*80)
    
    for _, row in df.iterrows():
        print(f"{row['Dimensi']:<30} {row['Rata-rata']:<10.2f} {row['Klinik Terbaik']:<10.2f} "
              f"{row['Selisih']:<10.2f} {row['Selisih (%)']:<10.1f}%")
    
    print("-"*80)
    print(f"{'RATA-RATA KESELURUHAN':<30} {avg_overall:<10.2f} {top_overall:<10.2f} "
          f"{top_overall - avg_overall:<10.2f} {((top_overall - avg_overall) / avg_overall * 100):<10.1f}%")
    print("="*80)
    
    print("\nWAWASAN KUNCI:")
    # Dimensi dengan gap terbesar
    max_gap_idx = df['Selisih'].idxmax()
    max_gap_dim = df.loc[max_gap_idx, 'Dimensi']
    max_gap_val = df.loc[max_gap_idx, 'Selisih']
    print(f"• Gap terbesar pada dimensi '{max_gap_dim}': {max_gap_val:.2f} poin")
    
    # Dimensi dengan gap terkecil
    min_gap_idx = df['Selisih'].idxmin()
    min_gap_dim = df.loc[min_gap_idx, 'Dimensi']
    min_gap_val = df.loc[min_gap_idx, 'Selisih']
    print(f"• Gap terkecil pada dimensi '{min_gap_dim}': {min_gap_val:.2f} poin")
    
    # Kinerja klinik terbaik
    perfect_dims = sum(1 for val in top_values if val == 5.0)
    print(f"• Klinik terbaik mencapai skor maksimal (5.0) pada {perfect_dims} dari {len(top_values)} dimensi")
    
    # Potensi peningkatan
    improvement_potential = 5.0 - avg_overall
    print(f"• Potensi peningkatan rata-rata: {improvement_potential:.2f} poin ({improvement_potential/5*100:.1f}%)")

def main() -> None:
    """
    Fungsi utama untuk menjalankan semua visualisasi dan analisis.
    """
    # Terapkan style guide
    apply_style()
    
    # Ambil data
    avg_data = get_average_digital_maturity_data()
    top_data = get_top_clinic_data()
    
    # Cetak statistik ringkasan
    print_summary_statistics(avg_data, top_data)
    
    print("\nMembuat visualisasi perbandingan...")
    print("\n1. Membuat spider chart perbandingan...")
    create_comparison_spider_chart(avg_data, top_data)
    
    print("\n✅ Visualisasi berhasil dibuat!")
    print("\nFile yang dihasilkan di direktori 'output/':")
    print("• digital_maturity_comparison_spider.png/.svg")
    
    # Simpan tabel perbandingan
    df_comparison = create_detailed_comparison_table(avg_data, top_data)
    print(f"\nTabel perbandingan detail:")
    print(df_comparison.to_string(index=False))

if __name__ == "__main__":
    main()
