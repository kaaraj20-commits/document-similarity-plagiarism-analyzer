DOCUMENT SIMILARITY & PLAGIARISM RISK ANALYZER
================================================

WHAT THIS PROJECT DOES
- Compares two text documents
- Calculates a TF-IDF cosine similarity score
- Finds exact matching sentences
- Creates a downloadable TXT report
- Runs locally and does not use external APIs

REQUIREMENTS
- Python 3.10 or newer
- Internet only for the initial package installation
- VS Code or another code editor

SETUP (Windows)
1. Extract the ZIP folder.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Install the packages:
       python -m pip install -r requirements.txt
5. Start the app:
       python -m streamlit run app.py
6. The app will open in your browser. If it does not, use the local URL shown in the terminal.

HOW TO USE
1. Upload two .txt files OR paste text into both boxes.
2. Click "Compare Documents".
3. Review the similarity percentage and exact matching sentences.
4. Download the report if needed.

IMPORTANT LIMITATIONS
- This starter version supports TXT files and pasted text. PDF support is not included yet.
- The similarity percentage measures text similarity; it does not prove plagiarism.
- Exact sentence matching will not catch every paraphrase.
- Results depend on document length, vocabulary, and the comparison method.
- Do not use the tool as the sole basis for academic misconduct decisions.

SUGGESTED FUTURE IMPROVEMENTS
- Add PDF and DOCX text extraction
- Highlight matching phrases in both documents
- Compare multiple documents at once
- Save previous reports locally
- Add a clear explanation of how the similarity score is calculated
