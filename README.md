# kpindex: A Python Package for Working with Kp Index Data

The `kpindex` package provides a simple interface for accessing and working with data related to the Kp index, which measures geomagnetic activity.

## Features:

* **Version Retrieval:** Automatically reads and reports the installed package version from the `__init__.py` file.
* **Data Access (Under Development):** While this structure sets up the foundation for handling kp index data, the actual data loading and processing functionalities are not yet implemented. You would need to add code within the `kpindex` module to fetch and manage the data.

## Installation:

You can install `kpindex` using pip:

```bash
pip install kpindex
```

## Usage Example:

Assuming future development includes data access functions, you might use the package like this:

```python
import kpindex

# Retrieve the current version of the package
version = kpindex.getversion()
print(f'kpindex Version: {version}')

# Load and process kp index data (example placeholder)
data = kpindex.load_kp_index_data('path/to/data.txt')
```

## Dependencies:
* `numpy`: For numerical operations on kp index data.
* `RecarrayTools`: Provides tools for working with recarrays, which are efficient for handling multi-dimensional scientific data. 
* `PyFileIO`: Enables reading and writing various file formats, potentially used for storing or accessing kp index data.

## Development:

This package is actively under development. Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License:

Copyright 2023 [Your Name/Organization]
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.