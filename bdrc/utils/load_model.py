def load_model(wid):
    
    from rdflib.namespace import Namespace

    BDR = Namespace("http://purl.bdrc.io/resource/")
    
    from rdflib import Graph, URIRef

    f = open('ttl/' + wid, 'rb')
    model_loaded = f.read()
    
    model = Graph()
    model.parse(model_loaded, format="ttl")
    
    node = URIRef(BDR + wid)
    
    return model, node
