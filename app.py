import re
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Document Similarity Analyzer", page_icon="📄", layout="wide")

st.title("📄 Document Similarity & Plagiarism Risk Analyzer")
st.write(
    "Compare two text documents locally and find similar content. "
    "This tool is a screening aid, not proof of plagiarism."
)

def read_uploaded_file(uploaded_file):
    """Read a TXT file and decode it safely."""
    raw = uploaded_file.getvalue()
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")

def split_sentences(text):
    """Simple sentence splitter suitable for a beginner project."""
    pieces = re.split(r"(?<=[.!?])\s+|\n+", text.strip())
    return [piece.strip() for piece in pieces if piece.strip()]

def clean_sentence(sentence):
    """Normalize case and whitespace for sentence matching."""
    return re.sub(r"\s+", " ", sentence.lower()).strip()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Document A")
    file_a = st.file_uploader("Upload the first TXT file", type=["txt"], key="file_a")
    text_a = read_uploaded_file(file_a) if file_a else st.text_area(
        "Or paste Document A text here", height=220, key="text_a"
    )

with col2:
    st.subheader("Document B")
    file_b = st.file_uploader("Upload the second TXT file", type=["txt"], key="file_b")
    text_b = read_uploaded_file(file_b) if file_b else st.text_area(
        "Or paste Document B text here", height=220, key="text_b"
    )

if st.button("🔍 Compare Documents", type="primary", use_container_width=True):
    if not text_a.strip() or not text_b.strip():
        st.warning("Please upload or paste text for both documents.")
    else:
        try:
            vectorizer = TfidfVectorizer(stop_words="english")
            matrix = vectorizer.fit_transform([text_a, text_b])
            score = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100

            st.divider()
            st.subheader("Comparison Results")
            result_col1, result_col2, result_col3 = st.columns(3)
            result_col1.metric("Text similarity", f"{score:.2f}%")
            result_col2.metric("Document A words", f"{len(text_a.split()):,}")
            result_col3.metric("Document B words", f"{len(text_b.split()):,}")

            if score >= 70:
                st.error("High similarity detected — review the matching content carefully.")
            elif score >= 35:
                st.warning("Moderate similarity detected — inspect the matching content.")
            else:
                st.success("Low similarity detected by this comparison method.")

            st.caption(
                "These ranges are simple project labels, not official plagiarism thresholds. "
                "A similarity score alone cannot determine plagiarism."
            )

            sentences_a = split_sentences(text_a)
            sentences_b = split_sentences(text_b)
            normalized_b = {clean_sentence(s) for s in sentences_b}
            exact_matches = []
            seen = set()

            for sentence in sentences_a:
                normalized = clean_sentence(sentence)
                if len(normalized.split()) >= 4 and normalized in normalized_b and normalized not in seen:
                    exact_matches.append(sentence)
                    seen.add(normalized)

            st.subheader("Exact Matching Sentences")
            if exact_matches:
                st.write(f"Found {len(exact_matches)} exact matching sentence(s):")
                for sentence in exact_matches:
                    st.markdown(f"- 🟨 {sentence}")
            else:
                st.info(
                    "No exact matching sentences were found. The documents may still contain "
                    "similar wording that is not an exact sentence match."
                )

            st.subheader("Download Report")
            report = (
                "DOCUMENT SIMILARITY REPORT\n"
                "==========================\n"
                f"Similarity score: {score:.2f}%\n"
                f"Document A word count: {len(text_a.split())}\n"
                f"Document B word count: {len(text_b.split())}\n"
                f"Exact matching sentences: {len(exact_matches)}\n\n"
                "Exact matches:\n"
                + ("\n".join(f"- {s}" for s in exact_matches) if exact_matches else "No exact matches found.")
                + "\n\nNote: This is a similarity screening tool, not proof of plagiarism.\n"
            )
            st.download_button(
                "⬇️ Download comparison report",
                data=report,
                file_name="similarity_report.txt",
                mime="text/plain",
                use_container_width=True,
            )

        except ValueError:
            st.error("The documents do not contain enough usable text to compare. Please add more text.")

st.divider()
st.caption("Privacy note: this basic app processes the text during the current session. Avoid uploading confidential documents.")
