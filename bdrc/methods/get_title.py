def get_title(model, node):

    '''Gets a title (prefLabel) for a given BDRC id.
       
       model | object | rdflib graph model based on .ttl file
       node | object | URIRef 
    '''

    from rdflib.namespace import SKOS
    
    out = []
    
    for s,p,o in model.triples((node, SKOS.prefLabel, None)):
        out.append(o)
        
    for title in out:
        if o.language == 'bo-x-ewts':
            return [title.title()]
        
    for title in out:
        if title.language == 'bo':
            return [title.title()]

    for title in out:
        if title.language == 'en':
            return [title.title()]
        
    else:
        return [None]

