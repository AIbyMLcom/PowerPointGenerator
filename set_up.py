#!/usr/bin/env python
from setuptools import setup, find_packages
import subprocess
import sys
import importlib.util
required_packages=[]
def check_dependency(package):
    """Check if a package is installed."""
    try:
        spec = importlib.util.find_spec(package)
        return spec is not None
    except (ModuleNotFoundError, ImportError):
        return False

def main():
    # List of required packages from the BAT file
    required_packages = [
        'flask',
        'python-pptx',
        'flask_limiter',
        'openai',
        'regex',
        'collection'
    ]

    # Check if all dependencies are already installed
    all_dependencies_installed = all(check_dependency(pkg.split('-')[0]) for pkg in required_packages)

    # If not all dependencies are installed, install them
    if not all_dependencies_installed:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + required_packages)
    
    # Run the main application
    print("Starting application...")
    subprocess.check_call([sys.executable, "app.py"])

if __name__ == "__main__":
    setup(
        name="your_app_name",
        version="0.1",
        packages=find_packages(),
        install_requires=required_packages,
        python_requires='>=3.6',
        author="Your Name",
        author_email="admin@aibyml.com",
        description="A short description of your application",
    )
    
    main()
