def get_tree_index(model, node):

    from rdflib.namespace import Namespace

    BDO = Namespace("http://purl.bdrc.io/ontology/core/")
    
    objects = []
    
    for _s, _p, o in model.triples((node, BDO.partTreeIndex, None)):
        objects.append(o.title())

    # return objects if a value is present
    if isinstance(objects[0], str):
        return objects
    
    # otherwise return None
    else:
        return [None]