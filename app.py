from flask import Flask, render_template, request
from Fetch_papers import fetch_arxiv_papers
from summarise import summarize_paper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        papers = fetch_arxiv_papers(query)
        
        if papers:
            summary = summarize_paper(papers)
            return render_template("index.html", summary=summary, query=query)
        return render_template("index.html", summary="No papers found.")

    return render_template("index.html", summary=None)

if __name__ == "__main__":
    app.run(debug=True)
