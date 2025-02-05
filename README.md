# Kpindex

The **Kpindex** module is a powerful and user-friendly Python package designed for obtaining and managing data related to the **planetary Kp index**. This index quantifies geomagnetic activity, playing a crucial role in space weather monitoring and research. Whether you're a researcher analyzing space weather phenomena or an enthusiast exploring the effects of solar activity on Earth, this module simplifies access to Kp index data, allowing you to focus on analysis rather than data retrieval.

## What is the Kp Index?
The Kp Index provides a standardized measure of geomagnetic activity, ranging from 0 (no activity) to 9 (extreme activity). It reflects disturbances in Earth’s magnetosphere caused by solar wind and is crucial in understanding and predicting space weather conditions. Understanding Kp index variations can facilitate better communication, navigation, and even protect satellites in orbit.

### Key Use Cases:
- **Research in Space Weather:** Analyze the correlation between solar activity and atmospheric phenomena.
- **Navigation Systems:** Enhance the reliability of navigation systems that could be affected by geomagnetic storms.
- **Satellite Operations:** Monitor conditions to safeguard satellite operations from harmful solar effects.
- **Educational Purposes:** Explore Kp index trends and their implications in classrooms or science fair projects.

## Installation
Kpindex is simple to install and supports major platforms. To get started, ensure you have Python 3.x installed on your machine. You can install Kpindex using any of the following methods:

### Method 1: Using pip
Open your command line or terminal and run:
```bash
pip3 install kpindex --user
```

### Method 2: Installing via Wheel
Download the wheel file from the [releases page](https://github.com/mattkjames7/kpindex/releases) and run:
```bash
pip3 install kpindex-0.0.1-py3-none-any.whl --user
```

### Method 3: Building from Source
If you prefer to build from source:
```bash
git clone https://github.com/mattkjames7/kpindex.git
cd kpindex
python3 setup.py bdist_wheel
pip3 install dist/kpindex-0.0.1-py3-none-any.whl --user
```

### Method 4: Manual Installation
To install manually, clone the repository and add the `kpindex` folder to your `$PYTHONPATH`.

### Post-Install Setup
To enable the module to download Kp index data, set the environmental variable `$KPDATA_PATH` to a directory where you have read and write permissions:
```bash
export KPDATA_PATH=/path/to/the/data
```
Insert it into your `~/.bashrc` file for persistence.

## Features
- **Data Downloading:** Automatically downloads Kp index data from a remote FTP server.
- **Local Database Management:** Updates and manages a local database of Kp indices.
- **Flexible Data Retrieval:** Retrieve Kp indices by specific dates or ranges.
- **Progress Indicators:** Provides feedback during lengthy data downloads.
- **Error Handling:** Built-in checks to ensure that files are processed only when updates are required.
- **File Conversion:** Converts downloaded data from ASCII to binary format for efficiency.

## Usage Examples
Here’s how you can utilize the Kpindex module to manage Kp index data:

### Update Local Data
Before accessing Kp index data, ensure your local database is up to date:
```python
import kpindex
kpindex.UpdateLocalData()  # Downloads the latest data
```

### Retrieve Kp Index Data
You can retrieve Kp index data for specific dates:
```python
# Retrieve all Kp indices:
data_all = kpindex.GetKp(None)

# Retrieve Kp index for a specific date (yyyymmdd):
data_specific = kpindex.GetKp(20220101)

# Retrieve Kp indices for a date range:
data_range = kpindex.GetKp((20220101, 20220131))  # From Jan 1 to Jan 31, 2022
```

## Dependencies
Kpindex has the following dependencies which are installed automatically via pip:
- **NumPy:** Used for numerical operations and data handling.
- **RecarrayTools:** Helps manage record arrays efficiently.
- **PyFileIO:** Required for file input/output operations.

## Roadmap
- Implement additional formats for data storage.
- Enhance error handling and user feedback during data retrieval.
- Plan for API integration to expand data sources.

## FAQs
- **What Python versions are supported?**  Kpindex supports Python 3.x.
- **Can I use Kpindex for real-time monitoring?**  While Kpindex focuses on historical data, you can automate data updates to keep your database current.
- **What should I do if I encounter issues?** Check the issues section on GitHub for known problems or troubleshooting tips.

## Troubleshooting
If you encounter issues:  
- Ensure that your directories are correctly set up and that the `$KPDATA_PATH` is valid.  
- Validate that your Python and package versions are compatible.  
- Review the console output for any error messages that could guide you in resolving problems.

Enjoy using Kpindex to explore and analyze geomagnetic data! If you have any questions or contributions, feel free to reach out on the [GitHub repository](https://github.com/mattkjames7/kpindex).  

---  

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.