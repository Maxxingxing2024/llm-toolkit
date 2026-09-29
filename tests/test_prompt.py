import pytest
from llm_toolkit.prompt import render_user

# tests/test_prompt.py 本次新增的测试
def test_render_user_truncates_long_text():
    long_text = "a" * 3000
    out = render_user(long_text, max_chars=10)
    assert "已截断" in out