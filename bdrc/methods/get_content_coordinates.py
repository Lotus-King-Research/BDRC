def get_content_coordinates(model):
    
    from rdflib import URIRef
    import numpy as np
    
    properties = ['contentLocationVolume',
                  'contentLocationPage',
                  'contentLocationEndPage',
                  'contentLocationLine',
                  'contentLocationEndLine']
    
    out = []
    
    for prop in properties:
        
        uri = URIRef(BDO + prop)
    
        before = len(out)
    
        for s,p,o in model.triples((None, uri, None)):
            
            out.append(o.title())
            
        after = len(out)
        
        if after - before == 0:
            if prop == 'contentLocationVolume': # QUESTION: does this make sense?
                out.append(1)
            else:
                out.append(np.nan)
            
    return out
