"""
Distribusi Klinik Berdasarkan Durasi Implementasi SIK
====================================================

Script ini menghasilkan visualisasi distribusi klinik berdasarkan durasi implementasi SIK.
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict
from style_guide import (
    apply_style,
    save_figure,
    get_color_palette,
    configure_bar_plot,
    configure_pie_plot,
    add_value_labels,
    format_percentage_labels,
    COLORS
)

def get_durasi_data() -> Dict[str, int]:
    """
    Data distribusi klinik berdasarkan durasi implementasi SIK.
    """
    return {
        '< 1 Tahun': 10,
        '1-5 Tahun': 33,
        '> 5 Tahun': 0
    }

def create_dataframe(data: Dict[str, int]) -> pd.DataFrame:
    df = pd.DataFrame(list(data.items()), columns=pd.Index(['Durasi Implementasi SIK', 'Jumlah Klinik']))
    df['Persentase'] = (df['Jumlah Klinik'] / df['Jumlah Klinik'].sum()) * 100
    # Sort by 'Jumlah Klinik' descending for better chart readability
    df = df.sort_values('Jumlah Klinik', ascending=False).reset_index(drop=True)
    return df

def create_bar_chart(data: Dict[str, int], save_path: str = 'durasi_implementasi_sik_bar') -> None:
    df = create_dataframe(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = get_color_palette(len(data))
    bars = ax.bar(df['Durasi Implementasi SIK'], df['Jumlah Klinik'], color=colors, edgecolor='white', linewidth=1.5, alpha=0.8)
    configure_bar_plot(
        ax,
        'Distribusi Klinik Berdasarkan Durasi Implementasi SIK',
        'Durasi Implementasi SIK',
        'Jumlah Klinik'
    )
    add_value_labels(ax, bars, df['Jumlah Klinik'].tolist())
    for i, (bar, count, pct) in enumerate(zip(bars, df['Jumlah Klinik'], df['Persentase'])):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height/2,
                f'{pct:.1f}%',
                ha='center', va='center',
                fontsize=11, fontweight='bold',
                color='white')
    ax.set_ylim(0, max(df['Jumlah Klinik']) * 1.1)
    total = df['Jumlah Klinik'].sum()
    ax.text(0.98, 0.98, f'Total Klinik: {total}',
            transform=ax.transAxes,
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], edgecolor=COLORS['neutral'], alpha=0.8),
            fontsize=10)
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    plt.tight_layout()
    plt.show()

def create_pie_chart(data: Dict[str, int], save_path: str = 'durasi_implementasi_sik_pie') -> None:
    df = create_dataframe(data)
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = get_color_palette(len(data))
    percentages = format_percentage_labels(df['Jumlah Klinik'].tolist())
    labels = [f'{durasi}\n({jumlah} klinik, {pct})' for durasi, jumlah, pct in zip(df['Durasi Implementasi SIK'], df['Jumlah Klinik'], percentages)]
    pie_result = ax.pie(
        df['Jumlah Klinik'],
        labels=labels,
        colors=colors,
        autopct='',
        startangle=90,
        explode=[0.05 if count > 0 else 0 for count in df['Jumlah Klinik']],
        shadow=True,
        textprops={'fontsize': 11}
    )
    if len(pie_result) == 3:
        wedges, texts, autotexts = pie_result
    else:
        wedges, texts = pie_result
        autotexts = []
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    configure_pie_plot(ax, 'Distribusi Klinik Berdasarkan Durasi Implementasi SIK')
    total = df['Jumlah Klinik'].sum()
    ax.text(0, -1.3, f'Total Klinik: {total}',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], edgecolor=COLORS['neutral'], alpha=0.9),
            fontsize=12, fontweight='bold')
    ax.set_aspect('equal')
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    plt.tight_layout()
    plt.show()

def create_horizontal_bar_chart(data: Dict[str, int], save_path: str = 'durasi_implementasi_sik_horizontal') -> None:
    df = create_dataframe(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = get_color_palette(len(data))
    bars = ax.barh(df['Durasi Implementasi SIK'], df['Jumlah Klinik'], color=colors, edgecolor='white', linewidth=1.5, alpha=0.8)
    ax.set_title('Distribusi Klinik Berdasarkan Durasi Implementasi SIK', fontweight='bold', pad=20, fontsize=14)
    ax.set_xlabel('Jumlah Klinik', fontsize=12)
    ax.set_ylabel('Durasi Implementasi SIK', fontsize=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for i, (bar, count, pct) in enumerate(zip(bars, df['Jumlah Klinik'], df['Persentase'])):
        width = bar.get_width()
        ax.text(width + width*0.02, bar.get_y() + bar.get_height()/2,
                f'{count} ({pct:.1f}%)',
                ha='left', va='center',
                fontsize=11, fontweight='bold',
                color=COLORS['dark_gray'])
    ax.set_xlim(0, max(df['Jumlah Klinik']) * 1.15)
    total = df['Jumlah Klinik'].sum()
    ax.text(0.98, 0.02, f'Total Klinik: {total}',
            transform=ax.transAxes,
            ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light_gray'], edgecolor=COLORS['neutral'], alpha=0.8),
            fontsize=10)
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')
    plt.tight_layout()
    plt.show()

def print_summary_statistics(data: Dict[str, int]) -> None:
    df = create_dataframe(data)
    total = df['Jumlah Klinik'].sum()
    print("\n" + "="*50)
    print("STATISTIK DISTRIBUSI KLINIK BERDASARKAN DURASI IMPLEMENTASI SIK")
    print("="*50)
    for _, row in df.iterrows():
        durasi = row['Durasi Implementasi SIK']
        count = row['Jumlah Klinik']
        percentage = row['Persentase']
        print(f"{durasi:15}: {count:3d} klinik ({percentage:5.1f}%)")
    print("-"*50)
    print(f"{'Total':15}: {total:3d} klinik (100.0%)")
    print("="*50)
    print("\nWAWASAN KUNCI:")
    primary_durasi = df.loc[df['Jumlah Klinik'].idxmax(), 'Durasi Implementasi SIK']
    primary_percentage = df.loc[df['Jumlah Klinik'].idxmax(), 'Persentase']
    print(f"• Durasi '{primary_durasi}' merupakan mayoritas dengan {primary_percentage:.1f}% dari total klinik")
    # Rasio dua kategori terbanyak
    sorted_df = df.sort_values('Jumlah Klinik', ascending=False)
    if len(sorted_df) > 1 and sorted_df.iloc[1]['Jumlah Klinik'] > 0:
        ratio = sorted_df.iloc[0]['Jumlah Klinik'] / sorted_df.iloc[1]['Jumlah Klinik']
        print(f"• Rasio {sorted_df.iloc[0]['Durasi Implementasi SIK']} terhadap {sorted_df.iloc[1]['Durasi Implementasi SIK']}: {ratio:.1f}:1")

def main() -> None:
    apply_style()
    data = get_durasi_data()
    print_summary_statistics(data)
    print("\nMembuat visualisasi...")
    print("\n1. Membuat diagram batang...")
    create_bar_chart(data)
    print("\n2. Membuat diagram lingkaran...")
    create_pie_chart(data)
    print("\n3. Membuat diagram batang horizontal...")
    create_horizontal_bar_chart(data)
    print("\n✅ Semua visualisasi berhasil dibuat!")
    print("\nFile yang dihasilkan di direktori 'output/':")
    print("• durasi_implementasi_sik_bar.png/.svg")
    print("• durasi_implementasi_sik_pie.png/.svg")
    print("• durasi_implementasi_sik_horizontal.png/.svg")

if __name__ == "__main__":
    main() 