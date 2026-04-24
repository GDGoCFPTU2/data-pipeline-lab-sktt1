import re


def process_pdf_data(raw_json: dict) -> dict:
    raw_text = raw_json.get("extractedText", "")

    cleaned_content = re.sub(r"HEADER_PAGE_\d+", "", raw_text)
    cleaned_content = re.sub(r"FOOTER_PAGE_\d+", "", cleaned_content)
    cleaned_content = re.sub(r"\n{3,}", "\n\n", cleaned_content).strip()

    return {
        "document_id": raw_json.get("docId", ""),
        "source_type": "PDF",
        "author": raw_json.get("authorName", "Unknown").strip(),
        "category": raw_json.get("docCategory", "Uncategorized"),
        "content": cleaned_content,
        "timestamp": raw_json.get("createdAt", ""),
    }


def process_video_data(raw_json: dict) -> dict:
    return {
        "document_id": raw_json.get("video_id", ""),
        "source_type": "Video",
        "author": raw_json.get("creator_name", "Unknown"),
        "category": raw_json.get("category", "Uncategorized"),
        "content": raw_json.get("transcript", ""),
        "timestamp": raw_json.get("published_timestamp", ""),
    }
