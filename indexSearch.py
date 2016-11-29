import whoosh.index as index
from whoosh import scoring
ix = index.open_dir(".")
def search(term, numResults):
	res = []
	from whoosh.qparser import QueryParser
	with ix.searcher(weighting=scoring.BM25F()) as searcher:
		query = QueryParser("text", ix.schema).parse(term)
		results = searcher.search(query, limit=numResults)
		for r in results:
			#res.append(r["text"])
			#res.append(r.score)
			res.append([r["text"],r.score])
	

	return res

