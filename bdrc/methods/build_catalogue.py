def build_catalogue(base_wids):
    
    '''Takes in wid (bdrc work id) and returns several meta-data:
    
    - Title
    - Tree Index*
    - Volume
    - Start Page*
    - End Page*
    - Start Line*
    - End Line*
    
    * Only given for multi volume works.
    
    base_wids | list | one or more bdrc work ids
    
    An example for building the catalog for 50 randomly picked
    works from OpenPecha: 
    
    base_wids = get_open_pecha_catalog(50)
    catalog = build_catalogue(base_wids)
    
    The data can additionally be 
    
    '''

    import pandas as pd
    import numpy as np
    import tqdm
    from rdflib import URIRef

    final_dict = {}
    final_out = []

    for wid in tqdm.tqdm(base_wids):

        final_reference = wid
        wid = 'M' + wid

        model, node = get_model(wid)
        nodes = get_has_part(model, node)

        wids = [node.title().split('/')[-1].upper() for node in nodes]

        # Handle those with just one part
        if len(wids) == 0:

            temp = [get_title(model, node)[0]]
            temp += [np.nan, 1, np.nan, np.nan, np.nan, np.nan]
            final_out.append([wid] + temp)

        # Handle those with more than just one part
        else:
            parts_temp = []

            model, _node = get_model(wid, 'graph') 

            for wid in wids:
                node = URIRef(BDR + wid)
                parts_temp += get_has_part(model, node)

            wids = [node.title().split('/')[-1].upper() for node in parts_temp]

            for wid in wids:
                
                model, node = get_model(wid)

                location_data_id = get_content_location_id(model, node)

                # get title
                title_temp = get_title(model, node)
                if len(title_temp) == 0:
                    title_temp.append("TITLE NOT AVAILABLE")

                # get tree part tree index
                tree_index_temp = get_part_tree_index(model, node)
                if len(tree_index_temp) == 0:
                    tree_index_temp.append("TREE PART INDEX NOT AVAILABLE")

                locations_wid = location_data_id[0].title().split('/')[-1].upper()

                model, node = get_model(locations_wid)

                final_out.append([[wid] + title_temp + tree_index_temp + get_content_coordinates(model)])
                
    return final_out
