import os
from rdflib import Graph


def main(filename='leon.ttl'):

    name = os.path.splitext(filename)[0]

    g = Graph()
    g.parse("leon.ttl", format="turtle")

    g.serialize(f"{name}.rdf", format='xml')
    g.serialize(f"{name}.nt", format='nt')
    g.serialize(f"{name}.json", format='json-ld')
    g.serialize(f"{name}.ttl", format='turtle')  # prettify!


if __name__ == "__main__":
    main()
