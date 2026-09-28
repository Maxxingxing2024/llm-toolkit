import pytest

from llm_toolkit.config import AppConfig, load_config


def test_load_config_from_dict():
    cfg = load_config({"API_KEY": "sk-test", "MODEL": "qwen-plus", "TIMEOUT": "5"})
    assert cfg.model == "qwen-plus"
    assert cfg.timeout == 5


def test_load_config_defaults():
    cfg = load_config({"API_KEY": "sk-test"})
    assert cfg.timeout == 30
    assert cfg.base_url.endswith("/v1")


def test_empty_key_is_rejected():
    with pytest.raises(ValueError):
        AppConfig(api_key="")