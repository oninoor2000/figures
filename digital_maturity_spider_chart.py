"""
Spider Chart Rata-rata Tingkat Kematangan Digital Klinik di Kabupaten Ponorogo
=============================================================================

Script ini menghasilkan visualisasi spider chart (radar chart) untuk rata-rata tingkat 
kematangan digital klinik dari 7 dimensi dengan skala 5.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Dict, List
from style_guide import (
    apply_style,
    save_figure,
    get_color_palette,
    COLORS
)

def get_digital_maturity_data() -> Dict[str, float]:
    """
    Data rata-rata tingkat kematangan digital klinik dari 7 dimensi.
    """
    return {
        'Tata Kelola & Kepemimpinan': 4.22,
        'Manusia, Keterampilan & Perilaku': 4.17,
        'Perawatan Berpusat pada Pasien': 4.04,
        'Strategi': 4.03,
        'Analisis Data': 4.04,
        'Kapabilitas TI': 3.89,
        'Interoperabilitas': 3.81
    }

def create_spider_chart(data: Dict[str, float], save_path: str = 'digital_maturity_spider') -> None:
    """
    Membuat spider chart untuk tingkat kematangan digital.
    
    Args:
        data: Dictionary dengan dimensi dan nilai rata-rata
        save_path: Path untuk menyimpan figure
    """
    # Persiapan data
    categories = list(data.keys())
    values = list(data.values())
    
    # Tambahkan nilai pertama di akhir untuk menutup polygon
    values += values[:1]
    
    # Hitung sudut untuk setiap kategori
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Warna tetap untuk rata-rata (konsisten untuk kombinasi dengan data lain)
    avg_color = COLORS['primary']  # Menggunakan warna primary yang konsisten
    
    # Plot data
    ax.plot(angles, values, 'o-', linewidth=2.5, label='Rata-rata Klinik', color=avg_color, markersize=8)
    ax.fill(angles, values, alpha=0.25, color=avg_color)
    
    # Kustomisasi grid dan skala
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    
    # Set skala radial (0-5)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Tambahkan nilai pada setiap titik
    for angle, value, category in zip(angles[:-1], values[:-1], categories):
        ax.text(angle, value + 0.15, f'{value:.2f}', 
               horizontalalignment='center', 
               verticalalignment='center',
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=avg_color, alpha=0.8))
    
    # Kustomisasi tampilan
    ax.set_title('Rata-rata Tingkat Kematangan Digital Klinik\ndi Kabupaten Ponorogo', 
                size=16, fontweight='bold', pad=30)
    
    # Tambahkan legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=12)
    
    # Tambahkan informasi tambahan
    avg_overall = np.mean(values[:-1])
    plt.figtext(0.02, 0.02, f'Rata-rata Keseluruhan: {avg_overall:.2f}/5.00', 
               fontsize=12, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], 
                        edgecolor=COLORS['neutral'], alpha=0.9))
    
    # Tambahkan skala referensi
    plt.figtext(0.98, 0.02, 'Skala: 1 (Rendah) - 5 (Tinggi)', 
               fontsize=10, ha='right',
               bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light_gray'], 
                        edgecolor=COLORS['neutral'], alpha=0.7))
    
    # Simpan figure
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    
    plt.tight_layout()
    plt.show()

def create_comparison_ready_spider_chart(data: Dict[str, float], save_path: str = 'digital_maturity_spider_comparison_ready') -> None:
    """
    Membuat spider chart yang siap untuk perbandingan dengan data lain.
    Menggunakan warna yang konsisten untuk rata-rata.
    
    Args:
        data: Dictionary dengan dimensi dan nilai rata-rata
        save_path: Path untuk menyimpan figure
    """
    # Persiapan data
    categories = list(data.keys())
    values = list(data.values())
    
    # Tambahkan nilai pertama di akhir untuk menutup polygon
    values += values[:1]
    
    # Hitung sudut untuk setiap kategori
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(projection='polar'))
    
    # Warna konsisten untuk rata-rata (untuk perbandingan)
    avg_color = '#2E86AB'  # Biru yang konsisten
    
    # Plot data dengan style yang lebih tebal untuk perbandingan
    ax.plot(angles, values, 'o-', linewidth=3, label='Rata-rata Klinik Ponorogo', 
           color=avg_color, markersize=10, markerfacecolor=avg_color, markeredgecolor='white', markeredgewidth=2)
    ax.fill(angles, values, alpha=0.2, color=avg_color)
    
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
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Tambahkan garis referensi untuk nilai rata-rata keseluruhan
    avg_overall = np.mean(values[:-1])
    ax.axhline(y=avg_overall, color=avg_color, linestyle='--', alpha=0.5, linewidth=1)
    
    # Tambahkan nilai pada setiap titik
    for angle, value in zip(angles[:-1], values[:-1]):
        ax.text(angle, value + 0.2, f'{value:.2f}', 
               horizontalalignment='center', 
               verticalalignment='center',
               fontsize=11, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor=avg_color, alpha=0.9))
    
    # Kustomisasi tampilan
    ax.set_title('Tingkat Kematangan Digital Klinik di Kabupaten Ponorogo\n(Siap untuk Perbandingan)', 
                size=16, fontweight='bold', pad=40)
    
    # Tambahkan legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=12)
    
    # Tambahkan informasi tambahan
    plt.figtext(0.02, 0.05, f'Rata-rata Keseluruhan: {avg_overall:.2f}/5.00', 
               fontsize=13, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], 
                        edgecolor=COLORS['neutral'], alpha=0.9))
    
    plt.figtext(0.02, 0.02, f'Jumlah Dimensi: {len(categories)} | Skala: 1-5', 
               fontsize=11,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light_gray'], 
                        edgecolor=COLORS['neutral'], alpha=0.7))
    
    # Simpan figure
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    
    plt.tight_layout()
    plt.show()

def print_summary_statistics(data: Dict[str, float]) -> None:
    """
    Mencetak statistik ringkasan untuk data kematangan digital.
    
    Args:
        data: Dictionary dengan dimensi dan nilai rata-rata
    """
    values = list(data.values())
    categories = list(data.keys())
    
    print("\n" + "="*75)
    print("STATISTIK TINGKAT KEMATANGAN DIGITAL KLINIK DI KABUPATEN PONOROGO")
    print("="*75)
    
    # Urutkan berdasarkan nilai tertinggi
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    
    for i, (dimension, value) in enumerate(sorted_data, 1):
        print(f"{i:2d}. {dimension:35}: {value:.2f}/5.00 ({value/5*100:5.1f}%)")
    
    print("-"*75)
    
    # Statistik deskriptif
    avg_value = np.mean(values)
    max_value = max(values)
    min_value = min(values)
    std_value = np.std(values)
    
    print(f"{'Rata-rata Keseluruhan':35}: {avg_value:.2f}/5.00 ({avg_value/5*100:5.1f}%)")
    print(f"{'Nilai Tertinggi':35}: {max_value:.2f}/5.00 ({categories[values.index(max_value)]})")
    print(f"{'Nilai Terendah':35}: {min_value:.2f}/5.00 ({categories[values.index(min_value)]})")
    print(f"{'Standar Deviasi':35}: {std_value:.2f}")
    print(f"{'Rentang Nilai':35}: {max_value - min_value:.2f}")
    
    print("="*75)
    
    # Analisis dan wawasan
    print("\nWAWASAN KUNCI:")
    print(f"• Dimensi dengan kematangan tertinggi: {categories[values.index(max_value)]} ({max_value:.2f}/5.00)")
    print(f"• Dimensi dengan kematangan terendah: {categories[values.index(min_value)]} ({min_value:.2f}/5.00)")
    print(f"• Gap antara tertinggi dan terendah: {max_value - min_value:.2f} poin")
    
    # Kategori berdasarkan nilai
    high_maturity = [cat for cat, val in data.items() if val >= 4.0]
    medium_maturity = [cat for cat, val in data.items() if 3.0 <= val < 4.0]
    low_maturity = [cat for cat, val in data.items() if val < 3.0]
    
    print(f"• Dimensi dengan kematangan tinggi (≥4.0): {len(high_maturity)} dimensi")
    print(f"• Dimensi dengan kematangan sedang (3.0-3.9): {len(medium_maturity)} dimensi")
    print(f"• Dimensi dengan kematangan rendah (<3.0): {len(low_maturity)} dimensi")
    
    if avg_value >= 4.0:
        maturity_level = "Tinggi"
    elif avg_value >= 3.0:
        maturity_level = "Sedang"
    else:
        maturity_level = "Rendah"
    
    print(f"• Tingkat kematangan digital keseluruhan: {maturity_level} ({avg_value:.2f}/5.00)")

def main() -> None:
    """
    Fungsi utama untuk menjalankan semua visualisasi dan analisis.
    """
    apply_style()
    data = get_digital_maturity_data()
    
    # Cetak statistik ringkasan
    print_summary_statistics(data)
    
    print("\nMembuat visualisasi...")
    
    print("\n1. Membuat spider chart standar...")
    create_spider_chart(data)
    
    print("\n2. Membuat spider chart siap perbandingan...")
    create_comparison_ready_spider_chart(data)
    
    print("\n✅ Semua visualisasi berhasil dibuat!")
    print("\nFile yang dihasilkan di direktori 'output/':")
    print("• digital_maturity_spider.png/.svg")
    print("• digital_maturity_spider_comparison_ready.png/.svg")
    
    print("\nCatatan:")
    print("• Warna spider chart konsisten untuk memungkinkan perbandingan dengan data lain")
    print("• File 'comparison_ready' dirancang khusus untuk overlay dengan data tambahan")

if __name__ == "__main__":
    main()
