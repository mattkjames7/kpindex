# KP Index Converter Module

## Overview
The KP Index Converter Module is designed to automate the conversion of ASCII Kp index files into a structured binary format. This process involves reading, parsing, and saving the data while maintaining metadata such as update dates and file names.

## Getting Started
1. **Prerequisites**
- Python 3.x or higher
- PyPI packages: numpy, pyfileio, recarraytools (for handling recarrays)
- A custom module `Globals` which contains constants like data types and paths
2. **Installation**
Run the following command to install the required dependencies:
```bash
pip install numpy pyfileio recarraytools
```
3. **Setup**
Create a directory structure as follows:
```
kpindex/
├── _ReadKpTxt.py
├── _ConvertFTPFile.py
├── _ReadDataIndex.py
└── Globals.py
```
4. **Configuration**
Modify the `Globals.py` file to include paths and data types relevant to your system.
5. **Usage**
See the examples below for usage instructions.

## Module Components
table of contents coming soon...

## Examples
Example 1: Converting an ASCII Kp File
```python
from kpindex._ConvertFTPFile import _ConvertFTPFile

# Convert a KP ASCII file to binary
result = _ConvertFTPFile('path/to/ascii_file.txt', 'filename.txt', 'YYYYMMDD')
print(f'Saved file: {result}
')
```

Example 2: Updating the Index File
```python
from kpindex._ReadDataIndex import _ReadDataIndex, _UpdateDataIndex

# Read current index data
idx = _ReadDataIndex()

# Update index entry with new binary file information
_ConvertFTPFile('path/to/ascii_file.txt', 'filename.txt', 'YYYYMMDD')
print('Index updated successfully.')
```

## Troubleshooting
If you encounter any issues, please:
1. Check the `Globals.py` for correct path configurations
2. Verify that all required imports are present in each module
3. Ensure that Python has been upgraded to version 3.x or higher
4. Search for error messages online and refer to the PyPI documentation for troubleshooting

## Changelog
- Version 1.0.0: Initial release
- Version 1.1.0: Added support for date-time handling, improved file saving logic
- Version 2.0.0: Complete rewrite with enhanced processing capabilities and error handling

## Contributing
If you'd like to contribute to this module, please fork the repository and create a pull request with your changes.

## Contact Information
For questions or feedback, contact:
- Email: support@kpindexconverter.com
- Website: https://kpindexconverter.com

## License
This project is under [MIT License](https://github.com/username/license)
``