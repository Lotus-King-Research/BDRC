def properties_dict(wid, model, properties=None):
    
    import bdrc

    out = {}
    
    if properties is None:
        properties = ['hasPart',
                      'hasTitle',
                      'instanceOf',
                      'isRoot',
                      'inRootInstance',
                      'numberOfVolumes',
                      'contentLocation',
                      'partTreeIndex',
                      'partType']
    
    node = bdrc.URIRef(bdrc.BDR + wid)

    for prop in properties:

        objects = []
        
        URI = bdrc.URIRef(bdrc.BDO + prop)
        
        for s, p, o in model.triples([node, URI, None]):
            
            if prop in ['hasPart',
                        'hasTitle',
                        'instanceOf', 
                        'contentLocation',
                        'inRootInstance']:
                objects.append(o.upper().rsplit('/')[-1])
            
            elif prop in ['partType']:
                objects.append(o.split('/')[-1])
            
            else:
                objects.append(o.title())
            
        if len(objects) > 0:
            out[prop] = objects
        else:
            out[prop] = [None]
            
    return out
