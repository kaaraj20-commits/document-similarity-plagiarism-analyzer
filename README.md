# 📄 Document Similarity & Plagiarism Risk Analyzer

A beginner-friendly Python web application that compares two text documents and identifies similar content. It calculates a similarity score, detects exact matching sentences, and generates a downloadable comparison report.

## 🚀 Features

- 📁 Upload two TXT documents or paste text directly
- 🔍 Calculate document similarity percentage
- 📝 Identify exact matching sentences
- 📊 Display word counts for both documents
- 📥 Download a comparison report
- 💻 Simple and interactive web interface
- 🔐 Runs locally without external APIs

## 🛠️ Technologies Used

- **Python** — core programming language
- **Streamlit** — web application interface
- **Scikit-learn** — TF-IDF vectorization and cosine similarity
- **Regular Expressions** — sentence splitting and text normalization

## ⚙️ How It Works

1. The user uploads two text documents or enters their content.
2. The application converts the text into numerical features using TF-IDF.
3. Cosine similarity measures how similar the document representations are.
4. The application identifies exact matching sentences.
5. Results are displayed, and a report can be downloaded.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/document-similarity-plagiarism-analyzer.git
```

### 2. Open the project folder

```bash
cd document-similarity-plagiarism-analyzer
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser at a local address provided by Streamlit.

## 📂 Project Structure

```text
document-similarity-plagiarism-analyzer/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧪 Example Use Case

Compare two academic paragraphs, essays, reports, or other text documents to identify shared content and review their similarity.

## ⚠️ Limitations

- The current version supports TXT files and pasted text.
- It identifies exact matching sentences and measures overall text similarity.
- It does not search the internet for copied content.
- It may not detect paraphrased content reliably.
- A similarity score is not proof of plagiarism.

## 🔮 Future Improvements

- Support PDF and DOCX files.
- Highlight matching phrases within both documents.
- Compare multiple documents at once.
- Improve paraphrase detection.
- Add a comparison history feature.
- Generate formatted PDF reports.

## 👩‍💻 Learning Outcomes

This project demonstrates practical use of Python, text preprocessing, TF-IDF, cosine similarity, and interactive web application development.

## 📜 Disclaimer

This application is intended for educational purposes and preliminary text similarity screening. Its results should not be used alone to determine academic misconduct.
