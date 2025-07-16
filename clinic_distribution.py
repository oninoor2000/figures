"""
Clinic Distribution Visualization
=================================

This script creates professional visualizations for clinic distribution data
showing the breakdown between "Klinik Utama" and "Klinik Pratama".

The script generates both bar chart and pie chart visualizations following
the research paper style guide.
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List, Tuple
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

# =============================================================================
# DATA DEFINITION
# =============================================================================

def get_clinic_data() -> Dict[str, int]:
    """
    Get the clinic distribution data.
    
    Returns:
        Dictionary with clinic types and their counts
    """
    return {
        'Klinik Utama': 5,
        'Klinik Pratama': 38
    }

def create_dataframe(data: Dict[str, int]) -> pd.DataFrame:
    """
    Convert clinic data to pandas DataFrame for easier manipulation.
    
    Args:
        data: Dictionary with clinic types and counts
        
    Returns:
        DataFrame with clinic data
    """
    df = pd.DataFrame(list(data.items()), columns=pd.Index(['Clinic_Type', 'Count']))
    df['Percentage'] = (df['Count'] / df['Count'].sum()) * 100
    # Sort by 'Count' descending for better chart readability
    df = df.sort_values('Count', ascending=False).reset_index(drop=True)
    return df

# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def create_bar_chart(data: Dict[str, int], save_path: str = 'clinic_distribution_bar') -> None:
    """
    Create a bar chart visualization for clinic distribution.
    
    Args:
        data: Dictionary with clinic types and counts
        save_path: Path to save the figure (without extension)
    """
    # Create DataFrame
    df = create_dataframe(data)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bar chart
    colors = get_color_palette(len(data))
    bars = ax.bar(df['Clinic_Type'], df['Count'], 
                  color=colors, 
                  edgecolor='white', 
                  linewidth=1.5,
                  alpha=0.8)
    
    # Configure the plot
    configure_bar_plot(
        ax, 
        'Distribusi Klinik Berdasarkan Jenis Klinik', 
        'Jenis Klinik', 
        'Jumlah Klinik'
    )
    
    # Add value labels on bars
    add_value_labels(ax, bars, df['Count'].tolist())
    
    # Add percentage labels as well
    for i, (bar, count, pct) in enumerate(zip(bars, df['Count'], df['Percentage'])):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height/2,
                f'{pct:.1f}%',
                ha='center', va='center',
                fontsize=11, fontweight='bold',
                color='white')
    
    # Customize y-axis
    ax.set_ylim(0, max(df['Count']) * 1.1)
    
    # Add total count annotation
    total_clinics = df['Count'].sum()
    ax.text(0.98, 0.98, f'Total Klinik: {total_clinics}',
            transform=ax.transAxes, 
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor=COLORS['light_gray'], 
                     edgecolor=COLORS['neutral'],
                     alpha=0.8),
            fontsize=10)
    
    # Save the figure to output directory
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')  # Vector format for Word documents
    
    plt.tight_layout()
    plt.show()

def create_pie_chart(data: Dict[str, int], save_path: str = 'clinic_distribution_pie') -> None:
    """
    Create a pie chart visualization for clinic distribution.
    
    Args:
        data: Dictionary with clinic types and counts
        save_path: Path to save the figure (without extension)
    """
    # Create DataFrame
    df = create_dataframe(data)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Create pie chart
    colors = get_color_palette(len(data))
    
    # Calculate percentages for display
    percentages = format_percentage_labels(df['Count'].tolist())
    
    # Create labels with both count and percentage
    labels = [f'{clinic_type}\n({count} klinik, {pct})' 
              for clinic_type, count, pct in zip(df['Clinic_Type'], df['Count'], percentages)]
    
    pie_result = ax.pie(
        df['Count'], 
        labels=labels,
        colors=colors,
        autopct='',  # We'll add custom labels
        startangle=90,
        explode=(0.05, 0),  # Slightly separate the first slice
        shadow=True,
        textprops={'fontsize': 11}
    )
    
    # Handle different return types from ax.pie
    if len(pie_result) == 3:
        wedges, texts, autotexts = pie_result
    else:
        wedges, texts = pie_result
        autotexts = []
    
    # Enhance the appearance
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    
    # Configure the plot
    configure_pie_plot(ax, 'Distribusi Klinik Berdasarkan Jenis Klinik')
    
    # Add total count annotation
    total_clinics = df['Count'].sum()
    ax.text(0, -1.3, f'Total Klinik: {total_clinics}',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor=COLORS['light_gray'], 
                     edgecolor=COLORS['neutral'],
                     alpha=0.9),
            fontsize=12, fontweight='bold')
    
    # Ensure the pie chart is circular
    ax.set_aspect('equal')
    
    # Save the figure to output directory
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')  # Vector format for Word documents
    
    plt.tight_layout()
    plt.show()

def create_horizontal_bar_chart(data: Dict[str, int], save_path: str = 'clinic_distribution_horizontal') -> None:
    """
    Create a horizontal bar chart visualization for clinic distribution.
    
    Args:
        data: Dictionary with clinic types and counts
        save_path: Path to save the figure (without extension)
    """
    # Create DataFrame
    df = create_dataframe(data)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create horizontal bar chart
    colors = get_color_palette(len(data))
    bars = ax.barh(df['Clinic_Type'], df['Count'], 
                   color=colors, 
                   edgecolor='white', 
                   linewidth=1.5,
                   alpha=0.8)
    
    # Configure the plot
    ax.set_title('Distribusi Klinik Berdasarkan Jenis Klinik', fontweight='bold', pad=20, fontsize=14)
    ax.set_xlabel('Jumlah Klinik', fontsize=12)
    ax.set_ylabel('Jenis Klinik', fontsize=12)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add value labels on bars
    for i, (bar, count, pct) in enumerate(zip(bars, df['Count'], df['Percentage'])):
        width = bar.get_width()
        ax.text(width + width*0.02, bar.get_y() + bar.get_height()/2,
                f'{count} ({pct:.1f}%)',
                ha='left', va='center',
                fontsize=11, fontweight='bold',
                color=COLORS['dark_gray'])
    
    # Customize x-axis
    ax.set_xlim(0, max(df['Count']) * 1.15)
    
    # Add total count annotation
    total_clinics = df['Count'].sum()
    ax.text(0.98, 0.02, f'Total Klinik: {total_clinics}',
            transform=ax.transAxes, 
            ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor=COLORS['light_gray'], 
                     edgecolor=COLORS['neutral'],
                     alpha=0.8),
            fontsize=10)
    
    # Save the figure to output directory
    save_figure(f'output/{save_path}', format='png')
    save_figure(f'output/{save_path}', format='svg')  # Vector format for Word documents
    
    plt.tight_layout()
    plt.show()

def print_summary_statistics(data: Dict[str, int]) -> None:
    """
    Print summary statistics for the clinic data.
    
    Args:
        data: Dictionary with clinic types and counts
    """
    df = create_dataframe(data)
    total = df['Count'].sum()
    
    print("\n" + "="*50)
    print("STATISTIK DISTRIBUSI KLINIK")
    print("="*50)
    
    for _, row in df.iterrows():
        clinic_type = row['Clinic_Type']
        count = row['Count']
        percentage = row['Percentage']
        print(f"{clinic_type:15}: {count:3d} klinik ({percentage:5.1f}%)")
    
    print("-"*50)
    print(f"{'Total':15}: {total:3d} klinik (100.0%)")
    print("="*50)
    
    # Additional insights
    print("\nWAWASAN KUNCI:")
    primary_clinic = df.loc[df['Count'].idxmax(), 'Clinic_Type']
    primary_percentage = df.loc[df['Count'].idxmax(), 'Percentage']
    print(f"• {primary_clinic} merupakan mayoritas dengan {primary_percentage:.1f}% dari total klinik")
    
    ratio = df.loc[df['Clinic_Type'] == 'Klinik Pratama', 'Count'].iloc[0] / df.loc[df['Clinic_Type'] == 'Klinik Utama', 'Count'].iloc[0]
    print(f"• Rasio Klinik Pratama terhadap Klinik Utama: {ratio:.1f}:1")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main() -> None:
    """
    Main function to generate all clinic distribution visualizations.
    """
    # Apply the research paper style
    apply_style()
    
    # Get the clinic data
    clinic_data = get_clinic_data()
    
    # Print summary statistics
    print_summary_statistics(clinic_data)
    
    print("\nMembuat visualisasi...")
    
    # Create different types of visualizations
    print("\n1. Membuat diagram batang...")
    create_bar_chart(clinic_data)
    
    print("\n2. Membuat diagram lingkaran...")
    create_pie_chart(clinic_data)
    
    print("\n3. Membuat diagram batang horizontal...")
    create_horizontal_bar_chart(clinic_data)
    
    print("\n✅ Semua visualisasi berhasil dibuat!")
    print("\nFile yang dihasilkan di direktori 'output/':")
    print("• clinic_distribution_bar.png/.svg")
    print("• clinic_distribution_pie.png/.svg") 
    print("• clinic_distribution_horizontal.png/.svg")

if __name__ == "__main__":
    main() 