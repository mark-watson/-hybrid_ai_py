from hybrid_ai_py.clhybridlib import query_dbpedia

from pprint import pprint

# pprint(query_dbpedia( "select * { ?s ?p ?o } limit 2"))

from hybrid_ai_py.clhybridlib import QA, generate_text

text_completion_result = generate_text("Q: Who is Bill Clinton married to?")

pprint(text_completion_result)

#text_completion_result = generate_text("Where is the Valley of Kings?")

#pprint(text_completion_result)

