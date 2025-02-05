# kpindex

The `kpindex` module is a straightforward yet powerful Python package designed to provide users with easy access to planetary Kp index data, which is crucial for understanding geomagnetic activity. This package is aimed at researchers, educators, and enthusiasts in fields like space weather, astronomy, and environmental science who need reliable data on geomagnetic disturbances. Users can harness the functionality provided by `kpindex` to keep track of significant fluctuations in geomagnetic activity, allowing for better-informed decisions in related research or applications.

## What is the Kp Index?
The Kp index is a scale from 0 to 9 that quantifies geomagnetic activity on Earth, where a higher Kp value indicates more intense geomagnetic disturbances, typically caused by solar winds or solar flares. Understanding this data is essential for predicting space weather events that can influence satellite operations, communication systems, and even power grids on Earth.

## Key Use Cases
- **Research Applications**: Analyze Kp index data trends over specific periods to study geomagnetic events.
- **Data Visualization**: Utilize the Kp data for designing informative charts or plots for presentations or reports.
- **Real-time Monitoring**: Keep track of current geomagnetic activity levels and their potential impacts on technology.

## Installation
### Prerequisites
- Python 3.6 or higher
- A working internet connection for data retrieval

### Methods to Install
You can install `kpindex` using one of the following methods:

#### Method 1: Using pip
This is the easiest method:
```bash
pip3 install kpindex --user
```

#### Method 2: Using Wheel Files
Download the wheel file from the "releases" section and install it:
```bash
pip3 install kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 3: Build from Source
For those who prefer building from source:
```bash
git clone https://github.com/mattkjames7/kpindex.git
cd kpindex
python3 setup.py bdist_wheel
pip3 install dist/kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 4: Manual Installation
If you prefer manual installation, clone the repository and move the "kpindex" folder to your `$PYTHONPATH`.

### Post-Installation Setup
To enable the module to download Kp index data, set the environment variable pointing to a directory with read and write access:
```bash
export KPDATA_PATH=/path/to/data
```
You can add this line to your `~/.bashrc` to make it persistent.

## Features
- **Data Update**: Easily download and update local Kp index data using `kpindex.UpdateLocalData()`.
- **Data Retrieval**: Fetch Kp index data for specific dates, date ranges, or retrieve all historical data with `kpindex.GetKp(Date)`.
- **Environment Configuration**: Set up your data directory for reading and writing with the `$KPDATA_PATH` variable.
- **Flexible Input Handling**: The `GetKp` function allows for single dates or ranges as input.

## Usage Examples
Once installed, you can use the package as follows:

### Updating Local Kp Data
```python
import kpindex

# Update local Kp index data
kpindex.UpdateLocalData()  # This will download and convert data if needed
```

### Retrieving Kp Index Data
```python
import kpindex

# Fetch Kp index data for a specific date
specific_date = 20230315  # format: yyyymmdd
kp_data = kpindex.GetKp(specific_date)
print(kp_data)

# Fetch Kp index data for a range of dates
date_range = (20230301, 20230315)
kp_data_range = kpindex.GetKp(date_range)
print(kp_data_range)

# Fetch all available Kp indices
all_kp_data = kpindex.GetKp(None)
print(all_kp_data)
```

## Dependencies
`kpindex` relies on the following packages:
- `numpy`: For efficient array operations and data manipulation.
- `RecarrayTools`: For handling structured arrays.
- `PyFileIO`: For file I/O operations.

All dependencies are available via PyPI and should be installed automatically with your `kpindex` installation via pip.

## Additional Information
Make sure to check the following sections for troubleshooting, FAQs, and future development plans.

### Roadmap
- **Future Features**: Potential support for additional data formats (e.g., CSV export).
- **User Documentation**: Developing comprehensive user documentation for more complex use-cases.

### FAQs
- **What should I do if I encounter an error while downloading data?**  Make sure your `$KPDATA_PATH` is correctly set and that you have write permissions in that directory.

- **Is it possible to revert to an earlier version?** Yes, you can install earlier versions using pip by specifying the version number.

### Troubleshooting
For issues related to installing or using `kpindex`, consider the following:
- Ensure your Python version is compatible.
- Check your internet connection for downloading data.
- Verify that required environment variables are correctly set.

Enjoy exploring Kp index data and understanding geomagnetic activities with `kpindex`!