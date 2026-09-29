def render_user(text: str, max_chars: int = 2000) -> str:
    body = text.strip()
    if not body:
        raise ValueError("text 不能为空")
    if len(body) > max_chars:
        body = body[:max_chars] + "……（已截断）"
    return f"请总结下面这段内容：\n{body}"
