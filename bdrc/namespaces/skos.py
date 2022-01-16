def skos(prop):
    
    from rdflib import URIRef
    from rdflib.namespace import SKOS

    namespace = SKOS

    uri = URIRef(namespace + prop)

    return uri
