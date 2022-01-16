def build_catalog(base_wids, debug=False, load=False):
    
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
    from rdflib.namespace import Namespace

    BDO = Namespace("http://purl.bdrc.io/ontology/core/")
    BDR = Namespace("http://purl.bdrc.io/resource/")

    from bdrc.methods.get_model import get_model
    from bdrc.methods.get_parts import get_parts
    from bdrc.methods.get_title import get_title
    from bdrc.methods.get_content_location_id import get_content_location_id
    from bdrc.methods.get_tree_index import get_tree_index
    from bdrc.methods.get_content_coordinates import get_content_coordinates

    # this will be returned
    out = []

    # iterate through the bdrc work ids
    for wid in tqdm.tqdm(base_wids):

        # add 'M' to all wids starting with 'W'
        if wid.startswith('W'):
            wid = 'M' + wid

        # get the ttl file and build the model for the work
        model, node = get_model(wid, load=load)

        # find the parts of the work
        nodes = get_parts(model, node)

        # get the ids (as strings) for the parts
        wids = [node.title().split('/')[-1].upper() for node in nodes]

        # CASE-1: Handle those with just one part
        if len(wids) == 0:

            title_temp = get_title(model, node) # QUESTION: how to get language from the triple
            tree_index_temp = [np.nan]
            content_coodridates_temp = [1, np.nan, np.nan, np.nan, np.nan]
            
            if debug is True:
                print('wid: %s' % wid)
                print('title: %s' % title_temp)
                print('tree_index: %s' % tree_index_temp)
                print('coordinates: %s' % content_coodridates_temp)
                print('------')
            
            # add new record to the catalogue
            out.append([wid] + title_temp + tree_index_temp + content_coodridates_temp)
            
            # move to next iteration of the main loop
            continue

        # CASE-2: Handle those with more than just one part
        else:
            parts_temp = []

            model, _node = get_model(wid=wid, mode='graph', load=load) 

            for wid in wids:
                node = URIRef(BDR + wid)
                parts_temp += get_parts(model, node)

            wids = [node.title().split('/')[-1].upper() for node in parts_temp]

            for wid in wids:
                
                model, node = get_model(wid, load=load)

                # get title
                title_temp = get_title(model, node)

                # get tree part tree index
                tree_index_temp = get_tree_index(model, node)

                # get the content coordinates
                location_data_id = get_content_location_id(model, node)
                locations_wid = location_data_id[0].title().split('/')[-1].upper()
                model, node = get_model(locations_wid, load=load)
                content_coodridates_temp = get_content_coordinates(model)

                if debug is True:
                    print('wid: %s' % wid)
                    print('title: %s' % title_temp)
                    print('tree_index: %s' % tree_index_temp)
                    print('coordinates: %s' % content_coodridates_temp)
                    print('------')
                
                # add new record to the catalogue
                out.append([wid] + title_temp + tree_index_temp + content_coodridates_temp)
                
    return out