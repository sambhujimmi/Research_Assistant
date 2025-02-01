from flask import Flask, render_template, request
from Fetch_papers import fetch_arxiv_papers
from summarise import summarize_paper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary_results = None
    papers = []

    if request.method == "POST":
        query = request.form["query"]
        papers = fetch_arxiv_papers(query)
        
        if papers:
            summary_results = [
                {"title": paper["title"], "summary": summarize_paper(paper["summary"]), "link": paper["link"]}
                for paper in papers
            ]
        else:
            summary_results = [{"title": "No papers found", "summary": "Try a different query."}]

    return render_template("index.html", summaries=summary_results, query=request.form.get("query", ""))

if __name__ == "__main__":
    app.run(debug=True)
