def catalog_to_dataframe(data, save=False):
    
    import pandas as pd

    df = pd.DataFrame(data)

    cols = ['bdrc_id',
            'title',
            'tree_index',
            'volume',
            'start_on_page',
            'end_on_page',
            'start_on_line',
            'end_on_line']

    df.columns = cols
    
    if save is True:
    
        df.to_csv('open_pecha_catalog.csv', index=None)
    
    return df