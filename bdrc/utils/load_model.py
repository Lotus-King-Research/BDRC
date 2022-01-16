def load_model(wid, mode='resource', local_path=None):

    '''Load model from .ttl file on local drive.
        
    wid | str | BDRC id
    mode | str | `graph` or `resource` or 'content_location'
    local_path | bool | The absolute path to where `ttl/` directory resides

    NOTE: For mode files are in `ttl/resource` and `ttl/graph` respectively
          i.e. the files have to be available in there.
    
    '''

    from rdflib.namespace import Namespace

    BDR = Namespace("http://purl.bdrc.io/resource/")
    from rdflib import Graph, URIRef
    if local_path is not None:
        f = open(local_path + 'ttl/' + mode + '/' + wid, 'rb') 
    else:
        f = open('ttl/' + mode + '/' + wid, 'rb')
    model_loaded = f.read()
    
    model = Graph()
    model.parse(model_loaded, format="ttl")
    
    node = URIRef(BDR + wid)
    
    return model, node




