from flask import Flask, render_template, request, jsonify
from fetch_papers import fetch_arxiv_papers
from summarise import summarize_paper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    papers = []

    if request.method == "POST":
        query = request.form["query"]
        sortby = request.form["sort"]
        papers = fetch_arxiv_papers(query, sortby=sortby)

    return render_template("index.html", papers=papers, query=request.form.get("query", ""))

@app.route("/summarize", methods=["POST"])
def get_summary():
    """Fetch summary for a specific paper when the button is clicked."""
    data = request.get_json()
    abstract = data.get("abstract")

    if not abstract:
        return jsonify({"error": "Abstract not found"}), 400

    summary = summarize_paper(abstract)
    return jsonify({"summary": summary})

@app.route("/load_more", methods=["POST"])
def load_more():
    """Fetch additional papers when the 'More' button is clicked."""
    data = request.get_json()
    query = data.get("query", "")
    start = data.get("start", 0)
    sortby = data.get("sort", "relevance")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    new_papers = fetch_arxiv_papers(query, max_results=5, start=start, sortby=sortby)
    return jsonify(new_papers)

if __name__ == "__main__":
    app.run(debug=True)
