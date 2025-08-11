from utils.rag_engine import query_rag

def detect_red_flags(text: str, doc_type: str = "Unknown") -> list[dict]:
    """
    Detects red flags in the legal document using rule-based + RAG methods.

    Args:
        text (str): Cleaned text content of the document
        doc_type (str): Type of the document detected (for context)

    Returns:
        list: List of dicts with {issue, suggestion, citation, quote}
    """

    flags = []
    if not text:
        return flags

    t = text.lower()

    # example heuristics
    if "indemnity" in t and "limit" not in t:
        flags.append({
            "issue": "Uncapped indemnity clause",
            "suggestion": "Consider adding a monetary cap to indemnity clauses where appropriate."
        })

    # check for governing law presence
    if "governing law" not in t and "governed by" not in t:
        flags.append({
            "issue": "Missing governing law clause",
            "suggestion": "Add a governing law clause specifying the applicable jurisdiction."
        })

    # check for termination notice period
    if "termination" in t and not re.search(r'notice\s+period', t):
        flags.append({
            "issue": "Termination clause without clear notice period",
            "suggestion": "Specify notice period and termination conditions."
        })

    # short doc
    if len(t) < 200:
        flags.append({
            "issue": "Very short document",
            "suggestion": "Document content seems short; verify completeness."
        })


    # Rule-based examples (you can expand this list)
    if "free zone" in text.lower():
        flags.append({
            "issue": "Mentions 'Free Zone' instead of ADGM",
            "suggestion": "Replace with 'Abu Dhabi Global Market' to reflect correct jurisdiction.",
            "citation": None,
            "quote": "free zone"
        })

    if "as mutually agreed" in text.lower():
        flags.append({
            "issue": "Vague agreement terms",
            "suggestion": "Define terms explicitly instead of using vague language.",
            "citation": None,
            "quote": "as mutually agreed"
        })

    if "tbd" in text.lower() or "to be decided" in text.lower():
        flags.append({
            "issue": "Unresolved or undefined terms (TBD)",
            "suggestion": "All terms must be fully specified in legal documents.",
            "citation": None,
            "quote": "TBD"
        })

    # 2️⃣ RAG-based checks (sample question per document type)
    rag_checklist = {
        "Articles of Association": [
            "What must be included in an AoA under ADGM law?",
            "Are there restrictions on director roles?"
        ],
        "UBO Form": [
            "What ownership details are mandatory in a UBO form?"
        ],
        "Employment Contract": [
            "What are required clauses in an ADGM employment contract?"
        ],
        "Balance Sheet": [
            "What fields must be filled in an ADGM balance sheet?"
        ]
    }

    questions = rag_checklist.get(doc_type, [])

    for question in questions:
        rag_response = query_rag(question + f"\nContext:\n{text[:1000]}")  # optional limit to avoid overflow
        if rag_response:
            flags.append({
                "issue": f"Check: {question}",
                "suggestion": rag_response,
                "citation": "Retrieved via RAG",
                "quote": None
            })

    return flags
