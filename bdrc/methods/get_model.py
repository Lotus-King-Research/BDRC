def get_model(wid, mode='resource', save=False):
    
    '''Get model and URIRef
    
    mode | str | `graph` or `resource`
    
    '''
    
    import requests
    from rdflib import Graph, URIRef

    from rdflib.namespace import Namespace

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
