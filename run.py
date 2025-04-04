#!/usr/bin/env python
import subprocess
import sys
import os
import importlib.util
import shutil

def check_dependency(package):
    """Check if a package is installed."""
    try:
        # Handle package names with hyphens (like python-pptx)
        package_name = package.split('-')[0] if '-' in package else package
        spec = importlib.util.find_spec(package_name)
        return spec is not None
    except (ModuleNotFoundError, ImportError):
        return False

def ensure_output_directory():
    """Ensure the working directory is set for PowerPoint downloads."""
    # Create an output directory in the current working directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), 'presentations')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def configure_app_output_path():
    """Configure the application to save PowerPoint presentations to the working directory."""
    # This function would be called by app.py or could modify app.py configuration
    # For now, we'll just ensure the directory exists
    output_dir = ensure_output_directory()
    print(f"PowerPoint presentations will be saved to: {output_dir}")
    
    # Setting environment variable that the Flask app can read
    os.environ['PRESENTATION_OUTPUT_DIR'] = output_dir

def main():
    # List of required packages from the BAT file
    required_packages = [
        'flask',
        'python-pptx',
        'flask_limiter',
        'openai',
        'regex',
        'collection',
        'pandas',
        'base64',
        'PILLOW',
        'uuid',
        'requests'
    ]

    # Check if all dependencies are already installed
    missing_dependencies = [pkg for pkg in required_packages if not check_dependency(pkg)]

    # If there are missing dependencies, install them
    if missing_dependencies:
        print("Installing dependencies:", ", ".join(missing_dependencies))
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_dependencies)
    else:
        print("All dependencies are already installed.")
    
    # Configure the application to save PowerPoint presentations to the working directory
    configure_app_output_path()
    
    # Run the main application
    print("Starting application...")
    subprocess.check_call([sys.executable, "app.py"])

if __name__ == "__main__":
    main()
