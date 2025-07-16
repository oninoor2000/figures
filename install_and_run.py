#!/usr/bin/env python3
"""
Installation and Setup Script for Research Figure Generator
==========================================================

This script handles the installation of dependencies and provides
an easy way to generate clinic distribution figures.

Usage:
    python install_and_run.py [--install-only] [--generate-only]
"""

import subprocess
import sys
import os
from pathlib import Path
from typing import List, Optional

def check_python_version() -> bool:
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required.")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies() -> bool:
    """Install required dependencies."""
    try:
        print("\n📦 Installing dependencies...")
        
        # Check if requirements.txt exists
        if not Path("requirements.txt").exists():
            print("❌ requirements.txt not found!")
            return False
        
        # Install dependencies
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Failed to install dependencies: {result.stderr}")
            return False
        
        print("✅ Dependencies installed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_dependencies() -> bool:
    """Check if all required dependencies are available."""
    required_packages = [
        'matplotlib',
        'seaborn', 
        'pandas',
        'numpy',
        'scipy',
        'PIL'  # Pillow
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is available")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        return False
    
    print("\n✅ All dependencies are available!")
    return True

def create_output_directory() -> None:
    """Create output directory if it doesn't exist."""
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        print("✅ Created output directory")
    else:
        print("✅ Output directory already exists")

def run_clinic_distribution() -> bool:
    """Run the clinic distribution visualization script."""
    try:
        print("\n🎨 Generating clinic distribution figures...")
        
        # Import and run the main function
        import clinic_distribution
        clinic_distribution.main()
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import clinic_distribution module: {e}")
        return False
    except Exception as e:
        print(f"❌ Error generating figures: {e}")
        return False

def list_generated_files() -> None:
    """List the generated files in the output directory."""
    output_dir = Path("output")
    if not output_dir.exists():
        print("❌ Output directory doesn't exist")
        return
    
    files = list(output_dir.glob("*"))
    if not files:
        print("❌ No files found in output directory")
        return
    
    print("\n📁 Generated files:")
    for file in sorted(files):
        size = file.stat().st_size / 1024  # Size in KB
        print(f"   • {file.name} ({size:.1f} KB)")

def main() -> None:
    """Main installation and execution function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Install dependencies and generate clinic figures")
    parser.add_argument("--install-only", action="store_true", 
                       help="Only install dependencies, don't generate figures")
    parser.add_argument("--generate-only", action="store_true",
                       help="Only generate figures, skip dependency installation")
    parser.add_argument("--check-deps", action="store_true",
                       help="Only check if dependencies are installed")
    
    args = parser.parse_args()
    
    print("🔬 Research Paper Figure Generator Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create output directory
    create_output_directory()
    
    # Handle different modes
    if args.check_deps:
        if check_dependencies():
            print("\n✅ All dependencies are ready!")
        else:
            print("\n❌ Some dependencies are missing. Run without --check-deps to install them.")
        return
    
    if args.generate_only:
        if not check_dependencies():
            print("\n❌ Dependencies are missing. Install them first by running without --generate-only")
            sys.exit(1)
        
        if run_clinic_distribution():
            list_generated_files()
            print("\n🎉 Figures generated successfully!")
        else:
            sys.exit(1)
        return
    
    # Default flow: install dependencies (if needed) and generate figures
    if not args.install_only:
        # Check if dependencies are already installed
        deps_available = check_dependencies()
        
        if not deps_available:
            print("\n📦 Installing missing dependencies...")
            if not install_dependencies():
                sys.exit(1)
            
            # Re-check dependencies after installation
            if not check_dependencies():
                sys.exit(1)
    else:
        # Install-only mode
        if not install_dependencies():
            sys.exit(1)
        if not check_dependencies():
            sys.exit(1)
        print("\n✅ Installation completed!")
        return
    
    # Generate figures
    if run_clinic_distribution():
        list_generated_files()
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("• Check the 'output/' directory for generated figures")
        print("• View the figures in PNG format for preview")
        print("• Use SVG format for Word documents (vector graphics)")
        print("• Modify clinic_distribution.py to customize visualizations")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main() 