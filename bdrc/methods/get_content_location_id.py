def get_content_location_id(model, node):

    from rdflib.namespace import Namespace

    BDO = Namespace("http://purl.bdrc.io/ontology/core/")

    objects = []
    
    for s, p, o in model.triples((node, BDO.contentLocation, None)):
        objects.append(o)

    if isinstance(objects, list):
        return objects
    
    else:
        return [None]   
