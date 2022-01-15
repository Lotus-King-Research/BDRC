def get_content_coordinates(model):
    
    from rdflib import URIRef
    import numpy as np
    
    from rdflib.namespace import Namespace

    BDO = Namespace("http://purl.bdrc.io/ontology/core/")
    
    properties = ['contentLocationVolume',
                  'contentLocationPage',
                  'contentLocationEndPage',
                  'contentLocationLine',
                  'contentLocationEndLine']
    
    out = []
    
    # handle the properties one by one
    for prop in properties:
        
        uri = URIRef(BDO + prop)
    
        # current number of objects in list
        before = len(out)
    
        # find the matching objects for the property
        for _s, _p, o in model.triples((None, uri, None)):
            out.append(o.title())
            
        # see if any were added
        after = len(out)
        
        # handle the cases where none were added
        if after - before == 0:
            
            # assume that if contentLocationVolume is not present, volume number is 1
            if prop == 'contentLocationVolume':
                out.append(1)
            
            # for everything else record as NaN
            else:
                out.append(np.nan)
            
    return out
