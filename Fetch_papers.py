import requests

def fetch_arxiv_papers(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.text  # Parse this XML to extract title, author, and abstract
    return None
