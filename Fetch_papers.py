import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(query, max_results=5):
    """Fetches and parses research papers from arXiv API."""
    base_url = "http://export.arxiv.org/api/query?"
    # query_url = f"{base_url}search_query={query}&start=0&max_results={max_results}&sortBy=lastUpdatedDate&sortOrder=descending"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": 5,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        return None  # Return None if the request fails

    root = ET.fromstring(response.text)
    papers = []

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        papers.append({
            "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
            "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
            "link": entry.find("{http://www.w3.org/2005/Atom}id").text,
            "published": entry.find("{http://www.w3.org/2005/Atom}published").text,
            "authors": [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")]
        })

    return papers
