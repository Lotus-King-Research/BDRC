def bdr(prop):
    
    from rdflib import Namespace, URIRef

    namespace = Namespace("http://purl.bdrc.io/resource/")

    uri = URIRef(namespace + prop)

    return uri