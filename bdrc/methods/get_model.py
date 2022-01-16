def get_model(wid, mode='resource', save=False, load=False):
    
    '''Get model and URIRef
    
    wid | str | BDRC id
    mode | str | `graph` or `resource`
    save | bool | If the ttl file is to be stored on local in `ttl/`
    load | bool | If the model is to be loaded from local file instead

    NOTE: For mode files are in `ttl/resource` and `ttl/graph` respectively
          i.e. the files have to be available in there.
    
    '''
    
    import requests
    from rdflib import Graph, URIRef

    from rdflib.namespace import Namespace

    from bdrc.utils.load_model import load_model

    if load is True:
        return load_model(wid, mode)

    BDR = Namespace("http://purl.bdrc.io/resource/")

    # get the response for the data
    data_url = 'https://purl.bdrc.io/' + mode + '/' + wid + '.ttl'
    response = requests.get(data_url)
    
    # build the graph
    model = Graph()
    model.parse(response.content, format="ttl")
    
    # create node reference
    node = URIRef(BDR + wid)
    
    if save is True:
        f = open('ttl/' + wid, 'wb')
        f.write(response.content)
        f.close()

    return model, node
