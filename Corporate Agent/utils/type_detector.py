def detect_document_type(text: str) -> str:
    """
    Very simple keyword-based document type detector.
    You can replace / improve this later with ML or regex rules.
    """
    if not text:
        return "Unknown"

    t = text.lower()
    if "articles of association" in t or "articles" in t and "association" in t:
        return "Articles of Association"
    if "memorandum of association" in t or "memorandum" in t and "association" in t:
        return "Memorandum of Association"
    if "board resolution" in t:
        return "Board Resolution"
    if "shareholder" in t and "resolution" in t:
        return "Shareholder Resolution"
    if "inclusion form" in t or "incorporation" in t:
        return "Incorporation Form"
    # fallback - try some guesses
    if "terms and conditions" in t:
        return "Terms and Conditions"
    return "Unknown"
