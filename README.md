### **📚 AI-Powered Research Assistant**  

This project is a **smart research assistant** that helps users **search, summarize, and analyze research papers** efficiently. It integrates with the **arXiv API** to fetch academic papers and uses **GPT-powered summarization** to provide quick insights into research topics.  

---

## **✨ Features**
✅ **Fetch Research Papers** – Search academic papers from **arXiv** by topic.  
✅ **AI-Powered Summarization** – Summarizes abstracts for faster understanding.  
✅ **Sorting & Filtering** – Sort results by **relevance, last update, or submission date**.  
✅ **"More" Button** – Loads additional papers dynamically without reloading.  
✅ **Beautiful UI** – Clean and responsive design for better readability.  

---

## **🔧 Installation**
### **1⃣ Clone the Repository**
```bash
git clone https://github.com/sambhujimmi/Research_Assistant.git
cd Research_Assistant
```

### **2⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4⃣ Set Up Environment Variables**
Export your **API keys** in the terminal:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export ARXIV_API_URL="http://export.arxiv.org/api/query?"
```

---

## **🚀 Usage**
### **1⃣ Start the Flask App**
```bash
python app.py
```
ℹ️ The application will run on `http://127.0.0.1:5000/`.

### **2⃣ Search for Research Papers**
- Open your browser and go to `http://127.0.0.1:5000/`.  
- Enter a **research topic** in the search bar.  
- Click **"Search"** to fetch papers from arXiv.  

### **3⃣ Summarize Papers**
- Click **"Summarize"** under any research paper to get a **GPT-powered summary** of the abstract.  

### **4⃣ Load More Papers**
- Click **"More"** to fetch additional papers dynamically.  

---

## **🌟 Future Enhancements**
🔸 **PDF Export** – Allow users to download research summaries as PDFs.  
🔸 **Bookmarking** – Save important papers for later reference.  
🔸 **Collaborative Research** – Share insights with others in real-time.  

---

