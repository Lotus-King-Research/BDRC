def get_parts(model, node):

    from rdflib.namespace import Namespace

    BDO = Namespace("http://purl.bdrc.io/ontology/core/")

    objects = []
    
    for s,p,o in model.triples((node, BDO.hasPart, None)):
        objects.append(o.title())

    return objects