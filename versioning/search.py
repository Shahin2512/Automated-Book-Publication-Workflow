from versioning.db import col

def search_versions(query: str, n=3):
    res = col.query(query_texts=[query], n_results=n)
    return res
