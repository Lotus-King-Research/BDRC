def bdo(prop):
    
    from rdflib import Namespace, URIRef

    namespace = Namespace("http://purl.bdrc.io/ontology/core/")

    uri = URIRef(namespace + prop)

    return uri