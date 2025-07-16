# Research Paper Figure Generator

A Python toolkit for creating publication-ready figures for research papers with consistent styling and professional appearance.

## Project Overview

This project provides a comprehensive solution for generating high-quality figures suitable for academic research papers. It includes a custom style guide and specialized scripts for common visualization types.

## Features

- **Consistent Style Guide**: Professional color palettes, typography, and layout settings
- **Publication Ready**: High-resolution outputs in multiple formats (PNG, PDF, SVG, EPS)
- **Type Safety**: Full TypeScript-style type hints for Python functions
- **Multiple Chart Types**: Bar charts, pie charts, horizontal bar charts, and more
- **Automated Labeling**: Automatic percentage calculations and value labels
- **Research Standards**: Follows academic publication guidelines

## Project Structure

```
figures/
├── requirements.txt              # Python dependencies
├── style_guide.py              # Main style guide module
├── clinic_distribution.py       # Clinic distribution visualization script
├── README.md                   # This file
└── output/                     # Generated figures (created when running scripts)
    ├── *.png                   # High-resolution PNG files
    └── *.pdf                   # PDF files for publications
```

## Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation** by running the style guide example:
   ```bash
   python style_guide.py
   ```

## Quick Start

### 1. Basic Usage

```python
from style_guide import apply_style, save_figure, get_color_palette

# Apply the research style
apply_style()

# Create your plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Your plotting code here...
ax.bar(['A', 'B'], [10, 20], color=get_color_palette(2))

# Save with consistent settings
save_figure('my_figure')
```

### 2. Generate Clinic Distribution Figures

```bash
python clinic_distribution.py
```

This will generate:

- Bar chart visualization
- Pie chart visualization
- Horizontal bar chart visualization
- Summary statistics

## Style Guide Features

### Color Palettes

- **Primary Colors**: Professional blue, purple-red, orange accent
- **Extended Palette**: 8 distinct colors for multi-category data
- **Sequential Palettes**: For heatmaps and gradients

### Typography

- **Font**: Arial (professional, widely available)
- **Sizes**: Hierarchical sizing for titles, labels, and annotations
- **Consistency**: Uniform text styling across all figures

### Layout

- **Figure Size**: 8x6 inches (standard for publications)
- **Resolution**: 300 DPI for high-quality printing
- **Grid**: Subtle grid lines for better readability
- **Spacing**: Optimal padding and margins

## Available Functions

### Style Guide (`style_guide.py`)

- `apply_style()`: Apply the research paper style to matplotlib
- `get_color_palette(n)`: Get n colors from the categorical palette
- `save_figure(filename, format)`: Save figures with consistent settings
- `format_percentage_labels(values)`: Format values as percentages
- `add_value_labels(ax, bars, values)`: Add labels to bar charts
- `configure_bar_plot(ax, title, xlabel, ylabel)`: Standard bar plot configuration
- `configure_pie_plot(ax, title)`: Standard pie plot configuration

### Clinic Distribution (`clinic_distribution.py`)

- `create_bar_chart(data)`: Generate bar chart visualization
- `create_pie_chart(data)`: Generate pie chart visualization
- `create_horizontal_bar_chart(data)`: Generate horizontal bar chart
- `print_summary_statistics(data)`: Display data summary

## Customization

### Modifying Colors

```python
from style_guide import COLORS

# Access predefined colors
primary_color = COLORS['primary']
secondary_color = COLORS['secondary']

# Or define custom colors
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
```

### Changing Figure Size

```python
from style_guide import apply_style
import matplotlib.pyplot as plt

apply_style()
fig, ax = plt.subplots(figsize=(12, 8))  # Custom size
```

### Adding New Visualization Types

1. Import the style guide
2. Apply the style with `apply_style()`
3. Use the provided color palettes and configuration functions
4. Save with `save_figure()`

## Output Formats

The toolkit supports multiple output formats:

- **PNG**: High-resolution raster images (300 DPI)
- **PDF**: Vector format ideal for publications
- **SVG**: Scalable vector graphics for web use
- **EPS**: Encapsulated PostScript for academic journals

## Example: Current Clinic Distribution Data

The included example visualizes:

- **Klinik Utama**: 5 clinics (11.6%)
- **Klinik Pratama**: 38 clinics (88.4%)
- **Total**: 43 clinics

Key insights automatically calculated:

- Klinik Pratama represents the majority (88.4%)
- Ratio of Pratama to Utama: 7.6:1

## Best Practices

1. **Always apply the style first**: Call `apply_style()` before creating plots
2. **Use consistent colors**: Leverage `get_color_palette()` for categorical data
3. **Save in multiple formats**: Use both PNG and PDF for different purposes
4. **Include data labels**: Use `add_value_labels()` for clarity
5. **Add context**: Include totals and key statistics in annotations

## Extending the Project

To add new visualization types:

1. Create a new Python file (e.g., `new_chart_type.py`)
2. Import and apply the style guide
3. Follow the existing patterns for configuration and saving
4. Add type hints for all functions
5. Include summary statistics and insights

## Dependencies

- **matplotlib**: Core plotting library
- **seaborn**: Additional color palettes and styling
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scipy**: Scientific computing utilities
- **pillow**: Image processing support

## License

This project is designed for academic and research use. Please ensure proper attribution when using in publications.

## Support

For questions or issues:

1. Check the example code in `style_guide.py`
2. Review the clinic distribution implementation
3. Ensure all dependencies are properly installed
4. Verify Python version compatibility (3.8+)
