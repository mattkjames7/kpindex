# kpindex
Very simple package for obtaining the planetary Kp index data (see 
https://www.gfz-potsdam.de/en/kp-index/ for more information)

## Installation

This package depends on the following:

* numpy
* RecarrayTools
* PyFileIO

which are all available on PyPI.

Installation is simple and can be done in one of four ways:

### Method 1

This method simply uses the Python `pip3` command to download this 
module and its dependencies:

```pip3 install kpindex --user``` 

### Method 2

This method uses the Python wheel on the "releases" page of this 
repository. Download the wheel, then isntall using `pip3`:

```pip3 install kpindex-0.0.1-py3-none-any.whl --user```

### Method 3

Don't trust my prepackaged stuff? OK, clone this repository and build
your own:

```
git clone https://github.com/mattkjames7/kpindex.git
cd kpindex
python3 setup.py bdist_wheel
pip3 install dist/kpindex-0.0.1-py3-none-any.whl --user
```

### Method 4

So you don't like wheels? Fine. Clone the repository and just move the
"kpindex" folder to your `$PYTHONPATH`.

## Post-Install

In order for the module to be able to download the Kp index data from
the FTP site, you will need to point it in the direction of a directory
where you have read and write access using the `$KPDATA_PATH`
environment variable. This can be done either by running the following
in the terminal before starting Python, or inserting it into your 
`~/.bashrc` file:

```
export KPDATA_PATH=/path/to/the/data
```

## Usage

Using this module is very simple: the first time you run it you will 
need to update the database (also when you think the database is out of 
date) e.g.

```python
import kpindex
kpindex.UpdateLocalData()
```

It may take a couple of minutes to download the data and convert it, 
then you are ready to read the data:

```python
data = kpindex.GetKp(Date)
```

where `Date` could be `None`, in which case ALL of the Kp indices ever
will be returned; `Date` could be a single date in the format yyyymmdd,
in which case only Kp indices fromt hat date will be returned; finally
it could be a two element array/list/tuple containing two dates, in this
case it will return all the indices from the start to the end date.


Enjoy!
