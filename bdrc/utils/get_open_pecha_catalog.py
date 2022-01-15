def get_open_pecha_catalog(n=None):
    
    '''Creates list of BDRC work ids based on OpenPecha Catalog.
    
    n | int | Unless none, set number of wids to pick randomly from the whole set.
    
    SOURCE: https://raw.githubusercontent.com/OpenPecha/catalog/master/data/catalog.csv
    
    '''

    import pandas as pd
    import numpy as np
    import wrangle
    import warnings

    warnings.simplefilter('ignore')
    
    # get the csv vatalog
    data_url = 'https://raw.githubusercontent.com/OpenPecha/catalog/master/data/catalog.csv'

    # read it to a dataframe
    open_pecha_catalogue = pd.read_csv(data_url, error_bad_lines=False)

    # reformat for the purpose
    wids = open_pecha_catalogue['Source ID'].dropna()[open_pecha_catalogue['Source ID'].dropna().str.startswith('bdr')]
    wids = wids.str.replace('bdr:', '')

    # replace missing values with NAN
    wids = wrangle.df_fill_empty(pd.DataFrame(wids), np.nan).dropna()
    
    # remove other than standard work id
    wids = wids[wids['Source ID'].str.startswith('W')]
    
    if isinstance(n, int):
        wids = wids.sample(n)
    
    return wids['Source ID'].tolist()
