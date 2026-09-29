import pytest
from llm_toolkit.prompt import render_user

# tests/test_prompt.py 本次新增的测试
def test_render_user_truncates_long_text():
    long_text = "a" * 3000
    out = render_user(long_text, max_chars=10)
    assert "已截断" in out

# tests/test_prompt.py 特性分支上补的第二个测试
@pytest.mark.parametrize("bad", ["", "   "])
def test_render_user_rejects_blank(bad):
    with pytest.raises(ValueError):
        render_user(bad)