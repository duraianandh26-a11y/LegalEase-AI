import streamlit as st
import requests

BACKEND_URL ="http://127.0.0.1:8000/generate"

st.set_page_config(
    page_title="LegalEase",
    layout="wide"
)

st.title("LegalEase")
st.subheader("AI-Powered Legal Document Generator")

document_type = st.text_input(
    "Document Type"
)

parties = st.text_area(
    "Parties Involved"
)

terms = st.text_area(
    "Terms and Conditions"
)

effective_date = st.text_input(
    "Effective Date"
)

if st.button("Generate Document"):

    payload = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "effective_date": effective_date
    }

    response = requests.post(
        BACKEND_URL,
        json=payload
    )

    if response.status_code == 200:

        document = response.json()["document"]

        st.session_state["document"] = document

if "document" in st.session_state:

    edited_text = st.text_area(
        "Edit Document",
        st.session_state["document"],
        height=500
    )

    st.download_button(
        "Download TXT",
        edited_text,
        file_name="legal_document.txt"
    )