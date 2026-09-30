from html import escape


def sanitize_text(text: str) -> str:
    """
    Clean text for safe HTML rendering.
    """
    if not text:
        return ""

    replacements = {
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "–": "-",
        "—": "-"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.strip()


def format_html_preview(text: str) -> str:
    """
    Convert generated legal document into a styled HTML preview.
    """

    text = sanitize_text(text)

    paragraphs = text.split("\n")

    html_content = ""

    for para in paragraphs:
        para = para.strip()

        if not para:
            continue

        if para.isupper() or len(para) < 60:
            html_content += f"<h3>{escape(para)}</h3>"
        else:
            html_content += f"<p>{escape(para)}</p>"

    return f"""
    <div style="
        background-color:#1e1e1e;
        color:white;
        padding:25px;
        border-radius:12px;
        border:1px solid #333;
        max-height:700px;
        overflow-y:auto;
        line-height:1.8;
        font-family:Arial, sans-serif;
    ">
        {html_content}
    </div>
    """