from hybrid_ai_py.clhybridlib import query_dbpedia

from pprint import pprint

# pprint(query_dbpedia( "select * { ?s ?p ?o } limit 2"))

from hybrid_ai_py.clhybridlib import QA, generate_text

# text_completion_result = generate_text("President Clinton went to Mexico to")
# pprint(text_completion_result)

pprint(QA("where does Bill Gates work?"))

