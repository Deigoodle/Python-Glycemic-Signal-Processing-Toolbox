# Built-in
import datetime

# 3rd party
import pandas as pd

def disjoin_days_and_hours(df,
                           date_column: str | int = 0, 
                           cgm_column: str | int = 1,
                           date_format: str | None = None) -> pd.DataFrame:
    '''
    Disjoins a dataframe with a column with datetime objects into a dataframe with columns for day, time and cgm values

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe to disjoin
    date_column : str or int, optional
        Column name or index with datetime objects, by default 0
    cgm_column : str or int, optional
        Column name or index with cgm values, by default 1
    date_format : str, default None
        Format of the date information, if None, it will be assumed that the date information is in a consistent format

    Returns
    -------
    disjoined_df : pd.DataFrame
        Disjoined dataframe
    '''

    disjoined_df = pd.DataFrame(columns=['Timestamp','Day','Time','CGM'])

    if isinstance(date_column, int):
        disjoined_df['Timestamp'] = pd.to_datetime(df.iloc[:, date_column],format=date_format)
    else:
        disjoined_df['Timestamp'] = pd.to_datetime(df.loc[:, date_column],format=date_format)

    if isinstance(cgm_column, int):
        disjoined_df['CGM'] = df.iloc[:, cgm_column]
    else:
        disjoined_df['CGM'] = df.loc[:, cgm_column]

    disjoined_df['Day'] = disjoined_df['Timestamp'].dt.date
    disjoined_df['Time'] = disjoined_df['Timestamp'].dt.time

    return disjoined_df