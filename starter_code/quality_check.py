# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    """Kiểm tra chất lượng dữ liệu trước khi đưa vào Knowledge Base.

    Args:
        doc_dict: Dictionary chứa thông tin document, cần có key "content".

    Returns:
        True nếu dữ liệu đạt chất lượng, False nếu không đạt.
    """
    content = doc_dict.get("content", "")

    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    if not content or len(content) < 10:
        return False

    # 2. Kiểm tra từ khóa lỗi
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    for keyword in toxic_keywords:
        if keyword in content:
            return False

    return True
