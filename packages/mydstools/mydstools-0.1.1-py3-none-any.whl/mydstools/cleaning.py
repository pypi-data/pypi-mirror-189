# This module is part of mydstools.
# Please refer to https://github.com/antobzzll/dstoolbox


import pandas as pd
import re


def clean_col_names(df_columns: pd.Index, wlen: int = 0) -> list:
    """
    Method for cleaning column names of a `pandas.DataFrame`.

    Args:
        df_columns (pd.Index): dataframe's dirty column names.
        wlen (int, optional): length of cleaned words. Defaults to 0.

    Raises:
        ValueError: if `df_columns` is not a `pd.Index`.

    Returns:
        list: list of new column names to be assigned to `df.columns`.
    """

    # usage:
    # df.columns = utilities.clean_col_names(df.columns)

    try:
        df_columns = df_columns.to_list()
    except AttributeError:
        raise ValueError(
            "Invalid argument type. `df_columns` takes a "
            "`pandas.Index` type.") from None
    else:
        def _fix(target: str):
            target = target.lower().split()
            res = []
            for elem in target:
                elem = re.sub(r'[^\w]', '', elem)
                
                if elem:
                    if wlen > 0:
                        res.append(elem[:wlen])
                    else:
                        res.append(elem)
            return '_'.join(res)

        return list(map(_fix, df_columns))
