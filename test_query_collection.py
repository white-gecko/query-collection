from pathlib import Path

from rdflib import Graph

from query_collection import TemplateQuery, TemplateQueryCollection

QUERY_STR = "select ?s ?p ?o { ?s ?p ?o }"
QUERY_FILE = Path("test_assets/example_dir/spo.rq")
QUERY_DIR = Path("test_assets/example_dir/")


def test_template_query_collection_set():
    tqc = TemplateQueryCollection()
    tqc.set("spo", QUERY_STR)
    query = tqc.get("spo")
    assert isinstance(query, TemplateQuery)
    assert query.query_object == QUERY_STR


def test_template_query_collection_from_file():
    tqc = TemplateQueryCollection()
    tqc.loadFromFile(QUERY_FILE)
    query = tqc.get("spo")
    assert isinstance(query, TemplateQuery)
    assert query.query_object == QUERY_STR


def test_template_query_collection_from_dir():
    tqc = TemplateQueryCollection()
    tqc.loadFromDirectory(QUERY_DIR)
    query = tqc.get("spo")
    assert isinstance(query, TemplateQuery)
    assert query.query_object == QUERY_STR


def test_template_query_collection_exec_query():
    g = Graph()
    tqc = TemplateQueryCollection()
    tqc.loadFromDirectory(QUERY_DIR)
    query = tqc.get("spo")
    assert isinstance(query, TemplateQuery)
    assert query.query_object == QUERY_STR
    g.query(**(query.p()))
