# 📄 Corporate Agent – ADGM Legal Document Reviewer

## 📌 Overview
The **Corporate Agent – ADGM Legal Document Reviewer** is an AI-powered compliance assistant built with **Streamlit**, **LangChain**, **LlamaIndex**, and the **Google Gemini API**.  
It automates the review of legal documents for **company incorporation** under ADGM regulations, performing **document classification**, **checklist verification**, **red flag detection**, and **compliance scoring**.  

This project was developed as part of an advanced AI engineering assignment to showcase the integration of **LLM-powered reasoning** with structured document analysis.

---

## 🚀 Features
- 📂 **Multiple Document Uploads** – Upload `.docx` files for instant processing.
- 📋 **Regulatory Checklist Verification** – Validates against required ADGM incorporation docs.
- 🚩 **Red Flag Detection** – Identifies compliance issues in document content.
- 📊 **Compliance Scoring** – Generates a percentage score based on checklist adherence.
- 📝 **Automated Summaries** – Creates structured JSON reports for each document.
- 🔍 **RAG Engine** – Query processed documents using **LangChain + LlamaIndex** for semantic search.
- 💾 **Reviewed Document Output** – Inserts comments directly into `.docx` files.

---

## 🛠 Tech Stack
### Core Frameworks & AI
- **[Streamlit](https://streamlit.io/)** – Interactive frontend for document review
- **[LangChain](https://www.langchain.com/)** – Orchestration and prompt chaining
- **[LlamaIndex](https://www.llamaindex.ai/)** – Document indexing and retrieval
- **[Google Gemini API](https://ai.google.dev/)** – LLM reasoning for classification, summarization, and compliance checks

### Document Processing
- **[python-docx](https://python-docx.readthedocs.io/en/latest/)** – Extract and annotate `.docx` files
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)** *(optional)* – For PDF support if extended
- **[tika](https://tika.apache.org/)** *(optional)* – For broader document parsing


---

## 📂 Required Documents Checklist
For **incorporation** processes, the tool checks for:
1. Articles of Association
2. Memorandum of Association
3. Board Resolution
4. Shareholder Resolution
5. Incorporation Form
6. UBO Form
7. Register
8. Address Notice

---

## 🖼 Screenshots

### 1️⃣ Uploading Documents
![Screenshot 1](Corporate%20Agent/images/Screenshot%202025-08-11%20093027.png)

### 2️⃣ Checklist Verification
![Screenshot 2](Corporate%20Agent/images/Screenshot%202025-08-11%20093049.png)

### 3️⃣ Missing Documents Detection
![Screenshot 3](Corporate%20Agent/images/Screenshot%202025-08-11%20093103.png)

### 4️⃣ Document Summaries
![Screenshot 4](Corporate%20Agent/images/Screenshot%202025-08-11%20093121.png)

### 5️⃣ Compliance Issues Example
![Screenshot 5](Corporate%20Agent/images/Screenshot%202025-08-11%20093149.png)

### 6️⃣ Summary JSON Output
![Screenshot 6](Corporate%20Agent/images/Screenshot%202025-08-11%20093209.png)

### 7️⃣ Red Flags & Recommendations
![Screenshot 7](Corporate%20Agent/images/Screenshot%202025-08-11%20093234.png)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
