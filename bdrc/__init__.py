from bdrc.build_catalog import build_catalog
from bdrc.methods.get_model import get_model
from bdrc.utils.catalog_to_dataframe import catalog_to_dataframe
from bdrc.utils.get_open_pecha_catalog import get_open_pecha_catalog

from rdflib import Namespace, URIRef

BDR = Namespace("http://purl.bdrc.io/resource/")
BDO = Namespace("http://purl.bdrc.io/ontology/core/")
