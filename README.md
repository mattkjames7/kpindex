# KpIndex

Welcome to the **KpIndex** Python package! This module provides a simple and efficient way to access planetary Kp index data, which is essential for understanding space weather conditions and its effects on Earth as well as in space. The Kp index quantifies geomagnetic activity, providing vital information for researchers, educators, and anyone interested in space weather phenomena.

## Overview

The Kp index is a scale ranging from 0 to 9 that indicates the level of geomagnetic disturbance caused by solar activity. Higher values on the Kp scale indicate greater activity and potential impacts on satellite operations, radio communications, and power grids. This package is designed for users who want to:
- Retrieve the latest Kp index data for specific dates.
- Update local databases with new Kp index data from credible sources.
- Analyze or visualize historical Kp indices for research or educational purposes.

Whether you are a space weather researcher, a teacher, or simply a curious enthusiast, KpIndex makes it easy to access and utilize important geomagnetic data.

## Installation

The KpIndex package can be easily installed using `pip`. Below are the installation instructions.

### Prerequisites
- Python 3.6 or later
- Operating System: Cross-platform

### Steps to Install
You can install KpIndex in several ways:

#### Method 1
Using pip directly from PyPI:
```bash
pip install kpindex --user
```

#### Method 2
Download the wheel file from the "Releases" section of this repository:
```bash
pip install kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 3
Clone the repository and build it yourself:
```bash
git clone https://github.com/mattkjames7/kpindex.git
cd kpindex
python setup.py bdist_wheel
pip install dist/kpindex-0.0.1-py3-none-any.whl --user
```

#### Method 4
If you prefer not to use wheels, you can also clone the repository and directly place the `kpindex` folder into your `$PYTHONPATH`.

### Setting up the Data Path
To download Kp index data from the FTP site, set the `$KPDATA_PATH` environment variable to a directory where you have read and write access. You can do this by running:
```bash
export KPDATA_PATH=/path/to/the/data
```
Alternatively, add this to your `~/.bashrc` file for persistence.

## Features
KpIndex offers a variety of functionalities:
- **Data Retrieval**: Get Kp index data for specific dates or date ranges, including:
  - All historical data when no date is provided.
  - Data for a specific date in `yyyymmdd` format.
  - Data over a range specified by a tuple of start and end dates.
- **Database Update**: Update your local Kp index database by downloading the latest data from an FTP server with:
  ```python
  kpindex.UpdateLocalData()
  ```
- **Data Management**: Functions to read, convert, and delete data files, keeping your data directories clean and organized.
- **Integration**: Easily integrate with existing Python workflows for data analysis and visualization.

## Usage Examples
Here are some quick examples to get you started with KpIndex:

### Update Local Data
To update your local Kp index database, simply run:
```python
import kpindex
kpindex.UpdateLocalData()
```
This will download the latest Kp data and update your local files.

### Retrieve Kp Data
To fetch Kp data for a specific date:
```python
data = kpindex.GetKp(20230101)  # For January 1, 2023
```
To retrieve data for a range of dates:
```python
data = kpindex.GetKp((20230101, 20230110))  # From January 1 to January 10, 2023
```

## Dependencies
KpIndex has a few essential dependencies:
- **Numpy**: Used for numerical operations and data handling.
- **RecarrayTools**: Custom library for managing record arrays, which structures the Kp data efficiently.
- **PyFileIO**: Utility for input/output operations, particularly for handling file reading and writing.

Ensure that these are available in your Python environment. They are generally installed when you run the `pip install kpindex` command.

## Roadmap
- **Planned Features**: Future developments may include extended functionality for more advanced data analysis and visualization techniques such as time-series plotting of Kp indices over specified periods.
- **Collaborations**: Contributions and collaborative features are welcome! Feel free to check out our issues to discuss proposed improvements.

## FAQs
**How often is Kp index data updated?**  
Kp index data is typically updated daily or on a more frequent basis during significant solar activity periods.

**Can I use KpIndex for commercial applications?**  
Yes, KpIndex is open-source under the MIT license, allowing you to use and modify it for personal or commercial purposes.

## Additional Information
For more details or to report issues, please visit the [GitHub repository](https://github.com/mattkjames7/kpindex). We hope you enjoy using the KpIndex package to explore and understand solar impacts on Earth!