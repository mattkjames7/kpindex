# KpIndex

A straightforward Python package designed to retrieve and manage planetary Kp index data. Whether you're a researcher studying geomagnetic activity or simply curating atmospheric data for educational purposes, the **KpIndex** package simplifies your access to vital Kp index information. If you've ever needed to download and process complex data sets, this library makes it easy without requiring deep technical knowledge.

## Understanding the Kp Index
The **Kp index** is a global scale that measures geomagnetic activity on a scale from 0 to 9, based on observations from multiple geomagnetic observatories around the world. Understanding the Kp index is crucial for predicting space weather phenomena, such as solar storms which can affect satellite communications, navigation systems, and power grids. 

This module is beneficial in various use cases, such as:
- **Space Weather Research**: Studying geomagnetic storms and their impacts on Earth.
- **Educational Purposes**: Teaching about space weather and its effects in a practical, data-driven manner.
- **Data Analysis**: Integrating Kp indices into larger atmospheric or astrophysical datasets for analysis and visualization.

## Installation
Installing the **KpIndex** package is simple. You can use `pip` package manager to install it from the Python Package Index (PyPI).

### Prerequisites
- Python version: **3.6** or higher
- Supported platforms: Cross-platform

### Installation Methods
Choose any of the following methods to install the package:

#### Method 1: Using pip
Simply use the following command to install the package and its dependencies:
```bash
pip install kpindex --user
```

#### Method 2: Installing from Wheel
Download the wheel file from the "releases" page, then install it:
```bash
pip install kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 3: Building from Source
If you prefer to build the package yourself, clone the repository:
```bash
git clone https://github.com/mattkjames7/kpindex.git
cd kpindex
python setup.py bdist_wheel
pip install dist/kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 4: Manual Installation
Clone the repository and manually move the ``kpindex`` folder to your `$PYTHONPATH`.

### Post-Installation Configuration
To enable the package to download Kp index data, set the environment variable `$KPDATA_PATH` to a directory where you have read/write access:
```bash
export KPDATA_PATH=/path/to/your/data
```
You can add this line to your `~/.bashrc` file for persistence.

## Features
- **Data Update**: Keep your local Kp index database up to date by downloading the latest data directly from the FTP server.
- **Data Retrieval**: Get Kp index data for specific dates or range of dates easily.
- **Flexible Queries**: Request all historical data or limit your query to particular time frames.
- **Future Development**: Features to extend functionality are planned, including more robust error handling and support for additional data formats.

## Usage Examples
The usage of the **KpIndex** package is simple and straightforward. Below are examples to get you started:

### Updating Local Kp Data
The first step after installation is to ensure you have the latest data:
```python
import kpindex
kpindex.UpdateLocalData()  # Downloads latest Kp data
```

### Retrieving Kp Data
You can retrieve Kp index data for specific dates:
```python
# Importing the package
import kpindex

# Retrieve Kp data for a specific date
data = kpindex.GetKp('20210801')  # YYYYMMDD format

# Retrieve all available data
all_data = kpindex.GetKp(None)

# Retrieve data for a range of dates
range_data = kpindex.GetKp(['20210801', '20210831'])
```

## Dependencies
The **KpIndex** package requires the following dependencies:
- **numpy**: For efficient numerical calculations and managing arrays.
- **RecarrayTools**: For handling structured NumPy record arrays.
- **PyFileIO**: Used for file input/output operations.

## Optional Sections
### FAQs
- **Q: Where can I find documentation for further features?**  
  **A:** Detailed documentation is provided [here](https://github.com/mattkjames7/kpindex).
- **Q: What to do if I encounter errors?**  
  **A:** Check the known issues on the GitHub repository, and feel free to open a new issue if needed.

### Troubleshooting
- **Issue: Data not downloading**  
  - Ensure you have set the `$KPDATA_PATH` environment variable correctly.

## Contributing
Contributions to the **KpIndex** package are welcome! Please fork the repository, make your changes, and submit a pull request. For larger changes, you might want to open an issue to discuss them first.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/mattkjames7/kpindex/blob/main/LICENSE) file for details.

## Acknowledgements
Thank you for considering **KpIndex** for your Kp index data needs! If you find it useful, let us know your experiences or any improvements you wish to see. Happy coding!