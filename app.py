from flask import Flask, render_template, request, jsonify
from Fetch_papers import fetch_arxiv_papers
from summarise import summarize_paper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    papers = []

    if request.method == "POST":
        query = request.form["query"]
        papers = fetch_arxiv_papers(query)

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

if __name__ == "__main__":
    app.run(debug=True)
