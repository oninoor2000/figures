"""
Research Paper Figure Style Guide
================================

This module provides a consistent style guide for creating publication-ready figures
for research papers. It includes color palettes, font settings, layout parameters,
and utility functions for maintaining visual consistency across all figures.

Usage:
    from style_guide import apply_style, COLORS, save_figure
    apply_style()
    # Create your plot
    save_figure('figure_name.png')
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from typing import Dict, List, Tuple, Optional
import seaborn as sns

# =============================================================================
# COLOR PALETTE
# =============================================================================

# Primary color palette for research figures - Monochrome focused
COLORS = {
    'primary': '#181A1B',      # Almost black (very dark gray)
    'secondary': '#7F8C8D',    # Medium gray
    'accent': '#34495E',       # Darker blue-gray
    'success': '#27AE60',      # Minimal green (only when needed)
    'warning': '#E74C3C',      # Minimal red (only when needed)
    'neutral': '#95A5A6',      # Light gray for neutral elements
    'light_gray': '#F8F9FA',   # Light background
    'dark_gray': '#181A1B',    # For text, match primary
}

# Extended palette for multi-category visualizations - Monochrome first, minimal colors when needed
CATEGORICAL_COLORS = [
    '#181A1B',  # Almost black
    '#7F8C8D',  # Medium gray
    '#34495E',  # Darker blue-gray
    '#95A5A6',  # Light gray
    '#BDC3C7',  # Very light gray
    '#27AE60',  # Professional green (when >5 categories)
    '#3498DB',  # Professional blue (when >6 categories)
    '#E74C3C',  # Professional red (when >7 categories)
]

# Sequential color palettes for heatmaps and gradients
SEQUENTIAL_BLUES = ['#EFF6FF', '#DBEAFE', '#BFDBFE', '#93C5FD', '#60A5FA', '#3B82F6', '#2563EB', '#1D4ED8']
SEQUENTIAL_PURPLES = ['#FAF5FF', '#E9D5FF', '#D8B4FE', '#C084FC', '#A855F7', '#9333EA', '#7C3AED', '#6B21A8']

# =============================================================================
# TYPOGRAPHY
# =============================================================================

FONTS = {
    'family': 'Arial',           # Professional, widely available font
    'title_size': 14,            # Main title
    'label_size': 12,            # Axis labels
    'tick_size': 10,             # Tick labels
    'legend_size': 10,           # Legend text
    'annotation_size': 9,        # Annotations and notes
}

# =============================================================================
# LAYOUT PARAMETERS
# =============================================================================

LAYOUT = {
    'figure_size': (8, 6),       # Default figure size (width, height) in inches
    'dpi': 300,                  # High resolution for publication
    'tight_layout': True,        # Automatic layout adjustment
    'grid_alpha': 0.3,           # Grid transparency
    'spine_width': 0.8,          # Border line width
    'tick_width': 0.6,           # Tick mark width
    'tick_length': 4,            # Tick mark length
}

# =============================================================================
# STYLE APPLICATION FUNCTIONS
# =============================================================================

def apply_style() -> None:
    """
    Apply the research paper style guide to matplotlib.
    Call this function before creating any plots.
    """
    # Set the overall style
    plt.style.use('default')
    
    # Configure matplotlib parameters
    mpl.rcParams.update({
        # Figure settings
        'figure.figsize': LAYOUT['figure_size'],
        'figure.dpi': LAYOUT['dpi'],
        'savefig.dpi': LAYOUT['dpi'],
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
        
        # Font settings
        'font.family': FONTS['family'],
        'font.size': FONTS['label_size'],
        'axes.titlesize': FONTS['title_size'],
        'axes.labelsize': FONTS['label_size'],
        'xtick.labelsize': FONTS['tick_size'],
        'ytick.labelsize': FONTS['tick_size'],
        'legend.fontsize': FONTS['legend_size'],
        
        # Axes settings
        'axes.linewidth': LAYOUT['spine_width'],
        'axes.edgecolor': COLORS['dark_gray'],
        'axes.labelcolor': COLORS['dark_gray'],
        'axes.axisbelow': True,
        
        # Grid settings
        'axes.grid': True,
        'grid.alpha': LAYOUT['grid_alpha'],
        'grid.linewidth': 0.5,
        'grid.color': COLORS['neutral'],
        
        # Tick settings
        'xtick.color': COLORS['dark_gray'],
        'ytick.color': COLORS['dark_gray'],
        'xtick.major.width': LAYOUT['tick_width'],
        'ytick.major.width': LAYOUT['tick_width'],
        'xtick.major.size': LAYOUT['tick_length'],
        'ytick.major.size': LAYOUT['tick_length'],
        
        # Legend settings
        'legend.frameon': True,
        'legend.framealpha': 0.9,
        'legend.fancybox': True,
        'legend.shadow': False,
        'legend.edgecolor': COLORS['neutral'],
        
        # Line settings
        'lines.linewidth': 2.0,
        'lines.markersize': 6,
        
        # Text settings
        'text.color': COLORS['dark_gray'],
    })

def get_color_palette(n_colors: int = 8) -> list[str]:
    """
    Get a color palette suitable for categorical data.
    - 2 kategori: monokrom
    - 3-5 kategori: monokrom + biru, hijau, oranye
    - >5: extend dengan warna profesional
    """
    if n_colors == 2:
        return ['#181A1B', '#7F8C8D']
    elif n_colors <= 5:
        base = ['#181A1B', '#7F8C8D', '#3498DB', '#27AE60', '#F39C12']
        return base[:n_colors]
    else:
        # Extended palette, tetap harmonis
        extended = [
            '#181A1B', '#7F8C8D', '#3498DB', '#27AE60', '#F39C12',
            '#8E44AD', '#E74C3C', '#16A085', '#34495E', '#95A5A6'
        ]
        if n_colors <= len(extended):
            return extended[:n_colors]
        else:
            import seaborn as sns
            return sns.color_palette("tab10", n_colors).as_hex()

def save_figure(filename: str, 
                format: str = 'png', 
                dpi: Optional[int] = None,
                bbox_inches: str = 'tight',
                pad_inches: float = 0.1) -> None:
    """
    Save figure with consistent settings for publication.
    
    Args:
        filename: Output filename (with or without extension)
        format: File format ('png', 'pdf', 'svg', 'eps')
        dpi: Resolution (defaults to style guide setting)
        bbox_inches: Bounding box setting
        pad_inches: Padding around the figure
    """
    if dpi is None:
        dpi = LAYOUT['dpi']
    
    # Add extension if not provided
    if not filename.endswith(f'.{format}'):
        filename = f"{filename}.{format}"
    
    plt.savefig(
        filename,
        format=format,
        dpi=dpi,
        bbox_inches=bbox_inches,
        pad_inches=pad_inches,
        facecolor='white',
        edgecolor='none'
    )
    print(f"Figure saved as: {filename}")

def format_percentage_labels(values: List[float], total: Optional[float] = None) -> List[str]:
    """
    Format values as percentage labels for plots.
    
    Args:
        values: List of values to format
        total: Total value for percentage calculation (if None, sum of values is used)
        
    Returns:
        List of formatted percentage strings
    """
    if total is None:
        total = sum(values)
    
    percentages = [(value / total) * 100 for value in values]
    return [f"{pct:.1f}%" for pct in percentages]

def add_value_labels(ax, bars, values: List[float], format_str: str = "{:.0f}") -> None:
    """
    Add value labels on top of bars in a bar chart.
    
    Args:
        ax: Matplotlib axes object
        bars: Bar container from plt.bar() or ax.bar()
        values: Values to display
        format_str: Format string for the values
    """
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                format_str.format(value),
                ha='center', va='bottom',
                fontsize=FONTS['annotation_size'],
                color=COLORS['dark_gray'])

# =============================================================================
# COMMON PLOT CONFIGURATIONS
# =============================================================================

def configure_bar_plot(ax, title: str, xlabel: str, ylabel: str) -> None:
    """Configure a bar plot with standard settings."""
    ax.set_title(title, fontweight='bold', pad=20)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def configure_pie_plot(ax, title: str) -> None:
    """Configure a pie plot with standard settings."""
    ax.set_title(title, fontweight='bold', pad=20)

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example of how to use the style guide
    apply_style()
    
    # Create a sample plot
    fig, ax = plt.subplots()
    
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values = [25, 40, 35]
    
    # Create bar plot
    bars = ax.bar(categories, values, color=get_color_palette(3))
    
    # Configure the plot
    configure_bar_plot(ax, 'Sample Bar Chart', 'Categories', 'Values')
    add_value_labels(ax, bars, values)
    
    # Save the figure
    save_figure('sample_figure')
    
    plt.show()
    
    print("Style guide applied successfully!")
    print(f"Available colors: {list(COLORS.keys())}")
    print(f"Font settings: {FONTS}")
    print(f"Layout settings: {LAYOUT}") 