def make_column_names(df, column_dict=None):
    """clean dataframe column names by lowering the case and replacing spaces with underscores.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to clean

    column_dict : dict
        A dictionary of old column names and their new names.

    Returns
    -------
    pandas.DataFrame
        The cleaned dataframe

    Examples
    --------
    >>> make_column_names(df, column_dict={'old_column_name': 'new_column_name'})  
    >>> make_column_names(df) # default column_dict is None   
    """
    column_names = df.columns
    df.rename(columns=column_dict, inplace=True)
    for column in column_names:        
        df.rename(columns={column: column.lower().replace(" ", "_").replace("-", "_")}, inplace=True)          
    return df
    