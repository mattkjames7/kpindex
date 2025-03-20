import kpindex
import numpy as np

def get_all():

    try:
        data = kpindex.GetKp()
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size > 270000, "Not enough data"

    return 0

def get_date():

    try:
        data = kpindex.GetKp(20100101)
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size != 8, "Unexpected amount of data"

    assert all(data.Date == 20100101), "Unexpected date found"

    return 0

def get_date_range():

    try:
        data = kpindex.GetKp([20100101,20100103])
    except:
        print("Failed to read data")
        raise RuntimeError
    
    assert isinstance(data,np.recarray), "Data should be np.recarray"

    assert data.size != 24, "Unexpected amount of data"

    assert all((data.Date >= 20100101) & (data.Date <= 20100103)), "Unexpected date found"

    return 0


def main():

    get_all()
    get_date()
    get_date_range()
    return 0

if __name__ == "__main__":
    main()