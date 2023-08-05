from numbers import Number
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.stats import gmean
from statistics import geometric_mean
from typing import Union

def comms(df: pd.DataFrame) -> pd.DataFrame:
    return df.isnull()

def zeros(df: pd.DataFrame) -> pd.DataFrame:
    return df == 0

def frozen(df: pd.DataFrame, window: Union[str, int] = None) -> pd.DataFrame:
    """ 'cutoff_limit' is minimum amount of time values must be unchanged to be considered frozen. 
    This parameters can be provided in the ContractParameters class in the config script. 
    The default is to use the minimum timedelta found in the DAS data.  """
    if window is None:
        return (df != 0) & (df.diff() == 0)
    if isinstance(window, str):
        df_freq = pd.infer_freq(df.index)
        window_range = 2*pd.Timedelta(window) - pd.Timedelta(df_freq)
    elif isinstance(window, Number):
        window_range = window
    else:
        raise TypeError('cutoff_limit for frozen values must be a number representing window size or a string in format ##min')

    frozen = df.rolling(window_range, center=True).apply(lambda x: np.all(x == x[0]), raw=True)

    return frozen == 1

def negatives(df: pd.DataFrame, cols: list=None) -> pd.DataFrame:
    df = df.copy()
    if cols:
        df = df[cols] < 0
    else:
        df = df <0
    return df

def decreasing(df: pd.DataFrame) -> pd.DataFrame:
    return df.diff() < 0

def band_pass(df: pd.DataFrame, col_limits: dict) -> pd.DataFrame:
    df=df.copy()
    for col, limits in col_limits:
        df.loc[:,col] = (df[col].lt(limits[0])) | (df[col].gt(limits[1]))

    return df

def spline_filter(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df_bool = ~df.isna()
    for col in df.columns:
        non_nulls = df[col][df[col].notna()]
        x = non_nulls.index.values.astype('float')
        y = non_nulls.values
        cs = CubicSpline(x, y)
        deriv = cs(x, 1)
        deriv_mean = np.mean(deriv)
        stdev = np.std(deriv)
        y = (deriv < -2.5*stdev) | (deriv > 2.5*stdev)
        bool_col = pd.DataFrame(index=pd.to_datetime(x), data={col: y})
        df_bool.update(bool_col)
    df_bool = df_bool.astype(np.bool)

    return df_bool



if __name__ == '__main__':
    dates = pd.date_range('2023-1-1 00:00', '2023-6-1 00:00', freq='5T')
    values = list(range(len(dates)))

    data = np.array([values, values, values, values, values]).T
    df = pd.DataFrame(index=dates, data=data)
    df.loc[df.index < '2023-01-01 00:10'] = 1
    df.loc[(df.index > '2023-01-01 00:20') & (df.index < '2023-01-01 01:00')] = 1
    df.loc[(df.index > '2023-01-01 01:10') & (df.index < '2023-01-01 01:40')] = -1
    frozen(df, '15T')